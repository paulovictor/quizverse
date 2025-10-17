#!/usr/bin/env python
"""
Script para criar quiz de facas do CS a partir de knives_urls.json

Estrutura do quiz:
{
    "question": "Qual é o nome desta faca?",
    "picture": "URL modificada com parâmetros Cloudinary",
    "correct_answer": "Nome da faca",
    "wrong_answers": ["Faca 1", "Faca 2", "Faca 3"]
}

Parâmetros Cloudinary a adicionar:
/a_320/a_hflip/w_1000,f_auto,q_auto:low,fl_lossy,fl_progressive,fl_strip_profile/
"""

import json
import re
from pathlib import Path

def extract_knife_name(public_id):
    """
    Extrai o nome da faca do public_id

    Exemplos:
    - "KARAMBIT-Doppler" -> "KARAMBIT Doppler"
    - "BAYONET-Fade" -> "BAYONET Fade"
    """
    # Remover underscores no final (IDs do Cloudinary)
    name = re.sub(r'_[a-z0-9]+$', '', public_id)

    # Substituir hífen por espaço
    name = name.replace('-', ' ')

    # Substituir underscores por espaços
    name = name.replace('_', ' ')

    return name.strip()

def get_knife_type(knife_name):
    """
    Extrai o tipo de faca (primeira palavra)

    Exemplo: "KARAMBIT Doppler" -> "KARAMBIT"
    """
    parts = knife_name.split()
    if parts:
        return parts[0]
    return ""

def get_knife_skin(knife_name):
    """
    Extrai a skin da faca (tudo após o tipo)

    Exemplo: "KARAMBIT Doppler" -> "Doppler"
    """
    parts = knife_name.split(maxsplit=1)
    if len(parts) > 1:
        return parts[1]
    return ""

def modify_cloudinary_url(url):
    """
    Adiciona parâmetros na URL do Cloudinary

    Formato original:
    https://res.cloudinary.com/dwm53cbu2/image/upload/v1760677330/Vice_doktdh.webp

    Formato modificado:
    https://res.cloudinary.com/dwm53cbu2/image/upload/a_320/a_hflip/w_1000,f_auto,q_auto:low,fl_lossy,fl_progressive,fl_strip_profile/v1760677330/Vice_doktdh.webp
    """
    # Parâmetros a adicionar
    params = "a_320/a_hflip/w_1000,f_auto,q_auto:low,fl_lossy,fl_progressive,fl_strip_profile"

    # Substituir /upload/ por /upload/{params}/
    modified_url = url.replace('/upload/', f'/upload/{params}/')

    return modified_url

def find_similar_knives(knife_name, all_knives, count=3):
    """
    Encontra facas similares para criar respostas erradas

    Critérios:
    - Mesma skin, tipo diferente (prioridade alta)
    - Mesmo tipo, skin diferente (prioridade média)
    - Aleatórias (prioridade baixa)
    """
    similar = []

    knife_type = get_knife_type(knife_name)
    knife_skin = get_knife_skin(knife_name)

    # Criar lista de candidatos com score
    candidates = []

    for other_knife in all_knives:
        other_name = other_knife['name']

        # Não incluir a própria faca
        if other_name == knife_name:
            continue

        other_type = get_knife_type(other_name)
        other_skin = get_knife_skin(other_name)

        score = 0

        # +10 pontos: mesma skin, tipo diferente (muito confuso!)
        if knife_skin and other_skin and knife_skin == other_skin and knife_type != other_type:
            score += 10

        # +5 pontos: mesmo tipo, skin diferente
        elif knife_type and other_type and knife_type == other_type and knife_skin != other_skin:
            score += 5

        # +1 ponto: skin similar (primeiras 3 letras iguais)
        if knife_skin and other_skin and len(knife_skin) >= 3 and len(other_skin) >= 3:
            if knife_skin[:3].lower() == other_skin[:3].lower():
                score += 1

        candidates.append({
            'name': other_name,
            'score': score
        })

    # Ordenar por score (maior primeiro)
    candidates.sort(key=lambda x: x['score'], reverse=True)

    # Pegar os top 'count'
    similar = [c['name'] for c in candidates[:count]]

    # Se não encontrou suficientes, pegar aleatórios
    if len(similar) < count:
        import random
        remaining = [c['name'] for c in candidates[len(similar):]]
        random.shuffle(remaining)
        similar.extend(remaining[:count - len(similar)])

    return similar[:count]

