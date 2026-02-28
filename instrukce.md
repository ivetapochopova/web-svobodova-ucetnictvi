(zadání pro AI agenta k tvorbě webu)

**Situace**
Jsi zkušený webový vývojář a designér s expertízou v tvorbě moderních, responzivních webových stránek. Tvým úkolem je vytvořit kompletní malý web podle specifikací níže.

**Cíl**
Dodej uživateli kompletní, profesionální mobile-first webovou stránku, která je vizuálně atraktivní, funkční na všech zařízeních a připravená k okamžitému použití.

**Úkol**
Vytvoř funkční web, který bude obsahovat:
•	Strukturovaný komentovaný HTML5 kód s validní sémantikou
•	Responzivní design (mobile-first přístup)
•	CSS styly pro přizpůsobení všem obrazovkám (4K monitory, desktop, tablet, mobil)
•	Používej moderní CSS vlastnosti (CSS variables, transitions, animations)
•	CSS jednotky velikosti: pro běžný text použij rem, pro nadpisy použij clamp 
•	Základní JavaScript pro interaktivitu (na jemné oživení stránek)
•	Dbej na bezpečnost webu (nastavení bezpečnostní HTTP hlavičky, u kontaktního formuláře řeš ochranu proti spamu pomocí honeypot)
•	Nedávej do soubor .htaccess pokyny k přesměrování (to se řeší na úrovni hostingu)

**Znalosti**
•	Zajisti rychlé načítání a optimalizovaný výkon
•	Dodržuj best practices pro přístupnost (barevný kontrast, velikost písma, ARIA)
•	Vlož favicon ve formát svg (pokud ho nemáš dodaný, vytvoř ho)
•	Pokud je potřeba Cookie lišta, vytvoř ji v barvách webu


**Základní SEO**
•	Strukturuj nadpisy H1-H6
•	Přidej meta title a description na každé stránce
•	Vytvoř strukturovaná data – LocalBusiness, FAQ, Article (pokud je to relevantní)
•	Přidej do adresáře soubory sitemap.xml, robot.txt a llms.txt
•	Urči kanonickou url
•	Obrázkům dej alt popisky
•	Propoj stránky vnitřními odkazy
•	Vytvoř Open Graph meta tagy (náhled webu pro Facebook a další sociální sítě)


**Optimalizace obrázků**
•	Přidej lazy loading ke všem obrázkům, které nejsou vidět hned při načtení stránky (below the fold). Tj. u hero sekce lazy loading nedělej.
•	Obrázky ti dodám zkomprimované ve formátu jpg nebo png, ale kdyby se ti zdály velké, řekni si o formát avif.
**Vizuální hierarchie a čitelnost**
•	Jasná typografická hierarchie (nadpisy H1-H6, konzistentní velikosti)
•	Dostatečný kontrast mezi textem a pozadím (minimum 4.5:1 pro běžný text)
•	Čitelné fonty s českou diakritikou, minimální velikost 16px
•	Správné řádkování (line-height 1.5-1.8 pro odstavce)
•	Nikdy nezarovnávej text do bloku
•	Maximální šířka textu 70% obrazovky (nikdy nepiš od kraje po kraj)

**Layout**
•	Šířku celého webu dej na 85% obrazovky
•	Jasné oddělení sekcí a obsahových celků
•	Pokud mám v sekci 4 karty/boxy – dej je po dvou na řádek (ne 3+1)
•	Vyvážené použití bílého prostoru (white space)
•	Intuitivní navigace - logo vlevo, hamburger menu na mobilu pravo
•	Dej si záležet na patičce webu
•	U prvku accordion (př. pro otázky a odpovědi) dávej ikonu šipky dolů a nahoru a pokud je jich víc než 3, tak je rozděl do dvou sloupců
•	Jednopísmenové znaky (spojky, předložky) zalamuj na nový řádek
•	Jednotky (Kč, m, kg, Eur, atd.) spoj s číslem nedělitelnou mezerou
•	Datum piš ve formátu 1. 1. 2026 a mezery dej nedělitelné

**Obsah**
•	Stručné a srozumitelné texty
•	Výrazné nadpisy s klíčovými informacemi a CTA tlačítka
•	Vizuální prvky podporující obsah (ikony, obrázky, grafika)
•	Logické uspořádání informací (nejdůležitější nahoře)
•	Chybová stránka (místo „404“ dej ikonu <wa-icon name="face-frown" variant="regular"></wa-icon>) a přidej ji na web pomocí příkazu v souboru .htaccess: ErrorDocument 404 /404.html
•	Kontrola povinných údajů na webu: jméno, sídlo, IČ, zápis v rejstříku

**Konzistence**
•	Jednotný styl tlačítek, karet a komponent
•	Stejný padding/margin napříč podobnými elementy
•	Stejné zaoblení prvků
•	Konzistentní ikonografie (používej font awesome, ne emotikony)
•	Stíny karet pouze velmi jemné
•	Jednotný projev značky (brand voice)
•	Konzistentní použití barev napříč celým webem
•	Jednotný spacing a odsazení (používej jednotný systém, např. 8px grid)

