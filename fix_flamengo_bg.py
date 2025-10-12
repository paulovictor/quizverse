#!/usr/bin/env python
"""
Script para corrigir o background do tema Flamengo
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme

# Encontrar o tema Flamengo
theme = Theme.objects.filter(slug__icontains='flamengo').first()

if theme:
    print(f"✅ Tema encontrado: {theme.title}")
    print(f"📝 Slug: {theme.slug}")
    print(f"\n🖼️  ANTES:")
    print(f"Background Image: {theme.background_image}")
    print(f"Background Color: {repr(theme.background_color)}")
    
    # Corrigir o background_color (remover aspas extras se houver)
    theme.background_color = "linear-gradient(135deg, #DC143C 0%, #8B0000 50%, #000000 100%)"
    theme.save()
    
    print(f"\n✨ DEPOIS DA CORREÇÃO:")
    print(f"Background Image: {theme.background_image}")
    print(f"Background Color: {theme.background_color}")
    
    print(f"\n🎨 O background está configurado!")
    print(f"🔗 Acesse: /flamengo/ ou /{theme.slug}/")
    
else:
    print("❌ Tema Flamengo não encontrado!")

