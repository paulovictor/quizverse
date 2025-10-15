#!/usr/bin/env python
"""
Script para listar todas as pastas e recursos do Cloudinary
"""

import os
import sys

try:
    import cloudinary
    import cloudinary.api
except ImportError:
    print("❌ Erro: Biblioteca 'cloudinary' não está instalada!")
    sys.exit(1)

# Configuração
CLOUD_NAME = 'dwm53cbu2'
API_KEY = '429396283651242'
API_SECRET = 'HTF--7Ceic5mmOo_oxboCTzXiis'

cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET,
    secure=True
)

print("=" * 70)
print("☁️  CLOUDINARY EXPLORER")
print("=" * 70)
print(f"✅ Conectado: {CLOUD_NAME}")
print()

# 1. Listar pastas
print("📁 LISTANDO PASTAS...")
print("-" * 70)
try:
    folders_response = cloudinary.api.root_folders()
    folders = folders_response.get('folders', [])
    
    if folders:
        for folder in folders:
            print(f"   📂 {folder['name']} (path: {folder['path']})")
    else:
        print("   ⚠️  Nenhuma pasta encontrada")
    print()
except Exception as e:
    print(f"   ❌ Erro ao listar pastas: {e}")
    print()

# 2. Listar alguns recursos (primeiros 20)
print("🖼️  LISTANDO RECURSOS (primeiros 20)...")
print("-" * 70)
try:
    resources_response = cloudinary.api.resources(
        type='upload',
        max_results=20
    )
    resources = resources_response.get('resources', [])
    
    if resources:
        for i, resource in enumerate(resources, 1):
            public_id = resource['public_id']
            url = resource['secure_url']
            print(f"   {i}. {public_id}")
            print(f"      URL: {url}")
            print()
    else:
        print("   ⚠️  Nenhum recurso encontrado")
except Exception as e:
    print(f"   ❌ Erro ao listar recursos: {e}")

print()
print("💡 Dica: Use o public_id ou o nome da pasta acima no script principal")

