#!/usr/bin/env python3

import json
import re
from pathlib import Path

def extract_varinhas_from_html():
    """
    Extrai TODAS as varinhas/wands da tabela do HTML da Tibia Wiki usando regex.
    """
    html_path = Path("tibia files/varinhas.html")
    
    with open(html_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    varinhas = {}
    
    # Padrão: procura por linhas de tabela que contém link para wiki e imagem
    pattern = r'<td><a href="/wiki/([^"]+)" title="([^"]+)">([^<]+)</a>\s*</td>\s*<td[^>]*><a[^>]*><img alt="[^"]*\.gif" src="(/images/[^"]+\.gif)"'
    
    matches = re.finditer(pattern, content, re.MULTILINE)
    
    for match in matches:
        wiki_link = match.group(1)
        title = match.group(2)
        varinha_name = match.group(3)
        img_src = match.group(4)
        
        # Constrói URL completa
        full_url = f"https://www.tibiawiki.com.br{img_src}"
        varinhas[varinha_name] = full_url
    
    # Salva o arquivo JSON
    output_path = Path("tibia_json/varinhas_items.json")
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(varinhas, file, indent=2, ensure_ascii=False)
    
    print(f"Extraídas {len(varinhas)} varinhas/wands da tabela HTML")
    print(f"Arquivo salvo em: {output_path}")
    
    # Mostra as primeiras 10 e últimas 10
    items = list(varinhas.items())
    print("\nPrimeiras 10 varinhas extraídas:")
    for i, (name, url) in enumerate(items[:10]):
        print(f"  {i+1}. {name}")
    
    if len(items) > 10:
        print(f"\nÚltimas 10 varinhas extraídas:")
        for i, (name, url) in enumerate(items[-10:]):
            print(f"  {len(items)-9+i}. {name}")

if __name__ == "__main__":
    extract_varinhas_from_html()

