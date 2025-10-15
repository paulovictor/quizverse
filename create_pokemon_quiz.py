#!/usr/bin/env python
"""
Script para criar quiz de Pokémon com alternativas similares
Usa os dados baixados de download_gen1_pokemon.py
"""
import os
import json
import random
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme, Quiz, Question, Answer


def load_pokemon_data():
    """Carrega os dados dos Pokémon do arquivo JSON"""
    data_file = Path('pokemon_gen1/pokemon_data.json')
    
    if not data_file.exists():
        print("❌ Erro: Arquivo pokemon_data.json não encontrado!")
        print("Execute primeiro: python download_gen1_pokemon.py")
        return None
    
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_similar_pokemon(target_pokemon, all_pokemon, count=3):
    """
    Retorna Pokémon similares ao alvo para usar como alternativas incorretas
    
    Critérios de similaridade:
    1. Mesmo tipo primário
    2. Mesmo tipo secundário
    3. Tipos em comum
    4. Pokémon aleatórios se não houver similares suficientes
    """
    similar = []
    target_types = set(target_pokemon['types'])
    
    # 1. Pokémon com tipos exatamente iguais
    exact_matches = [
        p for p in all_pokemon 
        if p['id'] != target_pokemon['id'] 
        and set(p['types']) == target_types
    ]
    similar.extend(random.sample(exact_matches, min(count, len(exact_matches))))
    
    if len(similar) >= count:
        return similar[:count]
    
    # 2. Pokémon com pelo menos um tipo em comum
    partial_matches = [
        p for p in all_pokemon 
        if p['id'] != target_pokemon['id']
        and p not in similar
        and len(set(p['types']) & target_types) > 0
    ]
    remaining = count - len(similar)
    similar.extend(random.sample(partial_matches, min(remaining, len(partial_matches))))
    
    if len(similar) >= count:
        return similar[:count]
    
    # 3. Pokémon aleatórios
    remaining_pokemon = [
        p for p in all_pokemon 
        if p['id'] != target_pokemon['id']
        and p not in similar
    ]
    remaining = count - len(similar)
    similar.extend(random.sample(remaining_pokemon, min(remaining, len(remaining_pokemon))))
    
    return similar[:count]

def create_pokemon_quiz(num_questions=50):
    """Cria um quiz de Pokémon com alternativas similares"""
    
    # Carregar dados
    all_pokemon = load_pokemon_data()
    if not all_pokemon:
        return
    
    print(f"📊 {len(all_pokemon)} Pokémon carregados")
    print()
    
    # Criar ou obter o tema
    theme, created = Theme.objects.get_or_create(
        slug='pokemon',
        defaults={
            'title': '🎮 Pokémon',
            'description': 'Teste seus conhecimentos sobre Pokémon da Geração 1!',
            'active': True
        }
    )
    
    if created:
        print(f"✅ Tema '{theme.title}' criado!")
    else:
        print(f"ℹ️  Tema '{theme.title}' já existe.")
    
    # Criar ou obter o quiz
    quiz, created = Quiz.objects.get_or_create(
        slug='adivinhe-o-pokemon-gen1',
        theme=theme,
        defaults={
            'title': 'Adivinhe o Pokémon - Geração 1',
            'description': 'Identifique os 151 Pokémon originais olhando suas imagens! Teste seu conhecimento sobre a primeira geração.',
            'difficulty': 'medium',
            'active': True,
            'order': 1
        }
    )
    
    if created:
        print(f"✅ Quiz '{quiz.title}' criado!")
    else:
        print(f"ℹ️  Quiz '{quiz.title}' já existe.")
        # Limpar perguntas antigas
        quiz.questions.all().delete()
        print("   Perguntas antigas removidas.")
    
    print()
    print(f"🎮 Criando {num_questions} perguntas...")
    print("=" * 70)
    print()
    
    # Selecionar Pokémon aleatórios para o quiz
    selected_pokemon = random.sample(all_pokemon, min(num_questions, len(all_pokemon)))
    
    for idx, pokemon in enumerate(selected_pokemon, 1):
        name = pokemon['name_pt']
        types = ' e '.join([t.capitalize() for t in pokemon['types']])
        
        print(f"[{idx}/{len(selected_pokemon)}] {name} (#{pokemon['id']:03d})")
        print(f"   Tipo: {types}")
        
        # Criar pergunta
        question_text = f"Qual é este Pokémon?"
        
        # Usar imagem local
        image_path = f"images/pokemon/{pokemon['id']:03d}_{pokemon['name'].lower()}.png"
        
        # Criar explicação
        explanation = f"Este é {name}, um Pokémon do tipo {types}."
        if len(pokemon['types']) == 1:
            explanation = f"Este é {name}, um Pokémon do tipo {types}."
        
        # Criar a pergunta
        question = Question.objects.create(
            quiz=quiz,
            text=question_text,
            image=image_path,
            explanation=explanation,
            order=idx
        )
        
        # Gerar alternativas similares
        similar_pokemon = get_similar_pokemon(pokemon, all_pokemon, count=3)
        
        # Criar respostas (correta + 3 incorretas)
        answers_data = [
            {'text': name, 'is_correct': True, 'pokemon': pokemon}
        ]
        
        for similar in similar_pokemon:
            answers_data.append({
                'text': similar['name_pt'],
                'is_correct': False,
                'pokemon': similar
            })
        
        # Embaralhar as respostas
        random.shuffle(answers_data)
        
        # Criar as respostas no banco
        for answer_data in answers_data:
            Answer.objects.create(
                question=question,
                text=answer_data['text'],
                is_correct=answer_data['is_correct']
            )
        
        print(f"   ✅ Resposta correta: {name}")
        print(f"   📝 Alternativas: {', '.join([a['text'] for a in answers_data if not a['is_correct']])}")
        print()
    
    print()
    print("=" * 70)
    print("🎉 Quiz criado com sucesso!")
    print("=" * 70)
    print(f"📊 Total de perguntas: {quiz.get_total_questions()}")
    print(f"🔗 Slug: {quiz.slug}")
    print(f"🌐 URL: /pokemon/adivinhe-o-pokemon-gen1/")
    print()
    print("⚠️  IMPORTANTE: Copie as imagens para o Django static:")
    print("   cp -r pokemon_gen1/images quizzes/static/images/pokemon")
    print()

def main():
    print("🎮 CRIADOR DE QUIZ DE POKÉMON")
    print("=" * 70)
    print()
    
    import sys
    
    # Verificar se os dados existem
    if not Path('pokemon_gen1/pokemon_data.json').exists():
        print("❌ Dados dos Pokémon não encontrados!")
        print()
        print("Execute primeiro:")
        print("   python download_gen1_pokemon.py")
        print()
        sys.exit(1)
    
    # Perguntar quantas perguntas criar
    print("Quantas perguntas você quer criar?")
    print("(Máximo: 151 Pokémon)")
    
    try:
        num_questions = input("Digite o número (padrão: 50): ").strip()
        num_questions = int(num_questions) if num_questions else 50
        num_questions = min(max(1, num_questions), 151)
    except ValueError:
        num_questions = 50
    
    print()
    print(f"📝 Criando quiz com {num_questions} perguntas...")
    print()
    
    create_pokemon_quiz(num_questions)

if __name__ == '__main__':
    main()

