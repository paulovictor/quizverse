#!/usr/bin/env python3
"""
Script para otimizar URLs do Cloudinary
Adiciona parâmetros de otimização: /w_1000,f_auto,q_auto:low,fl_lossy,fl_progressive,fl_strip_profile/
"""

import json
import os
import sys
from pathlib import Path

def list_cloudinary_files():
    """Lista todos os arquivos JSON do diretório cloudinary_urls"""
    cloudinary_dir = Path(__file__).parent / 'cloudinary_urls'
    
    if not cloudinary_dir.exists():
        print("❌ Diretório cloudinary_urls não encontrado!")
        return []
    
    json_files = list(cloudinary_dir.glob('*.json'))
    
    if not json_files:
        print("❌ Nenhum arquivo JSON encontrado em cloudinary_urls/")
        return []
    
    print("📁 Arquivos disponíveis em cloudinary_urls/:")
    print("=" * 50)
    
    for i, file_path in enumerate(json_files, 1):
        file_size = file_path.stat().st_size
        print(f"{i}. {file_path.name} ({file_size:,} bytes)")
    
    return json_files

def optimize_cloudinary_url(url, width):
    """
    Otimiza uma URL do Cloudinary adicionando parâmetros de otimização
    """
    if not url or not isinstance(url, str):
        return url
    
    # Parâmetros de otimização
    optimization_params = f"w_{width},f_auto,q_auto:low,fl_lossy,fl_progressive,fl_strip_profile"
    
    # Verificar se é uma URL do Cloudinary
    if 'cloudinary.com' not in url:
        return url
    
    # Verificar se já tem parâmetros de otimização
    if optimization_params in url:
        return url
    
    # Dividir a URL em partes
    if '/upload/' in url:
        # URL padrão: https://res.cloudinary.com/.../upload/v1234567890/image.jpg
        parts = url.split('/upload/')
        if len(parts) == 2:
            base_url = parts[0] + '/upload/'
            rest = parts[1]
            
            # Adicionar parâmetros de otimização
            optimized_url = f"{base_url}{optimization_params}/{rest}"
            return optimized_url
    
    return url

def process_json_file(file_path, width):
    """Processa um arquivo JSON otimizando as URLs"""
    print(f"\n🔄 Processando: {file_path.name}")
    
    try:
        # Ler arquivo original
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        original_size = len(json.dumps(data, ensure_ascii=False))
        optimized_count = 0
        
        def optimize_urls_recursive(obj):
            """Função recursiva para otimizar URLs em qualquer estrutura JSON"""
            nonlocal optimized_count
            
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if key == 'secure_url' and isinstance(value, str):
                        original_url = value
                        optimized_url = optimize_cloudinary_url(original_url, width)
                        if optimized_url != original_url:
                            obj[key] = optimized_url
                            optimized_count += 1
                    else:
                        optimize_urls_recursive(value)
            elif isinstance(obj, list):
                for item in obj:
                    optimize_urls_recursive(item)
        
        # Otimizar URLs
        optimize_urls_recursive(data)
        
        # Salvar arquivo otimizado
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        new_size = len(json.dumps(data, ensure_ascii=False))
        size_diff = new_size - original_size
        
        print(f"   ✅ {optimized_count} URLs otimizadas")
        print(f"   📊 Tamanho: {original_size:,} → {new_size:,} bytes ({size_diff:+,} bytes)")
        
        return optimized_count
        
    except Exception as e:
        print(f"   ❌ Erro ao processar {file_path.name}: {e}")
        return 0

def main():
    """Função principal"""
    print("🚀 OTIMIZADOR DE URLs DO CLOUDINARY")
    print("=" * 50)
    while True:
        width_input = input("Defina a largura máxima (ex: 500): ").strip()
        try:
            width_value = int(width_input)
            if width_value <= 0:
                raise ValueError
            width = str(width_value)
            break
        except ValueError:
            print("❌ Digite um número inteiro positivo.")

    print("Parâmetros de otimização:")
    print(f"  - w_{width}: Largura máxima {width}px")
    print("  - f_auto: Formato automático (WebP quando suportado)")
    print("  - q_auto:low: Qualidade baixa para menor tamanho")
    print("  - fl_lossy: Compressão com perda")
    print("  - fl_progressive: Carregamento progressivo")
    print("  - fl_strip_profile: Remove metadados")
    print()

    # Listar arquivos disponíveis
    json_files = list_cloudinary_files()
    
    if not json_files:
        return
    
    print()
    print("Selecione o arquivo para otimizar:")
    print("0. Otimizar TODOS os arquivos")
    
    try:
        choice = input("\nDigite o número (0 para todos): ").strip()
        
        if choice == '0':
            # Otimizar todos os arquivos
            total_optimized = 0
            for file_path in json_files:
                optimized_count = process_json_file(file_path, width)
                total_optimized += optimized_count
            
            print(f"\n✨ Processo concluído!")
            print(f"📊 Total de URLs otimizadas: {total_optimized}")
            
        else:
            # Otimizar arquivo específico
            try:
                file_index = int(choice) - 1
                if 0 <= file_index < len(json_files):
                    file_path = json_files[file_index]
                    optimized_count = process_json_file(file_path, width)
                    
                    print(f"\n✨ Processo concluído!")
                    print(f"📊 URLs otimizadas: {optimized_count}")
                else:
                    print("❌ Número inválido!")
            except ValueError:
                print("❌ Digite um número válido!")
                
    except KeyboardInterrupt:
        print("\n\n⏹️  Processo cancelado pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")

if __name__ == '__main__':
    main()
