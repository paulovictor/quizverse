#!/usr/bin/env python3

import json
import re
from pathlib import Path

def extract_armaduras_from_html():
    """
    Extrai TODAS as armaduras da tabela do HTML da Tibia Wiki usando regex.
    """
    html_path = Path("tibia files/armaduras.html")
    
    with open(html_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    armaduras = {}
    
    # Padrão: procura por linhas de tabela que contém link para wiki e imagem
    # <td><a href="/wiki/Nome_Armadura" title="Nome Armadura">Nome Armadura</a>
    # seguido por
    # <td width="5%"><a href="/wiki/Arquivo:Nome.gif" class="image fancybox"><img alt="Nome.gif" src="/images/caminho/Nome.gif"
    
    # Procura por todas as ocorrências de nome + imagem na tabela
    pattern = r'<td><a href="/wiki/([^"]+)" title="([^"]+)">([^<]+)</a>\s*</td>\s*<td[^>]*><a[^>]*><img alt="[^"]*\.gif" src="(/images/[^"]+\.gif)"'
    
    matches = re.finditer(pattern, content, re.MULTILINE)
    
    for match in matches:
        wiki_link = match.group(1)
        title = match.group(2)
        armor_name = match.group(3)
        img_src = match.group(4)
        
        # Constrói URL completa
        full_url = f"https://www.tibiawiki.com.br{img_src}"
        armaduras[armor_name] = full_url
    
    # Salva o arquivo JSON
    output_path = Path("tibia_json/armaduras_items.json")
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(armaduras, file, indent=2, ensure_ascii=False)
    
    print(f"Extraídas {len(armaduras)} armaduras da tabela HTML")
    print(f"Arquivo salvo em: {output_path}")
    
    # Mostra as primeiras 10 e últimas 10 armaduras
    items = list(armaduras.items())
    print("\nPrimeiras 10 armaduras extraídas:")
    for i, (name, url) in enumerate(items[:10]):
        print(f"  {i+1}. {name}")
    
    print(f"\nÚltimas 10 armaduras extraídas:")
    for i, (name, url) in enumerate(items[-10:]):
        print(f"  {len(items)-9+i}. {name}")

if __name__ == "__main__":
    extract_armaduras_from_html()