def create_quiz_questions(knives_data):
    """
    Cria as questões do quiz
    """
    quiz = []

    # Primeiro, extrair nomes de todas as facas
    all_knives = []
    for knife in knives_data:
        name = extract_knife_name(knife['public_id'])
        all_knives.append({
            'name': name,
            'public_id': knife['public_id'],
            'url': knife['secure_url']
        })

    print(f"   📊 Total de facas: {len(all_knives)}")
    print()

    # Criar questão para cada faca
    for i, knife in enumerate(all_knives):
        # URL modificada
        picture_url = modify_cloudinary_url(knife['url'])

        # Encontrar facas similares
        wrong_answers = find_similar_knives(knife['name'], all_knives, count=3)

        # Criar questão
        question = {
            'question': 'Qual é o nome desta faca?',
            'picture': picture_url,
            'correct_answer': knife['name'],
            'wrong_answers': wrong_answers
        }

        quiz.append(question)

        # Progress
        if (i + 1) % 100 == 0:
            print(f"   Processadas: {i + 1}/{len(all_knives)}")

    return quiz

def main():
    print("=" * 70)
    print("🔪 CRIANDO QUIZ DE FACAS DO CS")
    print("=" * 70)
    print()

    # Carregar dados
    print("📂 Carregando knives_urls.json...")
    input_file = Path('cloudinary_urls/knives_urls.json')

    if not input_file.exists():
        print(f"❌ Erro: Arquivo não encontrado: {input_file}")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        knives_data = json.load(f)

    print(f"   ✅ {len(knives_data)} facas carregadas")
    print()

    # Criar questões
    print("🎮 Criando questões do quiz...")
    quiz = create_quiz_questions(knives_data)
    print(f"   ✅ {len(quiz)} questões criadas")
    print()

    # Criar diretório build_quiz se não existir
    output_dir = Path('build_quiz')
    output_dir.mkdir(exist_ok=True)

    # Salvar arquivo
    output_file = output_dir / 'knives_quiz.json'

    print("💾 Salvando quiz...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(quiz, f, indent=2, ensure_ascii=False)

    print(f"   ✅ Salvo em: {output_file.absolute()}")
    print()

    # Estatísticas
    print("=" * 70)
    print("📊 ESTATÍSTICAS")
    print("=" * 70)
    print(f"Total de questões: {len(quiz)}")
    print()

    # Contar tipos de facas
    knife_types = {}
    for q in quiz:
        knife_type = get_knife_type(q['correct_answer'])
        knife_types[knife_type] = knife_types.get(knife_type, 0) + 1

    print("Distribuição por tipo:")
    for knife_type, count in sorted(knife_types.items(), key=lambda x: x[1], reverse=True):
        print(f"   • {knife_type}: {count} skins")

    print()

    # Preview
    print("=" * 70)
    print("📋 PREVIEW (3 primeiras questões)")
    print("=" * 70)
    for i, q in enumerate(quiz[:3], 1):
        print(f"\n{i}. {q['question']}")
        print(f"   Resposta correta: {q['correct_answer']}")
        print(f"   Respostas erradas:")
        for wrong in q['wrong_answers']:
            print(f"      - {wrong}")
        print(f"   URL: {q['picture'][:80]}...")

    print()
    print("🎉 Quiz criado com sucesso!")
    print()

if __name__ == '__main__':
    main()
