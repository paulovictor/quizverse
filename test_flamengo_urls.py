#!/usr/bin/env python
"""
Script para testar URLs de imagem e configurar o tema Flamengo
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme

# URLs alternativas para testar
urls = [
    # Opção 1: Sem imagem, só gradiente
    None,
    # Opção 2: Placeholder público
    'https://via.placeholder.com/1920x1080/DC143C/000000?text=Flamengo+Quiz',
    # Opção 3: ImgBB (você precisa fazer upload)
    # 'https://i.ibb.co/SEU_CODIGO/flamengo.jpg',
]

theme = Theme.objects.get(slug='flamengo')

print("🎨 CONFIGURAÇÃO ATUAL:")
print(f"Background Image: {theme.background_image}")
print(f"Background Color: {theme.background_color}")

print("\n" + "="*60)
print("📝 OPÇÕES DE CONFIGURAÇÃO:")
print("="*60)

print("\n1️⃣  SEM IMAGEM - Só Gradiente (FUNCIONA AGORA)")
print("   → Vai usar apenas o lindo gradiente vermelho-preto")

print("\n2️⃣  PLACEHOLDER Temporário")
print("   → Imagem temporária enquanto você faz upload da real")

print("\n3️⃣  ImgBB (Recomendado)")
print("   → Faça upload em https://imgbb.com/")
print("   → Copie o 'Direct Link'")

print("\n" + "="*60)
choice = input("Digite 1, 2 ou 3 (ou Enter para cancelar): ").strip()

if choice == "1":
    theme.background_image = None
    theme.background_color = "linear-gradient(135deg, #DC143C 0%, #8B0000 50%, #000000 100%)"
    theme.save()
    print("\n✅ Configurado! Só gradiente - ficou lindo!")
    
elif choice == "2":
    theme.background_image = urls[1]
    theme.background_color = "linear-gradient(135deg, #DC143C 0%, #8B0000 50%, #000000 100%)"
    theme.save()
    print("\n✅ Placeholder configurado!")
    
elif choice == "3":
    url = input("Cole a URL do ImgBB aqui: ").strip()
    if url:
        theme.background_image = url
        theme.save()
        print(f"\n✅ Imagem configurada: {url}")
else:
    print("\n❌ Cancelado")

print(f"\n🔗 Acesse: http://localhost:8000/flamengo/")

