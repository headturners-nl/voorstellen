import os
OUT = "/tmp/claude-0/-home-claude/13cf64e8-3345-5239-8f3b-5bfa63d14475/scratchpad/ht/site"

LOGO = '<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="13" fill="#FFCF4A"/><path d="M7.5 18.5c1.8-1.3 3-1.3 4.2 0M7.5 24h3.6M7.5 29.5c1.8 1.3 3 1.3 4.2 0" fill="none" stroke="#1F2A44" stroke-width="2.2" stroke-linecap="round"/><ellipse cx="21.5" cy="24" rx="6.2" ry="8.2" fill="#fff" stroke="#1F2A44" stroke-width="2.8"/><ellipse cx="34.5" cy="24" rx="6.2" ry="8.2" fill="#fff" stroke="#1F2A44" stroke-width="2.8"/><circle cx="24.6" cy="25" r="3.2" fill="#1F2A44"/><circle cx="37.6" cy="25" r="3.2" fill="#1F2A44"/><circle cx="25.5" cy="23.7" r="1" fill="#fff"/><circle cx="38.5" cy="23.7" r="1" fill="#fff"/></svg>'
CHK = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>'
CHK_W = CHK.replace('#1F2A44', '#FFCF4A')
PM = '<span class="pm" aria-hidden="true"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="3" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg></span>'
ARROW = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

ICONS = {
 "web": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 8h18M8 21h8"/></svg>',
 "ads": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11v2a1 1 0 001 1h2l5 4V6L6 10H4a1 1 0 00-1 1z"/><path d="M15 9a4 4 0 010 6M18 6a8 8 0 010 12"/></svg>',
 "social": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg>',
 "blog": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9a2.8 2.8 0 00-4-4L4 16v4z"/><path d="M13 7l4 4"/></svg>',
 "brand": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="8.5" cy="10" r="1.3"/><circle cx="12" cy="7.5" r="1.3"/><circle cx="15.5" cy="10" r="1.3"/><path d="M12 21a3 3 0 010-6h2a2 2 0 002-2"/></svg>',
}

NAV = [
 ("websites.html", "Websites", "Laten bouwen, kopen of huren"),
 ("advertenties.html", "Advertenties", "Google Ads en Meta Ads"),
 ("social-en-blogs.html", "Social media en blogs", "Content die je vindbaar maakt"),
 ("branding.html", "Branding", "Logo, kleuren, visie en missie"),
]

def li(t, c=CHK): return f'<li>{c}{t}</li>'
def faq(items): return "\n".join(f'<details><summary>{q}{PM}</summary><p>{a}</p></details>' for q, a in items)

def page(fname, title, desc, body, current=""):
    bodycls = ' class="no-mcta"' if fname=='contact.html' else ''
    dd_cur = ' aria-current="page"' if fname in [n[0] for n in NAV] else ''
    AC = ' aria-current="page"'
    panel = "".join(f'<a href="{h}"{AC if h==fname else ""}><b>{t}</b><span>{sub}</span></a>' for h, t, sub in NAV)
    def cur(h): return ' aria-current="page"' if h == fname else ''
    html = f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="logo-mark.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/fonts.css">
<link rel="stylesheet" href="assets/style.css">
</head>
<body{bodycls}>
<header class="site">
<div class="wrap nav">
<a class="brand" href="index.html" aria-label="Headturners, naar de homepage">{LOGO}<span class="brand-name"><b>Headturners</b><i>Brands that make people look twice</i></span></a>
<button class="burger" type="button" aria-label="Menu openen" aria-expanded="false" aria-controls="menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
<nav class="menu" id="menu" aria-label="Hoofdmenu">
<div class="dd"><button type="button" aria-expanded="false"{dd_cur}>Diensten <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dd-panel">{panel}</div></div>
<a href="voorbeelden.html"{cur("voorbeelden.html")}>Voorbeelden</a>
<a href="websites.html#prijzen">Prijzen</a>
<a href="over.html"{cur("over.html")}>Over mij</a>
<a href="contact.html"{cur("contact.html")}>Contact</a>
<a class="btn btn-sun" href="contact.html">Gratis voorstel</a>
</nav>
</div>
</header>
<main id="top">
{body}
</main>
<footer class="site">
<div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="index.html">{LOGO}<span class="brand-name"><b>Headturners</b><i>Brands that make people look twice</i></span></a><p>Websites, advertenties en content voor ondernemers. Door een ondernemer.</p></div>
<div><h3>Diensten</h3><ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h,t,s in NAV)}</ul></div>
<div><h3>Meer</h3><ul><li><a href="voorbeelden.html">Voorbeelden</a></li><li><a href="websites.html#prijzen">Prijzen</a></li><li><a href="over.html">Over mij</a></li><li><a href="contact.html">Contact</a></li></ul></div>
<div><h3>Contact</h3><ul><li><a href="contact.html">Gratis voorstel aanvragen</a></li><li><a href="mailto:info@headturners.nl">info@headturners.nl</a></li><li><span style="color:var(--muted-on-ink)">KvK [nummer]</span></li></ul></div>
</div>
<div class="small"><span>© <span id="jaar">2026</span> Headturners · Alle prijzen exclusief btw</span><span class="legal-links"><a href="algemene-voorwaarden.html">Algemene voorwaarden</a><a href="privacyverklaring.html">Privacyverklaring</a><a href="cookieverklaring.html">Cookieverklaring</a></span></div>
</div>
</footer>
<div class="mcta"><a class="btn btn-sun" href="contact.html">Vraag je gratis voorstel aan</a></div>
<script src="assets/main.js" defer></script>
</body>
</html>
'''
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote", fname)

def cta(title, text, btn="Vraag je gratis voorstel aan", href="contact.html"):
    return f'''<section class="cta-band"><div class="wrap cta-inner"><div><h2>{title}</h2><p>{text}</p></div><a class="btn btn-main" href="{href}">{btn}</a></div></section>'''

def crumb(name): return f'<p class="crumb"><a href="index.html">Home</a> &nbsp;/&nbsp; {name}</p>'

# ---------------- HOME ----------------
home = f'''
<section class="hero">
<div class="wrap hero-grid">
<div>
<h1>Een merk waar mensen van omkijken</h1>
<p class="lead">Ik bouw websites voor ondernemers die liever met hun vak bezig zijn dan met hun site. Je krijgt eerst gratis een voorstel van je nieuwe homepage, in je eigen huisstijl. Pas als je het mooi vindt, gaan we verder.</p>
<div class="ctas"><a class="btn btn-main" href="contact.html">Vraag je gratis voorstel aan</a><a class="btn btn-line" href="voorbeelden.html">Bekijk voorbeelden</a></div>
<p class="check">{CHK}Geen kosten en geen verplichtingen. Je ziet eerst wat je krijgt.</p>
</div>
<div class="stage">
<div class="laptop"><div class="screen"><img src="klanten/sami-na.jpg" alt="Website van Sami's Acupunctuur op een laptop" width="1600" height="1000"></div><div class="base" aria-hidden="true"></div></div>
<div class="phone"><img src="klanten/tppalneema-mobiel.jpg" alt="Website van Tandprothetische Praktijk Al Neema op een telefoon" width="711" height="1540"></div>
<div class="sticky"><p class="hand">Echte klanten, echte sites. Op laptop én telefoon.</p></div>
</div>
</div>
</section>

