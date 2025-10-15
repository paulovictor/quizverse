#!/usr/bin/env python
"""
Script para adicionar transformações do Cloudinary nas URLs dos Pokémon
Adiciona: w_300,h_300,c_thumb,g_face,f_auto
"""

import json
from pathlib import Path

# Ler o arquivo JSON existente
input_file = Path('cloudinary_pokemon_urls.json')

if not input_file.exists():
    print("❌ Arquivo cloudinary_pokemon_urls.json não encontrado!")
    exit(1)

with open(input_file, 'r', encoding='utf-8') as f:
    pokemon_data = json.load(f)

print("🔄 Adicionando transformações do Cloudinary...")
print()

# Parâmetros de transformação
transformations = "w_300,h_300,c_thumb,g_face,f_auto"

# Atualizar cada URL
updated_count = 0
for pokemon_id, data in pokemon_data.items():
    original_url = data['url']
    
    # Cloudinary URL pattern: https://res.cloudinary.com/CLOUD_NAME/image/upload/v123456/filename.png
    # Adicionar transformações após /upload/
    if '/upload/' in original_url:
        # Dividir a URL em partes
        parts = original_url.split('/upload/')
        
        # Reconstruir com transformações
        transformed_url = f"{parts[0]}/upload/{transformations}/{parts[1]}"
        
        # Atualizar no dicionário
        data['url_original'] = original_url  # Guardar URL original
        data['url'] = transformed_url
        data['transformations'] = transformations
        
        updated_count += 1
        
        # Mostrar primeiros 5
        if updated_count <= 5:
            print(f"#{pokemon_id} {data['name']}")
            print(f"  Original: {original_url}")
            print(f"  Nova:     {transformed_url}")
            print()

print(f"✅ {updated_count} URLs atualizadas com transformações")
print()

# Salvar arquivo atualizado
output_file = Path('cloudinary_pokemon_urls.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(pokemon_data, f, indent=2, ensure_ascii=False)

print(f"💾 Arquivo salvo: {output_file}")
print()

# Também atualizar o arquivo de texto com as URLs
output_urls_file = Path('cloudinary_pokemon_urls.txt')
with open(output_urls_file, 'w', encoding='utf-8') as f:
    for pokemon_id in sorted(pokemon_data.keys(), key=int):
        f.write(f"{pokemon_data[pokemon_id]['url']}\n")

print(f"📝 Lista de URLs atualizada: {output_urls_file}")
print()
print("🎉 Concluído!")
print()
print("💡 Os quizzes agora usarão URLs com:")
print(f"   - Largura: 300px")
print(f"   - Altura: 300px")
print(f"   - Crop: thumb (miniatura)")
print(f"   - Gravidade: face (foco na face)")
print(f"   - Formato: auto (melhor formato)")

