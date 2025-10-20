#!/usr/bin/env python3

import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_items_from_html(html_file_path: str, output_file_path: str) -> None:
    """
    Extrai itens do HTML da Tibia Wiki e cria um JSON com nome e URL da imagem.
    """
    with open(html_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    items = {}
    
    # Procura por imagens com alt contendo .gif e src contendo /images/
    img_tags = soup.find_all('img', alt=re.compile(r'\.gif$'), src=re.compile(r'^/images/'))
    
    for img in img_tags:
        alt_text = img.get('alt', '')
        src = img.get('src', '')
        
        # Remove .gif do nome para obter o nome limpo
        item_name = alt_text.replace('.gif', '')
        
        # Constrói a URL completa
        full_url = f"https://www.tibiawiki.com.br{src}"
        
        # Adiciona ao dicionário
        items[item_name] = full_url
    
    # Salva o JSON
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(items, file, indent=2, ensure_ascii=False)
    
    print(f"Extraídos {len(items)} itens de {html_file_path} para {output_file_path}")

def main():
    base_path = Path("tibia files")
    output_path = Path("tibia_json")
    output_path.mkdir(exist_ok=True)
    
    # Lista de arquivos HTML para processar
    html_files = [
        "armaduras.html",
        "elmos.html", 
        "calcas.html",
        "botas.html",
        "machados.html",
        "clavas.html",
        "espadas.html",
        "varinhas.html"
    ]
    
    for html_file in html_files:
        html_path = base_path / html_file
        if html_path.exists():
            # Nome do arquivo JSON baseado no HTML
            json_name = html_file.replace('.html', '_items.json')
            json_path = output_path / json_name
            
            extract_items_from_html(str(html_path), str(json_path))
        else:
            print(f"Arquivo não encontrado: {html_path}")

if __name__ == "__main__":
    main()
