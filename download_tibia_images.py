#!/usr/bin/env python3

import json
import os
import requests
from pathlib import Path
from urllib.parse import unquote

def download_image(url: str, output_path: str) -> bool:
    """
    Faz o download de uma imagem da URL e salva no caminho especificado.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")
        return False

def sanitize_filename(filename: str) -> str:
    """
    Remove caracteres inválidos do nome do arquivo.
    """
    # Remove caracteres inválidos
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def download_category_images(json_file: str, category_name: str, base_output_dir: str):
    """
    Faz o download de todas as imagens de uma categoria específica.
    """
    json_path = Path(f"tibia_json/{json_file}")
    output_dir = Path(base_output_dir) / f"{category_name}_images"
    
    # Cria o diretório de saída
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Lê o arquivo JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        items = json.load(f)
    
    print(f"\n{'='*60}")
    print(f"Baixando imagens de {category_name}...")
    print(f"Total de itens: {len(items)}")
    print(f"Diretório: {output_dir}")
    print(f"{'='*60}")
    
    success_count = 0
    failed_count = 0
    
    for item_name, image_url in items.items():
        # Extrai o nome do arquivo da URL
        filename = unquote(image_url.split('/')[-1])
        filename = sanitize_filename(filename)
        
        # Caminho completo de saída
        output_path = output_dir / filename
        
        # Pula se já existe
        if output_path.exists():
            print(f"  ✓ Já existe: {filename}")
            success_count += 1
            continue
        
        # Faz o download
        print(f"  Baixando: {filename}...", end=" ")
        if download_image(image_url, str(output_path)):
            print("✓")
            success_count += 1
        else:
            print("✗")
            failed_count += 1
    
    print(f"\n{category_name}: {success_count} sucesso, {failed_count} falhas")
    return success_count, failed_count

def main():
    base_output_dir = "tibia_images"
    
    # Define as categorias e seus arquivos JSON
    categories = {
        "armaduras": "armaduras_items.json",
        "elmos": "elmos_items.json",
        "calcas": "calcas_items.json",
        "botas": "botas_items.json",
        "machados": "machados_items.json",
        "clavas": "clavas_items.json",
        "espadas": "espadas_items.json",
        "varinhas": "varinhas_items.json"
    }
    
    print("="*60)
    print("DOWNLOAD DE IMAGENS DA TIBIA WIKI")
    print("="*60)
    
    total_success = 0
    total_failed = 0
    
    for category_name, json_file in categories.items():
        success, failed = download_category_images(json_file, category_name, base_output_dir)
        total_success += success
        total_failed += failed
    
    print("\n" + "="*60)
    print("RESUMO FINAL")
    print("="*60)
    print(f"Total de imagens baixadas com sucesso: {total_success}")
    print(f"Total de falhas: {total_failed}")
    print(f"Total geral: {total_success + total_failed}")
    print("="*60)

if __name__ == "__main__":
    main()

