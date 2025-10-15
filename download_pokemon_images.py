#!/usr/bin/env python
"""
Script para baixar todas as imagens de Pokémon para uso local
"""
import os
import requests
from pathlib import Path

# Lista de URLs das imagens de Pokémon
POKEMON_IMAGES = [
    {
        'url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png',
        'filename': 'pikachu.png',
        'pokemon': 'Pikachu'
    },
    {
        'url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png',
        'filename': 'charizard.png',
        'pokemon': 'Charizard'
    },
    {
        'url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png',
        'filename': 'snorlax.png',
        'pokemon': 'Snorlax'
    },
    {
        'url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png',
        'filename': 'mewtwo.png',
        'pokemon': 'Mewtwo'
    },
    {
        'url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png',
        'filename': 'blastoise.png',
        'pokemon': 'Blastoise'
    },
]

def download_pokemon_images():
    """Baixa todas as imagens de Pokémon para uma pasta local"""
    
    # Criar pasta pokemon se não existir
    pokemon_dir = Path('pokemon')
    pokemon_dir.mkdir(exist_ok=True)
    print(f"📁 Pasta criada/verificada: {pokemon_dir.absolute()}")
    print()
    
    # Baixar cada imagem
    success_count = 0
    failed_count = 0
    
    for img_data in POKEMON_IMAGES:
        url = img_data['url']
        filename = img_data['filename']
        pokemon_name = img_data['pokemon']
        filepath = pokemon_dir / filename
        
        try:
            print(f"📥 Baixando {pokemon_name}...")
            print(f"   URL: {url}")
            
            # Fazer requisição
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Salvar arquivo
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            file_size = filepath.stat().st_size / 1024  # KB
            print(f"   ✅ Salvo em: {filepath}")
            print(f"   📊 Tamanho: {file_size:.2f} KB")
            print()
            
            success_count += 1
            
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Erro ao baixar {pokemon_name}: {e}")
            print()
            failed_count += 1
        except IOError as e:
            print(f"   ❌ Erro ao salvar {pokemon_name}: {e}")
            print()
            failed_count += 1
    
    # Resumo
    print("=" * 60)
    print("📊 RESUMO DO DOWNLOAD")
    print("=" * 60)
    print(f"✅ Sucesso: {success_count}/{len(POKEMON_IMAGES)}")
    print(f"❌ Falhas: {failed_count}/{len(POKEMON_IMAGES)}")
    print()
    
    if success_count > 0:
        print(f"📁 Imagens salvas em: {pokemon_dir.absolute()}")
        print()
        print("💡 Para usar as imagens locais, copie a pasta 'pokemon/' para:")
        print("   quizzes/static/images/pokemon/")
        print()
        print("E atualize as URLs no script de criação do quiz para:")
        print("   {% static 'images/pokemon/pikachu.png' %}")
    
    return success_count, failed_count

def list_downloaded_images():
    """Lista todas as imagens baixadas"""
    pokemon_dir = Path('pokemon')
    
    if not pokemon_dir.exists():
        print("❌ Pasta 'pokemon' não encontrada!")
        return
    
    images = list(pokemon_dir.glob('*.png'))
    
    if not images:
        print("❌ Nenhuma imagem encontrada na pasta 'pokemon'!")
        return
    
    print("\n📋 IMAGENS BAIXADAS:")
    print("=" * 60)
    for img in sorted(images):
        size = img.stat().st_size / 1024
        print(f"   {img.name} - {size:.2f} KB")
    print()
    print(f"Total: {len(images)} imagens")

if __name__ == '__main__':
    print("🎮 DOWNLOAD DE IMAGENS DE POKÉMON")
    print("=" * 60)
    print()
    
    # Verificar se requests está instalado
    try:
        import requests
    except ImportError:
        print("❌ Erro: O módulo 'requests' não está instalado!")
        print()
        print("Para instalar, execute:")
        print("   uv add requests")
        print("   # ou")
        print("   pip install requests")
        exit(1)
    
    # Baixar imagens
    success, failed = download_pokemon_images()
    
    # Listar imagens baixadas
    if success > 0:
        list_downloaded_images()
    
    print()
    print("🎉 Processo concluído!")