**Barevná paleta**
•	Omezený počet barev (2-3 hlavní + neutrální)
•	Primární barva pro CTA (call-to-action) tlačítka
•	Neutrální jemné barvy pro pozadí 
•	Pro text #111E5A
•	Brand barvy (HEX): 
   - primární: #111E5A
   - sekundární: #8CAEFE
   - tlačítka: #FEB994
   - pozadí: #FFFFF2
   - text: [#111E5A]

**Fonty**
•	Zvol vhodný patkový nebo bezpatkový font podle obsahu webu
•	Pokud není jasné, zvol moderní sans-serif font (př. Outfit)
•	Brandový font: Source Sans 3
•	
**Struktura**
•	Jednostránkový web
•	Menu bude v barvě #070F37
•	Položky menu:
Služby 
O mně 
Ceník 
Kontakt


**Design**
Design hero sekce (celého webu) vytvoř podle vzoru, který ti dám před začátkem tvorby ve formátu jpg 
nebo
Vytvoř moderní mobile-first web: použít můžeš trendy jako souměrný bento grid layout se zaoblenými rohy, velká typografie, barevné gradienty, glass efekt, micro-animace na hover a scroll efekty či 3D prvky.
**Moderní design**
•	Layout: používej souměrný Bento grid 
•	Barvy: Jemné gradienty, plynulé přechody
•	Prvky: Zaoblené rohy (border-radius 16-24px), 3D prvky
•	Glass efekt: Skleněný efekt v pozadí karet (glassmorphism)
•	Animace: Mikro interakce na hover, jemné scroll animace 
•	Minimalistický čistý design
**obrázky**
Na webu použij fotky (př. přílohy), které najdeš ve složce 
Obrazky

**texty**
Vyjdi z dodaných textů, ale když budeš potřebovat, můžeš je mírně změnit nebo doplnit, zachovej vždy smysl a podstatu obsahu stránky. 
Hero sekce

Za každým dobrým rozhodnutím stojí správná čísla.

Trávíte nad účetnictvím víc času, než byste chtěli?
Nejste si jistí, jestli máte všechno v pořádku?
Chcete mít v číslech jasno a klid v hlavě?

Pomáhám firmám, podnikatelům i neziskovým organizacím mít účetnictví v pořádku, přehledné a srozumitelné.
Zakládám si na přesnosti účetních dat, správné aplikaci účetních standardů a transparentním reportingu.
Díky spolehlivým finančním výstupům získáte pevný základ pro kvalifikovaná rozhodnutí a klid v podnikání.


SLUŽBY

Jednoduché účetnictví (neziskový sektor)
Převezmu za vás administrativu i odpovědnost za účetní agendu, abyste se mohli naplno věnovat veřejně prospěšným aktivitám.
Zajistím pro vás:
vedení jednoduchého účetnictví
kontrolu náležitostí účetních dokladů
sledování zákonných termínů
přehledné výstupy pro vedení organizace
<!-- Slogan: Papíry a čísla nechte na mně. Vy se můžete plně soustředit na svou činnost. -->


Daňová evidence (OSVČ a drobní podnikatelé)

Zajistím kompletní vedení daňové evidence v souladu s aktuální legislativou.
Součástí služby je:
evidence příjmů a výdajů
evidence majetku a závazků
příprava podkladů pro daňové přiznání
průběžná kontrola daňových povinností



Účetní poradenství

Poskytuji odborné konzultace v oblasti účetnictví a daňové problematiky.
Pomohu vám správně nastavit procesy, zjednodušit administrativu a předcházet zbytečným chybám i rizikům.



Reporting a analýzy na míru

Účetnictví nemusí být jen zákonná povinnost.
Připravím pro vás manažerské reporty a přehledy, které vám pomohou lépe řídit firmu a dělat informovaná rozhodnutí.


Co získáte spoluprací

Úlevu od administrativy – profesionální zpracování vašich dokladů a administrativy
Individuální přístup – účetnictví nastavím podle vašich konkrétních potřeb
Online spolupráci – pracuji s klienty po celé České republice
Průběžnou podporu – konzultace a poradenství, kdykoliv je potřeba
Hlídání termínů a změn v legislativě
Manažerské přehledy pro lepší orientaci ve vašich číslech
Diskrétnost a důvěru – vaše informace jsou v bezpečí


CENÍK

Uvedené ceny jsou orientační.
Úvodní konzultaci poskytuji zdarma – během ní probereme vaše potřeby a navrhnu nejvhodnější řešení. Pro konkrétní nabídku mě prosím kontaktujte.

Přiznání k dani z příjmů fyzické osoby ze závislé činnosti: od 500 Kč

Přiznání k dani z příjmů OSVČ včetně přehledů ZP a SP: od 2 000 Kč

Mzdová agenda: 200 Kč / zaměstnanec

Daňová evidence pro OSVČ: od 500 Kč / měsíc

Podvojné účetnictví pro podnikatele: od 1 500 Kč / měsíc

Nezisková organizace: od 2 000 Kč / rok


O MNĚ

Jmenuji se Lucie a v oblasti účetnictví a financí působím více než 15 let.
Během své praxe jsem získala zkušenosti z interního i externího účetnictví, auditu i controllingu. Díky tomu dokážu vnímat finance v širších souvislostech a propojovat přesnost účetnictví s reálnými potřebami managementu.

Jsem členkou Komory certifikovaných účetních a vystudovala jsem finance a účetnictví na Vysoké škole ekonomické v Praze.
Ve své práci kladu důraz na správnost, transparentnost a spolehlivost účetních výstupů.

Pracuji systematicky, pečlivě a zodpovědně. Neustále sleduji legislativní změny i novinky v oblasti financí a průběžně si rozšiřuji odborné znalosti.
Zakládám si na férové komunikaci, diskrétnosti a individuálním přístupu ke každému klientovi.


KONTAKT

Máte zájem o spolupráci nebo se chcete jen nezávazně poradit?
Ozvěte se mi a domluvíme si úvodní konzultaci zdarma.
