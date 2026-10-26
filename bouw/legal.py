# Legal pages for Headturners. Plain HTML bodies, used by build.py
OWNER = "Maryam Al Neema"
ADRES = "[adres]"
KVK = "[KvK nummer]"
MAIL = "info@headturners.nl"
DATUM = "26 oktober 2026"


def doc(title, intro, body):
    return f'''
<section class="page-hero legal-hero">
<div class="wrap narrow-legal">
<p class="crumb"><a href="index.html">Home</a> &nbsp;/&nbsp; {title}</p>
<h1>{title}</h1>
<p class="lead">{intro}</p>
<p class="legal-date">Laatst bijgewerkt op {DATUM}</p>
</div>
</section>
<section class="tight-top">
<div class="wrap narrow-legal legal">
{body}
</div>
</section>
'''


WIE = f'''<p><b>Headturners B.V.</b><br>{ADRES}<br>KvK: {KVK}<br>Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>'''

PRIVACY = doc("Privacyverklaring",
 "Hoe Headturners omgaat met je persoonsgegevens. Kort en duidelijk, zonder kleine lettertjes.", f'''
<h2>Wie is verantwoordelijk</h2>
<p>Headturners B.V. is verantwoordelijk voor de verwerking van je persoonsgegevens zoals beschreven in deze verklaring. Aanspreekpunt is {OWNER}.</p>
{WIE}

<h2>Welke gegevens ik verwerk</h2>
<p><b>Als je het contactformulier invult of mij mailt:</b> je naam, bedrijfsnaam, mailadres, telefoonnummer, je huidige website of Instagram, waar je interesse in hebt en wat je zelf in je bericht zet.</p>
<p><b>Als je klant wordt:</b> daarnaast je adres, KvK nummer, btw nummer, factuurgegevens en de afspraken die we maken. Voor de uitvoering van de opdracht verwerk ik ook wat je aanlevert, zoals teksten, foto's en logo's.</p>
<p><b>Als je de website bezoekt:</b> de server van mijn hostingpartij slaat technische gegevens op, zoals je IP adres, het tijdstip en de pagina die je bekijkt. Dat is nodig om de site veilig en bereikbaar te houden. Ik gebruik geen analytische of advertentiecookies en volg je niet.</p>

<h2>Voorstellen voor bedrijven</h2>
<p>Ik maak soms uit eigen beweging een gratis voorstel voor een nieuwe homepage van een bedrijf. Daarvoor gebruik ik alleen openbare bedrijfsinformatie, zoals de huidige website, openbare socials en het openbare zakelijke mailadres. Het voorstel staat op een aparte link die nergens wordt gedeeld behalve met dat bedrijf, en wordt niet door zoekmachines opgenomen. Wil je dat ik je voorstel verwijder of je niet meer benader, stuur dan een mail. Ik doe dat dan direct.</p>

<h2>Waarvoor ik je gegevens gebruik</h2>
<ul>
<li>Om je aanvraag te beantwoorden en je een voorstel te sturen.</li>
<li>Om de opdracht uit te voeren: je website, advertenties, content of branding.</li>
<li>Om te factureren en mijn administratie bij te houden.</li>
<li>Om de website veilig en bereikbaar te houden.</li>
</ul>

<h2>Op welke grond</h2>
<ul>
<li><b>Overeenkomst:</b> als je klant bent of een voorstel aanvraagt, heb ik je gegevens nodig om de afspraak uit te voeren.</li>
<li><b>Wettelijke plicht:</b> facturen en administratie moet ik zeven jaar bewaren voor de Belastingdienst.</li>
<li><b>Gerechtvaardigd belang:</b> om bedrijven met een zwakke website een voorstel te doen en om de website te beveiligen.</li>
</ul>

<h2>Hoe lang ik gegevens bewaar</h2>
<ul>
<li>Contactaanvragen die geen opdracht worden: maximaal 12 maanden.</li>
<li>Klantgegevens en de afspraken over de opdracht: zolang je klant bent en daarna 2 jaar.</li>
<li>Facturen en administratie: 7 jaar, zoals de wet voorschrijft.</li>
<li>Technische serverlogs: maximaal 3 maanden.</li>
</ul>

<h2>Met wie ik gegevens deel</h2>
<p>Ik verkoop je gegevens nooit. Ik deel ze alleen met partijen die nodig zijn om mijn werk te doen:</p>
<ul>
<li><b>Cloud86</b> in Nederland, voor de hosting van websites en de mail.</li>
<li><b>GitHub</b>, voor het online zetten van voorstellen. GitHub kan gegevens buiten de Europese Unie opslaan, met de passende waarborgen die de wet vraagt.</li>
<li><b>Google en Meta</b>, alleen als je advertenties bij mij afneemt. De advertenties lopen dan via jouw eigen account bij die partijen.</li>
<li>Mijn boekhoudpakket en, als dat nodig is, de Belastingdienst.</li>
</ul>
<p>Met partijen die gegevens voor mij verwerken maak ik afspraken over beveiliging en geheimhouding.</p>

<h2>Beveiliging</h2>
<p>De website en de mail lopen via een beveiligde verbinding. Toegang tot klantgegevens is beschermd met sterke wachtwoorden en ik bewaar niet meer dan nodig.</p>

<h2>Jouw rechten</h2>
<p>Je mag je gegevens inzien, laten aanpassen of laten verwijderen. Je kunt ook bezwaar maken tegen het gebruik ervan, het gebruik laten beperken of je gegevens opvragen om aan een ander te geven. Stuur een mail naar <a href="mailto:{MAIL}">{MAIL}</a>. Ik reageer binnen vier weken.</p>
<p>Ben je het niet eens met hoe ik met je gegevens omga, dan kun je een klacht indienen bij de Autoriteit Persoonsgegevens via autoriteitpersoonsgegevens.nl. Ik hoor het natuurlijk het liefst eerst zelf.</p>

<h2>Wijzigingen</h2>
<p>Ik pas deze verklaring aan als dat nodig is. De datum bovenaan laat zien wanneer dat voor het laatst is gebeurd.</p>
''')

