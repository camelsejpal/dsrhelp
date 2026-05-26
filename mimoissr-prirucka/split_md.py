import os
import re
import sys
import unicodedata

def slugify(value):
    """
    Převede text na bezpečný název souboru/URL (odstraní diakritiku,
    speciální znaky a nahradí mezery pomlčkami).
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('utf-8')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

def split_markdown(input_file):
    if not os.path.exists(input_file):
        print(f"❌ Chyba: Soubor '{input_file}' neexistuje.")
        return

    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_dir = f"{base_name}-split"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    content = content.replace('\r\n', '\n')

    # CHYTRÝ REGEX PRO TENTO DOKUMENT: 
    # Hledá nový řádek, za kterým následuje 1 až 3 mřížky, mezera, dvě hvězdičky (tučné), číslo a tečka.
    # Přesně to zachytí "## **1. " i "### **6. " a ignoruje podkapitoly.
    pattern = r'\n(?=#{1,3}\s\*\*\d+\.\s)'
    chapters = re.split(pattern, '\n' + content)

    for i, chapter in enumerate(chapters):
        chapter = chapter.strip()
        if not chapter:
            continue
        
        lines = chapter.split('\n')
        first_line_raw = lines[0].strip()
        
        # Kontrola, jestli řádek začíná mřížkou
        if re.match(r'^#{1,3}\s', first_line_raw):
            title_frontmatter = re.sub(r'^#{1,3}\s', '', first_line_raw).strip()
            
            clean_title = re.sub(r'[*_`~\[\]]', '', title_frontmatter)
            clean_title = re.sub(r'!\[.*?\]\(.*?\)', '', clean_title) 
            clean_title = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', clean_title) 
            
            file_slug = slugify(clean_title)[:50].strip('-')
            file_name = f"{i:02d}-{file_slug}.md"
            
            # Odstranění tučného formátování a čísla z frontmatter titulku pro čistší vzhled
            title_frontmatter = re.sub(r'^\*\*\d+\.\s', '', title_frontmatter).replace('**', '')
        else:
            title_frontmatter = "Titulní strana"
            file_name = "00-titulni-strana.md"
            
        output_path = os.path.join(output_dir, file_name)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"---\ntitle: {title_frontmatter}\n---\n\n")
            f.write(chapter + "\n")
            
        print(f"Vytvořeno: {output_path}")

    print(f"\n✅ Hotovo! Soubor byl úspěšně naporcován do složky: {output_dir}")

if __name__ == "__main__":
    input_path = sys.argv[1] if len(sys.argv) > 1 else 'input.md'
    split_markdown(input_path)