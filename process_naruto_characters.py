#!/usr/bin/env python
"""
Script para processar naruto_urls e criar dois arquivos:
- naruto_characters.json: Personagens de Naruto e Naruto Shippuden
- boruto_characters.json: Personagens novos de Boruto

Estrutura de cada personagem:
{
    "name": "Nome do personagem",
    "picture": "URL da imagem",
    "similar_characters": ["personagem1", "personagem2", "personagem3"]
}
"""

import json
import re
from pathlib import Path

# Personagens novos de Boruto (introduzidos apenas em Boruto)
BORUTO_EXCLUSIVE_CHARACTERS = {
    'エイダ', 'Eida', 'Ada',  # Eida/Ada
    'アマド', 'Amado',  # Amado
    'ボルト', 'Boruto',  # Boruto Uzumaki
    'サラダ', 'Sarada',  # Sarada Uchiha
    'ミツキ', 'Mitsuki',  # Mitsuki (new generation)
    'シカダイ', 'Shikadai',  # Shikadai Nara
    'チョウチョウ', 'Chocho', 'Chōchō',  # Chocho Akimichi
    'いのじん', 'Inojin',  # Inojin Yamanaka
    'メタル', 'Metal',  # Metal Lee
    'イワベエ', 'Iwabee',  # Iwabee Yuino
    'デンキ', 'Denki',  # Denki Kaminarimon
    'すみれ', 'Sumire',  # Sumire Kakei
    'わさび', 'Wasabi',  # Wasabi Izuno
    'なみだ', 'Namida',  # Namida Suzumeno
    'カワキ', 'Kawaki',  # Kawaki
    'デルタ', 'Delta',  # Delta
    'コード', 'Code',  # Code
    'ジゲン', 'Jigen',  # Jigen
    'ビクター', 'Victor',  # Victor
    'ディーパ', 'Deepa',  # Deepa
    'カシン', 'Kashin',  # Kashin Koji
    'イッシキ', 'Isshiki',  # Isshiki Otsutsuki
    'モモシキ', 'Momoshiki',  # Momoshiki (if only in Boruto)
    'キンシキ', 'Kinshiki',  # Kinshiki
    'ウラシキ', 'Urashiki',  # Urashiki
    'Shinki',  # Shinki
    'Araya',  # Araya
    'Yodo',  # Yodo
    'Houki',  # Houki Taketori
    'Hako',  # Hako Kuroi
    'Renga',  # Renga Kokubou
}

def is_boruto_character(name):
    """Verifica se o personagem é exclusivo de Boruto"""
    name_lower = name.lower()

    # Verificar se contém algum nome de personagem de Boruto
    for boruto_char in BORUTO_EXCLUSIVE_CHARACTERS:
        if boruto_char.lower() in name_lower:
            return True

    return False

def clean_name(name):
    """Limpa o nome do personagem"""
    # Remover \n
    name = name.strip()

    # Se nome vazio, retornar None
    if not name:
        return None

    return name

def load_characters(file_path):
    """Carrega os personagens do arquivo JSON"""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data

def filter_characters(characters):
    """
    Filtra personagens:
    - Remove entradas com picture = default.jpg
    - Remove entradas com nome vazio
    - Separa entre Naruto e Boruto
    """
    naruto_chars = []
    boruto_chars = []

    seen_names = set()  # Para evitar duplicatas

    for char in characters:
        name = clean_name(char.get('name', ''))
        picture = char.get('picture', '')

        # Ignorar se nome vazio
        if not name:
            continue

        # Ignorar se picture é default.jpg
        if picture == 'default.jpg':
            continue

        # Ignorar se já vimos este nome
        if name in seen_names:
            continue

        seen_names.add(name)

        char_data = {
            'name': name,
            'picture': picture
        }

        # Classificar entre Naruto e Boruto
        if is_boruto_character(name):
            boruto_chars.append(char_data)
        else:
            naruto_chars.append(char_data)

    return naruto_chars, boruto_chars

