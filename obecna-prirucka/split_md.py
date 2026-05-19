import os
import re

input_file = 'ISSR_Obecna.md' 
output_dir = 'kapitoly'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Načtení s utf-8-sig pro případnou ignoraci BOM znaku
with open(input_file, 'r', encoding='utf-8-sig') as f:
    content = f.read()

# REGEX NA MÍRU: Hledá "## " + volitelný <span> tag + ČÍSLO bez tečky + mezeru.
# To zaručí, že se soubor rozdělí jen na hlavních kapitolách 1 až 18 (ignoruje 1.1 apod.)
pattern = r'\n(?=## (?:<span[^>]*></span>)?\d+ )'
chapters = re.split(pattern, '\n' + content)

for i, chapter in enumerate(chapters):
    chapter = chapter.strip()
    if not chapter:
        continue
    
    # Získání prvního řádku (syrový nadpis vč. span tagů)
    first_line_raw = chapter.split('\n')[0]
    
    # Odstranění HTML tagů a křížků pro čistý název do frontmatteru
    first_line_clean = re.sub(r'<[^>]+>', '', first_line_raw)
    first_line_clean = first_line_clean.replace('#', '').replace('*', '').strip()
    
    # Nultá sekce (vše před kapitolou 1 - Obsah, Úvodní logo, Zkratky)
    if i == 0:
        clean_name = "00-Uvodni-informace"
        title_frontmatter = "Úvodní informace"
    else:
        # Čištění pro bezpečný název souboru
        clean_name = re.sub(r'!\[.*?\]\(.*?\)', '', first_line_clean)
        clean_name = re.sub(r'[*_`~\[\]]', '', clean_name)
        clean_name = re.sub(r'[^\w\s-]', '', clean_name).strip()
        clean_name = re.sub(r'[-\s]+', '-', clean_name)
        
        # Výsledný název souboru (např. "01-1-Uvod")
        clean_name = f"{i:02d}-{clean_name[:50]}"
        title_frontmatter = first_line_clean
        
    file_name = f"{clean_name}.md"
    output_path = os.path.join(output_dir, file_name)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        # Přidání čistých metadat pro VitePress
        f.write(f"---\ntitle: {title_frontmatter}\n---\n\n")
        f.write(chapter + "\n")
        
    print(f"Vytvořeno: {output_path}")

print("✅ Soubor byl úspěšně naporcován!")