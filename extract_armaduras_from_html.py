#!/usr/bin/env python3

import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_armaduras_from_html():
    """
    Extrai TODAS as armaduras da tabela do HTML da Tibia Wiki.
    """
    html_path = Path("tibia files/armaduras.html")
    
    with open(html_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Encontra a tabela de armaduras (procura por tbody)
    tbody = soup.find('tbody')
    
    if not tbody:
        print("Erro: Tabela não encontrada!")
        return
    
    armaduras = {}
    
    # Processa cada linha da tabela
    for tr in tbody.find_all('tr'):
        # Primeira célula tem o link para a armadura
        first_td = tr.find('td')
        if not first_td:
            continue
            
        link = first_td.find('a')
        if not link:
            continue
        
        armor_name = link.get_text(strip=True)
        
        # Segunda célula tem a imagem
        img_td = tr.find_all('td')[1] if len(tr.find_all('td')) > 1 else None
        if not img_td:
            continue
            
        img = img_td.find('img')
        if not img:
            continue
        
        img_src = img.get('src', '')
        
        # Constrói URL completa
        if img_src.startswith('/images/'):
            full_url = f"https://www.tibiawiki.com.br{img_src}"
            armaduras[armor_name] = full_url
    
    # Salva o arquivo JSON
    output_path = Path("tibia_json/armaduras_items.json")
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(armaduras, file, indent=2, ensure_ascii=False)
    
    print(f"Extraídas {len(armaduras)} armaduras da tabela HTML")
    print(f"Arquivo salvo em: {output_path}")
    
    # Mostra as primeiras 10 armaduras
    print("\nPrimeiras 10 armaduras extraídas:")
    for i, (name, url) in enumerate(list(armaduras.items())[:10]):
        print(f"  {i+1}. {name}")

if __name__ == "__main__":
    extract_armaduras_from_html()

