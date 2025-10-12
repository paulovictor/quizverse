#!/usr/bin/env python
"""
Script para popular o quiz de Counter-Strike com imagens de armas
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme, Quiz, Question, Answer


def create_counterstrike_quiz():
    """Cria um quiz de Counter-Strike com perguntas de imagens de armas"""
    
    # Criar ou obter o tema de Counter-Strike
    theme, created = Theme.objects.get_or_create(
        slug='counter-strike',
        defaults={
            'title': '🔫 Counter-Strike',
            'description': 'Quizzes sobre Counter-Strike e suas armas',
            'active': True
        }
    )
    if created:
        print(f"✅ Tema '{theme.title}' criado!")
    else:
        print(f"ℹ️  Tema '{theme.title}' já existe.")
    
    # Criar ou obter o quiz de Armas do CS
    quiz, created = Quiz.objects.get_or_create(
        slug='adivinhe-a-arma-cs',
        theme=theme,
        defaults={
            'title': 'Adivinhe a Arma do CS',
            'description': 'Teste seus conhecimentos sobre as armas do Counter-Strike! Veja a imagem e tente adivinhar qual é a arma.',
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
    
    # Lista de perguntas com imagens de armas do Counter-Strike
    cs_questions = [
        {
            'text': 'Qual é esta arma icônica do Counter-Strike?',
            'image': 'https://raw.githubusercontent.com/ByMykel/counter-strike-image-tracker/main/static/panorama/images/econ/weapons/base_weapons/weapon_ak47_png.png',
            'order': 1,
            'explanation': 'Esta é a AK-47, uma das armas mais icônicas e poderosas do Counter-Strike. É a rifle de assalto preferida dos Terroristas!',
            'answers': [
                {'text': 'AK-47', 'is_correct': True},
                {'text': 'M4A4', 'is_correct': False},
                {'text': 'Galil AR', 'is_correct': False},
                {'text': 'AUG', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é esta arma de precisão?',
            'image': 'https://raw.githubusercontent.com/ByMykel/counter-strike-image-tracker/main/static/panorama/images/econ/weapons/base_weapons/weapon_awp_png.png',
            'order': 2,
            'explanation': 'Esta é a AWP (Arctic Warfare Police), o sniper rifle mais poderoso do jogo, capaz de eliminar com um único tiro!',
            'answers': [
                {'text': 'Scout', 'is_correct': False},
                {'text': 'AWP', 'is_correct': True},
                {'text': 'G3SG1', 'is_correct': False},
                {'text': 'SCAR-20', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é esta pistola icônica?',
            'image': 'https://raw.githubusercontent.com/ByMykel/counter-strike-image-tracker/main/static/panorama/images/econ/weapons/base_weapons/weapon_deagle_png.png',
            'order': 3,
            'explanation': 'Esta é a Desert Eagle, a pistola mais poderosa do Counter-Strike, capaz de dar headshot de um tiro!',
            'answers': [
                {'text': 'USP-S', 'is_correct': False},
                {'text': 'Glock-18', 'is_correct': False},
                {'text': 'Desert Eagle', 'is_correct': True},
                {'text': 'P250', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é esta rifle de assalto dos CT?',
            'image': 'https://raw.githubusercontent.com/ByMykel/counter-strike-image-tracker/main/static/panorama/images/econ/weapons/base_weapons/weapon_m4a1_png.png',
            'order': 4,
            'explanation': 'Esta é a M4A4, a rifle de assalto principal dos Counter-Terrorists, conhecida por sua precisão e baixo recuo!',
            'answers': [
                {'text': 'AK-47', 'is_correct': False},
                {'text': 'M4A4', 'is_correct': True},
                {'text': 'FAMAS', 'is_correct': False},
                {'text': 'SG 553', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é esta submetralhadora popular?',
            'image': 'https://raw.githubusercontent.com/ByMykel/counter-strike-image-tracker/main/static/panorama/images/econ/weapons/base_weapons/weapon_mp9_png.png',
            'order': 5,
            'explanation': 'Esta é a MP9, uma submetralhadora rápida e eficiente, muito usada pelos CT nos rounds de eco!',
            'answers': [
                {'text': 'MAC-10', 'is_correct': False},
                {'text': 'MP7', 'is_correct': False},
                {'text': 'MP9', 'is_correct': True},
                {'text': 'UMP-45', 'is_correct': False},
            ]
        },
    ]
    
    # Criar as perguntas e respostas
    for q_data in cs_questions:
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
    
    print(f"\n🎉 Quiz de Counter-Strike criado com sucesso!")
    print(f"📊 Total de perguntas: {quiz.get_total_questions()}")
    print(f"\n🔗 Acesse em: /counter-strike/adivinhe-a-arma-cs/")


if __name__ == '__main__':
    print("🔫 Criando Quiz de Counter-Strike...\n")
    create_counterstrike_quiz()


