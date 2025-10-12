#!/usr/bin/env python
"""
Script para configurar o CARD/CAIXA do tema Flamengo
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme

# Encontrar o tema Flamengo
theme = Theme.objects.get(slug='flamengo')

print(f"✅ Tema encontrado: {theme.title}")
print(f"📝 Slug: {theme.slug}")

print(f"\n🎨 CONFIGURANDO O CARD/CAIXA DO FLAMENGO...")

# REMOVER background da página (para não interferir)
theme.background_image = None
theme.background_color = None

# CONFIGURAR o CARD/CAIXA com a imagem e gradiente
theme.card_background_image = "https://i.ibb.co/SUA_URL_AQUI/flamengo.jpg"  # Cole sua URL do ImgBB aqui
theme.card_background_color = "linear-gradient(135deg, #DC143C 0%, #8B0000 50%, #000000 100%)"

theme.save()

print(f"\n✨ CARD DO FLAMENGO CONFIGURADO!")
print(f"\n📄 Background da PÁGINA:")
print(f"  • Image: {theme.background_image or 'Nenhuma'}")
print(f"  • Color: {theme.background_color or 'Padrão (azul)'}")

print(f"\n🎴 Background do CARD/CAIXA:")
print(f"  • Image: {theme.card_background_image or 'Nenhuma'}")
print(f"  • Color: {theme.card_background_color or 'Branco padrão'}")

print(f"\n🔗 Acesse: http://localhost:8000/flamengo/")

print(f"\n💡 PRÓXIMOS PASSOS:")
print(f"1. Faça upload da imagem em https://imgbb.com/")
print(f"2. Copie a URL 'Direct Link'")
print(f"3. Cole na linha 20 deste script")
print(f"4. Execute novamente: uv run python setup_flamengo_card.py")
print(f"\nOu configure pelo admin: /admin/quizzes/theme/")

