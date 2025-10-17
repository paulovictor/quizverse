#!/usr/bin/env python
"""
Script para listar todas as pastas no Cloudinary e encontrar o caminho correto
"""

import os
import sys

try:
    import cloudinary
    import cloudinary.api
except ImportError:
    print("❌ Erro: Biblioteca 'cloudinary' não está instalada!")
    print("Para instalar: pip install cloudinary")
    sys.exit(1)

# Credenciais
CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME', 'dwm53cbu2')
API_KEY = os.environ.get('CLOUDINARY_API_KEY', '429396283651242')
API_SECRET = os.environ.get('CLOUDINARY_API_SECRET', 'HTF--7Ceic5mmOo_oxboCTzXiis')

cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET,
    secure=True
)

print("=" * 70)
print("📁 LISTANDO TODAS AS PASTAS DO CLOUDINARY")
print("=" * 70)
print()

try:
    # Listar pastas raiz
    response = cloudinary.api.root_folders()
    folders = response.get('folders', [])

    print(f"✅ Encontradas {len(folders)} pastas raiz:")
    print()

    all_paths = []

    def list_subfolders(path='', level=0):
        """Lista subpastas recursivamente"""
        try:
            if path:
                response = cloudinary.api.subfolders(path)
            else:
                response = cloudinary.api.root_folders()

            folders = response.get('folders', [])

            for folder in folders:
                folder_name = folder.get('name')
                folder_path = folder.get('path', folder_name)

                indent = "  " * level
                print(f"{indent}📁 {folder_path}")
                all_paths.append(folder_path)

                # Recursivamente listar subpastas
                list_subfolders(folder_path, level + 1)

        except Exception as e:
            pass

    # Listar todas as pastas
    list_subfolders()

    print()
    print("=" * 70)
    print("🔍 BUSCANDO PASTAS COM 'ak' ou '47':")
    print("=" * 70)

    ak_folders = [p for p in all_paths if 'ak' in p.lower() or '47' in p.lower()]

    if ak_folders:
        for folder in ak_folders:
            print(f"  ✅ {folder}")
    else:
        print("  ⚠️  Nenhuma pasta encontrada com 'ak' ou '47'")

    print()
    print("=" * 70)
    print("📋 TODAS AS PASTAS ENCONTRADAS:")
    print("=" * 70)
    for path in sorted(all_paths):
        print(f"  • {path}")

except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()

print()
