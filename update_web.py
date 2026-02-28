import re

html_path = r"c:\VC weby\lucie.svobodova\web lucie.svobodova\index.html"
css_path = r"c:\VC weby\lucie.svobodova\web lucie.svobodova\style.css"

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Odstranit kontaktní formulář (kolem řádku 375-403)
# Najít <div class="contact-form"> ... </div> a smazat.
# Dáme to tam přesně (v contact.grid je .contact-info a .contact-form)
start_idx = html.find('<div class="contact-form">')
if start_idx != -1:
    end_idx = html.find('</div>\n\n                </div>\n            </div>\n        </section>', start_idx)
    if end_idx != -1:
        # replace just the form
        html = html[:start_idx] + '</div>\n            </div>\n        </section>' + html[end_idx + len('</div>\n\n                </div>\n            </div>\n        </section>'):]

# 2. Nedávej text na střed kromě nadpisů sekcí
# Tzn. "text-center reveal" předělám na ".section-header reveal" a upravím CSS.
html = html.replace('class="text-center reveal"', 'class="section-header reveal"')
# Taktéž odstavec s textem pod nadpisem "Ceník" byl centerován přes .text-center
html = html.replace('class="text-center reveal" style="margin-top: 2rem;"', 'class="section-footer reveal" style="margin-top: 2rem;"')

# Chtěli "různé prvky které se budou prolínat tak aby to vyplnilo šířku webu" a "čisté linie".
# Nahradíme `<section id="..." class="container">` za plnou šířku a vložíme do něj kontejner.
for s in ['sluzby', 'cenik', 'o-mne', 'kontakt']:
    old_sec = f'<section id="{s}" class="container">'
    new_sec = f'''<section id="{s}" class="modern-section">
            <!-- Dekorativni ciste linie prolínající celou šířku -->
            <div class="decor-line-h"></div>
            <div class="decor-line-v"></div>
            <div class="decor-box-1" aria-hidden="true"></div>
            <div class="decor-box-2" aria-hidden="true"></div>
            <div class="container container-relative">'''
    html = html.replace(old_sec, new_sec)

# A najít každý uzavírací tag sekcí a přidat </div> před </section> pro příslušné sekce
html = html.replace('</section>', '</div>\n        </section>')
# Ale sekce "hero" nebyla změněna. hero section:
# <section class="hero" id="domu"> ... </section>
# Tu musím opravit zpět.
html = html.replace('</div>\n        </section>\n\n\n        <!-- Služby Section (Bento Grid) -->', '</section>\n\n\n        <!-- Služby Section (Bento Grid) -->')
# To se týká i hero section uzavíracího tagu. Bude bezpecnejsi to projit a pro kazdou upravenou sekci zavrit.
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