<div class="proof"><div class="wrap proof-row">
<div>{CHK}Gratis voorstel vooraf</div>
<div>{CHK}Eén vast aanspreekpunt</div>
<div>{CHK}Kopen of huren vanaf €59 per maand</div>
<div>{CHK}Ook zelf ondernemer</div>
</div></div>

<section>
<div class="wrap">
<div class="head"><h2>Alles om online gevonden te worden</h2><p>Van een eerste logo tot advertenties die klanten opleveren. Kies wat je nodig hebt, of laat mij het hele traject doen.</p></div>
<div class="svc">
<a href="websites.html"><span class="ico">{ICONS["web"]}</span><h3>Websites</h3><p>Een site in je eigen huisstijl die klanten laat bellen, appen of een afspraak maken.</p><span class="from">vanaf €59 p/m {ARROW}</span></a>
<a href="advertenties.html"><span class="ico">{ICONS["ads"]}</span><h3>Advertenties</h3><p>Google Ads en Meta Ads, opgezet na een gesprek over jouw bedrijf en elke maand bijgestuurd.</p><span class="from">vanaf €295 p/m {ARROW}</span></a>
<a href="social-en-blogs.html"><span class="ico">{ICONS["social"]}</span><h3>Social media en blogs</h3><p>Een vast ritme van posts en blogs die je zichtbaar en vindbaar houden.</p><span class="from">vanaf €95 {ARROW}</span></a>
<a href="branding.html"><span class="ico">{ICONS["brand"]}</span><h3>Branding</h3><p>Logo, kleuren, visie en missie. Zodat alles wat je maakt herkenbaar is.</p><span class="from">vanaf €795 {ARROW}</span></a>
</div>
</div>
</section>

<section class="sage">
<div class="wrap">
<div class="head"><h2>Van verouderd naar visitekaartje</h2><p>Sleep het gele bolletje heen en weer om de oude en nieuwe site te vergelijken.</p></div>
<div data-cases="1"></div>
<p style="margin-top:40px"><a class="btn btn-line" href="voorbeelden.html">Bekijk alle voorbeelden</a></p>
</div>
</section>

<section class="on-ink">
<div class="wrap">
<div class="head"><h2>Zo werkt het</h2><p>Je ziet eerst wat je krijgt. Daarna beslis je pas.</p></div>
<div class="steps">
<div class="step"><div class="step-n">1</div><h3>Ik maak een voorstel</h3><p>Ik kijk naar je huidige site, je socials en je huisstijl, en maak daar een nieuwe homepage van.</p><span class="tag">Gratis</span></div>
<div class="step"><div class="step-n">2</div><h3>We maken hem samen af</h3><p>Je zegt wat je anders wilt. Ik bouw de rest van de pagina's en jij keurt alles goed.</p></div>
<div class="step"><div class="step-n">3</div><h3>Live, en ik houd hem bij</h3><p>Je site gaat online op je eigen domein. Wil je dat ik hem bijhoud of er klanten naartoe stuur, dan regelen we dat.</p></div>
</div>
</div>
</section>

