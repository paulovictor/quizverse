#!/usr/bin/env python3
"""
Script para renomear arquivos na pasta FACAS
Remove o hífen entre o tipo de faca e o estilo, e capitaliza corretamente
Exemplo: BAYONET-Autotronic.png -> Bayonet Autotronic.png
"""

import os
from pathlib import Path

def capitalize_knife_name(name):
    """
    Capitaliza o nome da faca corretamente
    Mantém siglas em maiúsculas (DDPAT)
    """
    # Palavras que devem permanecer em maiúsculas
    uppercase_words = ['DDPAT']
    
    # Split por espaços
    words = name.split()
    result = []
    
    for word in words:
        # Se a palavra está na lista de maiúsculas, mantém
        if word.upper() in uppercase_words:
            result.append(word.upper())
        # Se a palavra tem parênteses, capitaliza apenas a primeira letra antes do parêntese
        elif '(' in word:
            # Ex: (Phase -> (Phase
            parts = word.split('(')
            capitalized = parts[0].capitalize() + '(' + parts[1].capitalize()
            result.append(capitalized)
        else:
            # Capitaliza normalmente
            result.append(word.capitalize())
    
    return ' '.join(result)

def rename_facas_files():
    """Renomeia todos os arquivos na pasta FACAS"""
    facas_dir = Path("setup_upload/FACAS")
    
    if not facas_dir.exists():
        print(f"❌ Diretório não encontrado: {facas_dir}")
        return
    
    print("🔄 RENOMEANDO ARQUIVOS NA PASTA FACAS")
    print("=" * 60)
    
    # Lista todos os arquivos PNG
    files = sorted(facas_dir.glob("*.png"))
    
    if not files:
        print("❌ Nenhum arquivo PNG encontrado!")
        return
    
    print(f"📁 Total de arquivos: {len(files)}")
    print()
    
    renamed_count = 0
    skipped_count = 0
    
    for file_path in files:
        old_name = file_path.name
        
        # Remove a extensão
        name_without_ext = file_path.stem
        extension = file_path.suffix
        
        # Verifica se tem hífen
        if '-' in name_without_ext:
            # Separa pelo hífen
            parts = name_without_ext.split('-', 1)  # Split apenas no primeiro hífen
            
            if len(parts) == 2:
                knife_type = parts[0]  # Ex: BAYONET
                skin_name = parts[1]   # Ex: Autotronic
                
                # Capitaliza ambas as partes
                knife_type_capitalized = capitalize_knife_name(knife_type)
                skin_name_capitalized = capitalize_knife_name(skin_name)
                
                # Novo nome: junta com espaço
                new_name = f"{knife_type_capitalized} {skin_name_capitalized}{extension}"
                new_path = file_path.parent / new_name
                
                # Verifica se o novo nome é diferente
                if old_name != new_name:
                    # Renomeia o arquivo
                    try:
                        file_path.rename(new_path)
                        print(f"✅ {old_name}")
                        print(f"   → {new_name}")
                        renamed_count += 1
                    except Exception as e:
                        print(f"❌ Erro ao renomear {old_name}: {e}")
                else:
                    skipped_count += 1
            else:
                print(f"⚠️  Ignorado (formato inesperado): {old_name}")
                skipped_count += 1
        else:
            # Arquivo sem hífen, apenas capitaliza
            capitalized_name = capitalize_knife_name(name_without_ext) + extension
            
            if old_name != capitalized_name:
                new_path = file_path.parent / capitalized_name
                try:
                    file_path.rename(new_path)
                    print(f"✅ {old_name}")
                    print(f"   → {capitalized_name}")
                    renamed_count += 1
                except Exception as e:
                    print(f"❌ Erro ao renomear {old_name}: {e}")
            else:
                skipped_count += 1
    
    print()
    print("=" * 60)
    print(f"✨ Processo concluído!")
    print(f"📊 Arquivos renomeados: {renamed_count}")
    print(f"📊 Arquivos ignorados: {skipped_count}")
    print(f"📊 Total: {len(files)}")

if __name__ == '__main__':
    rename_facas_files()