COOKIES = doc("Cookieverklaring",
 "Welke cookies headturners.nl gebruikt. Het korte antwoord: alleen wat nodig is om de site te laten werken.", f'''
<h2>Wat zijn cookies</h2>
<p>Cookies zijn kleine bestanden die een website op je computer of telefoon zet. Sommige zijn nodig om een site te laten werken, andere worden gebruikt om je te volgen of advertenties te tonen.</p>

<h2>Welke cookies deze site gebruikt</h2>
<p>Deze website gebruikt <b>geen</b> analytische cookies, <b>geen</b> advertentiecookies en <b>geen</b> cookies van sociale media. Ik volg je niet en maak geen profiel van je.</p>
<div class="table-wrap"><table class="table">
<thead><tr><th>Cookie</th><th>Waarvoor</th><th>Bewaartermijn</th></tr></thead>
<tbody>
<tr><td>wordpress_test_cookie</td><td>Controleert of je browser cookies accepteert. Alleen bij het inloggen.</td><td>Tot je de browser sluit</td></tr>
<tr><td>wordpress_logged_in, wordpress_sec</td><td>Houdt beheerders ingelogd. Gewone bezoekers krijgen deze cookies niet.</td><td>Tot 14 dagen</td></tr>
<tr><td>wp_settings</td><td>Onthoudt instellingen van het beheerscherm. Alleen voor beheerders.</td><td>1 jaar</td></tr>
</tbody></table></div>
<p>Dit zijn functionele cookies. Daarvoor is volgens de wet geen toestemming nodig, en daarom zie je op deze site geen cookiemelding.</p>

<h2>Lettertypes en andere diensten</h2>
<p>De lettertypes staan op de eigen server van deze website. Er worden dus geen gegevens naar Google of andere partijen gestuurd als je de site bezoekt. Links naar andere websites, zoals de sites van klanten, openen pas als je erop klikt. Die sites hebben hun eigen cookiebeleid.</p>

<h2>Cookies verwijderen of blokkeren</h2>
<p>Je kunt cookies altijd zelf verwijderen of blokkeren via de instellingen van je browser. De site blijft dan gewoon werken.</p>

<h2>Vragen</h2>
<p>Heb je een vraag over cookies of privacy, mail dan naar <a href="mailto:{MAIL}">{MAIL}</a>. Lees ook de <a href="privacyverklaring.html">privacyverklaring</a>.</p>
''')


def art(n, title, items):
    lis = "".join(f"<li>{t}</li>" for t in items)
    return f'<h2>Artikel {n}. {title}</h2>\n<ol class="legal-ol">{lis}</ol>\n'


