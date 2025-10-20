#!/usr/bin/env python
"""Ferramenta interativa para enviar imagens ao Cloudinary.

Etapas:
1. Solicita o nome da subpasta dentro de ``upload/``.
2. Pede a pasta de destino no Cloudinary (ex.: ``cs/facas``).
3. Envia todas as imagens encontradas nessa subpasta.

Requisitos:
- Variáveis de ambiente ``CLOUDINARY_CLOUD_NAME``, ``CLOUDINARY_API_KEY`` e
  ``CLOUDINARY_API_SECRET`` configuradas (ou valores padrão já definidos).
- Biblioteca ``cloudinary`` instalada (``uv add cloudinary``).

Uso:
    uv run python upload_cloudinary.py
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Iterable, List

try:
    import cloudinary
    import cloudinary.uploader
except ImportError as exc:  # pragma: no cover - feedback rápido ao usuário
    print("❌ A biblioteca 'cloudinary' não está instalada.")
    print("💡 Execute: uv add cloudinary")
    raise SystemExit(1) from exc


# Credenciais (podem ser sobrescritas por variáveis de ambiente)
CLOUD_NAME = os.environ.get("CLOUDINARY_CLOUD_NAME", "dwm53cbu2")
API_KEY = os.environ.get("CLOUDINARY_API_KEY", "429396283651242")
API_SECRET = os.environ.get("CLOUDINARY_API_SECRET", "HTF--7Ceic5mmOo_oxboCTzXiis")

# Caminho raiz onde os arquivos aguardam upload
UPLOAD_ROOT = Path(__file__).resolve().parent.parent / "setup_upload"

# Extensões suportadas
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".avif"}


def configure_cloudinary() -> None:
    """Configura o SDK com credenciais obtidas do ambiente."""

    cloudinary.config(
        cloud_name=CLOUD_NAME,
        api_key=API_KEY,
        api_secret=API_SECRET,
        secure=True,
    )


def list_available_folders(base_path: Path) -> List[Path]:
    """Lista todas as pastas disponíveis no diretório base."""
    
    folders = []
    if base_path.exists() and base_path.is_dir():
        for item in base_path.iterdir():
            if item.is_dir():
                folders.append(item)
    
    return sorted(folders)


def request_folder(base_path: Path) -> Path:
    """Lista pastas disponíveis e solicita ao usuário selecionar por número."""

    # Listar pastas disponíveis
    available_folders = list_available_folders(base_path)
    
    if not available_folders:
        print("❌ Nenhuma pasta encontrada no diretório de upload.")
        raise SystemExit(1)
    
    print("\n📁 PASTAS DISPONÍVEIS:")
    print("=" * 50)
    for i, folder in enumerate(available_folders, 1):
        # Contar imagens na pasta
        image_count = len(collect_images(folder))
        print(f"{i:2d}. {folder.name} ({image_count} imagens)")
    
    print("=" * 50)
    
    while True:
        try:
            choice = input(f"\nSelecione uma pasta (1-{len(available_folders)}): ").strip()
        except EOFError:
            print("\n⚠️  Nenhum input recebido. Encerrando.")
            raise SystemExit(1)

        if not choice:
            print("⚠️  Por favor, digite um número.")
            continue

        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(available_folders):
                selected_folder = available_folders[choice_num - 1]
                print(f"✅ Pasta selecionada: {selected_folder.name}")
                return selected_folder
            else:
                print(f"⚠️  Por favor, digite um número entre 1 e {len(available_folders)}.")
        except ValueError:
            print("⚠️  Por favor, digite um número válido.")


def collect_images(folder: Path) -> List[Path]:
    """Retorna todas as imagens (recursivo) dentro da pasta informada."""

    files: List[Path] = []
    for path in folder.rglob("*"):
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
            files.append(path)

    return sorted(files)


def parse_multilingual_filename(filename: str) -> dict:
    """
    Analisa o nome do arquivo para extrair nomes em diferentes idiomas.
    
    Se o arquivo contém ponto e vírgula, assume formato: ENGLISH;PORTUGUESE;SPANISH
    Caso contrário, usa o nome original como português.
    
    Retorna dict com display_name, display_name_en, display_name_es
    """
    # Remove a extensão
    name_without_ext = Path(filename).stem
    
    # Verifica se contém ponto e vírgula
    if ';' in name_without_ext:
        parts = name_without_ext.split(';')
        if len(parts) >= 3:
            # Formato: ENGLISH;PORTUGUESE;SPANISH
            english = parts[0].strip()
            portuguese = parts[1].strip()
            spanish = parts[2].strip()
        elif len(parts) == 2:
            # Formato: ENGLISH;PORTUGUESE (sem espanhol)
            english = parts[0].strip()
            portuguese = parts[1].strip()
            spanish = portuguese  # Usa português como fallback
        else:
            # Formato inesperado, usa o nome original
            english = name_without_ext
            portuguese = name_without_ext
            spanish = name_without_ext
    else:
        # Sem ponto e vírgula, usa o nome original como português
        english = name_without_ext
        portuguese = name_without_ext
        spanish = name_without_ext
    
    return {
        "display_name": portuguese,  # Nome principal em português
        "display_name_en": english,
        "display_name_es": spanish
    }


def upload_files(files: Iterable[Path], cloud_folder: str) -> List[dict]:
    """Realiza o upload e retorna a lista com metadados das imagens enviadas."""

    uploaded: List[dict] = []

    for index, file_path in enumerate(files, start=1):
        print(f"[{index}] Enviando: {file_path.name}")

        # Analisar nome do arquivo para idiomas
        multilingual_info = parse_multilingual_filename(file_path.name)
        
        # Usar o nome em português para o upload
        upload_display_name = multilingual_info["display_name"]

        try:
            result = cloudinary.uploader.upload(
                str(file_path),
                folder=cloud_folder or None,
                resource_type="image",
                use_filename=False,          # garante URL com ID aleatório
                unique_filename=True,
                overwrite=False,
                display_name=upload_display_name,  # Nome em português para upload
            )
        except Exception as error:  # pragma: no cover - feedback em runtime
            print(f"   ❌ Erro ao enviar {file_path.name}: {error}")
            continue

        # Criar objeto com informações multilíngues
        item_data = {
            "filename": file_path.name,
            "display_name": multilingual_info["display_name"],  # Português
            "display_name_en": multilingual_info["display_name_en"],  # Inglês
            "display_name_es": multilingual_info["display_name_es"],  # Espanhol
            "public_id": result.get("public_id"),
            "secure_url": result.get("secure_url"),
            "asset_id": result.get("asset_id"),
            "bytes": result.get("bytes"),
            "width": result.get("width"),
            "height": result.get("height"),
        }

        uploaded.append(item_data)

        print(f"   ✅ Upload concluído. URL: {result.get('secure_url')}")
        print(f"   🌐 Nomes: PT='{multilingual_info['display_name']}', EN='{multilingual_info['display_name_en']}', ES='{multilingual_info['display_name_es']}'")

    return uploaded


def save_report(data: List[dict], output_name: str) -> None:
    """Salva o relatório das URLs em ``setup/cloudinary_urls/<nome>.json``."""

    if not data:
        return

    output_dir = Path(__file__).resolve().parent / "cloudinary_urls"
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / f"{output_name}.json"
    with output_file.open("w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=2, ensure_ascii=False)

    print(f"💾 Relatório salvo em: {output_file.resolve()}")


def generate_chatgpt_prompt(data: List[dict], folder_name: str) -> str:
    """Gera o texto para copiar e colar no ChatGPT."""
    
    if not data:
        return ""
    
    # Extrair nomes dos arquivos (sem extensão)
    item_names = []
    for item in data:
        filename = item.get('filename', '')
        # Remover extensão
        name = Path(filename).stem
        item_names.append(name)
    
    # Gerar o texto
    prompt = f"""* Crie uma lista de similaridade para todos esses itens:

