import re

html_path = r"c:\VC weby\lucie.svobodova\web lucie.svobodova\index.html"

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove contact form
start_idx = html.find('<div class="contact-form">')
end_idx = html.find('</div>', html.find('</div>', html.find('</div>', start_idx) + 1) + 1) 
# wait, better regex
form_regex = r'<div class="contact-form">.*?</form>\s*</div>'
html = re.sub(form_regex, '', html, flags=re.DOTALL)

# Also update the CSS grid for contact info, we might not need the grid or we center it.
html = html.replace('<div class="contact-grid">', '<div class="contact-grid no-form">')

# Modify text-center
html = html.replace('class="text-center reveal"', 'class="section-header reveal"')

# The sluzby container and others -> wrapping sections in full-width modern sections
sections = ['sluzby', 'cenik', 'o-mne', 'kontakt']
for sec in sections:
    html = html.replace(f'<section id="{sec}" class="container">', 
f'''<section id="{sec}" class="modern-section">
            <div class="decor-line-h decor-top-30"></div>
            <div class="decor-line-v decor-left-10"></div>
            <div class="decor-line-v decor-right-20"></div>
            <div class="decor-box decor-pos-{sec}"></div>
            <div class="container container-relative">''')

# Close the new container div before each </section> except hero
html = re.sub(r'(\s*)</section>', r'\1    </div>\n\1</section>', html)
# Fix hero: hero doesn't have the new wrapper, so hero gets an extra </div> which is bad.
# Wait, let's fix only the chosen ones.
# Actually hero is `<section class="hero" id="domu">` so `</section>` might appear for hero.
# Revert the hero one if modified.
html = html.replace('''            <div class="hero-cta reveal" style="transition-delay: 0.3s;">
                    <a href="#kontakt" class="btn btn-primary">Chci mít v číslech jasno</a>
                </div>

            </div>
        </div>
        </section>''', '''            <div class="hero-cta reveal" style="transition-delay: 0.3s;">
                    <a href="#kontakt" class="btn btn-primary">Chci mít v číslech jasno</a>
                </div>

            </div>
        </section>''')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
