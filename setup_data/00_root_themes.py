"""
Script para configurar os temas principais (root themes) em múltiplos países.
Criar categorias base para todos os 25 países suportados
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
            'slug_base': 'sports',
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485101/ChatGPT_Image_Oct_14_2025_08_21_19_PM_u8jcah.png',
            'primary_color': '#34d399',
            'secondary_color': '#10b981',
            'icon_bg_color_1': '#d1fae5',
            'icon_bg_color_2': '#a7f3d0',
            'order': 1,
            'translations': {
                'en': {'title': 'Sports', 'description': 'Test your knowledge about soccer, Olympics, world records and the greatest athletes in history!'},
                'pt': {'title': 'Esportes', 'description': 'Teste seus conhecimentos sobre futebol, olimpíadas, recordes mundiais e os maiores atletas da história!'},
                'es': {'title': 'Deportes', 'description': '¡Pon a prueba tus conocimientos sobre fútbol, olimpiadas, récords mundiales y los mejores atletas de la historia!'},
                'de': {'title': 'Sport', 'description': 'Testen Sie Ihr Wissen über Fußball, Olympische Spiele, Weltrekorde und die größten Athleten der Geschichte!'},
                'fr': {'title': 'Sports', 'description': 'Testez vos connaissances sur le football, les Jeux olympiques, les records mondiaux et les plus grands athlètes!'},
                'it': {'title': 'Sport', 'description': 'Metti alla prova le tue conoscenze su calcio, Olimpiadi, record mondiali e i più grandi atleti della storia!'},
                'nl': {'title': 'Sport', 'description': 'Test je kennis over voetbal, Olympische Spelen, wereldrecords en de grootste atleten uit de geschiedenis!'},
                'sv': {'title': 'Sport', 'description': 'Testa dina kunskaper om fotboll, OS, världsrekord och historiens största idrottare!'},
                'no': {'title': 'Sport', 'description': 'Test kunnskapen din om fotball, OL, verdensrekorder og historiens største idrettsutøvere!'},
                'pl': {'title': 'Sport', 'description': 'Przetestuj swoją wiedzę o piłce nożnej, Igrzyskach Olimpijskich, rekordach świata i największych sportowcach!'},
                'id': {'title': 'Olahraga', 'description': 'Uji pengetahuan Anda tentang sepak bola, Olimpiade, rekor dunia, dan atlet terhebat sepanjang masa!'},
                'ja': {'title': 'スポーツ', 'description': 'サッカー、オリンピック、世界記録、歴史上最高のアスリートについての知識をテストしよう!'},
                'ko': {'title': '스포츠', 'description': '축구, 올림픽, 세계 기록, 역사상 최고의 운동선수에 대한 지식을 테스트하세요!'},
                'th': {'title': 'กีฬา', 'description': 'ทดสอบความรู้เกี่ยวกับฟุตบอล โอลิมปิก สถิติโลก และนักกีฬาที่ยิ่งใหญ่ที่สุดในประวัติศาสตร์!'},
                'vi': {'title': 'Thể thao', 'description': 'Kiểm tra kiến thức của bạn về bóng đá, Olympic, kỷ lục thế giới và những vận động viên vĩ đại nhất!'},
            }
        },
        {
            'slug_base': 'entertainment',
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485101/ChatGPT_Image_Oct_14_2025_08_19_27_PM_vb9x9w.png',
            'primary_color': '#a78bfa',
            'secondary_color': '#8b5cf6',
            'icon_bg_color_1': '#ede9fe',
            'icon_bg_color_2': '#ddd6fe',
            'order': 2,
            'translations': {
                'en': {'title': 'Entertainment & Media', 'description': 'Dive into the universe of cinema, series, music and TV!'},
                'pt': {'title': 'Entretenimento & Mídia', 'description': 'Mergulhe no universo do cinema, séries, música e TV!'},
                'es': {'title': 'Entretenimiento y Medios', 'description': '¡Sumérgete en el universo del cine, series, música y TV!'},
                'de': {'title': 'Unterhaltung & Medien', 'description': 'Tauchen Sie ein in die Welt von Kino, Serien, Musik und TV!'},
                'fr': {'title': 'Divertissement & Médias', 'description': 'Plongez dans l\'univers du cinéma, des séries, de la musique et de la TV!'},
                'it': {'title': 'Intrattenimento & Media', 'description': 'Immergiti nell\'universo del cinema, serie TV, musica e televisione!'},
                'nl': {'title': 'Entertainment & Media', 'description': 'Duik in het universum van cinema, series, muziek en TV!'},
                'sv': {'title': 'Underhållning & Media', 'description': 'Dyk in i världen av bio, serier, musik och TV!'},
                'no': {'title': 'Underholdning & Media', 'description': 'Dykk ned i universet av kino, serier, musikk og TV!'},
                'pl': {'title': 'Rozrywka i Media', 'description': 'Zanurz się w świecie kina, seriali, muzyki i telewizji!'},
                'id': {'title': 'Hiburan & Media', 'description': 'Selami dunia sinema, serial, musik, dan TV!'},
                'ja': {'title': 'エンターテイメント', 'description': '映画、シリーズ、音楽、テレビの世界に飛び込もう!'},
                'ko': {'title': '엔터테인먼트', 'description': '영화, 시리즈, 음악, TV의 세계로 뛰어들어보세요!'},
                'th': {'title': 'บันเทิง', 'description': 'ดำดิ่งสู่จักรวาลของภาพยนตร์ ซีรีส์ เพลง และทีวี!'},
                'vi': {'title': 'Giải trí & Truyền thông', 'description': 'Hòa mình vào vũ trụ điện ảnh, phim truyền hình, âm nhạc và TV!'},
            }
        },
        {
            'slug_base': 'trivia',
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760486708/ChatGPT_Image_Oct_14_2025_09_04_59_PM_yclneb.png',
            'primary_color': '#fb7185',
            'secondary_color': '#f43f5e',
            'icon_bg_color_1': '#ffe4e6',
            'icon_bg_color_2': '#fecdd3',
            'order': 3,
            'translations': {
                'en': {'title': 'General Trivia', 'description': 'Discover surprising facts about the world!'},
                'pt': {'title': 'Curiosidades Gerais', 'description': 'Descubra fatos surpreendentes sobre o mundo!'},
                'es': {'title': 'Curiosidades Generales', 'description': '¡Descubre hechos sorprendentes sobre el mundo!'},
                'de': {'title': 'Allgemeinwissen', 'description': 'Entdecken Sie überraschende Fakten über die Welt!'},
                'fr': {'title': 'Culture Générale', 'description': 'Découvrez des faits surprenants sur le monde!'},
                'it': {'title': 'Curiosità Generali', 'description': 'Scopri fatti sorprendenti sul mondo!'},
                'nl': {'title': 'Algemene Kennis', 'description': 'Ontdek verrassende feiten over de wereld!'},
                'sv': {'title': 'Allmänbildning', 'description': 'Upptäck överraskande fakta om världen!'},
                'no': {'title': 'Allmenankunnskap', 'description': 'Oppdag overraskende fakta om verden!'},
                'pl': {'title': 'Ciekawostki', 'description': 'Odkryj zaskakujące fakty o świecie!'},
                'id': {'title': 'Trivia Umum', 'description': 'Temukan fakta mengejutkan tentang dunia!'},
                'ja': {'title': '一般知識', 'description': '世界についての驚くべき事実を発見しよう!'},
                'ko': {'title': '일반 상식', 'description': '세상에 대한 놀라운 사실을 발견하세요!'},
                'th': {'title': 'ความรู้ทั่วไป', 'description': 'ค้นพบข้อเท็จจริงที่น่าประหลาดใจเกี่ยวกับโลก!'},
                'vi': {'title': 'Kiến thức tổng hợp', 'description': 'Khám phá những sự thật đáng ngạc nhiên về thế giới!'},
            }
        },
        {
            'slug_base': 'science',
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485110/ChatGPT_Image_Oct_14_2025_05_59_31_PM_g7wxey.png',
            'primary_color': '#22d3ee',
            'secondary_color': '#06b6d4',
            'icon_bg_color_1': '#cffafe',
            'icon_bg_color_2': '#a5f3fc',
            'order': 4,
            'translations': {
                'en': {'title': 'Science & Technology', 'description': 'Explore the universe of innovation!'},
                'pt': {'title': 'Ciência & Tecnologia', 'description': 'Explore o universo da inovação!'},
                'es': {'title': 'Ciencia y Tecnología', 'description': '¡Explora el universo de la innovación!'},
                'de': {'title': 'Wissenschaft & Technologie', 'description': 'Erkunden Sie das Universum der Innovation!'},
                'fr': {'title': 'Science & Technologie', 'description': 'Explorez l\'univers de l\'innovation!'},
                'it': {'title': 'Scienza & Tecnologia', 'description': 'Esplora l\'universo dell\'innovazione!'},
                'nl': {'title': 'Wetenschap & Technologie', 'description': 'Verken het universum van innovatie!'},
                'sv': {'title': 'Vetenskap & Teknologi', 'description': 'Utforska innovationens universum!'},
                'no': {'title': 'Vitenskap & Teknologi', 'description': 'Utforsk innovasjonens univers!'},
                'pl': {'title': 'Nauka i Technologia', 'description': 'Odkryj wszechświat innowacji!'},
                'id': {'title': 'Sains & Teknologi', 'description': 'Jelajahi alam semesta inovasi!'},
                'ja': {'title': '科学技術', 'description': 'イノベーションの宇宙を探索しよう!'},
                'ko': {'title': '과학 기술', 'description': '혁신의 우주를 탐험하세요!'},
                'th': {'title': 'วิทยาศาสตร์และเทคโนโลยี', 'description': 'สำรวจจักรวาลแห่งนวัตกรรม!'},
                'vi': {'title': 'Khoa học & Công nghệ', 'description': 'Khám phá vũ trụ của sự đổi mới!'},
            }
        },
        {
            'slug_base': 'games',
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485108/ChatGPT_Image_Oct_14_2025_05_59_40_PM_u2r5vg.png',
            'primary_color': '#f472b6',
            'secondary_color': '#ec4899',
            'icon_bg_color_1': '#fce7f3',
            'icon_bg_color_2': '#fbcfe8',
            'order': 5,
            'translations': {
                'en': {'title': 'Games', 'description': 'From classic to modern video games and board games!'},
                'pt': {'title': 'Jogos', 'description': 'Do clássico ao moderno! Videogames e jogos de tabuleiro!'},
                'es': {'title': 'Juegos', 'description': '¡De lo clásico a lo moderno! Videojuegos y juegos de mesa!'},
                'de': {'title': 'Spiele', 'description': 'Von klassisch bis modern! Videospiele und Brettspiele!'},
                'fr': {'title': 'Jeux', 'description': 'Du classique au moderne! Jeux vidéo et jeux de société!'},
                'it': {'title': 'Giochi', 'description': 'Dal classico al moderno! Videogiochi e giochi da tavolo!'},
                'nl': {'title': 'Games', 'description': 'Van klassiek tot modern! Videogames en bordspellen!'},
                'sv': {'title': 'Spel', 'description': 'Från klassiskt till modernt! Videospel och brädspel!'},
                'no': {'title': 'Spill', 'description': 'Fra klassisk til moderne! Videospill og brettspill!'},
                'pl': {'title': 'Gry', 'description': 'Od klasyki po nowoczesność! Gry wideo i planszowe!'},
                'id': {'title': 'Game', 'description': 'Dari klasik hingga modern! Video game dan board game!'},
                'ja': {'title': 'ゲーム', 'description': 'クラシックからモダンまで！ビデオゲームとボードゲーム!'},
                'ko': {'title': '게임', 'description': '클래식부터 현대까지! 비디오 게임과 보드 게임!'},
                'th': {'title': 'เกม', 'description': 'จากคลาสสิกถึงสมัยใหม่! วิดีโอเกมและบอร์ดเกม!'},
                'vi': {'title': 'Trò chơi', 'description': 'Từ cổ điển đến hiện đại! Video game và board game!'},
            }
        },
        {
            'slug_base': 'celebrities',
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485107/ChatGPT_Image_Oct_14_2025_08_13_11_PM_pgimb4.png',
            'primary_color': '#fcd34d',
            'secondary_color': '#fbbf24',
            'icon_bg_color_1': '#fef9c3',
            'icon_bg_color_2': '#fef08a',
            'order': 6,
            'translations': {
                'en': {'title': 'Celebrities & Personalities', 'description': 'Learn about entertainment icons and historical leaders!'},
                'pt': {'title': 'Celebridades & Personalidades', 'description': 'Conheça ícones do entretenimento e líderes históricos!'},
                'es': {'title': 'Celebridades y Personalidades', 'description': '¡Conoce íconos del entretenimiento y líderes históricos!'},
                'de': {'title': 'Prominente & Persönlichkeiten', 'description': 'Erfahren Sie mehr über Entertainment-Ikonen und historische Führer!'},
                'fr': {'title': 'Célébrités & Personnalités', 'description': 'Découvrez les icônes du divertissement et les leaders historiques!'},
                'it': {'title': 'Celebrità & Personalità', 'description': 'Scopri le icone dello spettacolo e i leader storici!'},
                'nl': {'title': 'Beroemdheden & Persoonlijkheden', 'description': 'Leer over entertainment iconen en historische leiders!'},
                'sv': {'title': 'Kändisar & Personligheter', 'description': 'Lär dig om underhållningsikoner och historiska ledare!'},
                'no': {'title': 'Kjendiser & Personligheter', 'description': 'Lær om underholdningsikoner og historiske ledere!'},
                'pl': {'title': 'Celebryci i Osobistości', 'description': 'Poznaj ikony rozrywki i historycznych przywódców!'},
                'id': {'title': 'Selebriti & Tokoh', 'description': 'Pelajari tentang ikon hiburan dan pemimpin bersejarah!'},
                'ja': {'title': 'セレブ＆著名人', 'description': 'エンターテインメントのアイコンと歴史的指導者について学ぼう!'},
                'ko': {'title': '유명인사', 'description': '엔터테인먼트 아이콘과 역사적 지도자에 대해 알아보세요!'},
                'th': {'title': 'คนดังและบุคคลสำคัญ', 'description': 'เรียนรู้เกี่ยวกับไอคอนบันเทิงและผู้นำประวัติศาสตร์!'},
                'vi': {'title': 'Người nổi tiếng', 'description': 'Tìm hiểu về các biểu tượng giải trí và nhà lãnh đạo lịch sử!'},
            }
        },
        {
            'slug_base': 'arts',
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,f_auto/v1760485103/ChatGPT_Image_Oct_14_2025_08_18_00_PM_ooloop.png',
            'primary_color': '#c084fc',
            'secondary_color': '#a855f7',
            'icon_bg_color_1': '#f3e8ff',
            'icon_bg_color_2': '#e9d5ff',
            'order': 7,
            'translations': {
                'en': {'title': 'Arts & Culture', 'description': 'Dive into the world of visual arts, music, and literature!'},
                'pt': {'title': 'Arte & Cultura', 'description': 'Mergulhe no mundo das artes visuais, música e literatura!'},
                'es': {'title': 'Arte y Cultura', 'description': '¡Sumérgete en el mundo de las artes visuales, música y literatura!'},
                'de': {'title': 'Kunst & Kultur', 'description': 'Tauchen Sie ein in die Welt der bildenden Künste, Musik und Literatur!'},
                'fr': {'title': 'Arts & Culture', 'description': 'Plongez dans le monde des arts visuels, de la musique et de la littérature!'},
                'it': {'title': 'Arte & Cultura', 'description': 'Immergiti nel mondo delle arti visive, musica e letteratura!'},
                'nl': {'title': 'Kunst & Cultuur', 'description': 'Duik in de wereld van beeldende kunst, muziek en literatuur!'},
                'sv': {'title': 'Konst & Kultur', 'description': 'Dyk in i världen av bildkonst, musik och litteratur!'},
                'no': {'title': 'Kunst & Kultur', 'description': 'Dykk ned i verden av billedkunst, musikk og litteratur!'},
                'pl': {'title': 'Sztuka i Kultura', 'description': 'Zanurz się w świecie sztuk wizualnych, muzyki i literatury!'},
                'id': {'title': 'Seni & Budaya', 'description': 'Selami dunia seni visual, musik, dan sastra!'},
                'ja': {'title': '芸術文化', 'description': '視覚芸術、音楽、文学の世界に飛び込もう!'},
                'ko': {'title': '예술 문화', 'description': '시각 예술, 음악, 문학의 세계로 뛰어들어보세요!'},
                'th': {'title': 'ศิลปะและวัฒนธรรม', 'description': 'ดำดิ่งสู่โลกของศิลปะภาพ ดนตรี และวรรณกรรม!'},
                'vi': {'title': 'Nghệ thuật & Văn hóa', 'description': 'Hòa mình vào thế giới nghệ thuật thị giác, âm nhạc và văn học!'},
            }
        },
        {
            'slug_base': 'history',
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485109/ChatGPT_Image_Oct_14_2025_05_59_34_PM_km9cdk.png',
            'primary_color': '#fbbf24',
            'secondary_color': '#f59e0b',
            'icon_bg_color_1': '#fef3c7',
            'icon_bg_color_2': '#fde68a',
            'order': 8,
            'translations': {
                'en': {'title': 'History', 'description': 'Travel through time through ancient civilizations and epic wars!'},
                'pt': {'title': 'História', 'description': 'Viaje no tempo através de civilizações antigas e guerras épicas!'},
                'es': {'title': 'Historia', 'description': '¡Viaja en el tiempo a través de civilizaciones antiguas y guerras épicas!'},
                'de': {'title': 'Geschichte', 'description': 'Reisen Sie durch die Zeit durch antike Zivilisationen und epische Kriege!'},
                'fr': {'title': 'Histoire', 'description': 'Voyagez dans le temps à travers les civilisations anciennes et les guerres épiques!'},
                'it': {'title': 'Storia', 'description': 'Viaggia nel tempo attraverso civiltà antiche e guerre epiche!'},
                'nl': {'title': 'Geschiedenis', 'description': 'Reis door de tijd door oude beschavingen en epische oorlogen!'},
                'sv': {'title': 'Historia', 'description': 'Res genom tiden genom antika civilisationer och episka krig!'},
                'no': {'title': 'Historie', 'description': 'Reis gjennom tiden gjennom antikke sivilisasjoner og episke kriger!'},
                'pl': {'title': 'Historia', 'description': 'Podróżuj w czasie przez starożytne cywilizacje i epickie wojny!'},
                'id': {'title': 'Sejarah', 'description': 'Jelajahi waktu melalui peradaban kuno dan perang epik!'},
                'ja': {'title': '歴史', 'description': '古代文明と壮大な戦争を通じて時間を旅しよう!'},
                'ko': {'title': '역사', 'description': '고대 문명과 장대한 전쟁을 통해 시간을 여행하세요!'},
                'th': {'title': 'ประวัติศาสตร์', 'description': 'เดินทางผ่านเวลาผ่านอารยธรรมโบราณและสงครามมหากาพย์!'},
                'vi': {'title': 'Lịch sử', 'description': 'Du hành thời gian qua các nền văn minh cổ đại và cuộc chiến sử thi!'},
            }
        },
        {
            'slug_base': 'food',
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485104/ChatGPT_Image_Oct_14_2025_08_17_14_PM_ghpv3w.png',
            'primary_color': '#fbbf24',
            'secondary_color': '#f59e0b',
            'icon_bg_color_1': '#fef3c7',
            'icon_bg_color_2': '#fde68a',
            'order': 9,
            'translations': {
                'en': {'title': 'Food & Drink', 'description': 'For food lovers! Famous recipes and world cuisine!'},
                'pt': {'title': 'Comida & Bebida', 'description': 'Para os amantes da gastronomia! Receitas famosas e culinária mundial!'},
                'es': {'title': 'Comida y Bebida', 'description': '¡Para los amantes de la gastronomía! ¡Recetas famosas y cocina mundial!'},
                'de': {'title': 'Essen & Trinken', 'description': 'Für Feinschmecker! Berühmte Rezepte und Weltküche!'},
                'fr': {'title': 'Nourriture & Boissons', 'description': 'Pour les amateurs de gastronomie! Recettes célèbres et cuisine mondiale!'},
                'it': {'title': 'Cibo & Bevande', 'description': 'Per gli amanti della gastronomia! Ricette famose e cucina mondiale!'},
                'nl': {'title': 'Eten & Drinken', 'description': 'Voor voedselliefhebbers! Beroemde recepten en wereldkeuken!'},
                'sv': {'title': 'Mat & Dryck', 'description': 'För matälskare! Berömda recept och världskök!'},
                'no': {'title': 'Mat & Drikke', 'description': 'For matentusiaster! Berømte oppskrifter og verdenskjøkken!'},
                'pl': {'title': 'Jedzenie i Napoje', 'description': 'Dla miłośników jedzenia! Słynne przepisy i kuchnia światowa!'},
                'id': {'title': 'Makanan & Minuman', 'description': 'Untuk pecinta kuliner! Resep terkenal dan masakan dunia!'},
                'ja': {'title': '料理飲料', 'description': '食通のために！有名なレシピと世界の料理!'},
                'ko': {'title': '음식 음료', 'description': '미식가를 위한! 유명한 레시피와 세계 요리!'},
                'th': {'title': 'อาหารและเครื่องดื่ม', 'description': 'สำหรับคนรักอาหาร! สูตรอาหารชื่อดังและอาหารนานาชาติ!'},
                'vi': {'title': 'Ẩm thực', 'description': 'Dành cho người yêu ẩm thực! Công thức nổi tiếng và ẩm thực thế giới!'},
            }
        },
        {
            'slug_base': 'nature',
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485105/ChatGPT_Image_Oct_14_2025_08_16_46_PM_tclomp.png',
            'primary_color': '#4ade80',
            'secondary_color': '#22c55e',
            'icon_bg_color_1': '#dcfce7',
            'icon_bg_color_2': '#bbf7d0',
            'order': 10,
            'translations': {
                'en': {'title': 'Nature & Animals', 'description': 'Explore the planet\'s biodiversity!'},
                'pt': {'title': 'Natureza & Animais', 'description': 'Explore a biodiversidade do planeta!'},
                'es': {'title': 'Naturaleza y Animales', 'description': '¡Explora la biodiversidad del planeta!'},
                'de': {'title': 'Natur & Tiere', 'description': 'Erkunden Sie die Biodiversität des Planeten!'},
                'fr': {'title': 'Nature & Animaux', 'description': 'Explorez la biodiversité de la planète!'},
                'it': {'title': 'Natura & Animali', 'description': 'Esplora la biodiversità del pianeta!'},
                'nl': {'title': 'Natuur & Dieren', 'description': 'Verken de biodiversiteit van de planeet!'},
                'sv': {'title': 'Natur & Djur', 'description': 'Utforska planetens biologiska mångfald!'},
                'no': {'title': 'Natur & Dyr', 'description': 'Utforsk planetens biodiversitet!'},
                'pl': {'title': 'Przyroda i Zwierzęta', 'description': 'Odkryj bioróżnorodność planety!'},
                'id': {'title': 'Alam & Hewan', 'description': 'Jelajahi keanekaragaman hayati planet!'},
                'ja': {'title': '自然動物', 'description': '地球の生物多様性を探検しよう!'},
                'ko': {'title': '자연 동물', 'description': '지구의 생물 다양성을 탐험하세요!'},
                'th': {'title': 'ธรรมชาติและสัตว์', 'description': 'สำรวจความหลากหลายทางชีวภาพของโลก!'},
                'vi': {'title': 'Thiên nhiên & Động vật', 'description': 'Khám phá đa dạng sinh học của hành tinh!'},
            }
        },
        {
            'slug_base': 'geography',
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485102/ChatGPT_Image_Oct_14_2025_08_19_00_PM_e99coh.png',
            'primary_color': '#60a5fa',
            'secondary_color': '#3b82f6',
            'icon_bg_color_1': '#dbeafe',
            'icon_bg_color_2': '#bfdbfe',
            'order': 11,
            'translations': {
                'en': {'title': 'Geography', 'description': 'Explore countries, capitals, and natural wonders!'},
                'pt': {'title': 'Geografia', 'description': 'Explore países, capitais e maravilhas naturais!'},
                'es': {'title': 'Geografía', 'description': '¡Explora países, capitales y maravillas naturales!'},
                'de': {'title': 'Geographie', 'description': 'Erkunden Sie Länder, Hauptstädte und Naturwunder!'},
                'fr': {'title': 'Géographie', 'description': 'Explorez les pays, capitales et merveilles naturelles!'},
                'it': {'title': 'Geografia', 'description': 'Esplora paesi, capitali e meraviglie naturali!'},
                'nl': {'title': 'Geografie', 'description': 'Verken landen, hoofdsteden en natuurwonderen!'},
                'sv': {'title': 'Geografi', 'description': 'Utforska länder, huvudstäder och naturunder!'},
                'no': {'title': 'Geografi', 'description': 'Utforsk land, hovedsteder og naturundere!'},
                'pl': {'title': 'Geografia', 'description': 'Odkryj kraje, stolice i cuda natury!'},
                'id': {'title': 'Geografi', 'description': 'Jelajahi negara, ibu kota, dan keajaiban alam!'},
                'ja': {'title': '地理', 'description': '国、首都、自然の驚異を探検しよう!'},
                'ko': {'title': '지리', 'description': '국가, 수도, 자연의 경이를 탐험하세요!'},
                'th': {'title': 'ภูมิศาสตร์', 'description': 'สำรวจประเทศ เมืองหลวง และความมหัศจรรย์ทางธรรมชาติ!'},
                'vi': {'title': 'Địa lý', 'description': 'Khám phá các quốc gia, thủ đô và kỳ quan thiên nhiên!'},
            }
        },
        {
            'slug_base': 'politics',
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485106/Symbols_of_Justice_and_Voice_frytbp.png',
            'primary_color': '#94a3b8',
            'secondary_color': '#64748b',
            'icon_bg_color_1': '#f1f5f9',
            'icon_bg_color_2': '#e2e8f0',
            'order': 12,
            'translations': {
                'en': {'title': 'Politics & Society', 'description': 'Understand political systems and social movements!'},
                'pt': {'title': 'Política & Sociedade', 'description': 'Entenda sistemas políticos e movimentos sociais!'},
                'es': {'title': 'Política y Sociedad', 'description': '¡Comprende los sistemas políticos y movimientos sociales!'},
                'de': {'title': 'Politik & Gesellschaft', 'description': 'Verstehen Sie politische Systeme und soziale Bewegungen!'},
                'fr': {'title': 'Politique & Société', 'description': 'Comprenez les systèmes politiques et les mouvements sociaux!'},
                'it': {'title': 'Politica & Società', 'description': 'Comprendi i sistemi politici e i movimenti sociali!'},
                'nl': {'title': 'Politiek & Maatschappij', 'description': 'Begrijp politieke systemen en sociale bewegingen!'},
                'sv': {'title': 'Politik & Samhälle', 'description': 'Förstå politiska system och sociala rörelser!'},
                'no': {'title': 'Politikk & Samfunn', 'description': 'Forstå politiske systemer og sosiale bevegelser!'},
                'pl': {'title': 'Polityka i Społeczeństwo', 'description': 'Zrozum systemy polityczne i ruchy społeczne!'},
                'id': {'title': 'Politik & Masyarakat', 'description': 'Pahami sistem politik dan gerakan sosial!'},
                'ja': {'title': '政治社会', 'description': '政治システムと社会運動を理解しよう!'},
                'ko': {'title': '정치 사회', 'description': '정치 시스템과 사회 운동을 이해하세요!'},
                'th': {'title': 'การเมืองและสังคม', 'description': 'เข้าใจระบบการเมืองและการเคลื่อนไหวทางสังคม!'},
                'vi': {'title': 'Chính trị & Xã hội', 'description': 'Hiểu về hệ thống chính trị và phong trào xã hội!'},
            }
        },
    ]
    
    # Mapeamento de países para idiomas
    country_to_lang = {
        'en-US': 'en', 'en-CA': 'en', 'en-GB': 'en', 'en-IN': 'en', 'en-PH': 'en', 'en-AU': 'en', 'en-NZ': 'en',
        'pt-BR': 'pt', 'pt-PT': 'pt',
        'es-MX': 'es', 'es-ES': 'es', 'es-AR': 'es', 'es-CO': 'es',
        'de-DE': 'de',
        'fr-FR': 'fr',
        'it-IT': 'it',
        'nl-NL': 'nl',
        'sv-SE': 'sv',
        'no-NO': 'no',
        'pl-PL': 'pl',
        'id-ID': 'id',
        'ja-JP': 'ja',
        'ko-KR': 'ko',
        'th-TH': 'th',
        'vi-VN': 'vi',
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
            
            theme, created = Theme.objects.update_or_create(
                slug=theme_base['slug_base'],
                country=country_code,
                defaults={
                    'title': translation['title'],
                    'description': translation['description'],
                    'icon': theme_base['icon'],
                    'primary_color': theme_base['primary_color'],
                    'secondary_color': theme_base['secondary_color'],
                    'icon_bg_color_1': theme_base['icon_bg_color_1'],
                    'icon_bg_color_2': theme_base['icon_bg_color_2'],
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
            print(f"{status} [{country_code}] {country_emoji} {theme.title}")
    
    print("-" * 80)
    print(f"✨ Processo concluído!")
    print(f"📊 Temas criados: {created_count}")
    print(f"🔄 Temas atualizados: {updated_count}")
    print(f"📈 Total processado: {created_count + updated_count}")
    print(f"🌍 Países configurados: {len(countries)}")
    print(f"🎯 Temas por país: {len(themes_base)}")

if __name__ == '__main__':
    create_root_themes()