<section>
<div class="wrap">
<div class="about-card">
<img class="avatar" src="klanten/mar-rond.jpg" alt="Mar van Headturners" width="120" height="120" style="object-fit:cover;padding:0">
<div>
<h2>Hoi, ik ben Mar. Ook ondernemer.</h2>
<p>Naast Headturners heb ik mijn eigen tandprothetische praktijk in Driebergen. Ik weet dus hoe het is: je hebt het druk met klanten, en je website schuift steeds naar morgen.</p>
<p>Mijn eigen site, advertenties en social media doe ik zelf. Wat daar werkt, gebruik ik voor jou.</p>
<p class="hand">Mar</p>
<p style="margin-top:18px"><a class="btn btn-line" href="over.html">Lees mijn verhaal</a></p>
</div>
</div>
</div>
</section>

{cta("Benieuwd hoe jouw site eruit kan zien?", "Stuur je naam en je huidige website. Ik maak gratis een voorstel en stuur het je persoonlijk toe.")}
'''
page("index.html", "Headturners | Websites voor ondernemers, door een ondernemer",
     "Websites, advertenties, social media en branding voor ondernemers. Eerst gratis een voorstel van je nieuwe homepage, daarna beslis je.", home)

# ---------------- WEBSITES ----------------
web = f'''
<section class="page-hero">
<div class="wrap page-hero-grid">
<div>
{crumb("Websites")}
<h1>Een website die klanten oplevert</h1>
<p class="lead">Mooi is niet genoeg. Je site moet bezoekers laten bellen, appen of een afspraak maken. Ik bouw hem in je eigen huisstijl, op telefoon en computer, en je ziet eerst gratis een voorstel.</p>
<div class="ctas"><a class="btn btn-main" href="contact.html?dienst=Website">Vraag je gratis voorstel aan</a><a class="btn btn-line" href="#prijzen">Bekijk prijzen</a></div>
</div>
<div class="phone" style="position:relative;width:62%;margin:0 auto"><img src="klanten/sami-mobiel.jpg" alt="Website van Sami's Acupunctuur op een telefoon" width="711" height="1540"></div>
</div>
</section>

<section class="sage">
<div class="wrap">
<div class="head"><h2>Wat je krijgt</h2><p>Alles wat een ondernemer nodig heeft om online serieus genomen te worden.</p></div>
<div class="feat">
<div><b>Je eigen huisstijl</b><span>Je logo, kleuren en foto's. Geen standaard template dat je overal ziet.</span></div>
<div><b>Werkt op elke telefoon</b><span>De meeste bezoekers komen via hun telefoon. Daar ontwerp ik eerst voor.</span></div>
<div><b>Duidelijke actieknoppen</b><span>Bellen, WhatsApp of een afspraak maken, altijd binnen handbereik.</span></div>
<div><b>Gevonden in Google</b><span>Een goede basis voor zoekmachines: snelle pagina's, juiste titels en teksten.</span></div>
<div><b>Teksten die verkopen</b><span>Ik schrijf mee, in begrijpelijke taal die past bij jouw klanten.</span></div>
<div><b>Vast aanspreekpunt</b><span>Een vraag of aanpassing? Je hebt mij direct aan de lijn, geen ticketsysteem.</span></div>
</div>
</div>
</section>

<section id="prijzen">
<div class="wrap">
<div class="head"><h2>Huren of kopen</h2><p>Huur je site voor een vast bedrag per maand, of koop hem in één keer.</p></div>
<div class="switch" role="group" aria-label="Huren of kopen"><button type="button" data-mode="huren" aria-pressed="true">Huren</button><button type="button" data-mode="kopen" aria-pressed="false">Kopen</button></div>
<div class="plans">
<article class="plan">
<h3>Starter</h3><p class="sub">Eén sterke pagina met alles wat een klant wil weten.</p>
<div class="amount"><strong data-huren="€59" data-kopen="€695">€59</strong><span data-huren="per maand" data-kopen="eenmalig">per maand</span></div>
<p class="terms" data-huren="Minimaal 12 maanden, exclusief domeinnaam en back ups" data-kopen="Hosting vanaf €15 per maand, of kies een beheerpakket">Minimaal 12 maanden, exclusief domeinnaam en back ups</p>
<ul>{li("Homepage in je eigen huisstijl")}{li("Werkt goed op telefoon en computer")}{li("Bel, WhatsApp of afspraakknop")}<li class="only-huren">{CHK}Hosting en elke maand 30 minuten aanpassingen</li></ul>
<a class="btn btn-line" href="contact.html?dienst=Website">Kies Starter</a>
</article>
<article class="plan pick">
<span class="pick-note hand">meest gekozen</span>
<h3>Bedrijfssite</h3><p class="sub">Vier tot zes pagina's: diensten, over jou, prijzen en contact.</p>
<div class="amount"><strong data-huren="€89" data-kopen="€1.495">€89</strong><span data-huren="per maand" data-kopen="eenmalig">per maand</span></div>
<p class="terms" data-huren="Minimaal 12 maanden, exclusief domeinnaam en back ups" data-kopen="Hosting vanaf €15 per maand, of kies een beheerpakket">Minimaal 12 maanden, exclusief domeinnaam en back ups</p>
<ul>{li("4 tot 6 pagina's op maat")}{li("Goed vindbaar in Google")}{li("Contactformulier en reviews")}<li class="only-huren">{CHK}Hosting en elke maand 30 minuten aanpassingen</li></ul>
<a class="btn btn-main" href="contact.html?dienst=Website">Kies Bedrijfssite</a>
</article>
</div>
<div class="addons">
<div class="addon"><h3>Beheer Basis</h3><div class="p">€29 <span>p/m</span></div><p>Voor kopers. Hosting, updates en 30 minuten aanpassingen per maand.</p></div>
<div class="addon"><h3>Beheer Plus</h3><div class="p">€49 <span>p/m</span></div><p>Alles van Basis, met een uur aanpassingen en voorrang bij vragen.</p></div>
<div class="addon"><h3>Back ups</h3><div class="p">€5 <span>p/m</span></div><p>Dagelijkse back up voor huurders en kopers. Gaat er iets mis, dan staat alles snel terug.</p></div>
<div class="addon"><h3>Losse aanpassing</h3><div class="p">€45</div><p>Vaste prijs voor tekst, foto of openingstijden. Groter werk €65 per uur.</p></div>
</div>
<p class="fine">Alle prijzen zijn exclusief btw.</p>
</div>
</section>

