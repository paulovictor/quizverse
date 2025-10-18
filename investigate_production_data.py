#!/usr/bin/env python
"""
Script para investigar dados em produção que podem estar causando problemas na migração
"""
import os
import sys
import django

# Configurar o ambiente Django
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Quiz, Question, QuizAttempt, UserAnswer

def investigate_data():
    print("=" * 80)
    print("🔍 INVESTIGANDO DADOS EM PRODUÇÃO")
    print("=" * 80)
    print()
    
    # Contar registros
    print("📊 CONTAGEM DE REGISTROS:")
    print(f"   Quizzes: {Quiz.objects.count()}")
    print(f"   Questions: {Question.objects.count()}")
    print(f"   QuizAttempts: {QuizAttempt.objects.count()}")
    print(f"   UserAnswers: {UserAnswer.objects.count()}")
    print()
    
    # Verificar Questions órfãs
    print("🔍 VERIFICANDO QUESTIONS ÓRFÃS:")
    orphan_questions = 0
    for question in Question.objects.all()[:10]:  # Verificar apenas os primeiros 10
        try:
            quiz = question.quiz
            print(f"   ✅ Question {question.id} -> Quiz {quiz.slug}")
        except Quiz.DoesNotExist:
            print(f"   ❌ Question {question.id} -> Quiz não encontrado")
            orphan_questions += 1
        except Exception as e:
            print(f"   ⚠️  Question {question.id} -> Erro: {e}")
            orphan_questions += 1
    
    if orphan_questions > 0:
        print(f"   🚨 {orphan_questions} questions órfãs encontradas!")
    print()
    
    # Verificar QuizAttempts órfãos
    print("🔍 VERIFICANDO QUIZATTEMPTS ÓRFÃOS:")
    orphan_attempts = 0
    for attempt in QuizAttempt.objects.all()[:10]:  # Verificar apenas os primeiros 10
        try:
            quiz = attempt.quiz
            print(f"   ✅ QuizAttempt {attempt.id} -> Quiz {quiz.slug}")
        except Quiz.DoesNotExist:
            print(f"   ❌ QuizAttempt {attempt.id} -> Quiz não encontrado")
            orphan_attempts += 1
        except Exception as e:
            print(f"   ⚠️  QuizAttempt {attempt.id} -> Erro: {e}")
            orphan_attempts += 1
    
    if orphan_attempts > 0:
        print(f"   🚨 {orphan_attempts} quiz attempts órfãos encontrados!")
    print()
    
    # Verificar estrutura das tabelas
    print("🔍 VERIFICANDO ESTRUTURA DAS TABELAS:")
    from django.db import connection
    
    with connection.cursor() as cursor:
        # Verificar colunas da tabela quizzes_question
        cursor.execute("""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = 'quizzes_question' 
            AND column_name LIKE '%quiz%'
        """)
        question_columns = cursor.fetchall()
        print("   Colunas relacionadas a quiz em quizzes_question:")
        for col_name, data_type in question_columns:
            print(f"     - {col_name}: {data_type}")
        
        # Verificar colunas da tabela quizzes_quizattempt
        cursor.execute("""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = 'quizzes_quizattempt' 
            AND column_name LIKE '%quiz%'
        """)
        attempt_columns = cursor.fetchall()
        print("   Colunas relacionadas a quiz em quizzes_quizattempt:")
        for col_name, data_type in attempt_columns:
            print(f"     - {col_name}: {data_type}")
        
        # Verificar colunas da tabela quizzes_quiz
        cursor.execute("""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = 'quizzes_quiz'
        """)
        quiz_columns = cursor.fetchall()
        print("   Colunas da tabela quizzes_quiz:")
        for col_name, data_type in quiz_columns:
            print(f"     - {col_name}: {data_type}")
    
    print()
    print("=" * 80)
    print("✨ INVESTIGAÇÃO CONCLUÍDA!")
    print("=" * 80)

if __name__ == '__main__':
    investigate_data()
