#!/usr/bin/env python
"""
Script para renomear arquivos nas subpastas de FACAS

Pasta: /Users/paulo/Downloads/ALL SKINS/ALL SKINS/FACAS

Para cada subpasta (ex: KARAMBIT, BAYONET):
    Renomeia os arquivos dentro dela para: {PASTA}-{arquivo}.{extensao}

Exemplo:
    KARAMBIT/Doppler.png -> KARAMBIT/KARAMBIT-Doppler.png
    BAYONET/Tiger Tooth.webp -> BAYONET/BAYONET-Tiger Tooth.webp

Uso:
    python rename_facas_files.py
"""

import os
from pathlib import Path


# ========== CONFIGURAÇÃO ==========
# Pasta com as facas
FACAS_FOLDER = Path('/Users/paulo/Downloads/ALL SKINS/ALL SKINS/FACAS')
# ===================================


def rename_files_in_folder(folder_path):
    """
    Renomeia todos os arquivos em uma pasta adicionando o nome da pasta como prefixo

    Args:
        folder_path: Path da pasta

    Returns:
        tuple: (success_count, error_count, renames)
    """
    success_count = 0
    error_count = 0
    renames = []

    folder_name = folder_path.name

    # Listar todos os arquivos (não subpastas)
    files = [f for f in folder_path.iterdir() if f.is_file()]

    for file in files:
        # Nome original do arquivo
        original_name = file.name

        # Verificar se já tem o prefixo
        if original_name.startswith(f"{folder_name}-"):
            print(f"   ⏭️  Já renomeado: {original_name}")
            continue

        # Criar novo nome: {PASTA}-{arquivo}.{extensao}
        new_name = f"{folder_name}-{original_name}"
        new_path = file.parent / new_name

        try:
            # Renomear o arquivo
            file.rename(new_path)
            success_count += 1
            renames.append({
                'folder': folder_name,
                'old_name': original_name,
                'new_name': new_name
            })
            print(f"   ✅ {original_name} → {new_name}")

        except Exception as e:
            error_count += 1
            print(f"   ❌ Erro ao renomear {original_name}: {e}")

    return success_count, error_count, renames


def main():
    print("=" * 70)
    print("📝 RENOMEANDO ARQUIVOS DE FACAS")
    print("=" * 70)
    print()

    # Verificar se a pasta existe
    print(f"📁 Pasta: {FACAS_FOLDER}")

    if not FACAS_FOLDER.exists():
        print(f"❌ Erro: Pasta não encontrada!")
        return

    if not FACAS_FOLDER.is_dir():
        print(f"❌ Erro: Não é uma pasta!")
        return

    print(f"✅ Pasta encontrada!")
    print()

    # Listar subpastas
    print("🔍 Procurando subpastas...")
    subfolders = [f for f in FACAS_FOLDER.iterdir() if f.is_dir()]

    if not subfolders:
        print("⚠️  Nenhuma subpasta encontrada!")
        return

    print(f"📦 Encontradas {len(subfolders)} subpastas:")
    for folder in sorted(subfolders):
        file_count = len([f for f in folder.iterdir() if f.is_file()])
        print(f"   • {folder.name} ({file_count} arquivos)")

    print()

    # Pedir confirmação (ou usar argumento --yes)
    import sys
    if '--yes' in sys.argv or '-y' in sys.argv:
        print("✅ Modo automático ativado (--yes)")
        response = 's'
    else:
        try:
            response = input("Deseja continuar com a renomeação? (s/n): ").strip().lower()
        except EOFError:
            print("⚠️  Sem input disponível. Use --yes para modo automático")
            return

    if response != 's':
        print("⚠️  Operação cancelada pelo usuário")
        return

    print()
    print("=" * 70)
    print("🚀 INICIANDO RENOMEAÇÃO")
    print("=" * 70)
    print()

    # Processar cada subpasta
    total_success = 0
    total_errors = 0
    all_renames = []

    for folder in sorted(subfolders):
        print(f"📁 Processando: {folder.name}")

        success, errors, renames = rename_files_in_folder(folder)

        total_success += success
        total_errors += errors
        all_renames.extend(renames)

        print(f"   ✅ Sucessos: {success} | ❌ Erros: {errors}")
        print()

    # Resumo final
    print("=" * 70)
    print("📊 RESUMO FINAL")
    print("=" * 70)
    print(f"✅ Arquivos renomeados: {total_success}")
    print(f"❌ Erros: {total_errors}")
    print(f"📁 Subpastas processadas: {len(subfolders)}")
    print()

    if all_renames:
        # Salvar log de renomeações
        import json

        log_file = Path('rename_log.json')

        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(all_renames, f, indent=2, ensure_ascii=False)

        print(f"💾 Log salvo em: {log_file.absolute()}")
        print()

    print("🎉 Renomeação concluída!")
    print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("⚠️  Operação cancelada pelo usuário")
        exit(0)
    except Exception as e:
        print()
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
