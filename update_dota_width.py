#!/usr/bin/env python3
"""
Script para alterar a largura das URLs do Cloudinary no arquivo dota.json
De w_1000 para w_300
"""

import json
from pathlib import Path

def update_dota_width():
    """Atualiza a largura das URLs no arquivo dota.json"""
    file_path = Path("setup/cloudinary_urls/dota.json")
    
    print("🔄 ATUALIZANDO LARGURA - DOTA.JSON")
    print("=" * 50)
    print(f"📁 Arquivo: {file_path}")
    print(f"🎯 Mudança: w_1000 → w_300")
    print()
    
    if not file_path.exists():
        print(f"❌ Arquivo não encontrado: {file_path}")
        return
    
    try:
        # Ler arquivo original
        print("📖 Lendo arquivo...")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ {len(data)} itens encontrados")
        
        # Atualizar URLs
        print("\n🔄 Atualizando URLs...")
        updated_count = 0
        
        for item in data:
            if 'secure_url' in item:
                original_url = item['secure_url']
                
                # Substituir w_1000 por w_300
                if 'w_1000' in original_url:
                    new_url = original_url.replace('w_1000', 'w_300')
                    item['secure_url'] = new_url
                    updated_count += 1
        
        # Salvar arquivo atualizado
        print(f"\n💾 Salvando arquivo atualizado...")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"\n✨ Processo concluído!")
        print(f"📊 URLs atualizadas: {updated_count}/{len(data)}")
        print(f"📊 URLs já com w_300: {len(data) - updated_count}")
        
    except Exception as e:
        print(f"\n❌ Erro ao processar arquivo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    update_dota_width()

