"""
Script para inspecionar a estrutura do cs_data.json
"""

import json

def inspect_json():
    print("🔍 Inspecionando cs_data.json...\n")
    
    try:
        with open('cs_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ Arquivo carregado com sucesso!")
        print(f"📊 Tipo do objeto principal: {type(data)}")
        print(f"📊 Tamanho: {len(data)} items\n")
        
        # Se for dict, mostrar as chaves principais
        if isinstance(data, dict):
            print("🔑 Chaves principais do JSON:")
            for key in list(data.keys())[:10]:  # Primeiras 10 chaves
                print(f"   - {key}")
            
            if len(data.keys()) > 10:
                print(f"   ... e mais {len(data.keys()) - 10} chaves\n")
            
            # Pegar o primeiro item como exemplo
            first_key = list(data.keys())[0]
            first_item = data[first_key]
            
            print(f"\n📄 Exemplo do primeiro item (chave: '{first_key}'):")
            print(json.dumps(first_item, indent=2, ensure_ascii=False)[:500])
            
            if isinstance(first_item, dict):
                print(f"\n🔑 Campos disponíveis no item:")
                for field in first_item.keys():
                    print(f"   - {field}: {type(first_item[field])}")
        
        elif isinstance(data, list):
            print(f"📋 É uma lista com {len(data)} items")
            print(f"\n📄 Exemplo do primeiro item:")
            print(json.dumps(data[0], indent=2, ensure_ascii=False)[:500])
        
        # Buscar alguns items específicos para entender melhor
        print("\n\n🔎 Procurando por skins de armas...")
        weapon_count = 0
        
        if isinstance(data, dict):
            for key, value in list(data.items())[:100]:  # Primeiros 100
                if isinstance(value, dict):
                    name = value.get('name', key)
                    if ' | ' in name and 'Glock' in name:
                        print(f"\n✅ Encontrei uma skin da Glock-18:")
                        print(f"   Nome: {name}")
                        print(f"   Estrutura:")
                        print(json.dumps(value, indent=2, ensure_ascii=False)[:800])
                        weapon_count += 1
                        break
        
        if weapon_count == 0:
            print("⚠️  Não encontrei skins de armas nos primeiros 100 items")
            print("\n💡 Vou mostrar os primeiros 5 items completos:\n")
            
            if isinstance(data, dict):
                for idx, (key, value) in enumerate(list(data.items())[:5]):
                    print(f"\n--- Item {idx + 1} (chave: {key}) ---")
                    print(json.dumps(value, indent=2, ensure_ascii=False)[:400])
                    print("...")
    
    except FileNotFoundError:
        print("❌ Arquivo 'cs_data.json' não encontrado!")
    
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    inspect_json()