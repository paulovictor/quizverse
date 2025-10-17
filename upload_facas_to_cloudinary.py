#!/usr/bin/env python
"""
Script para fazer upload das facas para o Cloudinary

Pasta local: /Users/paulo/Downloads/ALL SKINS/ALL SKINS/FACAS
Pasta Cloudinary: cs/facas

Uso:
    python upload_facas_to_cloudinary.py
"""

import os
import sys
from pathlib import Path

try:
    import cloudinary
    import cloudinary.uploader
    import cloudinary.api
except ImportError:
    print("❌ Erro: Biblioteca 'cloudinary' não está instalada!")
    print()
    print("Para instalar:")
    print("   pip install cloudinary")
    print("   # ou")
    print("   uv add cloudinary")
    sys.exit(1)


# ========== CONFIGURAÇÃO ==========
# Credenciais do Cloudinary
CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME', 'dwm53cbu2')
API_KEY = os.environ.get('CLOUDINARY_API_KEY', '429396283651242')
API_SECRET = os.environ.get('CLOUDINARY_API_SECRET', 'HTF--7Ceic5mmOo_oxboCTzXiis')

# Pasta local com as facas
LOCAL_FOLDER = Path('/Users/paulo/Downloads/ALL SKINS/ALL SKINS/FACAS')

# Pasta no Cloudinary
CLOUDINARY_FOLDER = 'cs/facas'

# Extensões de imagem suportadas
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp'}
# ===================================


def configure_cloudinary():
    """Configura as credenciais do Cloudinary"""
    cloudinary.config(
        cloud_name=CLOUD_NAME,
        api_key=API_KEY,
        api_secret=API_SECRET,
        secure=True
    )
    print(f"✅ Conectado ao Cloudinary: {CLOUD_NAME}")


def get_image_files(folder_path):
    """
    Lista todos os arquivos de imagem na pasta

    Args:
        folder_path: Path da pasta local

    Returns:
        list: Lista de Path objects para arquivos de imagem
    """
    image_files = []

    if not folder_path.exists():
        print(f"❌ Erro: Pasta não encontrada: {folder_path}")
        return image_files

    if not folder_path.is_dir():
        print(f"❌ Erro: Não é uma pasta: {folder_path}")
        return image_files

    for file in folder_path.iterdir():
        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS:
            image_files.append(file)

    return sorted(image_files)


def upload_image(file_path, cloudinary_folder):
    """
    Faz upload de uma imagem para o Cloudinary

    Args:
        file_path: Path do arquivo local
        cloudinary_folder: Pasta de destino no Cloudinary

    Returns:
        dict: Resposta do upload ou None se falhar
    """
    try:
        # Nome do arquivo sem extensão
        filename = file_path.stem

        # Upload para o Cloudinary
        result = cloudinary.uploader.upload(
            str(file_path),
            folder=cloudinary_folder,
            public_id=filename,
            overwrite=True,  # Sobrescrever se já existir
            asset_folder=cloudinary_folder,  # Media Library folder
            use_filename=True,
            unique_filename=False,
        )

        return result

    except Exception as e:
        print(f"   ❌ Erro no upload: {e}")
        return None


def main():
    print("=" * 70)
    print("🔪 UPLOAD DE FACAS PARA O CLOUDINARY")
    print("=" * 70)
    print()

    # Verificar se a pasta existe
    print(f"📁 Pasta local: {LOCAL_FOLDER}")

    if not LOCAL_FOLDER.exists():
        print(f"❌ Erro: Pasta não encontrada!")
        print(f"   Verifique se o caminho está correto:")
        print(f"   {LOCAL_FOLDER}")
        return

    print(f"✅ Pasta encontrada!")
    print()

    # Listar arquivos de imagem
    print("🔍 Procurando arquivos de imagem...")
    image_files = get_image_files(LOCAL_FOLDER)

    if not image_files:
        print("⚠️  Nenhum arquivo de imagem encontrado!")
        print(f"   Extensões suportadas: {', '.join(IMAGE_EXTENSIONS)}")
        return

    print(f"📦 Encontrados {len(image_files)} arquivos de imagem")
    print()

    # Confirmar antes de fazer upload
    print("=" * 70)
    print("📋 ARQUIVOS QUE SERÃO ENVIADOS:")
    print("=" * 70)
    for i, file in enumerate(image_files[:10], 1):
        print(f"   {i}. {file.name}")

    if len(image_files) > 10:
        print(f"   ... e mais {len(image_files) - 10} arquivos")

    print()
    print(f"📂 Destino: {CLOUDINARY_FOLDER}")
    print()

    # Pedir confirmação
    response = input("Deseja continuar com o upload? (s/n): ").strip().lower()

    if response != 's':
        print("⚠️  Upload cancelado pelo usuário")
        return

    print()
    print("=" * 70)
    print("🚀 INICIANDO UPLOAD")
    print("=" * 70)
    print()

    # Configurar Cloudinary
    configure_cloudinary()
    print()

    # Fazer upload de cada arquivo
    success_count = 0
    error_count = 0
    uploaded_urls = []

    for i, file in enumerate(image_files, 1):
        print(f"[{i}/{len(image_files)}] Uploading: {file.name}")

        result = upload_image(file, CLOUDINARY_FOLDER)

        if result:
            success_count += 1
            uploaded_urls.append({
                'filename': file.name,
                'public_id': result.get('public_id'),
                'url': result.get('secure_url'),
                'format': result.get('format'),
                'width': result.get('width'),
                'height': result.get('height'),
                'bytes': result.get('bytes'),
            })
            print(f"   ✅ Sucesso! URL: {result.get('secure_url')}")
        else:
            error_count += 1

        print()

    # Resumo final
    print("=" * 70)
    print("📊 RESUMO DO UPLOAD")
    print("=" * 70)
    print(f"✅ Sucessos: {success_count}")
    print(f"❌ Erros: {error_count}")
    print(f"📦 Total: {len(image_files)}")
    print()

    if uploaded_urls:
        # Salvar URLs em arquivo JSON
        import json
        from pathlib import Path

        output_dir = Path('cloudinary_urls')
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / 'facas_urls.json'

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(uploaded_urls, f, indent=2, ensure_ascii=False)

        print(f"💾 URLs salvas em: {output_file.absolute()}")
        print()

    print("🎉 Upload concluído!")
    print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("⚠️  Operação cancelada pelo usuário")
        sys.exit(0)
    except Exception as e:
        print()
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