<section class="sage">
<div class="wrap split">
<div>
<h2>Huren en later toch eigenaar worden</h2>
<p class="lead" style="margin-top:18px">Na 12 maanden kun je per maand opzeggen. Wil je de site houden, dan neem je hem over. Hoe langer je huurt, hoe lager dat bedrag.</p>
</div>
<div class="table-wrap"><table class="table"><thead><tr><th>Overnemen na</th><th>Starter</th><th>Bedrijfssite</th></tr></thead><tbody><tr><td>12 maanden</td><td>€350</td><td>€750</td></tr><tr><td>24 maanden</td><td>€195</td><td>€395</td></tr><tr><td>36 maanden</td><td>€95</td><td>€195</td></tr></tbody></table></div>
</div>
</section>

<section>
<div class="wrap faq-grid">
<div><h2>Vragen over websites</h2></div>
<div>{faq([
 ("Kost het voorstel echt niets?", "Ja. Ik maak een homepage op basis van je huidige site en socials. Past het nog niet helemaal, dan pas ik het aan tot het klopt. Pas als jij tevreden bent, beslis je of we verder gaan."),
 ("Wat is het verschil tussen huren en kopen?", "Bij huren betaal je een vast bedrag per maand voor je site, inclusief hosting en elke maand een half uur aanpassingen. Je domeinnaam en back ups regel je zelf, of ik regel ze voor je als losse optie. Bij kopen betaal je één keer en is de site van jou."),
 ("Moet ik zelf teksten en foto's aanleveren?", "Hoeft niet. Ik gebruik wat er al is en schrijf de teksten mee. Eigen foto's maken je site wel persoonlijker, dus heb je die, dan graag."),
 ("Kan ik mijn eigen domeinnaam houden?", "Ja. Je huidige domein verhuist gewoon mee naar je nieuwe site."),
 ("Hoe lang duurt het voordat mijn site online staat?", "Dat hangt vooral af van hoe snel we samen de teksten en foto's rond hebben. In het eerste gesprek maken we een planning die bij jou past."),
])}</div>
</div>
</section>

{cta("Zien hoe jouw nieuwe site eruit kan zien?", "Je krijgt gratis een voorstel van je homepage in je eigen huisstijl. Geen verplichtingen.", href="contact.html?dienst=Website")}
'''
page("websites.html", "Websites laten maken | Headturners",
     "Een website in je eigen huisstijl die klanten oplevert. Huren vanaf €59 per maand of kopen vanaf €695. Eerst gratis een voorstel.", web)

# ---------------- ADVERTENTIES ----------------
ads = f'''
<section class="page-hero">
<div class="wrap page-hero-grid">
<div>
{crumb("Advertenties")}
<h1>Meer klanten via Google en Meta</h1>
<p class="lead">Een mooie site is stap één. Met advertenties op Google, Facebook en Instagram zorg je dat de juiste mensen hem ook vinden. Ik zet je campagnes op na een gesprek over jouw bedrijf, en houd ze elke maand bij.</p>
<div class="ctas"><a class="btn btn-main" href="contact.html?dienst=Advertenties">Plan een kennismaking</a><a class="btn btn-line" href="#prijzen">Bekijk prijzen</a></div>
</div>
<div class="note-card"><p class="hand">Dit doe ik ook voor mijn eigen praktijk.</p><p>Ik weet dus hoe het voelt om elke maand budget uit te geven en te willen zien wat het oplevert. Daarom krijg je van mij geen vaag rapport, maar een duidelijk verhaal.</p></div>
</div>
</section>

<section class="on-ink">
<div class="wrap">
<div class="head"><h2>Je wordt betrokken bij elke stap</h2><p>Geen campagnes uit een standaard doos. Alles begint bij jouw bedrijf.</p></div>
<div class="steps">
<div class="step"><div class="step-n">1</div><h3>Eerst een gesprek</h3><p>We gaan zitten over je producten en diensten, wie je klanten zijn, wat je onderscheidt en wat je wilt bereiken.</p></div>
<div class="step"><div class="step-n">2</div><h3>Plan en campagnes</h3><p>Je krijgt een duidelijk plan met doelgroep, boodschap en budget. Pas na jouw akkoord zet ik de campagnes live.</p></div>
<div class="step"><div class="step-n">3</div><h3>Elke maand bijsturen</h3><p>Ik kijk wat werkt en wat niet, en stuur bij. Elke maand een kort en begrijpelijk rapport.</p></div>
</div>
</div>
</section>

