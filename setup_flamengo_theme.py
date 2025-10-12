#!/usr/bin/env python
"""
Script para configurar o tema Flamengo com background personalizado
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme

def setup_flamengo_theme():
    """Configura o tema Flamengo com background personalizado"""
    
    # URL da imagem de background (você pode fazer upload para Imgur, Cloudinary, etc)
    # Por enquanto, vou deixar um placeholder - você pode substituir pela URL real
    background_url = "https://i.imgur.com/YOUR_IMAGE_ID.png"  # Substitua pela URL real da imagem
    
    # Tentar encontrar o tema Flamengo por diferentes slugs possíveis
    flamengo_theme = None
    possible_slugs = ['flamengo', 'libertadores', 'futebol-brasileiro']
    
    for slug in possible_slugs:
        try:
            flamengo_theme = Theme.objects.get(slug=slug)
            print(f"✅ Tema encontrado: {flamengo_theme.title} (slug: {slug})")
            break
        except Theme.DoesNotExist:
            continue
    
    if not flamengo_theme:
        print("❌ Tema Flamengo não encontrado. Criando novo tema...")
        flamengo_theme = Theme.objects.create(
            title='⚽ Flamengo',
            slug='flamengo',
            description='Quizzes sobre o Clube de Regatas do Flamengo',
            icon='⚽',
            active=True
        )
        print(f"✅ Tema criado: {flamengo_theme.title}")
    
    # Configurar o background
    flamengo_theme.background_image = background_url
    flamengo_theme.background_color = '#000000'  # Preto como cor base
    flamengo_theme.save()
    
    print("\n" + "="*60)
    print("✨ Tema Flamengo configurado com sucesso!")
    print("="*60)
    print(f"Título: {flamengo_theme.title}")
    print(f"Slug: {flamengo_theme.slug}")
    print(f"Background Image: {flamengo_theme.background_image}")
    print(f"Background Color: {flamengo_theme.background_color}")
    print("="*60)
    print("\n📝 PRÓXIMOS PASSOS:")
    print("1. Faça upload da imagem para um serviço como:")
    print("   - Imgur: https://imgur.com/upload")
    print("   - Cloudinary: https://cloudinary.com/")
    print("   - ImgBB: https://imgbb.com/")
    print("2. Copie a URL direta da imagem")
    print("3. Atualize a linha 16 deste script com a URL real")
    print("4. Execute o script novamente")
    print("\nOu configure manualmente pelo Django Admin:")
    print("   /admin/quizzes/theme/")
    print("="*60)


if __name__ == '__main__':
    print("🎨 Configurando tema Flamengo...\n")
    setup_flamengo_theme()

