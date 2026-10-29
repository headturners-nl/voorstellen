#!/usr/bin/env python3
"""Zet de pitchmails uit concepten/<datum>.json als CONCEPT in de map Concepten
van info@headturners.nl (IMAP). Verzendt nooit iets: het script maakt geen
SMTP-verbinding en schrijft alleen naar de conceptenmap.

Instellingen (GitHub Secrets / omgevingsvariabelen):
  IMAP_HOST      bv. mail.headturners.nl
  IMAP_USER      info@headturners.nl
  IMAP_PASSWORD  wachtwoord van de mailbox
  IMAP_PORT      optioneel, standaard 993 (SSL)
  IMAP_DRAFTS    optioneel, standaard INBOX.Drafts
  IMAP_SENT      optioneel, standaard INBOX.Sent (om de handtekening te vinden)
  MAIL_FROM      optioneel, standaard "Headturners B.V." <info@headturners.nl>
  DATUM          optioneel, standaard vandaag (Europe/Amsterdam)
"""
import base64
import datetime as dt
import email
import email.policy
import html
import imaplib
import json
import os
import re
import ssl
import sys
import time
import urllib.request
from email.header import decode_header, make_header
from email.message import EmailMessage
from email.utils import formatdate, make_msgid
from zoneinfo import ZoneInfo

URL_RE = re.compile(r"https?://[^\s<>\"]+")
VOORSTEL_RE = re.compile(r"https://voorstel\.headturners\.nl/[^/\s]+/")


def log(*a):
    print(*a, flush=True)


def samenvatting(regel):
    pad = os.environ.get("GITHUB_STEP_SUMMARY")
    if pad:
        with open(pad, "a", encoding="utf-8") as f:
            f.write(regel + "\n")


def decode(s):
    try:
        return str(make_header(decode_header(s or ""))).strip()
    except Exception:
        return (s or "").strip()


# ---------- 1. concepten laden ----------
def laad_concepten(datum):
    pad = os.path.join("concepten", f"{datum}.json")
    if not os.path.exists(pad):
        log(f"Geen bestand {pad}: de eerste taak heeft niets klaargezet.")
        samenvatting(f"Geen {pad} gevonden, niets gedaan.")
        sys.exit(0)
    with open(pad, encoding="utf-8") as f:
        data = json.load(f)
    for i, m in enumerate(data):
        if not isinstance(m.get("to"), list) or len(m["to"]) != 1:
            raise SystemExit(f"Mail {i}: 'to' moet precies één adres bevatten: {m.get('to')}")
        if not m.get("subject") or not m.get("body"):
            raise SystemExit(f"Mail {i}: onderwerp of tekst ontbreekt")
    return data


# ---------- 2. voorstellen online? ----------
def controleer_online(url, pogingen=10, wacht=60):
    for p in range(1, pogingen + 1):
        try:
            req = urllib.request.Request(url + ("&" if "?" in url else "?") + f"t={int(time.time())}",
                                         headers={"User-Agent": "headturners-concepten"})
            with urllib.request.urlopen(req, timeout=20) as r:
                if r.status == 200:
                    return True
        except Exception as e:
            log(f"  {url} nog niet bereikbaar (poging {p}): {e}")
        time.sleep(wacht)
    return False


# ---------- 3. IMAP ----------
def imap_verbind():
    host = os.environ["IMAP_HOST"]
    port = int(os.environ.get("IMAP_PORT", "993"))
    M = imaplib.IMAP4_SSL(host, port, ssl_context=ssl.create_default_context())
    M.login(os.environ["IMAP_USER"], os.environ["IMAP_PASSWORD"])
    return M


def q(mapnaam):
    return '"' + mapnaam.replace('"', '\\"') + '"'


