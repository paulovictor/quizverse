#!/usr/bin/env python
"""
Script para popular o quiz de Pokémon com imagens
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme, Quiz, Question, Answer


def create_pokemon_quiz():
    """Cria um quiz de Pokémon com perguntas de imagens"""
    
    # Criar ou obter o tema de Games
    theme, created = Theme.objects.get_or_create(
        slug='pokemon',
        defaults={
            'title': '🎮 Pokemon',
            'description': 'Quizzes sobre pokemon',
            'active': True
        }
    )
    if created:
        print(f"✅ Tema '{theme.title}' criado!")
    else:
        print(f"ℹ️  Tema '{theme.title}' já existe.")
    
    # Criar ou obter o quiz de Pokémon
    quiz, created = Quiz.objects.get_or_create(
        slug='adivinhe-o-pokemon',
        theme=theme,
        defaults={
            'title': 'Adivinhe o Pokémon',
            'description': 'Teste seus conhecimentos sobre Pokémon! Veja a imagem e tente adivinhar qual é o Pokémon.',
            'difficulty': 'easy',
            'active': True,
            'order': 1
        }
    )
    if created:
        print(f"✅ Quiz '{quiz.title}' criado!")
    else:
        print(f"ℹ️  Quiz '{quiz.title}' já existe.")
        # Limpar perguntas antigas se existirem
        quiz.questions.all().delete()
        print("   Perguntas antigas removidas.")
    
    # Lista de perguntas com imagens de Pokémon
    pokemon_questions = [
        {
            'text': 'Qual é este Pokémon?',
            'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png',
            'order': 1,
            'explanation': 'Este é o Pikachu, o Pokémon elétrico mais famoso e mascote da franquia Pokémon!',
            'answers': [
                {'text': 'Pikachu', 'is_correct': True},
                {'text': 'Raichu', 'is_correct': False},
                {'text': 'Pichu', 'is_correct': False},
                {'text': 'Pachirisu', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é este Pokémon?',
            'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png',
            'order': 2,
            'explanation': 'Este é o Charizard, um Pokémon do tipo Fogo/Voador, evolução final do Charmander!',
            'answers': [
                {'text': 'Moltres', 'is_correct': False},
                {'text': 'Dragonite', 'is_correct': False},
                {'text': 'Charizard', 'is_correct': True},
                {'text': 'Salamence', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é este Pokémon?',
            'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png',
            'order': 3,
            'explanation': 'Este é o Snorlax, um Pokémon Normal conhecido por dormir muito e bloquear caminhos!',
            'answers': [
                {'text': 'Munchlax', 'is_correct': False},
                {'text': 'Snorlax', 'is_correct': True},
                {'text': 'Slaking', 'is_correct': False},
                {'text': 'Ursaring', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é este Pokémon lendário?',
            'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png',
            'order': 4,
            'explanation': 'Este é o Mewtwo, um dos Pokémon lendários mais poderosos, criado geneticamente!',
            'answers': [
                {'text': 'Mew', 'is_correct': False},
                {'text': 'Mewtwo', 'is_correct': True},
                {'text': 'Alakazam', 'is_correct': False},
                {'text': 'Deoxys', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é este Pokémon aquático?',
            'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png',
            'order': 5,
            'explanation': 'Este é o Blastoise, um Pokémon do tipo Água, evolução final do Squirtle!',
            'answers': [
                {'text': 'Wartortle', 'is_correct': False},
                {'text': 'Lapras', 'is_correct': False},
                {'text': 'Blastoise', 'is_correct': True},
                {'text': 'Gyarados', 'is_correct': False},
            ]
        },
    ]
    
    # Criar as perguntas e respostas
    for q_data in pokemon_questions:
        question = Question.objects.create(
            quiz=quiz,
            text=q_data['text'],
            image=q_data['image'],
            explanation=q_data['explanation'],
            order=q_data['order']
        )
        print(f"   ✅ Pergunta {q_data['order']}: {q_data['text'][:50]}...")
        
        # Criar respostas
        for a_data in q_data['answers']:
            Answer.objects.create(
                question=question,
                text=a_data['text'],
                is_correct=a_data['is_correct']
            )
        
        correct_answer = [a['text'] for a in q_data['answers'] if a['is_correct']][0]
        print(f"      Resposta correta: {correct_answer}")
    
    print(f"\n🎉 Quiz de Pokémon criado com sucesso!")
    print(f"📊 Total de perguntas: {quiz.get_total_questions()}")
    print(f"\n🔗 Acesse em: /pokemon/adivinhe-o-pokemon/")


if __name__ == '__main__':
    print("🎮 Criando Quiz de Pokémon...\n")
    create_pokemon_quiz()