<section id="prijzen">
<div class="wrap">
<div class="head"><h2>Prijzen advertentiebeheer</h2><p>Een vast maandbedrag voor het beheer. Je advertentiebudget betaal je zelf rechtstreeks aan Google of Meta.</p></div>
<div class="plans three">
<article class="plan"><h3>Google Ads</h3><p class="sub">Gevonden worden op het moment dat iemand zoekt naar wat jij doet.</p>
<div class="amount"><strong>€295</strong><span>per maand</span></div><p class="terms">Eenmalig €895 voor gesprek, plan en opzet</p>
<ul>{li("Zoekwoordonderzoek voor jouw regio")}{li("Advertenties en budget op maat")}{li("Conversiemeting op je site")}{li("Maandelijks rapport en bijsturen")}</ul>
<a class="btn btn-line" href="contact.html?dienst=Advertenties">Plan een kennismaking</a></article>
<article class="plan"><h3>Meta Ads</h3><p class="sub">Zichtbaar op Facebook en Instagram bij mensen in jouw doelgroep.</p>
<div class="amount"><strong>€295</strong><span>per maand</span></div><p class="terms">Eenmalig €895 voor gesprek, plan en opzet</p>
<ul>{li("Doelgroep en regio afgebakend")}{li("Teksten en beelden voor je advertenties")}{li("Testen welke advertentie het beste werkt")}{li("Maandelijks rapport en bijsturen")}</ul>
<a class="btn btn-line" href="contact.html?dienst=Advertenties">Plan een kennismaking</a></article>
<article class="plan pick"><span class="pick-note hand">beste resultaat</span><h3>Google en Meta</h3><p class="sub">Beide kanalen, op elkaar afgestemd voor het meeste bereik.</p>
<div class="amount"><strong>€495</strong><span>per maand</span></div><p class="terms">Eenmalig €1.495 voor gesprek, plan en opzet</p>
<ul>{li("Alles van Google Ads en Meta Ads")}{li("Eén strategie en één rapport")}{li("Voorrang bij vragen en aanpassingen")}{li("Kwartaalgesprek over de resultaten")}</ul>
<a class="btn btn-main" href="contact.html?dienst=Advertenties">Plan een kennismaking</a></article>
</div>
<p class="fine">Exclusief advertentiebudget en btw. Na 3 maanden per maand opzegbaar.</p>
</div>
</section>

<section class="sage">
<div class="wrap faq-grid">
<div><h2>Vragen over advertenties</h2></div>
<div>{faq([
 ("Hoeveel advertentiebudget heb ik nodig?", "Dat hangt af van je branche en regio, dat bespreken we in het eerste gesprek. Als richtlijn: reken op minimaal €300 per maand per kanaal."),
 ("Waarom betaal ik het budget zelf?", "Zo staat alles op jouw naam en zie je altijd precies waar je geld naartoe gaat. Ik beheer de campagnes, jij houdt de controle."),
 ("Hoe snel zie ik resultaat?", "De eerste weken zijn om te leren wat werkt. Daarna stuur ik bij op wat klanten oplevert. Ik beloof geen aantallen, wel eerlijkheid over wat er gebeurt."),
 ("Ik zit in de zorg, mag ik wel adverteren?", "Ja, maar Google en Meta hebben strengere regels voor zorg en medische diensten. Daar heb ik zelf ervaring mee vanuit mijn eigen praktijk, dus daar houd ik rekening mee."),
])}</div>
</div>
</section>

{cta("Klaar voor meer klanten?", "Plan een vrijblijvende kennismaking. We kijken samen of advertenties voor jouw bedrijf zinvol zijn.", "Plan een kennismaking", "contact.html?dienst=Advertenties")}
'''
page("advertenties.html", "Google Ads en Meta Ads | Headturners",
     "Google Ads en Meta Ads beheer voor ondernemers. Eerst een gesprek over je bedrijf, daarna campagnes die elke maand worden bijgestuurd.", ads)

# ---------------- SOCIAL & BLOGS ----------------
soc = f'''
<section class="page-hero">
<div class="wrap page-hero-grid">
<div>
{crumb("Social media en blogs")}
<h1>Zichtbaar blijven zonder er zelf naar om te kijken</h1>
<p class="lead">Geen tijd om te posten of te schrijven? Dat neem ik van je over. We beginnen met een gesprek over je bedrijf en je klanten, zodat alles klinkt als jij. Jij keurt alles goed voordat het online gaat.</p>
<div class="ctas"><a class="btn btn-main" href="contact.html?dienst=Social%20media">Plan een kennismaking</a><a class="btn btn-line" href="#prijzen">Bekijk prijzen</a></div>
</div>
<div class="note-card"><p class="hand">Eén blog, vijf posts.</p><p>Elke blog die ik schrijf, hergebruik ik als posts op je socials. Zo sluit alles op elkaar aan en haal je meer uit hetzelfde verhaal.</p></div>
</div>
</section>

