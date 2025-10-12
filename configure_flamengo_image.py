#!/usr/bin/env python
"""
Script para configurar a imagem de fundo do card do Flamengo
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme

# Encontrar o tema Flamengo
try:
    theme = Theme.objects.get(slug='flamengo')
    
    print(f"✅ Tema encontrado: {theme.title}")
    print(f"📝 Slug: {theme.slug}")
    
    print(f"\n🎨 CONFIGURANDO O CARD DO FLAMENGO...")
    
    # Configurar o CARD com gradiente do Flamengo (vermelho e preto)
    theme.card_background_image = None  # Pode adicionar URL depois se quiser
    theme.card_background_color = "linear-gradient(135deg, #ef4444 0%, #dc2626 100%)"
    
    theme.save()
    
    print(f"\n✨ CARD DO FLAMENGO CONFIGURADO COM SUCESSO!")
    print(f"\n🎴 Background do CARD:")
    print(f"  • Image: {theme.card_background_image or 'Nenhuma (usando gradiente)'}")
    print(f"  • Color: {theme.card_background_color}")
    
    print(f"\n🌐 Acesse para ver: /futebol/")
    
    print(f"\n💡 PARA ADICIONAR UMA IMAGEM:")
    print(f"1. Faça upload da imagem em https://imgbb.com/ ou https://imgur.com/")
    print(f"2. Copie a URL 'Direct Link'")
    print(f"3. No admin Django (/admin/quizzes/theme/), edite o Flamengo")
    print(f"4. Cole a URL no campo 'Card background image'")
    print(f"5. Salve")
    
except Theme.DoesNotExist:
    print("❌ Tema Flamengo não encontrado!")
    print("Certifique-se de que o tema foi criado no banco de dados.")

