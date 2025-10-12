#!/usr/bin/env python
"""
Script para popular o banco de dados com dados de exemplo
Execute: uv run python populate_sample_data.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme, Quiz, Question, Answer


def create_sample_data():
    print("🎯 Criando dados de exemplo...\n")
    
    # Criar Tema: Flamengo
    print("📌 Criando tema: Flamengo")
    theme_flamengo, created = Theme.objects.get_or_create(
        slug='flamengo',
        defaults={
            'title': 'Flamengo',
            'description': 'Teste seus conhecimentos sobre o Clube de Regatas do Flamengo, o maior time do mundo!',
            'active': True
        }
    )
    
    # Criar Quiz do Flamengo
    print("📝 Criando quiz: Quiz Básico do Flamengo")
    quiz_flamengo, created = Quiz.objects.get_or_create(
        theme=theme_flamengo,
        slug='quiz-1',
        defaults={
            'title': 'Quiz Básico do Flamengo',
            'description': 'Perguntas básicas sobre a história e curiosidades do Mengão!',
            'difficulty': 'easy',
            'time_limit': 0,
            'active': True,
            'order': 1
        }
    )
    
    # Perguntas do Flamengo
    questions_flamengo = [
        {
            'text': 'Qual é o mascote oficial do Flamengo?',
            'explanation': 'O mascote do Flamengo é o Urubu, que representa a força e a garra do time.',
            'order': 1,
            'answers': [
                {'text': 'Urubu', 'is_correct': True},
                {'text': 'Papagaio', 'is_correct': False},
                {'text': 'Gavião', 'is_correct': False},
                {'text': 'Arara', 'is_correct': False},
            ]
        },
        {
            'text': 'Em que ano o Flamengo foi fundado?',
            'explanation': 'O Clube de Regatas do Flamengo foi fundado em 15 de novembro de 1895.',
            'order': 2,
            'answers': [
                {'text': '1895', 'is_correct': True},
                {'text': '1900', 'is_correct': False},
                {'text': '1912', 'is_correct': False},
                {'text': '1888', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é o nome do estádio do Flamengo?',
            'explanation': 'O Flamengo manda seus jogos no Maracanã, o templo do futebol brasileiro.',
            'order': 3,
            'answers': [
                {'text': 'Maracanã', 'is_correct': True},
                {'text': 'São Januário', 'is_correct': False},
                {'text': 'Engenhão', 'is_correct': False},
                {'text': 'Giulite Coutinho', 'is_correct': False},
            ]
        },
    ]
    
    for q_data in questions_flamengo:
        answers_data = q_data.pop('answers')
        question, created = Question.objects.get_or_create(
            quiz=quiz_flamengo,
            order=q_data['order'],
            defaults=q_data
        )
        
        if created:
            for idx, a_data in enumerate(answers_data):
                Answer.objects.create(
                    question=question,
                    order=idx,
                    **a_data
                )
    
    print(f"   ✓ Criadas {quiz_flamengo.questions.count()} perguntas\n")
    
    # Criar Tema: Harry Potter
    print("📌 Criando tema: Harry Potter")
    theme_hp, created = Theme.objects.get_or_create(
        slug='harrypotter',
        defaults={
            'title': 'Harry Potter',
            'description': 'Entre no mundo mágico e teste seus conhecimentos sobre Harry Potter!',
            'active': True
        }
    )
    
    # Quiz 1: Sonserina
    print("📝 Criando quiz: Quiz Sonserina")
    quiz_sonserina, created = Quiz.objects.get_or_create(
        theme=theme_hp,
        slug='quiz-sonserina',
        defaults={
            'title': 'Quiz da Sonserina',
            'description': 'Perguntas sobre a casa mais ambiciosa de Hogwarts!',
            'difficulty': 'medium',
            'time_limit': 0,
            'active': True,
            'order': 1
        }
    )
    
    questions_sonserina = [
        {
            'text': 'Quem é o fundador da Sonserina?',
            'explanation': 'Salazar Slytherin foi um dos quatro fundadores de Hogwarts.',
            'order': 1,
            'answers': [
                {'text': 'Salazar Slytherin', 'is_correct': True},
                {'text': 'Godric Gryffindor', 'is_correct': False},
                {'text': 'Rowena Ravenclaw', 'is_correct': False},
                {'text': 'Helga Hufflepuff', 'is_correct': False},
            ]
        },
        {
            'text': 'Qual é a cor da Sonserina?',
            'explanation': 'As cores da Sonserina são verde e prata.',
            'order': 2,
            'answers': [
                {'text': 'Verde e Prata', 'is_correct': True},
                {'text': 'Vermelho e Dourado', 'is_correct': False},
                {'text': 'Azul e Bronze', 'is_correct': False},
                {'text': 'Amarelo e Preto', 'is_correct': False},
            ]
        },
    ]
    
    for q_data in questions_sonserina:
        answers_data = q_data.pop('answers')
        question, created = Question.objects.get_or_create(
            quiz=quiz_sonserina,
            order=q_data['order'],
            defaults=q_data
        )
        
        if created:
            for idx, a_data in enumerate(answers_data):
                Answer.objects.create(
                    question=question,
                    order=idx,
                    **a_data
                )
    
    print(f"   ✓ Criadas {quiz_sonserina.questions.count()} perguntas\n")
    
    # Quiz 2: Lufa-Lufa
    print("📝 Criando quiz: Quiz Lufa-Lufa")
    quiz_lufalufa, created = Quiz.objects.get_or_create(
        theme=theme_hp,
        slug='quiz-lufalufa',
        defaults={
            'title': 'Quiz da Lufa-Lufa',
            'description': 'Teste seus conhecimentos sobre a casa mais leal!',
            'difficulty': 'easy',
            'time_limit': 0,
            'active': True,
            'order': 2
        }
    )
    
    questions_lufalufa = [
        {
            'text': 'Qual é o animal símbolo da Lufa-Lufa?',
            'explanation': 'O texugo representa a lealdade e o trabalho árduo da Lufa-Lufa.',
            'order': 1,
            'answers': [
                {'text': 'Texugo', 'is_correct': True},
                {'text': 'Leão', 'is_correct': False},
                {'text': 'Águia', 'is_correct': False},
                {'text': 'Serpente', 'is_correct': False},
            ]
        },
        {
            'text': 'Quem é o diretor da Lufa-Lufa na época de Harry?',
            'explanation': 'A Professora Pomona Sprout é a diretora da Lufa-Lufa.',
            'order': 2,
            'answers': [
                {'text': 'Pomona Sprout', 'is_correct': True},
                {'text': 'Minerva McGonagall', 'is_correct': False},
                {'text': 'Filius Flitwick', 'is_correct': False},
                {'text': 'Severus Snape', 'is_correct': False},
            ]
        },
    ]
    
    for q_data in questions_lufalufa:
        answers_data = q_data.pop('answers')
        question, created = Question.objects.get_or_create(
            quiz=quiz_lufalufa,
            order=q_data['order'],
            defaults=q_data
        )
        
        if created:
            for idx, a_data in enumerate(answers_data):
                Answer.objects.create(
                    question=question,
                    order=idx,
                    **a_data
                )
    
    print(f"   ✓ Criadas {quiz_lufalufa.questions.count()} perguntas\n")
    
    print("✅ Dados de exemplo criados com sucesso!\n")
    print("🌐 URLs para testar:")
    print(f"   → http://localhost:8000/{theme_flamengo.slug}/")
    print(f"   → http://localhost:8000/{theme_flamengo.slug}/{quiz_flamengo.slug}/")
    print(f"   → http://localhost:8000/{theme_hp.slug}/")
    print(f"   → http://localhost:8000/{theme_hp.slug}/{quiz_sonserina.slug}/")
    print(f"   → http://localhost:8000/{theme_hp.slug}/{quiz_lufalufa.slug}/")


if __name__ == '__main__':
    create_sample_data()