<section class="sage" id="prijzen">
<div class="wrap">
<div class="head"><h2>Facebook en Instagram</h2><p>Een vast ritme van posts in jouw huisstijl. Ik plan ze in, zodat je profiel actief blijft.</p></div>
<div class="plans">
<article class="plan"><h3>Social Basis</h3><p class="sub">Voor een actief en verzorgd profiel.</p>
<div class="amount"><strong>€245</strong><span>per maand</span></div><p class="terms">Eenmalig €295 voor gesprek, contentplan en templates</p>
<ul>{li("8 posts per maand op Facebook en Instagram")}{li("Teksten en beelden in je huisstijl")}{li("Vooraf ter goedkeuring")}</ul>
<a class="btn btn-line" href="contact.html?dienst=Social%20media">Kies Social Basis</a></article>
<article class="plan pick"><span class="pick-note hand">meer bereik</span><h3>Social Plus</h3><p class="sub">Voor wie echt wil groeien met social media.</p>
<div class="amount"><strong>€395</strong><span>per maand</span></div><p class="terms">Eenmalig €295 voor gesprek, contentplan en templates</p>
<ul>{li("12 posts en 8 stories per maand")}{li("Teksten en beelden in je huisstijl")}{li("Maandrapport met wat werkte")}</ul>
<a class="btn btn-main" href="contact.html?dienst=Social%20media">Kies Social Plus</a></article>
</div>
</div>
</section>

<section>
<div class="wrap">
<div class="head"><h2>Blogs voor Google</h2><p>Blogs die antwoord geven op de vragen die jouw klanten in Google intypen. Zo word je beter gevonden en laat je zien dat je weet waar je het over hebt.</p></div>
<div class="plans three">
<article class="plan"><h3>Losse blog</h3><p class="sub">Voor een specifiek onderwerp.</p><div class="amount"><strong>€95</strong></div>
<ul>{li("700 tot 900 woorden")}{li("Met zoekwoorden voor Google")}{li("Geplaatst op je site")}</ul><a class="btn btn-line" href="contact.html?dienst=Blogs">Bestel een blog</a></article>
<article class="plan pick"><span class="pick-note hand">beste keuze</span><h3>2 blogs per maand</h3><p class="sub">Een vaste stroom nieuwe content.</p><div class="amount"><strong>€175</strong><span>per maand</span></div>
<ul>{li("Planning op basis van zoekwoordonderzoek")}{li("Geplaatst op je site")}{li("Vooraf ter goedkeuring")}</ul><a class="btn btn-main" href="contact.html?dienst=Blogs">Kies 2 per maand</a></article>
<article class="plan"><h3>4 blogs per maand</h3><p class="sub">Snel groeien in Google.</p><div class="amount"><strong>€325</strong><span>per maand</span></div>
<ul>{li("Alles van 2 per maand")}{li("Elke blog ook gedeeld op je socials")}{li("Kwartaaloverzicht van je vindbaarheid")}</ul><a class="btn btn-line" href="contact.html?dienst=Blogs">Kies 4 per maand</a></article>
</div>
<p class="fine">Alle prijzen exclusief btw. Maandpakketten na 3 maanden per maand opzegbaar.</p>
</div>
</section>

<section class="sage">
<div class="wrap faq-grid">
<div><h2>Vragen over content</h2></div>
<div>{faq([
 ("Wie schrijft de posts en blogs?", "Ik, op basis van ons gesprek over je bedrijf en je klanten. Je krijgt alles eerst te zien en pas na jouw akkoord gaat het online."),
 ("Moet ik zelf foto's aanleveren?", "Het hoeft niet, maar eigen foto's van jou, je team of je werk werken altijd beter dan standaardbeelden. Ik geef je tips wat je kunt fotograferen."),
 ("Waarom helpen blogs bij Google?", "Google wil zoekers het beste antwoord geven. Met blogs over vragen die jouw klanten stellen, laat je zien dat jij dat antwoord hebt."),
])}</div>
</div>
</section>

{cta("Laat je profiel voor je werken", "Plan een kennismaking. Ik laat je zien hoe een maand content er voor jouw bedrijf uit kan zien.", "Plan een kennismaking", "contact.html?dienst=Social%20media")}
'''
page("social-en-blogs.html", "Social media en blogs | Headturners",
     "Social media beheer voor Facebook en Instagram en blogs voor Google. In jouw stijl, vooraf door jou goedgekeurd.", soc)

# ---------------- SAMI CASE ----------------
from sami_page import SAMI_PAGE
SAMI_STORY = f'''
<section class="tight-sec">
<div class="wrap">
<a class="brand-teaser" href="rebranding-sami.html">
<img src="klanten/sami-na.jpg" alt="Nieuwe huisstijl en website van Sami's Acupunctuur" loading="lazy" width="1600" height="1000">
<div><p class="case-where">Loop het traject zelf door</p><h3>Hoe voelt het om je merk opnieuw neer te zetten?</h3><p>Kijk mee naar de oude site van Samia, kies je eigen woorden, schuif van koel naar warm en schrap wat niet nodig is.</p><span class="link">Start bij de koffie {ARROW}</span></div>
</a>
</div>
</section>
'''

# ---------------- BRANDING ----------------
brand = f'''
<section class="page-hero">
<div class="wrap page-hero-grid">
<div>
{crumb("Branding")}
<h1>Een merk dat klopt, van logo tot missie</h1>
<p class="lead">Nog geen eigen huisstijl, of past je uitstraling niet meer bij wie je bent? Samen bepalen we waar je voor staat, voor wie je het doet en hoe je eruitziet. Daarna klopt alles: je site, je socials en je advertenties.</p>
<div class="ctas"><a class="btn btn-main" href="contact.html?dienst=Branding">Plan een kennismaking</a><a class="btn btn-line" href="#prijzen">Bekijk prijzen</a></div>
</div>
<div class="note-card"><p class="hand">Eerst weten wie je bent, dan pas ontwerpen.</p><p>Een logo zonder verhaal is alleen een plaatje. Daarom beginnen we altijd met een gesprek over jou en je klanten.</p></div>
</div>
</section>

