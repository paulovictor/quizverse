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


def request_folder(prompt: str, base_path: Path) -> Path:
    """Solicita ao usuário um nome de subpasta e valida sua existência."""

    while True:
        try:
            folder_name = input(prompt).strip()
        except EOFError:
            print("\n⚠️  Nenhum input recebido. Encerrando.")
            raise SystemExit(1)

        if not folder_name:
            print("⚠️  O nome da pasta não pode ficar em branco.")
            continue

        candidate = (base_path / folder_name).expanduser().resolve()

        if not candidate.exists() or not candidate.is_dir():
            print(f"❌ Pasta não encontrada: {candidate}")
            continue

        return candidate


def collect_images(folder: Path) -> List[Path]:
    """Retorna todas as imagens (recursivo) dentro da pasta informada."""

    files: List[Path] = []
    for path in folder.rglob("*"):
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
            files.append(path)

    return sorted(files)


def upload_files(files: Iterable[Path], cloud_folder: str) -> List[dict]:
    """Realiza o upload e retorna a lista com metadados das imagens enviadas."""

    uploaded: List[dict] = []

    for index, file_path in enumerate(files, start=1):
        print(f"[{index}] Enviando: {file_path.name}")

        try:
            result = cloudinary.uploader.upload(
                str(file_path),
                folder=cloud_folder or None,
                resource_type="image",
                use_filename=False,          # garante URL com ID aleatório
                unique_filename=True,
                overwrite=False,
                display_name=file_path.stem,  # mantém o display name legível
            )
        except Exception as error:  # pragma: no cover - feedback em runtime
            print(f"   ❌ Erro ao enviar {file_path.name}: {error}")
            continue

        uploaded.append(
            {
                "filename": file_path.name,
                "display_name": result.get("display_name"),
                "public_id": result.get("public_id"),
                "secure_url": result.get("secure_url"),
                "asset_id": result.get("asset_id"),
                "bytes": result.get("bytes"),
                "width": result.get("width"),
                "height": result.get("height"),
            }
        )

        print(f"   ✅ Upload concluído. URL: {result.get('secure_url')}")

    return uploaded


def save_report(data: List[dict], output_name: str) -> None:
    """Salva o relatório das URLs em ``cloudinary_urls/<nome>.json``."""

    if not data:
        return

    output_dir = Path(__file__).resolve().parent.parent / "cloudinary_urls"
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / f"{output_name}.json"
    with output_file.open("w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=2, ensure_ascii=False)

    print(f"💾 Relatório salvo em: {output_file.resolve()}")


def main() -> None:
    print("=" * 70)
    print("☁️  UPLOAD DE IMAGENS PARA O CLOUDINARY")
    print("=" * 70)

    if not UPLOAD_ROOT.exists():
        print(f"❌ Pasta raiz 'upload' não encontrada em {UPLOAD_ROOT}")
        raise SystemExit(1)

    print(f"📁 Pasta raiz local: {UPLOAD_ROOT}")

    # 1. Solicitar a subpasta local
    local_folder = request_folder(
        "Informe a subpasta dentro de 'upload/' a ser enviada: ", UPLOAD_ROOT
    )

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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  Interrompido pelo usuário.")
        sys.exit(1)