AV_BODY = (
 art(1, "Definities", [
  "<b>Headturners</b>: Headturners B.V., ingeschreven bij de KvK onder nummer " + KVK + ".",
  "<b>Klant</b>: het bedrijf of de persoon die een opdracht geeft aan Headturners.",
  "<b>Opdracht</b>: alle werkzaamheden die Headturners voor de klant doet, zoals het maken of verhuren van een website, beheer, advertenties, social media, blogs en branding.",
  "<b>Voorstel</b>: een ontwerp of uitwerking die Headturners vooraf en gratis maakt, zodat de klant kan zien wat hij krijgt.",
  "<b>Huursite</b>: een website die de klant voor een vast bedrag per maand huurt.",
  "<b>Koopsite</b>: een website die de klant in één keer koopt.",
 ]) +
 art(2, "Toepasselijkheid", [
  "Deze voorwaarden gelden voor alle voorstellen, offertes en opdrachten van Headturners.",
  "Voorwaarden van de klant gelden niet, tenzij Headturners daar schriftelijk mee akkoord gaat.",
  "Spreken de offerte en deze voorwaarden elkaar tegen, dan geldt wat in de offerte staat.",
 ]) +
 art(3, "Gratis voorstel", [
  "Een voorstel is gratis en vrijblijvend. De klant zit nergens aan vast.",
  "Het voorstel en alle rechten erop blijven van Headturners zolang er geen opdracht is. De klant mag het voorstel niet zelf gebruiken of door een ander laten nabouwen.",
  "Wordt het voorstel geen opdracht, dan haalt Headturners het op verzoek offline.",
 ]) +
 art(4, "Offerte en opdracht", [
  "Een offerte is 30 dagen geldig.",
  "De opdracht begint zodra de klant de offerte per mail of schriftelijk heeft geaccepteerd.",
  "Alle prijzen zijn in euro en exclusief btw, tenzij anders vermeld.",
 ]) +
 art(5, "Uitvoering en medewerking", [
  "Headturners voert de opdracht zo goed mogelijk uit, met de zorg die je van een vakkundig bureau mag verwachten.",
  "De klant levert op tijd de informatie, teksten, foto's en toegang die nodig zijn. Vertraging door de klant kan de planning en de prijs veranderen.",
  "De klant staat ervoor in dat hij de rechten heeft op alles wat hij aanlevert, zoals foto's, teksten en logo's. De klant vrijwaart Headturners tegen claims van anderen hierover.",
  "Headturners mag de opdracht laten uitvoeren door derden als dat nodig is. Headturners blijft het aanspreekpunt.",
 ]) +
 art(6, "Aanpassingen en meerwerk", [
  "Bij elke website horen twee correctierondes tijdens het bouwen. Wensen daarna zijn meerwerk.",
  "Meerwerk kost €65 per uur, of een vaste prijs als dat vooraf is afgesproken. Een losse kleine aanpassing, zoals een tekst, foto of openingstijden, kost €45.",
  "Bij een huursite of beheerpakket zit een vast aantal minuten aanpassingen per maand inbegrepen. Ongebruikte minuten vervallen aan het eind van de maand.",
 ]) +
 art(7, "Huursite", [
  "Een huursite heeft een minimale looptijd van 12 maanden. Daarna loopt de huur per maand door en kan de klant per maand opzeggen, met een opzegtermijn van één maand.",
  "Bij de huur zitten hosting en het afgesproken aantal minuten aanpassingen per maand inbegrepen. De domeinnaam en back ups zijn niet inbegrepen, tenzij dat apart is afgesproken.",
  "De huursite blijft eigendom van Headturners. De klant krijgt het recht om de site te gebruiken zolang de huur loopt en betaald wordt.",
  "Na de minimale looptijd kan de klant de site overnemen voor het bedrag dat op de website of in de offerte staat. Hoe langer de klant huurt, hoe lager dat bedrag. Na betaling wordt de site eigendom van de klant.",
  "Zegt de klant op zonder de site over te nemen, dan gaat de site aan het eind van de huur offline. De domeinnaam blijft van de klant. Teksten en foto's die de klant zelf heeft aangeleverd krijgt hij op verzoek terug.",
  "Betaalt de klant niet op tijd, dan mag Headturners de site na een herinnering tijdelijk offline halen tot er betaald is.",
 ]) +
 art(8, "Koopsite", [
  "Bij een koopsite betaalt de klant 50 procent bij akkoord op de offerte en 50 procent bij oplevering, tenzij iets anders is afgesproken.",
  "Na volledige betaling is de site van de klant. Headturners mag de site in haar portfolio laten zien, tenzij de klant dat niet wil.",
  "Hosting, onderhoud en aanpassingen na oplevering zijn niet inbegrepen. Daarvoor kan de klant een beheerpakket afnemen.",
 ]) +
 art(9, "Beheer, hosting en back ups", [
  "Beheerpakketten en back ups lopen per maand en zijn per maand opzegbaar, met een opzegtermijn van één maand.",
  "Headturners zorgt voor updates en beveiliging volgens het gekozen pakket. Een website is nooit volledig te beveiligen. Headturners is niet aansprakelijk voor schade door hacks of storingen bij de hostingpartij, tenzij Headturners zelf ernstig tekort is geschoten.",
  "Heeft de klant geen back ups afgenomen, dan kan Headturners een site na een storing niet altijd terugzetten.",
 ]) +
 art(10, "Advertenties", [
  "Het advertentiebudget betaalt de klant rechtstreeks aan Google, Meta of het andere platform. Dat budget is niet inbegrepen in de prijs van Headturners.",
  "Advertentiepakketten hebben een minimale looptijd van 3 maanden. Daarna zijn ze per maand opzegbaar, met een opzegtermijn van één maand.",
  "Headturners zet de campagnes op en stuurt ze bij, maar kan geen garantie geven op een bepaald aantal klanten, klikken of omzet.",
  "De klant blijft eigenaar van zijn advertentieaccounts en de gegevens daarin. De klant houdt zich aan de regels van het platform.",
 ]) +
 art(11, "Social media en blogs", [
  "Maandpakketten voor social media en blogs hebben een minimale looptijd van 3 maanden. Daarna zijn ze per maand opzegbaar, met een opzegtermijn van één maand.",
  "Headturners legt berichten en blogs vooraf ter goedkeuring voor, tenzij de klant aangeeft dat dat niet nodig is. Wat de klant goedkeurt of niet binnen 5 werkdagen afkeurt, mag Headturners plaatsen.",
  "Na betaling mag de klant de geleverde teksten en beelden vrij gebruiken.",
 ]) +
 art(12, "Branding", [
  "Bij een brandingtraject horen de afgesproken sessies en twee correctierondes op het ontwerp.",
  "Na volledige betaling krijgt de klant alle rechten op het definitieve logo en de huisstijl. Schetsen en ontwerpen die niet zijn gekozen blijven van Headturners.",
 ]) +
 art(13, "Intellectueel eigendom", [
  "Alle rechten op ontwerpen, code en teksten van Headturners blijven bij Headturners, behalve wat in deze voorwaarden of de offerte aan de klant wordt overgedragen.",
  "Headturners mag geleverd werk laten zien in haar portfolio en op social media, tenzij de klant laat weten dat niet te willen.",
 ]) +
 art(14, "Betaling", [
  "Facturen moeten binnen 14 dagen worden betaald.",
  "Maandbedragen worden vooraf per maand gefactureerd.",
  "Betaalt de klant niet op tijd, dan stuurt Headturners een herinnering. Wordt daarna nog steeds niet betaald, dan mag Headturners de wettelijke handelsrente en redelijke incassokosten rekenen, en het werk stilleggen tot er betaald is.",
  "Headturners mag prijzen één keer per jaar aanpassen. Dat wordt minstens één maand van tevoren gemeld. Bij een stijging van meer dan 10 procent mag de klant de overeenkomst per die datum opzeggen.",
 ]) +
 art(15, "Aansprakelijkheid", [
  "De aansprakelijkheid van Headturners is beperkt tot het bedrag dat de klant voor de betreffende opdracht heeft betaald, en bij maandpakketten tot het bedrag van de laatste 3 maanden.",
  "Headturners is niet aansprakelijk voor indirecte schade, zoals gemiste omzet, gemiste klanten of verloren gegevens.",
  "Deze beperkingen gelden niet bij opzet of grove schuld van Headturners.",
 ]) +
 art(16, "Overmacht", [
  "Bij overmacht, zoals storingen bij hosting of platforms, ziekte of andere omstandigheden buiten de macht van Headturners, worden de verplichtingen opgeschort zolang de overmacht duurt.",
  "Duurt de overmacht langer dan 2 maanden, dan mogen beide partijen de overeenkomst beëindigen zonder schadevergoeding.",
 ]) +
 art(17, "Geheimhouding en privacy", [
  "Beide partijen houden vertrouwelijke informatie van de ander geheim.",
  'Headturners gaat met persoonsgegevens om volgens de <a href="privacyverklaring.html">privacyverklaring</a>. Verwerkt Headturners voor de klant persoonsgegevens van diens klanten, dan maken we daar op verzoek een verwerkersovereenkomst voor.',
 ]) +
 art(18, "Toepasselijk recht", [
  "Op alle afspraken met Headturners is Nederlands recht van toepassing.",
  "Komen we er samen niet uit, dan gaat een geschil naar de bevoegde rechter in het arrondissement Midden Nederland.",
 ])
)

AV = doc("Algemene voorwaarden",
 "De afspraken die gelden als je met Headturners werkt. Heb je een vraag over een artikel, mail me gerust.", AV_BODY)

PAGES = [
 ("privacyverklaring.html", "Privacyverklaring | Headturners", "Hoe Headturners omgaat met je persoonsgegevens.", PRIVACY),
 ("cookieverklaring.html", "Cookieverklaring | Headturners", "Welke cookies headturners.nl gebruikt.", COOKIES),
 ("algemene-voorwaarden.html", "Algemene voorwaarden | Headturners", "De algemene voorwaarden van Headturners.", AV),
]