me retorne um json nessa estrutura 
{{ {{item}}:[similar1, similar2, similar3] }} 

faça 1 desse para cada item desta lista: 
{json.dumps(item_names, indent=2, ensure_ascii=False)}"""
    
    return prompt


def main() -> None:
    print("=" * 70)
    print("☁️  UPLOAD DE IMAGENS PARA O CLOUDINARY")
    print("=" * 70)

    if not UPLOAD_ROOT.exists():
        print(f"❌ Pasta raiz 'upload' não encontrada em {UPLOAD_ROOT}")
        raise SystemExit(1)

    print(f"📁 Pasta raiz local: {UPLOAD_ROOT}")

    # 1. Solicitar a subpasta local
    local_folder = request_folder(UPLOAD_ROOT)

    # 2. Destino no Cloudinary
    try:
        cloudinary_folder = input(
            "Pasta de destino no Cloudinary (ex.: cs/facas) [enter para root]: "
        ).strip()
    except EOFError:
        print("\n⚠️  Nenhum input recebido. Encerrando.")
        raise SystemExit(1)

    # 3. Coletar arquivos
    image_files = collect_images(local_folder)
    if not image_files:
        print("⚠️  Nenhuma imagem encontrada nessa pasta.")
        raise SystemExit(0)

    print(f"🔎 Encontradas {len(image_files)} imagens para upload.")

    # Confirmar antes de enviar
    preview = ", ".join(file.name for file in image_files[:5])
    if len(image_files) > 5:
        preview += f" … (+{len(image_files) - 5} arquivos)"

    print(f"Mostrando alguns exemplos: {preview}")

    try:
        proceed = input("Deseja continuar? (s/n): ").strip().lower()
    except EOFError:
        print("\n⚠️  Nenhum input recebido. Encerrando.")
        raise SystemExit(1)
    if proceed != "s":
        print("⚠️  Operação cancelada pelo usuário.")
        raise SystemExit(0)

    # Iniciar upload
    configure_cloudinary()

    uploaded = upload_files(image_files, cloudinary_folder)

    print("=" * 70)
    print("📊 RESUMO")
    print("=" * 70)
    print(f"✅ Sucessos: {len(uploaded)}")
    print(f"❌ Falhas: {len(image_files) - len(uploaded)}")

    save_report(uploaded, local_folder.name)
    
    # Gerar prompt para ChatGPT
    if uploaded:
        print("\n" + "=" * 70)
        print("🤖 TEXTO PARA COPIAR NO CHATGPT")
        print("=" * 70)
        chatgpt_prompt = generate_chatgpt_prompt(uploaded, local_folder.name)
        print(chatgpt_prompt)
        print("=" * 70)
        print("📋 Copie o texto acima e cole no ChatGPT para gerar similaridades!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  Interrompido pelo usuário.")
        sys.exit(1)

