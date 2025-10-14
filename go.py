"""
CS2 Skins - Processar arquivo JSON local do CSGOBackpack
Cole o JSON que você recebeu em um arquivo chamado 'csgo_items.json'

Execução:
python cs2_local_json.py
"""

import json
import os
import random

def create_filename(weapon_name):
    """Cria nome de arquivo válido"""
    return weapon_name.lower().replace(' ', '_').replace('-', '_').replace('/', '_')

def extract_condition(name):
    """Extrai a condição da skin"""
    conditions = {
        '(Factory New)': 5,
        '(Minimal Wear)': 4,
        '(Field-Tested)': 3,
        '(Well-Worn)': 2,
        '(Battle-Scarred)': 1
    }
    
    for condition, priority in conditions.items():
        if condition in name:
            return condition, priority
    
    return None, 0

def load_json_file(filename='cs_data.json'):
    """Carrega arquivo JSON local"""
    print(f"📂 Carregando arquivo: {filename}")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Verificar se tem a estrutura do CSGOBackpack
        if isinstance(data, dict) and 'items_list' in data:
            items = data['items_list']
            print(f"✅ Arquivo carregado com {len(items)} items")
            return items
        
        # Se não, assumir que já é a lista de items
        print(f"✅ Arquivo carregado com {len(data)} items")
        return data
    
    except FileNotFoundError:
        print(f"❌ Arquivo '{filename}' não encontrado!")
        print("\n💡 Certifique-se de que o arquivo 'cs_data.json' está na mesma pasta do script")
        return {}
    
    except Exception as e:
        print(f"❌ Erro ao carregar arquivo: {str(e)}")
        return {}

def organize_by_weapon(items):
    """Organiza items por arma, priorizando melhor condição"""
    print("\n📊 Organizando skins por arma (priorizando Factory New)...")
    
    weapons_skins = {}
    
    for item_name, item_data in items.items():
        # Pular StatTrak e Souvenir
        if 'StatTrak™' in item_name or 'Souvenir' in item_name:
            continue
        
        # Pular stickers e outros
        if 'Sticker' in item_name or 'Patch' in item_name or 'Pin' in item_name:
            continue
        
        # Filtrar apenas skins de armas (tem " | " no nome)
        if ' | ' not in item_name:
            continue
        
        # Separar arma e skin
        parts = item_name.split(' | ')
        if len(parts) != 2:
            continue
        
        weapon = parts[0].strip()
        skin_with_condition = parts[1].strip()
        
        # Extrair condição e prioridade
        condition, priority = extract_condition(skin_with_condition)
        
        # Remove condição do nome da skin
        skin = skin_with_condition
        if condition:
            skin = skin.replace(condition, '').strip()
        
        # Remove ★ (facas)
        weapon = weapon.replace('★', '').strip()
        skin = skin.replace('★', '').strip()
        
        # Construir URL completa da imagem
        icon_url = item_data.get('icon_url', '')
        if icon_url:
            # Remover o "-" inicial se existir
            if icon_url.startswith('-'):
                icon_url = icon_url[1:]
            
            # Construir URL correta do Steam CDN
            image_url = f"https://steamcommunity-a.akamaihd.net/economy/image/{icon_url}/330x192"
        else:
            image_url = ''
        
        # Inicializar arma se não existir
        if weapon not in weapons_skins:
            weapons_skins[weapon] = {}
        
        # Adicionar ou atualizar skin se for melhor condição
        if skin not in weapons_skins[weapon]:
            weapons_skins[weapon][skin] = {
                'name': skin,
                'weapon': weapon,
                'image': image_url,
                'condition': condition or 'N/A',
                'priority': priority,
                'full_name': item_name
            }
        else:
            # Se já existe, manter apenas se for melhor condição
            if priority > weapons_skins[weapon][skin]['priority']:
                weapons_skins[weapon][skin] = {
                    'name': skin,
                    'weapon': weapon,
                    'image': image_url,
                    'condition': condition or 'N/A',
                    'priority': priority,
                    'full_name': item_name
                }
    
    return weapons_skins

def generate_options(all_skins, current_skin_name, count=3):
    """Gera opções aleatórias"""
    other_skins = [s for s in all_skins if s != current_skin_name]
    
    if len(other_skins) >= count:
        return random.sample(other_skins, count)
    else:
        return other_skins + [''] * (count - len(other_skins))

def save_weapon_json(weapon_name, skins_dict):
    """Salva JSON de uma arma"""
    output_dir = './cs2_skins'
    os.makedirs(output_dir, exist_ok=True)
    
    filename = create_filename(weapon_name)
    filepath = os.path.join(output_dir, f'{filename}.json')
    
    # Converter dict para lista
    skins_list = list(skins_dict.values())
    
    # Ordenar por prioridade (Factory New primeiro)
    skins_list.sort(key=lambda x: x['priority'], reverse=True)
    
    skin_names = [s['name'] for s in skins_list]
    
    # Preparar dados no formato do quiz
    quiz_data = []
    
    for idx, skin in enumerate(skins_list, 1):
        options = generate_options(skin_names, skin['name'], 3)
        
        quiz_data.append({
            'id': idx,
            'name': skin['name'],
            'foto': skin['image'],
            'opcoes': options
        })
    
    # Salvar JSON
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(quiz_data, f, indent=2, ensure_ascii=False)
    
    # Contar condições
    fn_count = sum(1 for s in skins_list if s['condition'] == '(Factory New)')
    mw_count = sum(1 for s in skins_list if s['condition'] == '(Minimal Wear)')
    
    print(f"💾 {weapon_name}: {len(quiz_data)} skins (FN: {fn_count}, MW: {mw_count})")
    return len(quiz_data)

def main():
    """Função principal"""
    print("=" * 70)
    print("🚀 CS2 SKINS - PROCESSANDO JSON LOCAL")
    print("=" * 70)
    print()
    
    # Carregar arquivo local
    items = load_json_file()
    
    if not items:
        print("\n❌ Sem dados para processar")
        return
    
    # Organizar por arma
    weapons_skins = organize_by_weapon(items)
    
    if not weapons_skins:
        print("❌ Nenhuma arma encontrada no arquivo")
        return
    
    print(f"\n✅ {len(weapons_skins)} armas encontradas")
    print("\n📝 Salvando arquivos JSON...\n")
    
    total_skins = 0
    total_fn = 0
    total_mw = 0
    
    for weapon, skins in sorted(weapons_skins.items()):
        if len(skins) >= 3:  # Apenas armas com pelo menos 3 skins
            count = save_weapon_json(weapon, skins)
            total_skins += count
            
            # Contar condições
            for skin_data in skins.values():
                if skin_data['condition'] == '(Factory New)':
                    total_fn += 1
                elif skin_data['condition'] == '(Minimal Wear)':
                    total_mw += 1
    
    # Resumo final
    print("\n" + "=" * 70)
    print("✨ CONCLUÍDO!")
    print("=" * 70)
    print(f"📊 Armas processadas: {len(weapons_skins)}")
    print(f"📊 Total de skins: {total_skins}")
    print(f"🏆 Factory New: {total_fn}")
    print(f"🥈 Minimal Wear: {total_mw}")
    print(f"🥉 Outras: {total_skins - total_fn - total_mw}")
    print(f"📁 Arquivos salvos em: ./cs2_skins/")
    print("=" * 70)

if __name__ == '__main__':
    main()