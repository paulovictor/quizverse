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
            'icon': 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,g_face,f_auto/v1760485101/ChatGPT_Image_Oct_14_2025_08_21_19_PM_u8jcah.png',
            'primary_color': '#34d399',
            'secondary_color': '#10b981',
            'order': 1,
            'translations': {
                'en': {'title': 'Sports', 'slug': 'sports', 'description': 'Test your knowledge about soccer, Olympics, world records and the greatest athletes in history!'},
                'pt': {'title': 'Esportes', 'slug': 'esportes', 'description': 'Teste seus conhecimentos sobre futebol, olimpíadas, recordes mundiais e os maiores atletas da história!'},
                'es': {'title': 'Deportes', 'slug': 'deportes', 'description': '¡Pon a prueba tus conocimientos sobre fútbol, olimpiadas, récords mundiales y los mejores atletas de la historia!'},
                'de': {'title': 'Sport', 'slug': 'sport', 'description': 'Testen Sie Ihr Wissen über Fußball, Olympische Spiele, Weltrekorde und die größten Athleten der Geschichte!'},
                'fr': {'title': 'Sports', 'slug': 'sports', 'description': 'Testez vos connaissances sur le football, les Jeux olympiques, les records mondiaux et les plus grands athlètes!'},
                'it': {'title': 'Sport', 'slug': 'sport', 'description': 'Metti alla prova le tue conoscenze su calcio, Olimpiadi, record mondiali e i più grandi atleti della storia!'},
                'nl': {'title': 'Sport', 'slug': 'sport', 'description': 'Test je kennis over voetbal, Olympische Spelen, wereldrecords en de grootste atleten uit de geschiedenis!'},
                'sv': {'title': 'Sport', 'slug': 'sport', 'description': 'Testa dina kunskaper om fotboll, OS, världsrekord och historiens största idrottare!'},
                'no': {'title': 'Sport', 'slug': 'sport', 'description': 'Test kunnskapen din om fotball, OL, verdensrekorder og historiens største idrettsutøvere!'},
                'pl': {'title': 'Sport', 'slug': 'sport', 'description': 'Przetestuj swoją wiedzę o piłce nożnej, Igrzyskach Olimpijskich, rekordach świata i największych sportowcach!'},
                'id': {'title': 'Olahraga', 'slug': 'olahraga', 'description': 'Uji pengetahuan Anda tentang sepak bola, Olimpiade, rekor dunia, dan atlet terhebat sepanjang masa!'},
                'ja': {'title': 'スポーツ', 'slug': 'supotsu', 'description': 'サッカー、オリンピック、世界記録、歴史上最高のアスリートについての知識をテストしよう!'},
                'ko': {'title': '스포츠', 'slug': 'seupocheu', 'description': '축구, 올림픽, 세계 기록, 역사상 최고의 운동선수에 대한 지식을 테스트하세요!'},
                'th': {'title': 'กีฬา', 'slug': 'kila', 'description': 'ทดสอบความรู้เกี่ยวกับฟุตบอล โอลิมปิก สถิติโลก และนักกีฬาที่ยิ่งใหญ่ที่สุดในประวัติศาสตร์!'},
                'vi': {'title': 'Thể thao', 'slug': 'the-thao', 'description': 'Kiểm tra kiến thức của bạn về bóng đá, Olympic, kỷ lục thế giới và những vận động viên vĩ đại nhất!'},
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
                'de': {'title': 'Unterhaltung & Medien', 'slug': 'unterhaltung', 'description': 'Tauchen Sie ein in die Welt von Kino, Serien, Musik und TV!'},
                'fr': {'title': 'Divertissement & Médias', 'slug': 'divertissement', 'description': 'Plongez dans l\'univers du cinéma, des séries, de la musique et de la TV!'},
                'it': {'title': 'Intrattenimento & Media', 'slug': 'intrattenimento', 'description': 'Immergiti nell\'universo del cinema, serie TV, musica e televisione!'},
                'nl': {'title': 'Entertainment & Media', 'slug': 'entertainment', 'description': 'Duik in het universum van cinema, series, muziek en TV!'},
                'sv': {'title': 'Underhållning & Media', 'slug': 'underhallning', 'description': 'Dyk in i världen av bio, serier, musik och TV!'},
                'no': {'title': 'Underholdning & Media', 'slug': 'underholdning', 'description': 'Dykk ned i universet av kino, serier, musikk og TV!'},
                'pl': {'title': 'Rozrywka i Media', 'slug': 'rozrywka', 'description': 'Zanurz się w świecie kina, seriali, muzyki i telewizji!'},
                'id': {'title': 'Hiburan & Media', 'slug': 'hiburan', 'description': 'Selami dunia sinema, serial, musik, dan TV!'},
                'ja': {'title': 'エンターテイメント', 'slug': 'entateinmento', 'description': '映画、シリーズ、音楽、テレビの世界に飛び込もう!'},
                'ko': {'title': '엔터테인먼트', 'slug': 'enteoteinmeonteu', 'description': '영화, 시리즈, 음악, TV의 세계로 뛰어들어보세요!'},
                'th': {'title': 'บันเทิง', 'slug': 'banthoeng', 'description': 'ดำดิ่งสู่จักรวาลของภาพยนตร์ ซีรีส์ เพลง และทีวี!'},
                'vi': {'title': 'Giải trí & Truyền thông', 'slug': 'giai-tri', 'description': 'Hòa mình vào vũ trụ điện ảnh, phim truyền hình, âm nhạc và TV!'},
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
                'de': {'title': 'Allgemeinwissen', 'slug': 'allgemeinwissen', 'description': 'Entdecken Sie überraschende Fakten über die Welt!'},
                'fr': {'title': 'Culture Générale', 'slug': 'culture-generale', 'description': 'Découvrez des faits surprenants sur le monde!'},
                'it': {'title': 'Curiosità Generali', 'slug': 'curiosita', 'description': 'Scopri fatti sorprendenti sul mondo!'},
                'nl': {'title': 'Algemene Kennis', 'slug': 'algemene-kennis', 'description': 'Ontdek verrassende feiten over de wereld!'},
                'sv': {'title': 'Allmänbildning', 'slug': 'allmanbildning', 'description': 'Upptäck överraskande fakta om världen!'},
                'no': {'title': 'Allmenankunnskap', 'slug': 'allmennkunnskap', 'description': 'Oppdag overraskende fakta om verden!'},
                'pl': {'title': 'Ciekawostki', 'slug': 'ciekawostki', 'description': 'Odkryj zaskakujące fakty o świecie!'},
                'id': {'title': 'Trivia Umum', 'slug': 'trivia-umum', 'description': 'Temukan fakta mengejutkan tentang dunia!'},
                'ja': {'title': '一般知識', 'slug': 'ippan-chishiki', 'description': '世界についての驚くべき事実を発見しよう!'},
                'ko': {'title': '일반 상식', 'slug': 'ilban-sangsik', 'description': '세상에 대한 놀라운 사실을 발견하세요!'},
                'th': {'title': 'ความรู้ทั่วไป', 'slug': 'khwam-ru-thuapai', 'description': 'ค้นพบข้อเท็จจริงที่น่าประหลาดใจเกี่ยวกับโลก!'},
                'vi': {'title': 'Kiến thức tổng hợp', 'slug': 'kien-thuc', 'description': 'Khám phá những sự thật đáng ngạc nhiên về thế giới!'},
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
                'de': {'title': 'Wissenschaft & Technologie', 'slug': 'wissenschaft', 'description': 'Erkunden Sie das Universum der Innovation!'},
                'fr': {'title': 'Science & Technologie', 'slug': 'science', 'description': 'Explorez l\'univers de l\'innovation!'},
                'it': {'title': 'Scienza & Tecnologia', 'slug': 'scienza', 'description': 'Esplora l\'universo dell\'innovazione!'},
                'nl': {'title': 'Wetenschap & Technologie', 'slug': 'wetenschap', 'description': 'Verken het universum van innovatie!'},
                'sv': {'title': 'Vetenskap & Teknologi', 'slug': 'vetenskap', 'description': 'Utforska innovationens universum!'},
                'no': {'title': 'Vitenskap & Teknologi', 'slug': 'vitenskap', 'description': 'Utforsk innovasjonens univers!'},
                'pl': {'title': 'Nauka i Technologia', 'slug': 'nauka', 'description': 'Odkryj wszechświat innowacji!'},
                'id': {'title': 'Sains & Teknologi', 'slug': 'sains', 'description': 'Jelajahi alam semesta inovasi!'},
                'ja': {'title': '科学技術', 'slug': 'kagaku', 'description': 'イノベーションの宇宙を探索しよう!'},
                'ko': {'title': '과학 기술', 'slug': 'gwahak', 'description': '혁신의 우주를 탐험하세요!'},
                'th': {'title': 'วิทยาศาสตร์และเทคโนโลยี', 'slug': 'wittayasat', 'description': 'สำรวจจักรวาลแห่งนวัตกรรม!'},
                'vi': {'title': 'Khoa học & Công nghệ', 'slug': 'khoa-hoc', 'description': 'Khám phá vũ trụ của sự đổi mới!'},
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
                'de': {'title': 'Spiele', 'slug': 'spiele', 'description': 'Von klassisch bis modern! Videospiele und Brettspiele!'},
                'fr': {'title': 'Jeux', 'slug': 'jeux', 'description': 'Du classique au moderne! Jeux vidéo et jeux de société!'},
                'it': {'title': 'Giochi', 'slug': 'giochi', 'description': 'Dal classico al moderno! Videogiochi e giochi da tavolo!'},
                'nl': {'title': 'Games', 'slug': 'games', 'description': 'Van klassiek tot modern! Videogames en bordspellen!'},
                'sv': {'title': 'Spel', 'slug': 'spel', 'description': 'Från klassiskt till modernt! Videospel och brädspel!'},
                'no': {'title': 'Spill', 'slug': 'spill', 'description': 'Fra klassisk til moderne! Videospill og brettspill!'},
                'pl': {'title': 'Gry', 'slug': 'gry', 'description': 'Od klasyki po nowoczesność! Gry wideo i planszowe!'},
                'id': {'title': 'Game', 'slug': 'game', 'description': 'Dari klasik hingga modern! Video game dan board game!'},
                'ja': {'title': 'ゲーム', 'slug': 'gemu', 'description': 'クラシックからモダンまで！ビデオゲームとボードゲーム!'},
                'ko': {'title': '게임', 'slug': 'geim', 'description': '클래식부터 현대까지! 비디오 게임과 보드 게임!'},
                'th': {'title': 'เกม', 'slug': 'gem', 'description': 'จากคลาสสิกถึงสมัยใหม่! วิดีโอเกมและบอร์ดเกม!'},
                'vi': {'title': 'Trò chơi', 'slug': 'tro-choi', 'description': 'Từ cổ điển đến hiện đại! Video game và board game!'},
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
                'de': {'title': 'Prominente & Persönlichkeiten', 'slug': 'prominente', 'description': 'Erfahren Sie mehr über Entertainment-Ikonen und historische Führer!'},
                'fr': {'title': 'Célébrités & Personnalités', 'slug': 'celebrites', 'description': 'Découvrez les icônes du divertissement et les leaders historiques!'},
                'it': {'title': 'Celebrità & Personalità', 'slug': 'celebrita', 'description': 'Scopri le icone dello spettacolo e i leader storici!'},
                'nl': {'title': 'Beroemdheden & Persoonlijkheden', 'slug': 'beroemdheden', 'description': 'Leer over entertainment iconen en historische leiders!'},
                'sv': {'title': 'Kändisar & Personligheter', 'slug': 'kandisar', 'description': 'Lär dig om underhållningsikoner och historiska ledare!'},
                'no': {'title': 'Kjendiser & Personligheter', 'slug': 'kjendiser', 'description': 'Lær om underholdningsikoner og historiske ledere!'},
                'pl': {'title': 'Celebryci i Osobistości', 'slug': 'celebryci', 'description': 'Poznaj ikony rozrywki i historycznych przywódców!'},
                'id': {'title': 'Selebriti & Tokoh', 'slug': 'selebriti', 'description': 'Pelajari tentang ikon hiburan dan pemimpin bersejarah!'},
                'ja': {'title': 'セレブ＆著名人', 'slug': 'serebu', 'description': 'エンターテインメントのアイコンと歴史的指導者について学ぼう!'},
                'ko': {'title': '유명인사', 'slug': 'yumyeong-insa', 'description': '엔터테인먼트 아이콘과 역사적 지도자에 대해 알아보세요!'},
                'th': {'title': 'คนดังและบุคคลสำคัญ', 'slug': 'khondang', 'description': 'เรียนรู้เกี่ยวกับไอคอนบันเทิงและผู้นำประวัติศาสตร์!'},
                'vi': {'title': 'Người nổi tiếng', 'slug': 'nguoi-noi-tieng', 'description': 'Tìm hiểu về các biểu tượng giải trí và nhà lãnh đạo lịch sử!'},
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
                'de': {'title': 'Kunst & Kultur', 'slug': 'kunst', 'description': 'Tauchen Sie ein in die Welt der bildenden Künste, Musik und Literatur!'},
                'fr': {'title': 'Arts & Culture', 'slug': 'arts', 'description': 'Plongez dans le monde des arts visuels, de la musique et de la littérature!'},
                'it': {'title': 'Arte & Cultura', 'slug': 'arte', 'description': 'Immergiti nel mondo delle arti visive, musica e letteratura!'},
                'nl': {'title': 'Kunst & Cultuur', 'slug': 'kunst', 'description': 'Duik in de wereld van beeldende kunst, muziek en literatuur!'},
                'sv': {'title': 'Konst & Kultur', 'slug': 'konst', 'description': 'Dyk in i världen av bildkonst, musik och litteratur!'},
                'no': {'title': 'Kunst & Kultur', 'slug': 'kunst', 'description': 'Dykk ned i verden av billedkunst, musikk og litteratur!'},
                'pl': {'title': 'Sztuka i Kultura', 'slug': 'sztuka', 'description': 'Zanurz się w świecie sztuk wizualnych, muzyki i literatury!'},
                'id': {'title': 'Seni & Budaya', 'slug': 'seni', 'description': 'Selami dunia seni visual, musik, dan sastra!'},
                'ja': {'title': '芸術文化', 'slug': 'geijutsu', 'description': '視覚芸術、音楽、文学の世界に飛び込もう!'},
                'ko': {'title': '예술 문화', 'slug': 'yesul', 'description': '시각 예술, 음악, 문학의 세계로 뛰어들어보세요!'},
                'th': {'title': 'ศิลปะและวัฒนธรรม', 'slug': 'sinlapa', 'description': 'ดำดิ่งสู่โลกของศิลปะภาพ ดนตรี และวรรณกรรม!'},
                'vi': {'title': 'Nghệ thuật & Văn hóa', 'slug': 'nghe-thuat', 'description': 'Hòa mình vào thế giới nghệ thuật thị giác, âm nhạc và văn học!'},
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
                'de': {'title': 'Geschichte', 'slug': 'geschichte', 'description': 'Reisen Sie durch die Zeit durch antike Zivilisationen und epische Kriege!'},
                'fr': {'title': 'Histoire', 'slug': 'histoire', 'description': 'Voyagez dans le temps à travers les civilisations anciennes et les guerres épiques!'},
                'it': {'title': 'Storia', 'slug': 'storia', 'description': 'Viaggia nel tempo attraverso civiltà antiche e guerre epiche!'},
                'nl': {'title': 'Geschiedenis', 'slug': 'geschiedenis', 'description': 'Reis door de tijd door oude beschavingen en epische oorlogen!'},
                'sv': {'title': 'Historia', 'slug': 'historia', 'description': 'Res genom tiden genom antika civilisationer och episka krig!'},
                'no': {'title': 'Historie', 'slug': 'historie', 'description': 'Reis gjennom tiden gjennom antikke sivilisasjoner og episke kriger!'},
                'pl': {'title': 'Historia', 'slug': 'historia', 'description': 'Podróżuj w czasie przez starożytne cywilizacje i epickie wojny!'},
                'id': {'title': 'Sejarah', 'slug': 'sejarah', 'description': 'Jelajahi waktu melalui peradaban kuno dan perang epik!'},
                'ja': {'title': '歴史', 'slug': 'rekishi', 'description': '古代文明と壮大な戦争を通じて時間を旅しよう!'},
                'ko': {'title': '역사', 'slug': 'yeoksa', 'description': '고대 문명과 장대한 전쟁을 통해 시간을 여행하세요!'},
                'th': {'title': 'ประวัติศาสตร์', 'slug': 'prawatisat', 'description': 'เดินทางผ่านเวลาผ่านอารยธรรมโบราณและสงครามมหากาพย์!'},
                'vi': {'title': 'Lịch sử', 'slug': 'lich-su', 'description': 'Du hành thời gian qua các nền văn minh cổ đại và cuộc chiến sử thi!'},
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
                'de': {'title': 'Essen & Trinken', 'slug': 'essen', 'description': 'Für Feinschmecker! Berühmte Rezepte und Weltküche!'},
                'fr': {'title': 'Nourriture & Boissons', 'slug': 'nourriture', 'description': 'Pour les amateurs de gastronomie! Recettes célèbres et cuisine mondiale!'},
                'it': {'title': 'Cibo & Bevande', 'slug': 'cibo', 'description': 'Per gli amanti della gastronomia! Ricette famose e cucina mondiale!'},
                'nl': {'title': 'Eten & Drinken', 'slug': 'eten', 'description': 'Voor voedselliefhebbers! Beroemde recepten en wereldkeuken!'},
                'sv': {'title': 'Mat & Dryck', 'slug': 'mat', 'description': 'För matälskare! Berömda recept och världskök!'},
                'no': {'title': 'Mat & Drikke', 'slug': 'mat', 'description': 'For matentusiaster! Berømte oppskrifter og verdenskjøkken!'},
                'pl': {'title': 'Jedzenie i Napoje', 'slug': 'jedzenie', 'description': 'Dla miłośników jedzenia! Słynne przepisy i kuchnia światowa!'},
                'id': {'title': 'Makanan & Minuman', 'slug': 'makanan', 'description': 'Untuk pecinta kuliner! Resep terkenal dan masakan dunia!'},
                'ja': {'title': '料理飲料', 'slug': 'ryori', 'description': '食通のために！有名なレシピと世界の料理!'},
                'ko': {'title': '음식 음료', 'slug': 'eumsik', 'description': '미식가를 위한! 유명한 레시피와 세계 요리!'},
                'th': {'title': 'อาหารและเครื่องดื่ม', 'slug': 'ahan', 'description': 'สำหรับคนรักอาหาร! สูตรอาหารชื่อดังและอาหารนานาชาติ!'},
                'vi': {'title': 'Ẩm thực', 'slug': 'am-thuc', 'description': 'Dành cho người yêu ẩm thực! Công thức nổi tiếng và ẩm thực thế giới!'},
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
                'de': {'title': 'Natur & Tiere', 'slug': 'natur', 'description': 'Erkunden Sie die Biodiversität des Planeten!'},
                'fr': {'title': 'Nature & Animaux', 'slug': 'nature', 'description': 'Explorez la biodiversité de la planète!'},
                'it': {'title': 'Natura & Animali', 'slug': 'natura', 'description': 'Esplora la biodiversità del pianeta!'},
                'nl': {'title': 'Natuur & Dieren', 'slug': 'natuur', 'description': 'Verken de biodiversiteit van de planeet!'},
                'sv': {'title': 'Natur & Djur', 'slug': 'natur', 'description': 'Utforska planetens biologiska mångfald!'},
                'no': {'title': 'Natur & Dyr', 'slug': 'natur', 'description': 'Utforsk planetens biodiversitet!'},
                'pl': {'title': 'Przyroda i Zwierzęta', 'slug': 'przyroda', 'description': 'Odkryj bioróżnorodność planety!'},
                'id': {'title': 'Alam & Hewan', 'slug': 'alam', 'description': 'Jelajahi keanekaragaman hayati planet!'},
                'ja': {'title': '自然動物', 'slug': 'shizen', 'description': '地球の生物多様性を探検しよう!'},
                'ko': {'title': '자연 동물', 'slug': 'jayeon', 'description': '지구의 생물 다양성을 탐험하세요!'},
                'th': {'title': 'ธรรมชาติและสัตว์', 'slug': 'thammachat', 'description': 'สำรวจความหลากหลายทางชีวภาพของโลก!'},
                'vi': {'title': 'Thiên nhiên & Động vật', 'slug': 'thien-nhien', 'description': 'Khám phá đa dạng sinh học của hành tinh!'},
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
                'de': {'title': 'Geographie', 'slug': 'geographie', 'description': 'Erkunden Sie Länder, Hauptstädte und Naturwunder!'},
                'fr': {'title': 'Géographie', 'slug': 'geographie', 'description': 'Explorez les pays, capitales et merveilles naturelles!'},
                'it': {'title': 'Geografia', 'slug': 'geografia', 'description': 'Esplora paesi, capitali e meraviglie naturali!'},
                'nl': {'title': 'Geografie', 'slug': 'geografie', 'description': 'Verken landen, hoofdsteden en natuurwonderen!'},
                'sv': {'title': 'Geografi', 'slug': 'geografi', 'description': 'Utforska länder, huvudstäder och naturunder!'},
                'no': {'title': 'Geografi', 'slug': 'geografi', 'description': 'Utforsk land, hovedsteder og naturundere!'},
                'pl': {'title': 'Geografia', 'slug': 'geografia', 'description': 'Odkryj kraje, stolice i cuda natury!'},
                'id': {'title': 'Geografi', 'slug': 'geografi', 'description': 'Jelajahi negara, ibu kota, dan keajaiban alam!'},
                'ja': {'title': '地理', 'slug': 'chiri', 'description': '国、首都、自然の驚異を探検しよう!'},
                'ko': {'title': '지리', 'slug': 'jiri', 'description': '국가, 수도, 자연의 경이를 탐험하세요!'},
                'th': {'title': 'ภูมิศาสตร์', 'slug': 'phumisat', 'description': 'สำรวจประเทศ เมืองหลวง และความมหัศจรรย์ทางธรรมชาติ!'},
                'vi': {'title': 'Địa lý', 'slug': 'dia-ly', 'description': 'Khám phá các quốc gia, thủ đô và kỳ quan thiên nhiên!'},
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
                'de': {'title': 'Politik & Gesellschaft', 'slug': 'politik', 'description': 'Verstehen Sie politische Systeme und soziale Bewegungen!'},
                'fr': {'title': 'Politique & Société', 'slug': 'politique', 'description': 'Comprenez les systèmes politiques et les mouvements sociaux!'},
                'it': {'title': 'Politica & Società', 'slug': 'politica', 'description': 'Comprendi i sistemi politici e i movimenti sociali!'},
                'nl': {'title': 'Politiek & Maatschappij', 'slug': 'politiek', 'description': 'Begrijp politieke systemen en sociale bewegingen!'},
                'sv': {'title': 'Politik & Samhälle', 'slug': 'politik', 'description': 'Förstå politiska system och sociala rörelser!'},
                'no': {'title': 'Politikk & Samfunn', 'slug': 'politikk', 'description': 'Forstå politiske systemer og sosiale bevegelser!'},
                'pl': {'title': 'Polityka i Społeczeństwo', 'slug': 'polityka', 'description': 'Zrozum systemy polityczne i ruchy społeczne!'},
                'id': {'title': 'Politik & Masyarakat', 'slug': 'politik', 'description': 'Pahami sistem politik dan gerakan sosial!'},
                'ja': {'title': '政治社会', 'slug': 'seiji', 'description': '政治システムと社会運動を理解しよう!'},
                'ko': {'title': '정치 사회', 'slug': 'jeongchi', 'description': '정치 시스템과 사회 운동을 이해하세요!'},
                'th': {'title': 'การเมืองและสังคม', 'slug': 'kanmueang', 'description': 'เข้าใจระบบการเมืองและการเคลื่อนไหวทางสังคม!'},
                'vi': {'title': 'Chính trị & Xã hội', 'slug': 'chinh-tri', 'description': 'Hiểu về hệ thống chính trị và phong trào xã hội!'},
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
