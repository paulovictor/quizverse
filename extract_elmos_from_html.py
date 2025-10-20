#!/usr/bin/env python3

import json
import re
from pathlib import Path

def extract_elmos_from_html():
    """
    Extrai TODOS os elmos/capacetes da tabela do HTML da Tibia Wiki usando regex.
    """
    html_path = Path("tibia files/elmos.html")
    
    with open(html_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    elmos = {}
    
    # Padrão: procura por linhas de tabela que contém link para wiki e imagem
    pattern = r'<td><a href="/wiki/([^"]+)" title="([^"]+)">([^<]+)</a>\s*</td>\s*<td[^>]*><a[^>]*><img alt="[^"]*\.gif" src="(/images/[^"]+\.gif)"'
    
    matches = re.finditer(pattern, content, re.MULTILINE)
    
    for match in matches:
        wiki_link = match.group(1)
        title = match.group(2)
        elmo_name = match.group(3)
        img_src = match.group(4)
        
        # Constrói URL completa
        full_url = f"https://www.tibiawiki.com.br{img_src}"
        elmos[elmo_name] = full_url
    
    # Salva o arquivo JSON
    output_path = Path("tibia_json/elmos_items.json")
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(elmos, file, indent=2, ensure_ascii=False)
    
    print(f"Extraídos {len(elmos)} elmos/capacetes da tabela HTML")
    print(f"Arquivo salvo em: {output_path}")
    
    # Mostra as primeiras 10 e últimas 10
    items = list(elmos.items())
    print("\nPrimeiros 10 elmos extraídos:")
    for i, (name, url) in enumerate(items[:10]):
        print(f"  {i+1}. {name}")
    
    if len(items) > 10:
        print(f"\nÚltimos 10 elmos extraídos:")
        for i, (name, url) in enumerate(items[-10:]):
            print(f"  {len(items)-9+i}. {name}")

if __name__ == "__main__":
    extract_elmos_from_html()

