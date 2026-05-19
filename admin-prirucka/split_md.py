import os
import re

input_file = 'ISSR_lokaladmin.md' 
output_dir = 'admin-prirucka'  # Směřuje do složky pro administrátorskou příručku

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Načtení s utf-8-sig pro bezpečné odstranění případného BOM znaku
with open(input_file, 'r', encoding='utf-8-sig') as f:
    content = f.read()

# REGEX NA MÍRU: Vyhledá "# " + volitelný <span> tag + tučný horní index **<sup>číslo</sup>**
# Díky tomu přesně zachytí kapitoly 1 až 5 a ignoruje podsekce jako "# 5.2.1"
pattern = r'\n(?=# (?:<span[^>]*></span>)?\*\*<sup>\d+</sup>\*\*)'
chapters = re.split(pattern, '\n' + content)

for i, chapter in enumerate(chapters):
    chapter = chapter.strip()
    if not chapter:
        continue
    
    # Získání prvního řádku (syrový nadpis s tagy)
    first_line_raw = chapter.split('\n')[0]
    
    # Vyčištění nadpisu pro potřeby VitePress frontmatter
    first_line_clean = re.sub(r'<[^>]+>', '', first_line_raw)  # Odstraní <span> a <sup>
    first_line_clean = re.sub(r'\*\*[\d\s]*\*\*', '', first_line_clean)  # Odstraní původní tučné číslo kapitoly
    first_line_clean = first_line_clean.replace('#', '').strip()
    
    # Nultá sekce (vše před 1. kapitolou - loga, úvodní nadpisy)
    if i == 0:
        clean_name = "00-Titulni-strana"
        title_frontmatter = "Titulní strana"
    else:
        # Čištění pro bezpečný název souboru v operačním systému
        clean_name = re.sub(r'!\[.*?\]\(.*?\)', '', first_line_clean)
        clean_name = re.sub(r'[*_`~\[\]]', '', clean_name)
        clean_name = re.sub(r'[^\w\s-]', '', clean_name).strip()
        clean_name = re.sub(r'[-\s]+', '-', clean_name)
        
        # Výsledný název souboru (např. "01-1-Verze-dokumentu.md")
        clean_name = f"{i:02d}-{i}-{clean_name[:50]}"
        title_frontmatter = f"{i}. {first_line_clean}"
        
    file_name = f"{clean_name}.md"
    output_path = os.path.join(output_dir, file_name)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        # Zápis čistých metadat pro VitePress
        f.write(f"---\ntitle: {title_frontmatter}\n---\n\n")
        f.write(chapter + "\n")
        
    print(f"Vytvořeno: {output_path}")

print("✅ Příručka lokálního administrátora byla úspěšně naporcována!")