<section class="on-ink">
<div class="wrap">
<div class="head"><h2>Wat we samen bepalen</h2></div>
<div class="feat">
<div><b>Visie en missie</b><span>Waar je voor staat en waar je naartoe wilt.</span></div>
<div><b>Doelgroep</b><span>Wie je klanten zijn en wat ze belangrijk vinden.</span></div>
<div><b>Logo</b><span>Een logo dat past bij je bedrijf, in alle formaten die je nodig hebt.</span></div>
<div><b>Kleuren en letters</b><span>Een vast palet en lettertypes voor alles wat je maakt.</span></div>
<div><b>Tone of voice</b><span>Hoe je praat en schrijft tegen je klanten.</span></div>
<div><b>Stijlgids</b><span>Alles op een rij, zodat het altijd herkenbaar blijft.</span></div>
</div>
</div>
</section>

<section class="tight-sec">
<div class="wrap">
<a class="brand-teaser" href="rebranding-sami.html">
<img src="klanten/sami-na.jpg" alt="Nieuwe huisstijl en website van Sami's Acupunctuur" loading="lazy" width="1600" height="1000">
<div><p class="case-where">Voorbeeld</p><h3>Sami's Acupunctuur: van Jimdo site naar eigen merk</h3><p>Nieuw logo, warm palet, eigen domein en een site die rust uitstraalt. Lees welke stappen we hebben gezet.</p><span class="link">Loop het traject zelf door {ARROW}</span></div>
</a>
</div>
</section>

<section id="prijzen">
<div class="wrap">
<div class="head"><h2>Branding pakketten</h2></div>
<div class="plans">
<article class="plan"><h3>Branding Basis</h3><p class="sub">Voor wie snel een herkenbare uitstraling wil.</p>
<div class="amount"><strong>€795</strong><span>eenmalig</span></div>
<ul>{li("Eén gesprek over je bedrijf en klanten")}{li("Logo in alle formaten")}{li("Kleurenpalet en lettertypes")}{li("Korte stijlgids")}</ul>
<a class="btn btn-line" href="contact.html?dienst=Branding">Kies Basis</a></article>
<article class="plan pick"><span class="pick-note hand">het complete verhaal</span><h3>Branding Compleet</h3><p class="sub">Voor een merk met een duidelijk verhaal.</p>
<div class="amount"><strong>€1.695</strong><span>eenmalig</span></div>
<ul>{li("Twee sessies over visie, missie, kernwaarden en doelgroep")}{li("Logo, kleuren en lettertypes")}{li("Tone of voice")}{li("Uitgebreide stijlgids")}{li("Templates voor je social media")}</ul>
<a class="btn btn-main" href="contact.html?dienst=Branding">Kies Compleet</a></article>
</div>
<p class="fine">Exclusief btw. Combineer je branding met een nieuwe website en je krijgt €150 korting op de branding.</p>
</div>
</section>