def find_similar_characters(char_name, all_characters, count=3):
    """
    Encontra personagens similares para criar alternativas no quiz

    Critérios de similaridade:
    - Mesma primeira letra
    - Tamanho de nome similar
    - Não incluir o próprio personagem
    """
    similar = []

    char_first_letter = char_name[0].lower() if char_name else ''
    char_length = len(char_name)

    # Criar lista de candidatos com score de similaridade
    candidates = []

    for other_char in all_characters:
        other_name = other_char['name']

        # Não incluir o próprio personagem
        if other_name == char_name:
            continue

        score = 0

        # +2 pontos se começa com mesma letra
        if other_name and other_name[0].lower() == char_first_letter:
            score += 2

        # +1 ponto se tamanho similar (diferença <= 3)
        if abs(len(other_name) - char_length) <= 3:
            score += 1

        candidates.append({
            'name': other_name,
            'score': score
        })

    # Ordenar por score (maior primeiro) e pegar os top 'count'
    candidates.sort(key=lambda x: x['score'], reverse=True)
    similar = [c['name'] for c in candidates[:count]]

    # Se não encontrou suficientes, pegar aleatórios
    if len(similar) < count:
        remaining = [c['name'] for c in candidates[len(similar):]]
        import random
        random.shuffle(remaining)
        similar.extend(remaining[:count - len(similar)])

    return similar[:count]

def create_quiz_structure(characters):
    """
    Cria a estrutura de quiz com similar_characters
    """
    quiz_data = []

    for i, char in enumerate(characters):
        similar = find_similar_characters(char['name'], characters, count=3)

        quiz_char = {
            'name': char['name'],
            'picture': char['picture'],
            'similar_characters': similar
        }

        quiz_data.append(quiz_char)

        # Progress
        if (i + 1) % 100 == 0:
            print(f"   Processados: {i + 1}/{len(characters)}")

    return quiz_data

def main():
    print("=" * 70)
    print("📊 PROCESSANDO PERSONAGENS DE NARUTO")
    print("=" * 70)
    print()

    # Carregar dados
    print("📂 Carregando naruto_urls...")
    characters = load_characters('naruto_urls')
    print(f"   ✅ {len(characters)} entradas carregadas")
    print()

    # Filtrar e separar
    print("🔍 Filtrando e separando personagens...")
    naruto_chars, boruto_chars = filter_characters(characters)
    print(f"   ✅ Naruto/Shippuden: {len(naruto_chars)} personagens")
    print(f"   ✅ Boruto exclusivos: {len(boruto_chars)} personagens")
    print()

    # Criar estrutura de quiz para Naruto
    print("🎮 Criando estrutura de quiz para Naruto/Shippuden...")
    naruto_quiz = create_quiz_structure(naruto_chars)
    print(f"   ✅ {len(naruto_quiz)} personagens processados")
    print()

    # Criar estrutura de quiz para Boruto
    print("🎮 Criando estrutura de quiz para Boruto...")
    boruto_quiz = create_quiz_structure(boruto_chars)
    print(f"   ✅ {len(boruto_quiz)} personagens processados")
    print()

    # Salvar arquivos
    print("💾 Salvando arquivos...")

    # naruto_characters.json
    with open('naruto_characters.json', 'w', encoding='utf-8') as f:
        json.dump(naruto_quiz, f, indent=2, ensure_ascii=False)
    print(f"   ✅ naruto_characters.json ({len(naruto_quiz)} personagens)")

    # boruto_characters.json
    with open('boruto_characters.json', 'w', encoding='utf-8') as f:
        json.dump(boruto_quiz, f, indent=2, ensure_ascii=False)
    print(f"   ✅ boruto_characters.json ({len(boruto_quiz)} personagens)")

    print()
    print("=" * 70)
    print("📊 RESUMO")
    print("=" * 70)
    print(f"Total original: {len(characters)} entradas")
    print(f"Naruto/Shippuden: {len(naruto_quiz)} personagens")
    print(f"Boruto: {len(boruto_quiz)} personagens")
    print()

    # Preview
    print("=" * 70)
    print("📋 PREVIEW - Naruto (5 primeiros)")
    print("=" * 70)
    for char in naruto_quiz[:5]:
        print(f"• {char['name']}")
        print(f"  Similares: {', '.join(char['similar_characters'])}")

    print()
    print("=" * 70)
    print("📋 PREVIEW - Boruto (5 primeiros)")
    print("=" * 70)
    for char in boruto_quiz[:5]:
        print(f"• {char['name']}")
        print(f"  Similares: {', '.join(char['similar_characters'])}")

    print()
    print("🎉 Concluído!")
    print()

if __name__ == '__main__':
    main()
