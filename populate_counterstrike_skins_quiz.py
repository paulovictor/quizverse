#!/usr/bin/env python
"""
Script para popular o quiz de Skins do Counter-Strike
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme, Quiz, Question, Answer


def create_counterstrike_skins_quiz():
    """Cria um quiz de Skins do Counter-Strike com perguntas de modelos específicos"""
    
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
    
    # Criar ou obter o quiz de Skins do CS
    quiz, created = Quiz.objects.get_or_create(
        slug='adivinhe-a-skin-cs',
        theme=theme,
        defaults={
            'title': 'Adivinhe a Skin do CS',
            'description': 'Teste seus conhecimentos sobre as skins mais icônicas do Counter-Strike! Veja a imagem e tente adivinhar qual é o modelo da arma.',
            'difficulty': 'hard',
            'active': True,
            'order': 2
        }
    )
    if created:
        print(f"✅ Quiz '{quiz.title}' criado!")
    else:
        print(f"ℹ️  Quiz '{quiz.title}' já existe.")
        # Limpar perguntas antigas se existirem
        quiz.questions.all().delete()
        print("   Perguntas antigas removidas.")
    
    # Lista de perguntas com skins específicas do Counter-Strike
    # Usando URLs do CSGOStash que são mais estáveis
    skins_questions = [
        # AWP Skins
        {
            'text': 'Qual é esta skin lendária da AWP?',
            'image': 'https://csgostash.com/img/skins/large_1920/s269.png',
            'order': 1,
            'points': 15,
            'explanation': 'Esta é a AWP | Dragon Lore, uma das skins mais raras e caras do CS:GO!',
            'answers': [
                {'text': 'AWP | Dragon Lore', 'is_correct': True},
                {'text': 'AWP | Medusa', 'is_correct': False},
                {'text': 'AWP | Gungnir', 'is_correct': False},
                {'text': 'AWP | Asiimov', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é esta skin futurística da AWP?',
            'image': 'https://csgostash.com/img/skins/large_1920/s302.png',
            'order': 2,
            'points': 15,
            'explanation': 'Esta é a AWP | Asiimov, conhecida por seu design futurista e cores vibrantes!',
            'answers': [
                {'text': 'AWP | Hyper Beast', 'is_correct': False},
                {'text': 'AWP | Neo-Noir', 'is_correct': False},
                {'text': 'AWP | Asiimov', 'is_correct': True},
                {'text': 'AWP | Redline', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é esta skin mítica da AWP?',
            'image': 'https://csgostash.com/img/skins/large_1920/s1477.png',
            'order': 3,
            'points': 15,
            'explanation': 'Esta é a AWP | Gungnir, uma das skins mais raras e caras, do Norse Collection!',
            'answers': [
                {'text': 'AWP | Containment Breach', 'is_correct': False},
                {'text': 'AWP | Prince', 'is_correct': False},
                {'text': 'AWP | Gungnir', 'is_correct': True},
                {'text': 'AWP | Wildfire', 'is_correct': False},
            ]
        },
        
        # AK-47 Skins
        {
            'text': 'Qual é esta skin azul da AK-47?',
            'image': 'https://csgostash.com/img/skins/large_1920/s44.png',
            'order': 4,
            'points': 15,
            'explanation': 'Esta é a AK-47 | Case Hardened (Blue Gem), uma das skins mais valiosas quando tem muito azul!',
            'answers': [
                {'text': 'AK-47 | Vulcan', 'is_correct': False},
                {'text': 'AK-47 | Aquamarine Revenge', 'is_correct': False},
                {'text': 'AK-47 | Case Hardened', 'is_correct': True},
                {'text': 'AK-47 | Blue Laminate', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é esta skin vermelha da AK-47?',
            'image': 'https://csgostash.com/img/skins/large_1920/s215.png',
            'order': 5,
            'points': 15,
            'explanation': 'Esta é a AK-47 | Fire Serpent, uma das skins mais desejadas e caras do jogo!',
            'answers': [
                {'text': 'AK-47 | Redline', 'is_correct': False},
                {'text': 'AK-47 | Fire Serpent', 'is_correct': True},
                {'text': 'AK-47 | Bloodsport', 'is_correct': False},
                {'text': 'AK-47 | Red Laminate', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é esta skin colorida da AK-47?',
            'image': 'https://csgostash.com/img/skins/large_1920/s675.png',
            'order': 6,
            'points': 15,
            'explanation': 'Esta é a AK-47 | Neon Rider, com design neon vibrante e futurista!',
            'answers': [
                {'text': 'AK-47 | Neon Rider', 'is_correct': True},
                {'text': 'AK-47 | Asiimov', 'is_correct': False},
                {'text': 'AK-47 | Vulcan', 'is_correct': False},
                {'text': 'AK-47 | Fuel Injector', 'is_correct': False},
            ]
        },
        
        # M4A4 Skins
        {
            'text': 'Qual é esta skin mítica da M4A4?',
            'image': 'https://csgostash.com/img/skins/large_1920/s309.png',
            'order': 7,
            'points': 20,
            'explanation': 'Esta é a M4A4 | Howl, a única skin Contraband do jogo devido a problemas de copyright!',
            'answers': [
                {'text': 'M4A4 | Howl', 'is_correct': True},
                {'text': 'M4A4 | Dragon King', 'is_correct': False},
                {'text': 'M4A4 | Desolate Space', 'is_correct': False},
                {'text': 'M4A4 | The Emperor', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é esta skin futurística da M4A4?',
            'image': 'https://csgostash.com/img/skins/large_1920/s305.png',
            'order': 8,
            'points': 15,
            'explanation': 'Esta é a M4A4 | Asiimov, parte da popular coleção Asiimov!',
            'answers': [
                {'text': 'M4A4 | Neo-Noir', 'is_correct': False},
                {'text': 'M4A4 | Asiimov', 'is_correct': True},
                {'text': 'M4A4 | Cyber Security', 'is_correct': False},
                {'text': 'M4A4 | The Battlestar', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é esta skin tropical da M4A4?',
            'image': 'https://csgostash.com/img/skins/large_1920/s663.png',
            'order': 9,
            'points': 15,
            'explanation': 'Esta é a M4A4 | Poseidon, com design mitológico e cores vibrantes!',
            'answers': [
                {'text': 'M4A4 | Hellfire', 'is_correct': False},
                {'text': 'M4A4 | In Living Color', 'is_correct': False},
                {'text': 'M4A4 | Poseidon', 'is_correct': True},
                {'text': 'M4A4 | The Emperor', 'is_correct': False},
            ]
        },
        
        # Desert Eagle Skin
        {
            'text': 'Qual é esta skin lendária da Desert Eagle?',
            'image': 'https://csgostash.com/img/skins/large_1920/s1469.png',
            'order': 10,
            'points': 20,
            'explanation': 'Esta é a Desert Eagle | Printstream, uma das skins mais caras e desejadas da Deagle!',
            'answers': [
                {'text': 'Desert Eagle | Blaze', 'is_correct': False},
                {'text': 'Desert Eagle | Code Red', 'is_correct': False},
                {'text': 'Desert Eagle | Printstream', 'is_correct': True},
                {'text': 'Desert Eagle | Crimson Web', 'is_correct': False},
            ]
        },
    ]
    
    # Criar as perguntas e respostas
    for q_data in skins_questions:
        question = Question.objects.create(
            quiz=quiz,
            text=q_data['text'],
            image=q_data['image'],
            explanation=q_data['explanation'],
            order=q_data['order'],
            points=q_data['points']
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
    
    print(f"\n🎉 Quiz de Skins do Counter-Strike criado com sucesso!")
    print(f"📊 Total de perguntas: {quiz.get_total_questions()}")
    print(f"🏆 Total de pontos: {quiz.get_total_points()}")
    print(f"\n🔗 Acesse em: /counter-strike/adivinhe-a-skin-cs/")


if __name__ == '__main__':
    print("🎨 Criando Quiz de Skins do Counter-Strike...\n")
    create_counterstrike_skins_quiz()