def onderwerpen_in_map(M, mapnaam):
    typ, _ = M.select(q(mapnaam), readonly=True)
    if typ != "OK":
        raise SystemExit(f"Map {mapnaam} niet gevonden op de IMAP-server")
    typ, data = M.uid("SEARCH", None, "ALL")
    uids = data[0].split() if data and data[0] else []
    onderwerpen = set()
    for i in range(0, len(uids), 200):
        reeks = b",".join(uids[i:i + 200]).decode()
        typ, resp = M.uid("FETCH", reeks, "(BODY.PEEK[HEADER.FIELDS (SUBJECT)])")
        for item in resp:
            if isinstance(item, tuple):
                msg = email.message_from_bytes(item[1])
                onderwerpen.add(decode(msg.get("Subject")))
    return onderwerpen


def zoek_handtekening(M, mappen):
    """Pak de handtekening (HTML + logo + platte tekst) uit de nieuwste mail
    in Concepten of Verzonden die een Roundcube-handtekening bevat."""
    for mapnaam in mappen:
        typ, _ = M.select(q(mapnaam), readonly=True)
        if typ != "OK":
            continue
        typ, data = M.uid("SEARCH", None, "ALL")
        uids = data[0].split() if data and data[0] else []
        for uid in reversed(uids[-60:]):
            typ, resp = M.uid("FETCH", uid, "(BODY.PEEK[])")
            raw = next((x[1] for x in resp if isinstance(x, tuple)), None)
            if not raw:
                continue
            msg = email.message_from_bytes(raw, policy=email.policy.default)
            html_deel = next((p for p in msg.walk() if p.get_content_type() == "text/html"), None)
            if not html_deel:
                continue
            h = html_deel.get_content()
            start = h.find('<div id="_rc_sig"')
            if start < 0:
                continue
            einde = h.lower().rfind("</body>")
            sig_html = h[start:einde if einde > start else len(h)].strip()
            if "<img" not in sig_html:
                continue  # we willen de handtekening mét logo
            # inline afbeeldingen (cid:) meenemen
            afbeeldingen = {}
            compleet = True
            for cid in set(re.findall(r'src="cid:([^"]+)"', sig_html)):
                for p in msg.walk():
                    if (p.get("Content-ID") or "").strip().strip("<>") == cid:
                        afbeeldingen[cid] = (p.get_content_type(), p.get_content())
                if cid not in afbeeldingen:
                    compleet = False
            if not compleet:
                continue

            # data:-afbeeldingen omzetten naar cid-bijlagen
            def vervang(mt):
                mime, b64 = mt.group(1), mt.group(2)
                cid = make_msgid(domain="headturners.nl")[1:-1]
                afbeeldingen[cid] = (mime, base64.b64decode(b64))
                return f'src="cid:{cid}"'
            sig_html = re.sub(r'src="data:(image/[a-z+.-]+);base64,([^"]+)"', vervang, sig_html)
            if not afbeeldingen:
                continue  # logo staat extern of ontbreekt; zoek verder

            tekst_deel = next((p for p in msg.walk() if p.get_content_type() == "text/plain"), None)
            sig_tekst = ""
            if tekst_deel:
                t = tekst_deel.get_content().replace("\r\n", "\n")
                i = t.find("\n-- \n")
                sig_tekst = t[i + 1:].strip() if i >= 0 else ""
            if not sig_tekst:
                sig_tekst = html_naar_tekst(sig_html)
            log(f"Handtekening gevonden in {mapnaam} (uid {uid.decode()}), {len(afbeeldingen)} afbeelding(en)")
            return sig_html, afbeeldingen, sig_tekst
    raise SystemExit("Geen handtekening met logo gevonden in Concepten of Verzonden; gestopt zodat er geen mail zonder handtekening ontstaat.")


def html_naar_tekst(h):
    h = re.sub(r"<br\s*/?>|</div>|</p>", "\n", h, flags=re.I)
    h = re.sub(r"<[^>]+>", "", h)
    return re.sub(r"\n{3,}", "\n\n", html.unescape(h).replace("\xa0", " ")).strip()


# ---------- 4. mail opbouwen ----------
def tekst_naar_html(body):
    def regel(r):
        uit, pos = [], 0
        for m in URL_RE.finditer(r):
            uit.append(html.escape(r[pos:m.start()]))
            u = m.group(0)
            uit.append(f'<a href="{html.escape(u, quote=True)}">{html.escape(u)}</a>')
            pos = m.end()
        uit.append(html.escape(r[pos:]))
        return "".join(uit)
    alineas = [a for a in re.split(r"\n\s*\n", body.strip()) if a.strip()]
    return "".join("<p>" + "<br />".join(regel(r) for r in a.split("\n")) + "</p>\n" for a in alineas)


