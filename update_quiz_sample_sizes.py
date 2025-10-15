#!/usr/bin/env python
"""
Script para atualizar o campo question_sample_size dos quizzes existentes.
Execute com: python update_quiz_sample_sizes.py

Este script ajuda a configurar o número de questões que serão apresentadas
em cada tentativa de quiz.
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Quiz


def main():
    print("=" * 70)
    print("ATUALIZAÇÃO DO CAMPO question_sample_size")
    print("=" * 70)
    print()
    
    # Buscar todos os quizzes
    quizzes = Quiz.objects.all().order_by('theme__title', 'title')
    
    if not quizzes:
        print("❌ Nenhum quiz encontrado no banco de dados.")
        return
    
    print(f"📊 Total de quizzes encontrados: {quizzes.count()}")
    print()
    
    # Mostrar estatísticas atuais
    print("📈 Estatísticas atuais:")
    print("-" * 70)
    for quiz in quizzes:
        total_questions = quiz.get_total_questions()
        print(f"  • {quiz.theme.title} - {quiz.title}")
        print(f"    Total de questões: {total_questions}")
        print(f"    Sample size atual: {quiz.question_sample_size}")
        print()
    
    print("=" * 70)
    print()
    
    # Perguntar se quer atualizar
    print("🔧 Opções de atualização:")
    print("  1. Definir um valor padrão para TODOS os quizzes")
    print("  2. Atualizar individualmente cada quiz")
    print("  3. Cancelar")
    print()
    
    choice = input("Escolha uma opção (1-3): ").strip()
    
    if choice == '1':
        # Atualização em massa
        print()
        sample_size = input("Digite o número de questões (0 = usar todas): ").strip()
        
        try:
            sample_size = int(sample_size)
            if sample_size < 0:
                print("❌ Valor inválido. Deve ser >= 0")
                return
            
            confirm = input(f"\n⚠️  Confirma atualizar TODOS os {quizzes.count()} quizzes para {sample_size} questões? (s/n): ").strip().lower()
            
            if confirm == 's':
                Quiz.objects.all().update(question_sample_size=sample_size)
                print(f"✅ Todos os quizzes foram atualizados para {sample_size} questões!")
            else:
                print("❌ Operação cancelada.")
        
        except ValueError:
            print("❌ Valor inválido.")
    
    elif choice == '2':
        # Atualização individual
        print()
        print("💡 Para cada quiz, digite o número de questões (Enter = manter atual)")
        print()
        
        updated_count = 0
        for quiz in quizzes:
            total_questions = quiz.get_total_questions()
            print(f"\n📝 {quiz.theme.title} - {quiz.title}")
            print(f"   Total disponível: {total_questions} questões")
            print(f"   Sample size atual: {quiz.question_sample_size}")
            
            new_value = input("   Novo valor (Enter para manter): ").strip()
            
            if new_value:
                try:
                    new_value = int(new_value)
                    if new_value < 0:
                        print("   ⚠️  Valor inválido, mantendo atual.")
                        continue
                    
                    quiz.question_sample_size = new_value
                    quiz.save()
                    updated_count += 1
                    print(f"   ✅ Atualizado para {new_value}")
                except ValueError:
                    print("   ⚠️  Valor inválido, mantendo atual.")
        
        print()
        print(f"✅ {updated_count} quizzes foram atualizados!")
    
    else:
        print("❌ Operação cancelada.")
    
    print()
    print("=" * 70)
    print("✨ Script finalizado!")
    print("=" * 70)


if __name__ == '__main__':
    main()