{cta("Klaar om je merk neer te zetten?", "Plan een kennismaking en vertel me over je bedrijf. Daarna weet je precies wat het oplevert.", "Plan een kennismaking", "contact.html?dienst=Branding")}
'''
page("branding.html", "Branding: logo, huisstijl, visie en missie | Headturners",
     "Branding voor ondernemers: visie, missie, doelgroep, logo, kleuren, lettertypes en een stijlgids. Vanaf €795.", brand)

# ---------------- VOORBEELDEN ----------------
work = f'''
<section class="page-hero">
<div class="wrap">
{crumb("Voorbeelden")}
<h1>Ondernemers die je voorgingen</h1>
<p class="lead">Sleep het gele bolletje heen en weer om de oude en de nieuwe site te vergelijken. Klik door om de site live te bekijken.</p>
</div>
</section>
<section class="tight-top">
<div class="wrap"><div data-cases="99"></div></div>
</section>
{SAMI_STORY}
{cta("Wil jij de volgende zijn?", "Ik maak gratis een voorstel van je nieuwe homepage, zodat je het verschil meteen ziet.")}
'''
page("voorbeelden.html", "Voorbeelden van websites | Headturners",
     "Bekijk het verschil tussen de oude en nieuwe websites van ondernemers die met Headturners werken.", work)

# ---------------- OVER ----------------
over = f'''
<section class="page-hero">
<div class="wrap page-hero-grid">
<div>
{crumb("Over mij")}
<h1>Hoi, ik ben Mar</h1>
<p class="lead">Ik ben ondernemer, net als jij. Naast Headturners heb ik mijn eigen tandprothetische praktijk in Driebergen.</p>
</div>
<img src="klanten/mar-portret.jpg" alt="Mar, oprichter van Headturners" width="720" height="900" style="width:min(360px,100%);height:auto;justify-self:center;border:2px solid #1F2A44;border-radius:24px;box-shadow:10px 10px 0 #FFCF4A">
</div>
</section>
<section class="sage">
<div class="wrap split">
<div>
<h2>Waarom ik dit doe</h2>
<p class="lead" style="margin-top:18px">Je website is je visitekaartje. Vaak is het het eerste wat een klant van je ziet, en dan wil je dat hij laat zien wie je bent, precies zoals jij het voor je ziet.</p>
<p class="lead" style="margin-top:14px">Toen ik mijn praktijk begon, liep ik ertegenaan dat bureaus enorm veel geld vragen voor hun diensten. Dat kon ik als startende ondernemer niet betalen. Dus moest ik het zelf doen: mijn site, mijn advertenties, mijn social media.</p>
<p class="lead" style="margin-top:14px">Daardoor heb ik geleerd hoe het moet en wat echt werkt. Met die kennis help ik nu andere ondernemers, voor een eerlijke prijs.</p>
</div>
<div class="note-card"><p class="hand">Wat je van mij kunt verwachten</p><p>Eerlijk advies, ook als dat betekent dat iets niet nodig is. Begrijpelijke taal in plaats van vakjargon. En één aanspreekpunt dat je bedrijf echt kent.</p></div>
</div>
</section>
<section>
<div class="wrap">
<div class="head"><h2>Hoe ik werk</h2></div>
<div class="feat">
<div><b>Eerst laten zien</b><span>Je krijgt een gratis voorstel voordat je iets betaalt. Zo weet je waar je aan toe bent.</span></div>
<div><b>Persoonlijk</b><span>Geen accountmanagers of ticketsystemen. Je belt of appt gewoon met mij.</span></div>
<div><b>Duidelijke prijzen</b><span>Vaste bedragen, vooraf afgesproken. Geen verrassingen op de factuur.</span></div>
</div>
</div>
</section>
{cta("Zullen we kennismaken?", "Vertel me over je bedrijf. Ik denk graag met je mee, ook als je nog niet precies weet wat je nodig hebt.")}
'''
page("over.html", "Over Mar | Headturners",
     "Mar is ondernemer met een eigen praktijk en bouwt websites, advertenties en content voor andere ondernemers.", over)

# ---------------- CONTACT ----------------
contact = f'''
<section class="page-hero">
<div class="wrap contact-grid">
<div>
{crumb("Contact")}
<h1>Vraag je gratis voorstel aan</h1>
<p class="lead">Laat je gegevens achter. Ik bekijk je huidige site en socials en maak een voorstel van je nieuwe homepage, helemaal gratis.</p>
<div class="after-steps">
<div><div class="step-n">1</div><div><b>Je stuurt je aanvraag</b><span>Duurt een minuut. Je hoeft nog niets te beslissen.</span></div></div>
<div><div class="step-n">2</div><div><b>Ik maak je voorstel</b><span>Een homepage in jouw huisstijl, gebaseerd op je huidige site en socials.</span></div></div>
<div><div class="step-n">3</div><div><b>We bespreken het</b><span>We kijken samen wat je wilt aanpassen tot het helemaal klopt. Daarna beslis je pas, je zit nergens aan vast.</span></div></div>
</div>
<p class="check">{CHK}Geen kosten, geen verplichtingen</p>
</div>
<form class="card" id="aanvraag" novalidate>
<label>Je naam<input type="text" name="naam" autocomplete="name" placeholder="Bijvoorbeeld Sanne de Vries" required></label>
<label>Je mailadres<input type="email" name="email" autocomplete="email" placeholder="Zodat ik je voorstel kan sturen" required></label>
<label>Je bedrijf<input type="text" name="bedrijf" autocomplete="organization" placeholder="Bijvoorbeeld Bakkerij De Vries"></label>
<label>Telefoonnummer<input type="tel" name="telefoon" autocomplete="tel" placeholder="Zodat ik je even kan bellen"></label>
<label>Je huidige website of Instagram<input type="text" name="site" placeholder="Laat leeg als je nog geen site hebt"></label>
<fieldset style="border:0;padding:0;margin:0;display:grid;gap:8px"><legend style="font-weight:700;font-size:16px;margin-bottom:8px">Waar ben je in geïnteresseerd?</legend>
<div class="chips">
<label><input type="checkbox" name="dienst" value="Website" checked>Website</label>
<label><input type="checkbox" name="dienst" value="Advertenties">Advertenties</label>
<label><input type="checkbox" name="dienst" value="Social media">Social media</label>
<label><input type="checkbox" name="dienst" value="Blogs">Blogs</label>
<label><input type="checkbox" name="dienst" value="Branding">Branding</label>
</div></fieldset>
<label>Iets wat ik moet weten?<textarea name="bericht" placeholder="Optioneel"></textarea></label>
<button class="btn btn-main" type="submit">Vraag mijn gratis voorstel aan</button>
<p class="hp" aria-hidden="true"><label>Laat dit veld leeg<input type="text" name="website_url" tabindex="-1" autocomplete="off"></label></p>
<p class="form-note">Ik gebruik je gegevens alleen om je aanvraag te beantwoorden. Lees de <a href="privacyverklaring.html">privacyverklaring</a>.</p>
<p class="form-msg" id="form-msg" role="status" aria-live="polite"></p>
</form>
</div>
</section>
'''
page("contact.html", "Gratis voorstel aanvragen | Headturners",
     "Vraag gratis een voorstel aan voor je nieuwe website. Geen kosten, geen verplichtingen.", contact)

page("rebranding-sami.html", "De rebranding van Sami's Acupunctuur | Headturners",
     "Loop zelf het branding traject van Sami's Acupunctuur door: kijken, kiezen, voelen, schrappen en live.", SAMI_PAGE)

from legal import PAGES as LEGAL
for f, t, d, b in LEGAL:
    page(f, t, d, b)
