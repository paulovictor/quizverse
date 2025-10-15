"""
Script para configurar os temas principais (root themes) em múltiplos idiomas.
Criar categorias base para todos os idiomas suportados: pt, en, es, de, fr, it
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
    """Cria temas principais em todos os idiomas"""
    
    # Definição dos temas com traduções
    themes_data = [
        {
            'translations': {
                'pt-BR': {
                    'title': 'Esportes',
                    'slug': 'esportes',
                    'description': 'Teste seus conhecimentos sobre futebol, olimpíadas, recordes mundiais e os maiores atletas da história. De regras a curiosidades esportivas!'
                },
                'en': {
                    'title': 'Sports',
                    'slug': 'sports',
                    'description': 'Test your knowledge about soccer, Olympics, world records and the greatest athletes in history. From rules to sports trivia!'
                },
                'es': {
                    'title': 'Deportes',
                    'slug': 'deportes',
                    'description': '¡Pon a prueba tus conocimientos sobre fútbol, olimpiadas, récords mundiales y los mejores atletas de la historia. ¡De reglas a curiosidades deportivas!'
                },
                'de': {
                    'title': 'Sport',
                    'slug': 'sport',
                    'description': 'Testen Sie Ihr Wissen über Fußball, Olympische Spiele, Weltrekorde und die größten Athleten der Geschichte. Von Regeln bis zu Sport-Trivia!'
                },
                'fr': {
                    'title': 'Sports',
                    'slug': 'sports',
                    'description': 'Testez vos connaissances sur le football, les Jeux olympiques, les records mondiaux et les plus grands athlètes de l\'histoire. Des règles aux anecdotes sportives!'
                },
                'it': {
                    'title': 'Sport',
                    'slug': 'sport',
                    'description': 'Metti alla prova le tue conoscenze su calcio, Olimpiadi, record mondiali e i più grandi atleti della storia. Dalle regole alle curiosità sportive!'
                }
            },
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485101/ChatGPT_Image_Oct_14_2025_08_21_19_PM_u8jcah.png',
            'primary_color': '#34d399',
            'secondary_color': '#10b981',
            'icon_bg_color_1': '#d1fae5',
            'icon_bg_color_2': '#a7f3d0',
            'order': 1
        },
        {
            'translations': {
                'pt-BR': {
                    'title': 'Entretenimento & Mídia',
                    'slug': 'entretenimento-midia',
                    'description': 'Mergulhe no universo do cinema, séries, música e TV! De blockbusters a clássicos cult, teste seu conhecimento sobre tudo que diverte o mundo.'
                },
                'en': {
                    'title': 'Entertainment & Media',
                    'slug': 'entertainment-media',
                    'description': 'Dive into the universe of cinema, series, music and TV! From blockbusters to cult classics, test your knowledge about everything that entertains the world.'
                },
                'es': {
                    'title': 'Entretenimiento y Medios',
                    'slug': 'entretenimiento-medios',
                    'description': '¡Sumérgete en el universo del cine, series, música y TV! Desde éxitos de taquilla hasta clásicos de culto, pon a prueba tus conocimientos sobre todo lo que divierte al mundo.'
                },
                'de': {
                    'title': 'Unterhaltung & Medien',
                    'slug': 'unterhaltung-medien',
                    'description': 'Tauchen Sie ein in die Welt von Kino, Serien, Musik und TV! Von Blockbustern bis Kultklassikern, testen Sie Ihr Wissen über alles, was die Welt unterhält.'
                },
                'fr': {
                    'title': 'Divertissement & Médias',
                    'slug': 'divertissement-medias',
                    'description': 'Plongez dans l\'univers du cinéma, des séries, de la musique et de la TV! Des blockbusters aux classiques cultes, testez vos connaissances sur tout ce qui divertit le monde.'
                },
                'it': {
                    'title': 'Intrattenimento & Media',
                    'slug': 'intrattenimento-media',
                    'description': 'Immergiti nell\'universo del cinema, serie TV, musica e televisione! Dai blockbuster ai classici cult, metti alla prova le tue conoscenze su tutto ciò che intrattiene il mondo.'
                }
            },
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485101/ChatGPT_Image_Oct_14_2025_08_19_27_PM_vb9x9w.png',
            'primary_color': '#a78bfa',
            'secondary_color': '#8b5cf6',
            'icon_bg_color_1': '#ede9fe',
            'icon_bg_color_2': '#ddd6fe',
            'order': 2
        },
        {
            'translations': {
                'pt-BR': {
                    'title': 'Curiosidades Gerais',
                    'slug': 'curiosidades-gerais',
                    'description': 'Descubra fatos surpreendentes e bizarros sobre o mundo! Perguntas aleatórias e divertidas que vão testar sua cultura geral de forma imprevisível.'
                },
                'en': {
                    'title': 'General Trivia',
                    'slug': 'general-trivia',
                    'description': 'Discover surprising and bizarre facts about the world! Random and fun questions that will test your general knowledge in unpredictable ways.'
                },
                'es': {
                    'title': 'Curiosidades Generales',
                    'slug': 'curiosidades-generales',
                    'description': '¡Descubre hechos sorprendentes y extraños sobre el mundo! Preguntas aleatorias y divertidas que pondrán a prueba tu cultura general de manera impredecible.'
                },
                'de': {
                    'title': 'Allgemeinwissen',
                    'slug': 'allgemeinwissen',
                    'description': 'Entdecken Sie überraschende und bizarre Fakten über die Welt! Zufällige und unterhaltsame Fragen, die Ihr Allgemeinwissen auf unvorhersehbare Weise testen.'
                },
                'fr': {
                    'title': 'Culture Générale',
                    'slug': 'culture-generale',
                    'description': 'Découvrez des faits surprenants et bizarres sur le monde! Des questions aléatoires et amusantes qui testeront votre culture générale de manière imprévisible.'
                },
                'it': {
                    'title': 'Curiosità Generali',
                    'slug': 'curiosita-generali',
                    'description': 'Scopri fatti sorprendenti e bizzarri sul mondo! Domande casuali e divertenti che metteranno alla prova la tua cultura generale in modi imprevedibili.'
                }
            },
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760486708/ChatGPT_Image_Oct_14_2025_09_04_59_PM_yclneb.png',
            'primary_color': '#fb7185',
            'secondary_color': '#f43f5e',
            'icon_bg_color_1': '#ffe4e6',
            'icon_bg_color_2': '#fecdd3',
            'order': 3
        },
        {
            'translations': {
                'pt-BR': {
                    'title': 'Ciência & Tecnologia',
                    'slug': 'ciencia-tecnologia',
                    'description': 'Explore o universo da inovação! De física quântica a inteligência artificial, descubra as descobertas que transformam nosso mundo.'
                },
                'en': {
                    'title': 'Science & Technology',
                    'slug': 'science-technology',
                    'description': 'Explore the universe of innovation! From quantum physics to artificial intelligence, discover the discoveries that transform our world.'
                },
                'es': {
                    'title': 'Ciencia y Tecnología',
                    'slug': 'ciencia-tecnologia',
                    'description': '¡Explora el universo de la innovación! Desde física cuántica hasta inteligencia artificial, descubre los hallazgos que transforman nuestro mundo.'
                },
                'de': {
                    'title': 'Wissenschaft & Technologie',
                    'slug': 'wissenschaft-technologie',
                    'description': 'Erkunden Sie das Universum der Innovation! Von Quantenphysik bis künstlicher Intelligenz, entdecken Sie die Entdeckungen, die unsere Welt verändern.'
                },
                'fr': {
                    'title': 'Science & Technologie',
                    'slug': 'science-technologie',
                    'description': 'Explorez l\'univers de l\'innovation! De la physique quantique à l\'intelligence artificielle, découvrez les découvertes qui transforment notre monde.'
                },
                'it': {
                    'title': 'Scienza & Tecnologia',
                    'slug': 'scienza-tecnologia',
                    'description': 'Esplora l\'universo dell\'innovazione! Dalla fisica quantistica all\'intelligenza artificiale, scopri le scoperte che trasformano il nostro mondo.'
                }
            },
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485110/ChatGPT_Image_Oct_14_2025_05_59_31_PM_g7wxey.png',
            'primary_color': '#22d3ee',
            'secondary_color': '#06b6d4',
            'icon_bg_color_1': '#cffafe',
            'icon_bg_color_2': '#a5f3fc',
            'order': 4
        },
        {
            'translations': {
                'pt-BR': {
                    'title': 'Jogos',
                    'slug': 'jogos',
                    'description': 'Do clássico ao moderno! Teste sua memória sobre videogames, jogos de tabuleiro e os universos que marcaram gerações de jogadores.'
                },
                'en': {
                    'title': 'Games',
                    'slug': 'games',
                    'description': 'From classic to modern! Test your memory about video games, board games and the universes that marked generations of players.'
                },
                'es': {
                    'title': 'Juegos',
                    'slug': 'juegos',
                    'description': '¡De lo clásico a lo moderno! Pon a prueba tu memoria sobre videojuegos, juegos de mesa y los universos que marcaron generaciones de jugadores.'
                },
                'de': {
                    'title': 'Spiele',
                    'slug': 'spiele',
                    'description': 'Vom Klassiker bis zur Moderne! Testen Sie Ihr Gedächtnis über Videospiele, Brettspiele und die Universen, die Generationen von Spielern geprägt haben.'
                },
                'fr': {
                    'title': 'Jeux',
                    'slug': 'jeux',
                    'description': 'Du classique au moderne! Testez votre mémoire sur les jeux vidéo, les jeux de société et les univers qui ont marqué des générations de joueurs.'
                },
                'it': {
                    'title': 'Giochi',
                    'slug': 'giochi',
                    'description': 'Dal classico al moderno! Metti alla prova la tua memoria su videogiochi, giochi da tavolo e gli universi che hanno segnato generazioni di giocatori.'
                }
            },
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485108/ChatGPT_Image_Oct_14_2025_05_59_40_PM_u2r5vg.png',
            'primary_color': '#f472b6',
            'secondary_color': '#ec4899',
            'icon_bg_color_1': '#fce7f3',
            'icon_bg_color_2': '#fbcfe8',
            'order': 5
        },
        {
            'translations': {
                'pt-BR': {
                    'title': 'Celebridades & Personalidades',
                    'slug': 'celebridades-personalidades',
                    'description': 'Conheça a vida de ícones do entretenimento, líderes históricos e figuras que influenciaram a cultura pop e a sociedade moderna.'
                },
                'en': {
                    'title': 'Celebrities & Personalities',
                    'slug': 'celebrities-personalities',
                    'description': 'Learn about the lives of entertainment icons, historical leaders and figures who influenced pop culture and modern society.'
                },
                'es': {
                    'title': 'Celebridades y Personalidades',
                    'slug': 'celebridades-personalidades',
                    'description': 'Conoce la vida de íconos del entretenimiento, líderes históricos y figuras que influenciaron la cultura pop y la sociedad moderna.'
                },
                'de': {
                    'title': 'Prominente & Persönlichkeiten',
                    'slug': 'prominente-personlichkeiten',
                    'description': 'Erfahren Sie mehr über das Leben von Entertainment-Ikonen, historischen Führern und Persönlichkeiten, die die Popkultur und moderne Gesellschaft beeinflusst haben.'
                },
                'fr': {
                    'title': 'Célébrités & Personnalités',
                    'slug': 'celebrites-personnalites',
                    'description': 'Découvrez la vie d\'icônes du divertissement, de leaders historiques et de figures qui ont influencé la culture pop et la société moderne.'
                },
                'it': {
                    'title': 'Celebrità & Personalità',
                    'slug': 'celebrita-personalita',
                    'description': 'Scopri la vita delle icone dello spettacolo, leader storici e figure che hanno influenzato la cultura pop e la società moderna.'
                }
            },
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485107/ChatGPT_Image_Oct_14_2025_08_13_11_PM_pgimb4.png',
            'primary_color': '#fcd34d',
            'secondary_color': '#fbbf24',
            'icon_bg_color_1': '#fef9c3',
            'icon_bg_color_2': '#fef08a',
            'order': 6
        },
        {
            'translations': {
                'pt-BR': {
                    'title': 'Arte & Cultura',
                    'slug': 'arte-cultura',
                    'description': 'Mergulhe no mundo das artes visuais, música, cinema, literatura e tradições culturais que enriquecem nossa sociedade.'
                },
                'en': {
                    'title': 'Arts & Culture',
                    'slug': 'arts-culture',
                    'description': 'Dive into the world of visual arts, music, cinema, literature and cultural traditions that enrich our society.'
                },
                'es': {
                    'title': 'Arte y Cultura',
                    'slug': 'arte-cultura',
                    'description': 'Sumérgete en el mundo de las artes visuales, música, cine, literatura y tradiciones culturales que enriquecen nuestra sociedad.'
                },
                'de': {
                    'title': 'Kunst & Kultur',
                    'slug': 'kunst-kultur',
                    'description': 'Tauchen Sie ein in die Welt der bildenden Künste, Musik, Kino, Literatur und kulturellen Traditionen, die unsere Gesellschaft bereichern.'
                },
                'fr': {
                    'title': 'Arts & Culture',
                    'slug': 'arts-culture',
                    'description': 'Plongez dans le monde des arts visuels, de la musique, du cinéma, de la littérature et des traditions culturelles qui enrichissent notre société.'
                },
                'it': {
                    'title': 'Arte & Cultura',
                    'slug': 'arte-cultura',
                    'description': 'Immergiti nel mondo delle arti visive, musica, cinema, letteratura e tradizioni culturali che arricchiscono la nostra società.'
                }
            },
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,f_auto/v1760485103/ChatGPT_Image_Oct_14_2025_08_18_00_PM_ooloop.png',
            'primary_color': '#c084fc',
            'secondary_color': '#a855f7',
            'icon_bg_color_1': '#f3e8ff',
            'icon_bg_color_2': '#e9d5ff',
            'order': 7
        },
        {
            'translations': {
                'pt-BR': {
                    'title': 'História',
                    'slug': 'historia',
                    'description': 'Viaje no tempo através de civilizações antigas, guerras épicas e momentos que mudaram o curso da humanidade. Você conhece o passado?'
                },
                'en': {
                    'title': 'History',
                    'slug': 'history',
                    'description': 'Travel through time through ancient civilizations, epic wars and moments that changed the course of humanity. Do you know the past?'
                },
                'es': {
                    'title': 'Historia',
                    'slug': 'historia',
                    'description': 'Viaja en el tiempo a través de civilizaciones antiguas, guerras épicas y momentos que cambiaron el curso de la humanidad. ¿Conoces el pasado?'
                },
                'de': {
                    'title': 'Geschichte',
                    'slug': 'geschichte',
                    'description': 'Reisen Sie durch die Zeit durch antike Zivilisationen, epische Kriege und Momente, die den Lauf der Menschheit verändert haben. Kennen Sie die Vergangenheit?'
                },
                'fr': {
                    'title': 'Histoire',
                    'slug': 'histoire',
                    'description': 'Voyagez dans le temps à travers les civilisations anciennes, les guerres épiques et les moments qui ont changé le cours de l\'humanité. Connaissez-vous le passé?'
                },
                'it': {
                    'title': 'Storia',
                    'slug': 'storia',
                    'description': 'Viaggia nel tempo attraverso civiltà antiche, guerre epiche e momenti che hanno cambiato il corso dell\'umanità. Conosci il passato?'
                }
            },
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485109/ChatGPT_Image_Oct_14_2025_05_59_34_PM_km9cdk.png',
            'primary_color': '#fbbf24',
            'secondary_color': '#f59e0b',
            'icon_bg_color_1': '#fef3c7',
            'icon_bg_color_2': '#fde68a',
            'order': 8
        },
        {
            'translations': {
                'pt-BR': {
                    'title': 'Comida & Bebida',
                    'slug': 'comida-bebida',
                    'description': 'Para os amantes da gastronomia! Receitas famosas, ingredientes exóticos, chefs renomados e curiosidades sobre a culinária mundial.'
                },
                'en': {
                    'title': 'Food & Drink',
                    'slug': 'food-drink',
                    'description': 'For food lovers! Famous recipes, exotic ingredients, renowned chefs and curiosities about world cuisine.'
                },
                'es': {
                    'title': 'Comida y Bebida',
                    'slug': 'comida-bebida',
                    'description': '¡Para los amantes de la gastronomía! Recetas famosas, ingredientes exóticos, chefs reconocidos y curiosidades sobre la cocina mundial.'
                },
                'de': {
                    'title': 'Essen & Trinken',
                    'slug': 'essen-trinken',
                    'description': 'Für Feinschmecker! Berühmte Rezepte, exotische Zutaten, renommierte Köche und Kuriositäten über die Weltküche.'
                },
                'fr': {
                    'title': 'Nourriture & Boissons',
                    'slug': 'nourriture-boissons',
                    'description': 'Pour les amateurs de gastronomie! Recettes célèbres, ingrédients exotiques, chefs renommés et curiosités sur la cuisine mondiale.'
                },
                'it': {
                    'title': 'Cibo & Bevande',
                    'slug': 'cibo-bevande',
                    'description': 'Per gli amanti della gastronomia! Ricette famose, ingredienti esotici, chef rinomati e curiosità sulla cucina mondiale.'
                }
            },
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485104/ChatGPT_Image_Oct_14_2025_08_17_14_PM_ghpv3w.png',
            'primary_color': '#fbbf24',
            'secondary_color': '#f59e0b',
            'icon_bg_color_1': '#fef3c7',
            'icon_bg_color_2': '#fde68a',
            'order': 9
        },
        {
            'translations': {
                'pt-BR': {
                    'title': 'Natureza & Animais',
                    'slug': 'natureza-animais',
                    'description': 'Explore a biodiversidade do planeta! Espécies fascinantes, ecossistemas únicos e os segredos da vida selvagem aguardam você.'
                },
                'en': {
                    'title': 'Nature & Animals',
                    'slug': 'nature-animals',
                    'description': 'Explore the planet\'s biodiversity! Fascinating species, unique ecosystems and the secrets of wildlife await you.'
                },
                'es': {
                    'title': 'Naturaleza y Animales',
                    'slug': 'naturaleza-animales',
                    'description': '¡Explora la biodiversidad del planeta! Especies fascinantes, ecosistemas únicos y los secretos de la vida silvestre te esperan.'
                },
                'de': {
                    'title': 'Natur & Tiere',
                    'slug': 'natur-tiere',
                    'description': 'Erkunden Sie die Biodiversität des Planeten! Faszinierende Arten, einzigartige Ökosysteme und die Geheimnisse der Tierwelt erwarten Sie.'
                },
                'fr': {
                    'title': 'Nature & Animaux',
                    'slug': 'nature-animaux',
                    'description': 'Explorez la biodiversité de la planète! Des espèces fascinantes, des écosystèmes uniques et les secrets de la faune vous attendent.'
                },
                'it': {
                    'title': 'Natura & Animali',
                    'slug': 'natura-animali',
                    'description': 'Esplora la biodiversità del pianeta! Specie affascinanti, ecosistemi unici e i segreti della fauna selvatica ti aspettano.'
                }
            },
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485105/ChatGPT_Image_Oct_14_2025_08_16_46_PM_tclomp.png',
            'primary_color': '#4ade80',
            'secondary_color': '#22c55e',
            'icon_bg_color_1': '#dcfce7',
            'icon_bg_color_2': '#bbf7d0',
            'order': 10
        },
        {
            'translations': {
                'pt-BR': {
                    'title': 'Geografia',
                    'slug': 'geografia',
                    'description': 'Explore países, capitais, continentes e maravilhas naturais! Desafie-se com perguntas sobre mapas, culturas e paisagens ao redor do globo.'
                },
                'en': {
                    'title': 'Geography',
                    'slug': 'geography',
                    'description': 'Explore countries, capitals, continents and natural wonders! Challenge yourself with questions about maps, cultures and landscapes around the globe.'
                },
                'es': {
                    'title': 'Geografía',
                    'slug': 'geografia',
                    'description': '¡Explora países, capitales, continentes y maravillas naturales! Desafíate con preguntas sobre mapas, culturas y paisajes alrededor del mundo.'
                },
                'de': {
                    'title': 'Geographie',
                    'slug': 'geographie',
                    'description': 'Erkunden Sie Länder, Hauptstädte, Kontinente und Naturwunder! Fordern Sie sich mit Fragen zu Karten, Kulturen und Landschaften auf der ganzen Welt heraus.'
                },
                'fr': {
                    'title': 'Géographie',
                    'slug': 'geographie',
                    'description': 'Explorez les pays, capitales, continents et merveilles naturelles! Défiez-vous avec des questions sur les cartes, cultures et paysages du monde entier.'
                },
                'it': {
                    'title': 'Geografia',
                    'slug': 'geografia',
                    'description': 'Esplora paesi, capitali, continenti e meraviglie naturali! Sfida te stesso con domande su mappe, culture e paesaggi di tutto il mondo.'
                }
            },
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485102/ChatGPT_Image_Oct_14_2025_08_19_00_PM_e99coh.png',
            'primary_color': '#60a5fa',
            'secondary_color': '#3b82f6',
            'icon_bg_color_1': '#dbeafe',
            'icon_bg_color_2': '#bfdbfe',
            'order': 11
        },
        {
            'translations': {
                'pt-BR': {
                    'title': 'Política & Sociedade',
                    'slug': 'politica-sociedade',
                    'description': 'Entenda sistemas políticos, movimentos sociais e os eventos que moldam a organização da sociedade contemporânea.'
                },
                'en': {
                    'title': 'Politics & Society',
                    'slug': 'politics-society',
                    'description': 'Understand political systems, social movements and the events that shape the organization of contemporary society.'
                },
                'es': {
                    'title': 'Política y Sociedad',
                    'slug': 'politica-sociedad',
                    'description': 'Comprende los sistemas políticos, movimientos sociales y los eventos que moldean la organización de la sociedad contemporánea.'
                },
                'de': {
                    'title': 'Politik & Gesellschaft',
                    'slug': 'politik-gesellschaft',
                    'description': 'Verstehen Sie politische Systeme, soziale Bewegungen und die Ereignisse, die die Organisation der zeitgenössischen Gesellschaft prägen.'
                },
                'fr': {
                    'title': 'Politique & Société',
                    'slug': 'politique-societe',
                    'description': 'Comprenez les systèmes politiques, les mouvements sociaux et les événements qui façonnent l\'organisation de la société contemporaine.'
                },
                'it': {
                    'title': 'Politica & Società',
                    'slug': 'politica-societa',
                    'description': 'Comprendi i sistemi politici, i movimenti sociali e gli eventi che plasmano l\'organizzazione della società contemporanea.'
                }
            },
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485106/Symbols_of_Justice_and_Voice_frytbp.png',
            'primary_color': '#94a3b8',
            'secondary_color': '#64748b',
            'icon_bg_color_1': '#f1f5f9',
            'icon_bg_color_2': '#e2e8f0',
            'order': 12
        }
    ]
    
    languages = ['pt-BR', 'en', 'es', 'de', 'fr', 'it']
    
    print("🚀 Criando temas principais em múltiplos idiomas...")
    print(f"📚 Idiomas: {', '.join(languages)}")
    print(f"🎯 Total de temas: {len(themes_data)}")
    print("-" * 60)
    
    created_count = 0
    updated_count = 0
    
    for theme_data in themes_data:
        for lang in languages:
            translation = theme_data['translations'][lang]
            
            theme, created = Theme.objects.update_or_create(
                slug=translation['slug'],
                language=lang,
                defaults={
                    'title': translation['title'],
                    'description': translation['description'],
                    'icon': theme_data['icon'],
                    'primary_color': theme_data['primary_color'],
                    'secondary_color': theme_data['secondary_color'],
                    'icon_bg_color_1': theme_data['icon_bg_color_1'],
                    'icon_bg_color_2': theme_data['icon_bg_color_2'],
                    'order': theme_data['order'],
                    'parent': None,
                    'active': True
                }
            )
            
            if created:
                created_count += 1
                status = "✅ CRIADO"
            else:
                updated_count += 1
                status = "🔄 ATUALIZADO"
            
            print(f"{status}: [{lang.upper()}] {theme.title} ({theme.slug})")
    
    print("-" * 60)
    print(f"✨ Processo concluído!")
    print(f"📊 Temas criados: {created_count}")
    print(f"🔄 Temas atualizados: {updated_count}")
    print(f"📈 Total processado: {created_count + updated_count}")

if __name__ == '__main__':
    create_root_themes()

