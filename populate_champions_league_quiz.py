#!/usr/bin/env python
"""
Script para popular o banco de dados com o Quiz Champions League 2024/25
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme, Quiz, Question, Answer, Product
from django.utils.text import slugify


def create_champions_league_quiz():
    """Cria o tema Futebol e o quiz Champions League 2024/25"""
    
    # Criar ou obter o tema Futebol
    theme, created = Theme.objects.get_or_create(
        slug='futebol',
        defaults={
            'title': 'Futebol',
            'description': 'Teste seus conhecimentos sobre futebol mundial, times, jogadores e competições.',
            'active': True
        }
    )
    
    if created:
        print(f'✅ Tema criado: {theme.title}')
    else:
        print(f'ℹ️  Tema já existe: {theme.title}')
    
    # Criar ou obter o quiz Champions League
    quiz, created = Quiz.objects.get_or_create(
        theme=theme,
        slug='champions-league-2024-25',
        defaults={
            'title': 'Champions League 2024/25',
            'description': 'Identifique os 36 times da UEFA Champions League 2024/25 pelos escudos dos clubes.',
            'difficulty': 'medium',
            'time_limit': 0,
            'active': True,
            'order': 1
        }
    )
    
    if created:
        print(f'✅ Quiz criado: {quiz.title}')
    else:
        print(f'ℹ️  Quiz já existe: {quiz.title}')
        # Limpar perguntas antigas se o quiz já existia
        quiz.questions.all().delete()
        print('🗑️  Perguntas antigas removidas')
    
    # Dados das perguntas
    questions_data = [
        {
            "question": "Real Madrid",
            "url": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
            "answers": ["Real Madrid", "Real Sociedad", "Real Betis", "Racing Santander"],
            "correct": 0
        },
        {
            "question": "Arsenal",
            "url": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg",
            "answers": ["Arsenal", "Aston Villa", "Athletic Bilbao", "Atlético Madrid"],
            "correct": 0
        },
        {
            "question": "Bayern München",
            "url": "https://upload.wikimedia.org/wikipedia/commons/1/1b/FC_Bayern_München_logo_%282017%29.svg",
            "answers": ["Bayer Leverkusen", "Bayern München", "Borussia Dortmund", "RB Leipzig"],
            "correct": 1
        },
        {
            "question": "Inter Milan",
            "url": "https://upload.wikimedia.org/wikipedia/commons/0/05/FC_Internazionale_Milano_2021.svg",
            "answers": ["Inter Milan", "AC Milan", "Internazionale", "Atalanta"],
            "correct": 0
        },
        {
            "question": "Paris Saint-Germain",
            "url": "https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg",
            "answers": ["Paris FC", "Paris Saint-Germain", "Olympique Paris", "PSV Eindhoven"],
            "correct": 1
        },
        {
            "question": "Liverpool",
            "url": "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg",
            "answers": ["Manchester United", "Liverpool", "Lille", "Bayer Leverkusen"],
            "correct": 1
        },
        {
            "question": "Barcelona",
            "url": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
            "answers": ["Atlético Madrid", "Barcelona", "Sporting CP", "Real Madrid"],
            "correct": 1
        },
        {
            "question": "Borussia Dortmund",
            "url": "https://upload.wikimedia.org/wikipedia/commons/6/67/Borussia_Dortmund_logo.svg",
            "answers": ["Borussia Dortmund", "BSC Young Boys", "Borussia Mönchengladbach", "Bayer Leverkusen"],
            "correct": 0
        },
        {
            "question": "Manchester City",
            "url": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg",
            "answers": ["Manchester City", "Manchester United", "Chelsea", "Celtic"],
            "correct": 0
        },
        {
            "question": "Atlético Madrid",
            "url": "https://upload.wikimedia.org/wikipedia/en/f/f4/Atletico_Madrid_2017_logo.svg",
            "answers": ["Athletic Bilbao", "Atlético Madrid", "Alavés", "Arsenal"],
            "correct": 1
        },
        {
            "question": "Juventus",
            "url": "https://upload.wikimedia.org/wikipedia/commons/1/15/Juventus_FC_2017_logo.svg",
            "answers": ["Juventus", "AC Milan", "Inter Milan", "Atalanta"],
            "correct": 0
        },
        {
            "question": "Bayer Leverkusen",
            "url": "https://upload.wikimedia.org/wikipedia/en/5/59/Bayer_04_Leverkusen_logo.svg",
            "answers": ["Bayer Leverkusen", "Bayern München", "Borussia Dortmund", "RB Leipzig"],
            "correct": 0
        },
        {
            "question": "Olympique Lyon",
            "url": "https://upload.wikimedia.org/wikipedia/en/e/e2/Olympique_Lyonnais_logo.svg",
            "answers": ["Olympique Lyon", "Lille", "Olympique Marseille", "Lens"],
            "correct": 0
        },
        {
            "question": "Aston Villa",
            "url": "https://upload.wikimedia.org/wikipedia/en/f/f9/Aston_Villa_FC_crest_%282016%29.svg",
            "answers": ["Aston Villa", "Arsenal", "Atalanta", "Athletic Bilbao"],
            "correct": 0
        },
        {
            "question": "Atalanta",
            "url": "https://upload.wikimedia.org/wikipedia/en/6/66/Atalanta_BC_logo.svg",
            "answers": ["Atalanta", "AC Milan", "Inter Milan", "Aston Villa"],
            "correct": 0
        },
        {
            "question": "RB Leipzig",
            "url": "https://upload.wikimedia.org/wikipedia/en/0/04/RB_Leipzig_2014_logo.svg",
            "answers": ["RB Leipzig", "Red Bull Salzburg", "Bayer Leverkusen", "Eintracht Frankfurt"],
            "correct": 0
        },
        {
            "question": "Dinamo Zagreb",
            "url": "https://upload.wikimedia.org/wikipedia/commons/8/8a/GNK_Dinamo_Zagreb_logo.svg",
            "answers": ["Dinamo Zagreb", "Dinamo Moscow", "Dynamo Kyiv", "Dinamo Tbilisi"],
            "correct": 0
        },
        {
            "question": "Lille",
            "url": "https://upload.wikimedia.org/wikipedia/en/5/54/LOSC_Lille_logo_%282021%29.svg",
            "answers": ["Lyon", "Lille", "Lens", "Liverpool"],
            "correct": 1
        },
        {
            "question": "Benfica",
            "url": "https://upload.wikimedia.org/wikipedia/en/a/a2/SL_Benfica_logo.svg",
            "answers": ["Benfica", "Belenenses", "Boavista", "Braga"],
            "correct": 0
        },
        {
            "question": "Celtic",
            "url": "https://upload.wikimedia.org/wikipedia/en/3/35/Celtic_FC.svg",
            "answers": ["Celtic", "Hibernian", "Shamrock Rovers", "Sporting CP"],
            "correct": 0
        },
        {
            "question": "Red Star Belgrade",
            "url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Red_Star_Belgrade_crest.svg",
            "answers": ["Red Star Belgrade", "Red Bull Salzburg", "Spartak Moscow", "Slavia Praha"],
            "correct": 0
        },
        {
            "question": "Red Bull Salzburg",
            "url": "https://upload.wikimedia.org/wikipedia/en/7/77/FC_Red_Bull_Salzburg_logo.svg",
            "answers": ["Red Bull Salzburg", "RB Leipzig", "Red Star Belgrade", "Austria Vienna"],
            "correct": 0
        },
        {
            "question": "BSC Young Boys",
            "url": "https://upload.wikimedia.org/wikipedia/en/5/56/BSC_Young_Boys_logo.svg",
            "answers": ["BSC Young Boys", "FC Basel", "Borussia Dortmund", "Bayern München"],
            "correct": 0
        },
        {
            "question": "Sparta Praha",
            "url": "https://upload.wikimedia.org/wikipedia/en/1/1e/AC_Sparta_Prague_logo.svg",
            "answers": ["Sparta Praha", "Slavia Praha", "Spartak Moscow", "Sporting CP"],
            "correct": 0
        },
        {
            "question": "Slovan Bratislava",
            "url": "https://upload.wikimedia.org/wikipedia/en/8/8f/%C5%A0K_Slovan_Bratislava_logo.svg",
            "answers": ["Slovan Bratislava", "Slavia Praha", "Sparta Praha", "Dynamo Kyiv"],
            "correct": 0
        },
        {
            "question": "PSV Eindhoven",
            "url": "https://upload.wikimedia.org/wikipedia/en/0/05/PSV_Eindhoven.svg",
            "answers": ["PSV Eindhoven", "Paris Saint-Germain", "FC Porto", "Philips Sport"],
            "correct": 0
        },
        {
            "question": "Club Brugge",
            "url": "https://upload.wikimedia.org/wikipedia/en/d/d0/Club_Brugge_KV_logo.svg",
            "answers": ["Club Brugge", "Anderlecht", "Standard Liège", "Borussia Dortmund"],
            "correct": 0
        },
        {
            "question": "FC Porto",
            "url": "https://upload.wikimedia.org/wikipedia/en/f/f1/FC_Porto.svg",
            "answers": ["FC Porto", "Sporting CP", "Belenenses", "Paris Saint-Germain"],
            "correct": 0
        },
        {
            "question": "AC Milan",
            "url": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Logo_of_AC_Milan.svg",
            "answers": ["AC Milan", "Inter Milan", "AS Roma", "Atalanta"],
            "correct": 0
        },
        {
            "question": "Shakhtar Donetsk",
            "url": "https://upload.wikimedia.org/wikipedia/en/a/a1/FC_Shakhtar_Donetsk.svg",
            "answers": ["Shakhtar Donetsk", "Dynamo Kyiv", "Dnipro", "Sparta Praha"],
            "correct": 0
        },
        {
            "question": "Sporting CP",
            "url": "https://upload.wikimedia.org/wikipedia/en/3/3e/Sporting_Clube_de_Portugal_%28Logo%29.svg",
            "answers": ["Sporting CP", "Sparta Praha", "Sporting Braga", "Celtic"],
            "correct": 0
        },
        {
            "question": "Feyenoord",
            "url": "https://upload.wikimedia.org/wikipedia/en/0/0e/Feyenoord_logo.svg",
            "answers": ["Feyenoord", "PSV Eindhoven", "Ajax Amsterdam", "FC Utrecht"],
            "correct": 0
        },
        {
            "question": "Stade Brestois",
            "url": "https://upload.wikimedia.org/wikipedia/en/6/62/Stade_Brestois_29_logo.svg",
            "answers": ["Stade Brestois", "Bordeaux", "Bastia", "Bologna"],
            "correct": 0
        },
        {
            "question": "Bologna",
            "url": "https://upload.wikimedia.org/wikipedia/commons/9/93/Bologna_FC_1909_logo.svg",
            "answers": ["Bologna", "Boavista", "Bayer Leverkusen", "Benfica"],
            "correct": 0
        },
        {
            "question": "Girona",
            "url": "https://upload.wikimedia.org/wikipedia/en/7/79/Girona_FC_logo.svg",
            "answers": ["Girona", "Granada", "Getafe", "Gimnàstic"],
            "correct": 0
        },
        {
            "question": "VfB Stuttgart",
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/VfB_Stuttgart_1893_Logo.svg",
            "answers": ["VfB Stuttgart", "Bayer Leverkusen", "Eintracht Frankfurt", "Sparta Praha"],
            "correct": 0
        }
    ]
    
    # Criar perguntas e respostas
    for idx, q_data in enumerate(questions_data, 1):
        question = Question.objects.create(
            quiz=quiz,
            text=f"Qual time é representado por este escudo?",
            image=q_data['url'],
            explanation=f"Este é o escudo do {q_data['question']}, um dos 36 times participantes da UEFA Champions League 2024/25.",
            order=idx,
            points=1
        )
        
        # Criar as 4 alternativas
        for answer_idx, answer_text in enumerate(q_data['answers']):
            is_correct = (answer_idx == q_data['correct'])
            Answer.objects.create(
                question=question,
                text=answer_text,
                is_correct=is_correct,
                order=answer_idx
            )
        
        print(f'✅ Pergunta {idx}/36: {q_data["question"]}')
    
    # Criar produtos relacionados
    products_data = [
        {
            'title': 'Camisa Champions League Oficial',
            'price': 249.90,
            'image_url': 'https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=400',
            'product_url': 'https://www.google.com/search?q=camisa+champions+league',
            'order': 1
        },
        {
            'title': 'Bola Oficial UEFA Champions League',
            'price': 189.90,
            'image_url': 'https://images.unsplash.com/photo-1614632537197-38a17061ce4c?w=400',
            'product_url': 'https://www.google.com/search?q=bola+champions+league',
            'order': 2
        },
        {
            'title': 'Cachecol UEFA Champions League',
            'price': 79.90,
            'image_url': 'https://images.unsplash.com/photo-1588731247989-c31e34ec7d1a?w=400',
            'product_url': 'https://www.google.com/search?q=cachecol+champions+league',
            'order': 3
        }
    ]
    
    # Remover produtos antigos
    Product.objects.filter(theme=theme).delete()
    
    for prod_data in products_data:
        product = Product.objects.create(
            theme=theme,
            **prod_data,
            active=True
        )
        print(f'✅ Produto criado: {product.title}')
    
    print('\n' + '='*60)
    print(f'✨ Quiz "{quiz.title}" criado com sucesso!')
    print(f'📊 Total de perguntas: {quiz.questions.count()}')
    print(f'🎯 Total de pontos: {quiz.get_total_points()}')
    print(f'🛍️  Total de produtos: {Product.objects.filter(theme=theme).count()}')
    print('='*60)


if __name__ == '__main__':
    print('🚀 Iniciando população do banco de dados...\n')
    create_champions_league_quiz()
    print('\n✅ Processo concluído!')

