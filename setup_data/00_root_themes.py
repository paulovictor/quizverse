"""
Script para configurar os temas principais (root themes) em múltiplos países.
Criar categorias base para os países suportados (pt, en, es)
"""

import os
import sys
import django

# Configuração do Django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme

def create_root_themes():
    """Cria temas principais em todos os países"""
    
    # Definição dos temas com suas configurações visuais
    themes_base = [
        {
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485101/ChatGPT_Image_Oct_14_2025_08_21_19_PM_u8jcah.png',
            'primary_color': '#34d399',
            'secondary_color': '#10b981',
            'order': 1,
            'translations': {
                'en': {'title': 'Sports', 'slug': 'sports', 'description': 'Test your knowledge about soccer, Olympics, world records and the greatest athletes in history!'},
                'pt': {'title': 'Esportes', 'slug': 'esportes', 'description': 'Teste seus conhecimentos sobre futebol, olimpíadas, recordes mundiais e os maiores atletas da história!'},
                'es': {'title': 'Deportes', 'slug': 'deportes', 'description': '¡Pon a prueba tus conocimientos sobre fútbol, olimpiadas, récords mundiales y los mejores atletas de la historia!'},
            }
        },
        {
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485101/ChatGPT_Image_Oct_14_2025_08_19_27_PM_vb9x9w.png',
            'primary_color': '#a78bfa',
            'secondary_color': '#8b5cf6',
            'order': 2,
            'translations': {
                'en': {'title': 'Entertainment & Media', 'slug': 'entertainment', 'description': 'Dive into the universe of cinema, series, music and TV!'},
                'pt': {'title': 'Entretenimento & Mídia', 'slug': 'entretenimento', 'description': 'Mergulhe no universo do cinema, séries, música e TV!'},
                'es': {'title': 'Entretenimiento y Medios', 'slug': 'entretenimiento', 'description': '¡Sumérgete en el universo del cine, series, música y TV!'},
            }
        },
        {
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760486708/ChatGPT_Image_Oct_14_2025_09_04_59_PM_yclneb.png',
            'primary_color': '#fb7185',
            'secondary_color': '#f43f5e',
            'order': 3,
            'translations': {
                'en': {'title': 'General Trivia', 'slug': 'trivia', 'description': 'Discover surprising facts about the world!'},
                'pt': {'title': 'Curiosidades Gerais', 'slug': 'curiosidades', 'description': 'Descubra fatos surpreendentes sobre o mundo!'},
                'es': {'title': 'Curiosidades Generales', 'slug': 'curiosidades', 'description': '¡Descubre hechos sorprendentes sobre el mundo!'},
            }
        },
        {
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485110/ChatGPT_Image_Oct_14_2025_05_59_31_PM_g7wxey.png',
            'primary_color': '#22d3ee',
            'secondary_color': '#06b6d4',
            'order': 4,
            'translations': {
                'en': {'title': 'Science & Technology', 'slug': 'science', 'description': 'Explore the universe of innovation!'},
                'pt': {'title': 'Ciência & Tecnologia', 'slug': 'ciencia', 'description': 'Explore o universo da inovação!'},
                'es': {'title': 'Ciencia y Tecnología', 'slug': 'ciencia', 'description': '¡Explora el universo de la innovación!'},
            }
        },
        {
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485108/ChatGPT_Image_Oct_14_2025_05_59_40_PM_u2r5vg.png',
            'primary_color': '#f472b6',
            'secondary_color': '#ec4899',
            'order': 5,
            'translations': {
                'en': {'title': 'Games', 'slug': 'games', 'description': 'From classic to modern video games and board games!'},
                'pt': {'title': 'Jogos', 'slug': 'jogos', 'description': 'Do clássico ao moderno! Videogames e jogos de tabuleiro!'},
                'es': {'title': 'Juegos', 'slug': 'juegos', 'description': '¡De lo clásico a lo moderno! Videojuegos y juegos de mesa!'},
            }
        },
        {
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485107/ChatGPT_Image_Oct_14_2025_08_13_11_PM_pgimb4.png',
            'primary_color': '#fcd34d',
            'secondary_color': '#fbbf24',
            'order': 6,
            'translations': {
                'en': {'title': 'Celebrities & Personalities', 'slug': 'celebrities', 'description': 'Learn about entertainment icons and historical leaders!'},
                'pt': {'title': 'Celebridades & Personalidades', 'slug': 'celebridades', 'description': 'Conheça ícones do entretenimento e líderes históricos!'},
                'es': {'title': 'Celebridades y Personalidades', 'slug': 'celebridades', 'description': '¡Conoce íconos del entretenimiento y líderes históricos!'},
            }
        },
        {
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,f_auto/v1760485103/ChatGPT_Image_Oct_14_2025_08_18_00_PM_ooloop.png',
            'primary_color': '#c084fc',
            'secondary_color': '#a855f7',
            'order': 7,
            'translations': {
                'en': {'title': 'Arts & Culture', 'slug': 'arts', 'description': 'Dive into the world of visual arts, music, and literature!'},
                'pt': {'title': 'Arte & Cultura', 'slug': 'arte', 'description': 'Mergulhe no mundo das artes visuais, música e literatura!'},
                'es': {'title': 'Arte y Cultura', 'slug': 'arte', 'description': '¡Sumérgete en el mundo de las artes visuales, música y literatura!'},
            }
        },
        {
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485109/ChatGPT_Image_Oct_14_2025_05_59_34_PM_km9cdk.png',
            'primary_color': '#fbbf24',
            'secondary_color': '#f59e0b',
            'order': 8,
            'translations': {
                'en': {'title': 'History', 'slug': 'history', 'description': 'Travel through time through ancient civilizations and epic wars!'},
                'pt': {'title': 'História', 'slug': 'historia', 'description': 'Viaje no tempo através de civilizações antigas e guerras épicas!'},
                'es': {'title': 'Historia', 'slug': 'historia', 'description': '¡Viaja en el tiempo a través de civilizaciones antiguas y guerras épicas!'},
            }
        },
        {
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485104/ChatGPT_Image_Oct_14_2025_08_17_14_PM_ghpv3w.png',
            'primary_color': '#fbbf24',
            'secondary_color': '#f59e0b',
            'order': 9,
            'translations': {
                'en': {'title': 'Food & Drink', 'slug': 'food', 'description': 'For food lovers! Famous recipes and world cuisine!'},
                'pt': {'title': 'Comida & Bebida', 'slug': 'comida', 'description': 'Para os amantes da gastronomia! Receitas famosas e culinária mundial!'},
                'es': {'title': 'Comida y Bebida', 'slug': 'comida', 'description': '¡Para los amantes de la gastronomía! ¡Recetas famosas y cocina mundial!'},
            }
        },
        {
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485105/ChatGPT_Image_Oct_14_2025_08_16_46_PM_tclomp.png',
            'primary_color': '#4ade80',
            'secondary_color': '#22c55e',
            'order': 10,
            'translations': {
                'en': {'title': 'Nature & Animals', 'slug': 'nature', 'description': 'Explore the planet\'s biodiversity!'},
                'pt': {'title': 'Natureza & Animais', 'slug': 'natureza', 'description': 'Explore a biodiversidade do planeta!'},
                'es': {'title': 'Naturaleza y Animales', 'slug': 'naturaleza', 'description': '¡Explora la biodiversidad del planeta!'},
            }
        },
        {
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485102/ChatGPT_Image_Oct_14_2025_08_19_00_PM_e99coh.png',
            'primary_color': '#60a5fa',
            'secondary_color': '#3b82f6',
            'order': 11,
            'translations': {
                'en': {'title': 'Geography', 'slug': 'geography', 'description': 'Explore countries, capitals, and natural wonders!'},
                'pt': {'title': 'Geografia', 'slug': 'geografia', 'description': 'Explore países, capitais e maravilhas naturais!'},
                'es': {'title': 'Geografía', 'slug': 'geografia', 'description': '¡Explora países, capitales y maravillas naturales!'},
            }
        },
        {
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485106/Symbols_of_Justice_and_Voice_frytbp.png',
            'primary_color': '#94a3b8',
            'secondary_color': '#64748b',
            'order': 12,
            'translations': {
                'en': {'title': 'Politics & Society', 'slug': 'politics', 'description': 'Understand political systems and social movements!'},
                'pt': {'title': 'Política & Sociedade', 'slug': 'politica', 'description': 'Entenda sistemas políticos e movimentos sociais!'},
                'es': {'title': 'Política y Sociedad', 'slug': 'politica', 'description': '¡Comprende los sistemas políticos y movimientos sociales!'},
            }
        },
    ]
    
    # Mapeamento de países para idiomas
    country_to_lang = {
        'en-US': 'en', 'en-CA': 'en', 'en-GB': 'en', 'en-IN': 'en', 'en-PH': 'en', 'en-AU': 'en', 'en-NZ': 'en',
        'pt-BR': 'pt', 'pt-PT': 'pt',
        'es-MX': 'es', 'es-ES': 'es', 'es-AR': 'es', 'es-CO': 'es',
    }
    
    countries = list(country_to_lang.keys())
    
    print("🚀 Criando temas principais em múltiplos países...")
    print(f"🌍 Países: {len(countries)}")
    print(f"🎯 Temas base: {len(themes_base)}")
    print(f"📊 Total a processar: {len(themes_base) * len(countries)}")
    print("-" * 80)
    
    created_count = 0
    updated_count = 0
    
    for theme_base in themes_base:
        for country_code in countries:
            lang_code = country_to_lang[country_code]
            translation = theme_base['translations'].get(lang_code, theme_base['translations']['en'])
            
            # Determinar o slug: Brasil não tem sufixo, outros países sempre têm
            base_slug = translation['slug']
            if country_code == 'pt-BR':
                slug = base_slug
            else:
                country_suffix = country_code.split('-')[1].lower()
                slug = f"{base_slug}-{country_suffix}"
            
            theme, created = Theme.objects.update_or_create(
                slug=slug,
                country=country_code,
                defaults={
                    'title': translation['title'],
                    'description': translation['description'],
                    'icon': theme_base['icon'],
                    'primary_color': theme_base['primary_color'],
                    'secondary_color': theme_base['secondary_color'],
                    'order': theme_base['order'],
                    'parent': None,
                    'active': True
                }
            )
            
            if created:
                created_count += 1
                status = "✅"
            else:
                updated_count += 1
                status = "🔄"
            
            country_emoji = dict(Theme.COUNTRY_CHOICES).get(country_code, country_code).split()[0]
            print(f"{status} [{country_code}] {country_emoji} {theme.title} (slug: {slug})")
    
    print("-" * 80)
    print(f"✨ Processo concluído!")
    print(f"📊 Temas criados: {created_count}")
    print(f"🔄 Temas atualizados: {updated_count}")
    print(f"📈 Total processado: {created_count + updated_count}")
    print(f"🌍 Países configurados: {len(countries)}")
    print(f"🎯 Temas por país: {len(themes_base)}")

if __name__ == '__main__':
    create_root_themes()