def bouw_mail(m, afzender, sig_html, afbeeldingen, sig_tekst):
    msg = EmailMessage()
    msg["From"] = afzender
    msg["To"] = m["to"][0]
    msg["Subject"] = m["subject"]
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain="headturners.nl")
    msg["X-Headturners"] = "concept-automatisch"
    msg.set_content(m["body"].strip() + "\n\n" + sig_tekst + "\n")
    html_doc = ('<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head>'
                '<body style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif">\n'
                + tekst_naar_html(m["body"]) + "<p>&nbsp;</p>\n" + sig_html + "\n</body></html>")
    msg.add_alternative(html_doc, subtype="html")
    html_part = msg.get_payload()[1]
    for cid, (mime, data) in afbeeldingen.items():
        maintype, subtype = mime.split("/", 1)
        html_part.add_related(data, maintype=maintype, subtype=subtype, cid=f"<{cid}>",
                              filename=f"logo.{subtype.split('+')[0]}", disposition="inline")
    return msg


def main():
    datum = os.environ.get("DATUM") or dt.datetime.now(ZoneInfo("Europe/Amsterdam")).date().isoformat()
    log(f"Datum: {datum}")
    samenvatting(f"## Concepten {datum}\n")
    mails = laad_concepten(datum)
    log(f"{len(mails)} mail(s) in het bestand")

    # voorstellen online?
    offline = []
    for m in mails:
        for url in sorted(set(VOORSTEL_RE.findall(m["body"]))):
            if not controleer_online(url):
                offline.append((m["subject"], url))
    if offline:
        for s, u in offline:
            samenvatting(f"- NIET online: {u} ({s})")
        raise SystemExit(f"{len(offline)} voorstel(len) niet online; geen concepten gemaakt.")

    drafts = os.environ.get("IMAP_DRAFTS", "INBOX.Drafts")
    sent = os.environ.get("IMAP_SENT", "INBOX.Sent")
    afzender = os.environ.get("MAIL_FROM", '"Headturners B.V." <info@headturners.nl>')

    M = imap_verbind()
    try:
        bestaand = onderwerpen_in_map(M, drafts)
        sig_html, afbeeldingen, sig_tekst = zoek_handtekening(M, [drafts, sent])
        gemaakt, overgeslagen = [], []
        for m in mails:
            if m["subject"].strip() in bestaand:
                overgeslagen.append(m)
                log(f"Overgeslagen (bestaat al): {m['subject']}")
                continue
            msg = bouw_mail(m, afzender, sig_html, afbeeldingen, sig_tekst)
            typ, resp = M.append(q(drafts), r"(\Draft \Seen)", imaplib.Time2Internaldate(time.time()),
                                 msg.as_bytes(policy=email.policy.SMTP))
            if typ != "OK":
                raise SystemExit(f"Opslaan mislukt voor {m['subject']}: {resp}")
            gemaakt.append(m)
            log(f"Concept opgeslagen: {m['subject']} -> {m['to'][0]}")

        # controle
        na = onderwerpen_in_map(M, drafts)
        ontbreekt = [m["subject"] for m in mails if m["subject"].strip() not in na]
    finally:
        try:
            M.logout()
        except Exception:
            pass

    for m in gemaakt:
        samenvatting(f"- Concept gemaakt: **{m['subject']}** aan {m['to'][0]}")
    for m in overgeslagen:
        samenvatting(f"- Bestond al, overgeslagen: {m['subject']}")
    if ontbreekt:
        samenvatting(f"- ONTBREEKT na controle: {', '.join(ontbreekt)}")
        raise SystemExit("Niet alle concepten staan in de map Concepten.")
    log(f"Klaar: {len(gemaakt)} gemaakt, {len(overgeslagen)} overgeslagen.")


if __name__ == "__main__":
    main()
