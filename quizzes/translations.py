# quizzes/translations.py
"""
Sistema de tradução simples para o Quizverso
Cada chave tem traduções para os 15 idiomas suportados:
- pt-BR/pt (Português)
- en (English)
- es (Español)
- fr (Français)
- de (Deutsch)
- it (Italiano)
- nl (Nederlands)
- sv (Svenska)
- no (Norsk)
- pl (Polski)
- id (Bahasa Indonesia)
- ja (日本語)
- ko (한국어)
- th (ไทย)
- vi (Tiếng Việt)
"""

TRANSLATIONS = {
    # Header & Navigation
    'site_name': {
        'pt-BR': 'Quizverso', 'en': 'Quizverso', 'es': 'Quizverso', 'fr': 'Quizverso', 'de': 'Quizverso', 'it': 'Quizverso',
        'nl': 'Quizverso', 'sv': 'Quizverso', 'no': 'Quizverso', 'pl': 'Quizverso', 'id': 'Quizverso',
        'ja': 'Quizverso', 'ko': 'Quizverso', 'th': 'Quizverso', 'vi': 'Quizverso',
    },
    'hello': {
        'pt-BR': 'Olá', 'en': 'Hello', 'es': 'Hola', 'fr': 'Bonjour', 'de': 'Hallo', 'it': 'Ciao',
        'nl': 'Hallo', 'sv': 'Hej', 'no': 'Hei', 'pl': 'Cześć', 'id': 'Halo',
        'ja': 'こんにちは', 'ko': '안녕하세요', 'th': 'สวัสดี', 'vi': 'Xin chào',
    },
    'my_profile': {
        'pt-BR': 'Meu Perfil', 'en': 'My Profile', 'es': 'Mi Perfil', 'fr': 'Mon Profil', 'de': 'Mein Profil', 'it': 'Il mio Profilo',
        'nl': 'Mijn Profiel', 'sv': 'Min Profil', 'no': 'Min Profil', 'pl': 'Mój Profil', 'id': 'Profil Saya',
        'ja': 'マイプロフィール', 'ko': '내 프로필', 'th': 'โปรไฟล์ของฉัน', 'vi': 'Hồ sơ của tôi',
    },
    'logout': {
        'pt-BR': 'Sair', 'en': 'Logout', 'es': 'Cerrar sesión', 'fr': 'Déconnexion', 'de': 'Abmelden', 'it': 'Esci',
        'nl': 'Uitloggen', 'sv': 'Logga ut', 'no': 'Logg ut', 'pl': 'Wyloguj', 'id': 'Keluar',
        'ja': 'ログアウト', 'ko': '로그아웃', 'th': 'ออกจากระบบ', 'vi': 'Đăng xuất',
    },
    'login': {
        'pt-BR': 'Entrar', 'en': 'Login', 'es': 'Iniciar sesión', 'fr': 'Connexion', 'de': 'Anmelden', 'it': 'Accedi',
        'nl': 'Inloggen', 'sv': 'Logga in', 'no': 'Logg inn', 'pl': 'Zaloguj', 'id': 'Masuk',
        'ja': 'ログイン', 'ko': '로그인', 'th': 'เข้าสู่ระบบ', 'vi': 'Đăng nhập',
    },
    'create_account': {
        'pt-BR': 'Criar conta', 'en': 'Sign up', 'es': 'Crear cuenta', 'fr': 'Créer un compte', 'de': 'Konto erstellen', 'it': 'Crea account',
        'nl': 'Account aanmaken', 'sv': 'Skapa konto', 'no': 'Opprett konto', 'pl': 'Utwórz konto', 'id': 'Buat akun',
        'ja': 'アカウント作成', 'ko': '계정 만들기', 'th': 'สร้างบัญชี', 'vi': 'Tạo tài khoản',
    },
    
    # Home Page & Navigation
    'home': {
        'pt-BR': 'Início', 'en': 'Home', 'es': 'Inicio', 'fr': 'Accueil', 'de': 'Startseite', 'it': 'Home',
        'nl': 'Home', 'sv': 'Hem', 'no': 'Hjem', 'pl': 'Strona główna', 'id': 'Beranda',
        'ja': 'ホーム', 'ko': '홈', 'th': 'หน้าแรก', 'vi': 'Trang chủ',
    },
    'explore_by_category': {
        'pt-BR': 'Explorar por Categoria', 'en': 'Explore by Category', 'es': 'Explorar por Categoría', 'fr': 'Explorer par Catégorie', 'de': 'Nach Kategorie erkunden', 'it': 'Esplora per Categoria',
        'nl': 'Verkennen per Categorie', 'sv': 'Utforska efter Kategori', 'no': 'Utforsk etter Kategori', 'pl': 'Przeglądaj według Kategorii', 'id': 'Jelajahi berdasarkan Kategori',
        'ja': 'カテゴリーで探す', 'ko': '카테고리별 탐색', 'th': 'สำรวจตามหมวดหมู่', 'vi': 'Khám phá theo Danh mục',
    },
    'items': {
        'pt-BR': 'Itens', 'en': 'Items', 'es': 'Artículos', 'fr': 'Éléments', 'de': 'Artikel', 'it': 'Articoli',
        'nl': 'Items', 'sv': 'Objekt', 'no': 'Elementer', 'pl': 'Elementy', 'id': 'Item',
        'ja': 'アイテム', 'ko': '항목', 'th': 'รายการ', 'vi': 'Mục',
    },
    'play': {
        'pt-BR': 'Jogar', 'en': 'Play', 'es': 'Jugar', 'fr': 'Jouer', 'de': 'Spielen', 'it': 'Gioca',
        'nl': 'Spelen', 'sv': 'Spela', 'no': 'Spill', 'pl': 'Graj', 'id': 'Main',
        'ja': 'プレイ', 'ko': '플레이', 'th': 'เล่น', 'vi': 'Chơi',
    },
    'play_again': {
        'pt-BR': 'Jogar novamente', 'en': 'Play again', 'es': 'Jugar de nuevo', 'fr': 'Rejouer', 'de': 'Nochmal spielen', 'it': 'Gioca di nuovo',
        'nl': 'Opnieuw spelen', 'sv': 'Spela igen', 'no': 'Spill igjen', 'pl': 'Zagraj ponownie', 'id': 'Main lagi',
        'ja': 'もう一度プレイ', 'ko': '다시 플레이', 'th': 'เล่นอีกครั้ง', 'vi': 'Chơi lại',
    },
    'more_quizzes': {
        'pt-BR': 'Mais quizzes', 'en': 'More quizzes', 'es': 'Más quizzes', 'fr': 'Plus de quiz', 'de': 'Mehr Quiz', 'it': 'Altri quiz',
        'nl': 'Meer quizzen', 'sv': 'Fler frågesporter', 'no': 'Flere quizer', 'pl': 'Więcej quizów', 'id': 'Kuis lainnya',
        'ja': 'もっとクイズ', 'ko': '더 많은 퀴즈', 'th': 'แบบทดสอบเพิ่มเติม', 'vi': 'Thêm câu đố',
    },
    'welcome_title': {
        'pt-BR': 'Desafie seus conhecimentos', 'en': 'Challenge your knowledge', 'es': 'Desafía tus conocimientos', 
        'fr': 'Défiez vos connaissances', 'de': 'Fordern Sie Ihr Wissen heraus', 'it': 'Sfida le tue conoscenze',
        'nl': 'Daag je kennis uit', 'sv': 'Utmana din kunskap', 'no': 'Utfordre kunnskapen din', 'pl': 'Sprawdź swoją wiedzę', 'id': 'Tantang pengetahuan Anda',
        'ja': 'あなたの知識に挑戦', 'ko': '지식에 도전하세요', 'th': 'ท้าทายความรู้ของคุณ', 'vi': 'Thách thức kiến thức của bạn',
    },
    'welcome_subtitle': {
        'pt-BR': 'Explore milhares de quizzes em diversas categorias', 'en': 'Explore thousands of quizzes in various categories', 
        'es': 'Explora miles de quizzes en diversas categorías', 'fr': 'Explorez des milliers de quiz dans diverses catégories', 
        'de': 'Erkunden Sie Tausende von Quiz in verschiedenen Kategorien', 'it': 'Esplora migliaia di quiz in diverse categorie',
        'nl': 'Ontdek duizenden quizzen in verschillende categorieën', 'sv': 'Utforska tusentals frågesporter i olika kategorier', 
        'no': 'Utforsk tusenvis av quizer i forskjellige kategorier', 'pl': 'Odkryj tysiące quizów w różnych kategoriach', 
        'id': 'Jelajahi ribuan kuis dalam berbagai kategori',
        'ja': '様々なカテゴリーの何千ものクイズを探索', 'ko': '다양한 카테고리의 수천 개 퀴즈 탐색', 
        'th': 'สำรวจแบบทดสอบหลายพันรายการในหมวดหมู่ต่างๆ', 'vi': 'Khám phá hàng nghìn câu đố trong nhiều danh mục',
    },
    'choose_category': {
        'pt-BR': 'Escolha sua Categoria', 'en': 'Choose your Category', 'es': 'Elige tu Categoría', 'fr': 'Choisissez votre catégorie', 
        'de': 'Wählen Sie Ihre Kategorie', 'it': 'Scegli la tua Categoria',
        'nl': 'Kies je Categorie', 'sv': 'Välj din Kategori', 'no': 'Velg din Kategori', 'pl': 'Wybierz swoją Kategorię', 'id': 'Pilih Kategori Anda',
        'ja': 'カテゴリーを選択', 'ko': '카테고리 선택', 'th': 'เลือกหมวดหมู่ของคุณ', 'vi': 'Chọn Danh mục của bạn',
    },
    'categories_subtitle': {
        'pt-BR': 'Selecione um tema para começar', 'en': 'Select a theme to get started', 'es': 'Selecciona un tema para comenzar', 
        'fr': 'Sélectionnez un thème pour commencer', 'de': 'Wählen Sie ein Thema zum Starten', 'it': 'Seleziona un tema per iniziare',
        'nl': 'Selecteer een thema om te beginnen', 'sv': 'Välj ett tema för att komma igång', 'no': 'Velg et tema for å komme i gang', 
        'pl': 'Wybierz temat, aby rozpocząć', 'id': 'Pilih tema untuk memulai',
        'ja': '開始するテーマを選択', 'ko': '시작할 테마 선택', 'th': 'เลือกธีมเพื่อเริ่มต้น', 'vi': 'Chọn chủ đề để bắt đầu',
    },
    
    # Stats
    'total_themes': {
        'pt-BR': 'temas', 'en': 'themes', 'es': 'temas', 'fr': 'thèmes', 'de': 'Themen', 'it': 'temi',
        'nl': 'thema\'s', 'sv': 'teman', 'no': 'temaer', 'pl': 'tematy', 'id': 'tema',
        'ja': 'テーマ', 'ko': '테마', 'th': 'ธีม', 'vi': 'chủ đề',
    },
    'total_quizzes': {
        'pt-BR': 'quizzes', 'en': 'quizzes', 'es': 'quizzes', 'fr': 'quiz', 'de': 'Quiz', 'it': 'quiz',
        'nl': 'quizzen', 'sv': 'frågesporter', 'no': 'quizer', 'pl': 'quizy', 'id': 'kuis',
        'ja': 'クイズ', 'ko': '퀴즈', 'th': 'แบบทดสอบ', 'vi': 'câu đố',
    },
    'total_questions': {
        'pt-BR': 'questões', 'en': 'questions', 'es': 'preguntas', 'fr': 'questions', 'de': 'Fragen', 'it': 'domande',
        'nl': 'vragen', 'sv': 'frågor', 'no': 'spørsmål', 'pl': 'pytania', 'id': 'pertanyaan',
        'ja': '質問', 'ko': '질문', 'th': 'คำถาม', 'vi': 'câu hỏi',
    },
    'subcategories': {
        'pt-BR': 'subcategorias', 'en': 'subcategories', 'es': 'subcategorías', 'fr': 'sous-catégories', 'de': 'Unterkategorien', 'it': 'sottocategorie',
        'nl': 'subcategorieën', 'sv': 'underkategorier', 'no': 'underkategorier', 'pl': 'podkategorie', 'id': 'subkategori',
        'ja': 'サブカテゴリー', 'ko': '하위 카테고리', 'th': 'หมวดหมู่ย่อย', 'vi': 'danh mục con',
    },
    
    # Quiz Detail
    'questions_label': {
        'pt-BR': 'Questões', 'en': 'Questions', 'es': 'Preguntas', 'fr': 'Questions', 'de': 'Fragen', 'it': 'Domande',
        'nl': 'Vragen', 'sv': 'Frågor', 'no': 'Spørsmål', 'pl': 'Pytania', 'id': 'Pertanyaan',
        'ja': '質問数', 'ko': '질문 수', 'th': 'คำถาม', 'vi': 'Câu hỏi',
    },
    'questions': {
        'pt-BR': 'questões', 'en': 'questions', 'es': 'preguntas', 'fr': 'questions', 'de': 'Fragen', 'it': 'domande',
        'nl': 'vragen', 'sv': 'frågor', 'no': 'spørsmål', 'pl': 'pytania', 'id': 'pertanyaan',
        'ja': '質問', 'ko': '質問', 'th': 'คำถาม', 'vi': 'câu hỏi',
    },
    'estimated_time_label': {
        'pt-BR': 'Tempo estimado', 'en': 'Estimated time', 'es': 'Tiempo estimado', 'fr': 'Temps estimé', 'de': 'Geschätzte Zeit', 'it': 'Tempo stimato',
        'nl': 'Geschatte tijd', 'sv': 'Uppskattad tid', 'no': 'Estimert tid', 'pl': 'Szacowany czas', 'id': 'Perkiraan waktu',
        'ja': '所要時間', 'ko': '예상 시간', 'th': 'เวลาโดยประมาณ', 'vi': 'Thời gian ước tính',
    },
    'estimated_time': {
        'pt-BR': 'min', 'en': 'min', 'es': 'min', 'fr': 'min', 'de': 'Min', 'it': 'min',
        'nl': 'min', 'sv': 'min', 'no': 'min', 'pl': 'min', 'id': 'mnt',
        'ja': '分', 'ko': '분', 'th': 'นาที', 'vi': 'phút',
    },
    'difficulty_label': {
        'pt-BR': 'Dificuldade', 'en': 'Difficulty', 'es': 'Dificultad', 'fr': 'Difficulté', 'de': 'Schwierigkeit', 'it': 'Difficoltà',
        'nl': 'Moeilijkheidsgraad', 'sv': 'Svårighetsgrad', 'no': 'Vanskelighetsgrad', 'pl': 'Trudność', 'id': 'Kesulitan',
        'ja': '難易度', 'ko': '난이도', 'th': 'ความยาก', 'vi': 'Độ khó',
    },
    'difficulty': {
        'pt-BR': 'Dificuldade', 'en': 'Difficulty', 'es': 'Dificultad', 'fr': 'Difficulté', 'de': 'Schwierigkeit', 'it': 'Difficoltà',
        'nl': 'Moeilijkheidsgraad', 'sv': 'Svårighetsgrad', 'no': 'Vanskelighetsgrad', 'pl': 'Trudność', 'id': 'Kesulitan',
        'ja': '難易度', 'ko': '난이도', 'th': 'ความยาก', 'vi': 'Độ khó',
    },
    'easy': {
        'pt-BR': 'Fácil', 'en': 'Easy', 'es': 'Fácil', 'fr': 'Facile', 'de': 'Einfach', 'it': 'Facile',
        'nl': 'Gemakkelijk', 'sv': 'Lätt', 'no': 'Lett', 'pl': 'Łatwy', 'id': 'Mudah',
        'ja': '簡単', 'ko': '쉬움', 'th': 'ง่าย', 'vi': 'Dễ',
    },
    'medium': {
        'pt-BR': 'Médio', 'en': 'Medium', 'es': 'Medio', 'fr': 'Moyen', 'de': 'Mittel', 'it': 'Medio',
        'nl': 'Gemiddeld', 'sv': 'Medel', 'no': 'Middels', 'pl': 'Średni', 'id': 'Sedang',
        'ja': '普通', 'ko': '보통', 'th': 'ปานกลาง', 'vi': 'Trung bình',
    },
    'hard': {
        'pt-BR': 'Difícil', 'en': 'Hard', 'es': 'Difícil', 'fr': 'Difficile', 'de': 'Schwer', 'it': 'Difficile',
        'nl': 'Moeilijk', 'sv': 'Svår', 'no': 'Vanskelig', 'pl': 'Trudny', 'id': 'Sulit',
        'ja': '難しい', 'ko': '어려움', 'th': 'ยาก', 'vi': 'Khó',
    },
    'start_quiz': {
        'pt-BR': 'Iniciar Quiz', 'en': 'Start Quiz', 'es': 'Iniciar Quiz', 'fr': 'Commencer le Quiz', 'de': 'Quiz starten', 'it': 'Inizia Quiz',
        'nl': 'Quiz starten', 'sv': 'Starta Quiz', 'no': 'Start Quiz', 'pl': 'Rozpocznij Quiz', 'id': 'Mulai Kuis',
        'ja': 'クイズ開始', 'ko': '퀴즈 시작', 'th': 'เริ่มแบบทดสอบ', 'vi': 'Bắt đầu Câu đố',
    },
    'your_previous_attempts': {
        'pt-BR': 'Suas Tentativas Anteriores', 'en': 'Your Previous Attempts', 'es': 'Tus Intentos Anteriores', 'fr': 'Vos Tentatives Précédentes', 'de': 'Ihre vorherigen Versuche', 'it': 'I tuoi Tentativi Precedenti',
        'nl': 'Jouw Eerdere Pogingen', 'sv': 'Dina Tidigare Försök', 'no': 'Dine Tidligere Forsøk', 'pl': 'Twoje Poprzednie Próby', 'id': 'Percobaan Sebelumnya',
        'ja': '過去の試行', 'ko': '이전 시도', 'th': 'ความพยายามก่อนหน้า', 'vi': 'Các Lần Thử Trước',
    },
    'showing_last_attempts': {
        'pt-BR': 'Exibindo suas últimas 10 tentativas', 'en': 'Showing your last 10 attempts', 'es': 'Mostrando tus últimos 10 intentos', 'fr': 'Affichage de vos 10 dernières tentatives', 'de': 'Zeigt Ihre letzten 10 Versuche', 'it': 'Mostrando i tuoi ultimi 10 tentativi',
        'nl': 'Toont je laatste 10 pogingen', 'sv': 'Visar dina senaste 10 försök', 'no': 'Viser dine siste 10 forsøk', 'pl': 'Wyświetlanie ostatnich 10 prób', 'id': 'Menampilkan 10 percobaan terakhir Anda',
        'ja': '最後の10回の試行を表示', 'ko': '최근 10번의 시도 표시', 'th': 'แสดง 10 ครั้งล่าสุด', 'vi': 'Hiển thị 10 lần thử gần nhất',
    },
    'attempts_stat': {
        'pt-BR': 'Tentativas', 'en': 'Attempts', 'es': 'Intentos', 'fr': 'Tentatives', 'de': 'Versuche', 'it': 'Tentativi',
        'nl': 'Pogingen', 'sv': 'Försök', 'no': 'Forsøk', 'pl': 'Próby', 'id': 'Percobaan',
        'ja': '試行回数', 'ko': '시도 횟수', 'th': 'ความพยายาม', 'vi': 'Lần thử',
    },
    'best_score': {
        'pt-BR': 'Melhor Score', 'en': 'Best Score', 'es': 'Mejor Puntuación', 'fr': 'Meilleur Score', 'de': 'Beste Punktzahl', 'it': 'Punteggio Migliore',
        'nl': 'Beste Score', 'sv': 'Bästa Resultat', 'no': 'Beste Poengsum', 'pl': 'Najlepszy Wynik', 'id': 'Skor Terbaik',
        'ja': '最高スコア', 'ko': '최고 점수', 'th': 'คะแนนสูงสุด', 'vi': 'Điểm Cao Nhất',
    },
    'average': {
        'pt-BR': 'Média', 'en': 'Average', 'es': 'Promedio', 'fr': 'Moyenne', 'de': 'Durchschnitt', 'it': 'Media',
        'nl': 'Gemiddelde', 'sv': 'Genomsnitt', 'no': 'Gjennomsnitt', 'pl': 'Średnia', 'id': 'Rata-rata',
        'ja': '平均', 'ko': '평균', 'th': 'เฉลี่ย', 'vi': 'Trung bình',
    },
    'not_finished': {
        'pt-BR': 'Não finalizado', 'en': 'Not finished', 'es': 'No finalizado', 'fr': 'Non terminé', 'de': 'Nicht beendet', 'it': 'Non finito',
        'nl': 'Niet voltooid', 'sv': 'Inte avslutad', 'no': 'Ikke fullført', 'pl': 'Nie ukończono', 'id': 'Tidak selesai',
        'ja': '未完了', 'ko': '완료되지 않음', 'th': 'ยังไม่เสร็จ', 'vi': 'Chưa hoàn thành',
    },
    'continue': {
        'pt-BR': 'Continuar', 'en': 'Continue', 'es': 'Continuar', 'fr': 'Continuer', 'de': 'Fortsetzen', 'it': 'Continua',
        'nl': 'Doorgaan', 'sv': 'Fortsätt', 'no': 'Fortsett', 'pl': 'Kontynuuj', 'id': 'Lanjutkan',
        'ja': '続ける', 'ko': '계속하기', 'th': 'ดำเนินการต่อ', 'vi': 'Tiếp tục',
    },
    'answered': {
        'pt-BR': 'respondidas', 'en': 'answered', 'es': 'respondidas', 'fr': 'répondues', 'de': 'beantwortet', 'it': 'risposte',
        'nl': 'beantwoord', 'sv': 'besvarade', 'no': 'besvart', 'pl': 'odpowiedzi', 'id': 'dijawab',
        'ja': '回答済み', 'ko': '응답완료', 'th': 'ตอบแล้ว', 'vi': 'đã trả lời',
    },
    'remaining': {
        'pt-BR': 'restantes', 'en': 'remaining', 'es': 'restantes', 'fr': 'restantes', 'de': 'verbleibend', 'it': 'rimanenti',
        'nl': 'resterend', 'sv': 'återstående', 'no': 'gjenstående', 'pl': 'pozostałe', 'id': 'tersisa',
        'ja': '残り', 'ko': '남은', 'th': 'เหลือ', 'vi': 'còn lại',
    },
    'completed': {
        'pt-BR': 'Concluído', 'en': 'Completed', 'es': 'Completado', 'fr': 'Terminé', 'de': 'Abgeschlossen', 'it': 'Completato',
        'nl': 'Voltooid', 'sv': 'Slutförd', 'no': 'Fullført', 'pl': 'Ukończono', 'id': 'Selesai',
        'ja': '完了', 'ko': '완료됨', 'th': 'เสร็จสิ้น', 'vi': 'Hoàn thành',
    },
    'in_progress': {
        'pt-BR': 'Em Progresso', 'en': 'In Progress', 'es': 'En Progreso', 'fr': 'En cours', 'de': 'In Bearbeitung', 'it': 'In corso',
        'nl': 'Bezig', 'sv': 'Pågår', 'no': 'Pågår', 'pl': 'W trakcie', 'id': 'Berlangsung',
        'ja': '進行中', 'ko': '진행 중', 'th': 'กำลังดำเนินการ', 'vi': 'Đang tiến hành',
    },
    'correct_questions': {
        'pt-BR': 'questões corretas', 'en': 'correct answers', 'es': 'respuestas correctas', 'fr': 'bonnes réponses', 'de': 'richtige Antworten', 'it': 'risposte corrette',
        'nl': 'juiste antwoorden', 'sv': 'rätta svar', 'no': 'riktige svar', 'pl': 'poprawne odpowiedzi', 'id': 'jawaban benar',
        'ja': '正解', 'ko': '정답', 'th': 'คำตอบที่ถูกต้อง', 'vi': 'câu trả lời đúng',
    },
    'correct_answers_label': {
        'pt-BR': 'Acertos', 'en': 'Correct', 'es': 'Aciertos', 'fr': 'Corrects', 'de': 'Richtig', 'it': 'Corretti',
        'nl': 'Correct', 'sv': 'Rätt', 'no': 'Riktig', 'pl': 'Poprawne', 'id': 'Benar',
        'ja': '正解数', 'ko': '정답 수', 'th': 'ถูก', 'vi': 'Đúng',
    },
    'of': {
        'pt-BR': 'de', 'en': 'of', 'es': 'de', 'fr': 'sur', 'de': 'von', 'it': 'di',
        'nl': 'van', 'sv': 'av', 'no': 'av', 'pl': 'z', 'id': 'dari',
        'ja': 'の', 'ko': '중', 'th': 'จาก', 'vi': 'trên',
    },
    'duration': {
        'pt-BR': 'Duração', 'en': 'Duration', 'es': 'Duración', 'fr': 'Durée', 'de': 'Dauer', 'it': 'Durata',
        'nl': 'Duur', 'sv': 'Varaktighet', 'no': 'Varighet', 'pl': 'Czas trwania', 'id': 'Durasi',
        'ja': '所要時間', 'ko': '소요 시간', 'th': 'ระยะเวลา', 'vi': 'Thời lượng',
    },
    'view_answers': {
        'pt-BR': 'Ver Respostas', 'en': 'View Answers', 'es': 'Ver Respuestas', 'fr': 'Voir les réponses', 'de': 'Antworten ansehen', 'it': 'Vedi risposte',
        'nl': 'Antwoorden bekijken', 'sv': 'Visa svar', 'no': 'Se svar', 'pl': 'Zobacz odpowiedzi', 'id': 'Lihat Jawaban',
        'ja': '回答を見る', 'ko': '답변 보기', 'th': 'ดูคำตอบ', 'vi': 'Xem câu trả lời',
    },
    'your_history': {
        'pt-BR': 'Seu Histórico', 'en': 'Your History', 'es': 'Tu Historial', 'fr': 'Votre Historique', 'de': 'Ihre Geschichte', 'it': 'La tua Storia',
        'nl': 'Jouw Geschiedenis', 'sv': 'Din Historik', 'no': 'Din Historie', 'pl': 'Twoja Historia', 'id': 'Riwayat Anda',
        'ja': 'あなたの履歴', 'ko': '당신의 기록', 'th': 'ประวัติของคุณ', 'vi': 'Lịch sử của bạn',
    },
    'no_attempts_yet': {
        'pt-BR': 'Você ainda não tentou este quiz.', 'en': "You haven't tried this quiz yet.", 'es': 'Aún no has intentado este quiz.', 
        'fr': "Vous n'avez pas encore essayé ce quiz.", 'de': 'Sie haben dieses Quiz noch nicht versucht.', 'it': 'Non hai ancora provato questo quiz.',
        'nl': 'Je hebt deze quiz nog niet geprobeerd.', 'sv': 'Du har inte provat denna frågesport än.', 'no': 'Du har ikke prøvd denne quizen ennå.', 
        'pl': 'Nie próbowałeś jeszcze tego quizu.', 'id': 'Anda belum mencoba kuis ini.',
        'ja': 'このクイズをまだ試していません。', 'ko': '아직 이 퀴즈를 시도하지 않았습니다.', 'th': 'คุณยังไม่ได้ลองแบบทดสอบนี้', 'vi': 'Bạn chưa thử câu đố này.',
    },
    
    # Quiz Play
    'question': {
        'pt-BR': 'Questão', 'en': 'Question', 'es': 'Pregunta', 'fr': 'Question', 'de': 'Frage', 'it': 'Domanda',
        'nl': 'Vraag', 'sv': 'Fråga', 'no': 'Spørsmål', 'pl': 'Pytanie', 'id': 'Pertanyaan',
        'ja': '質問', 'ko': '질문', 'th': 'คำถาม', 'vi': 'Câu hỏi',
    },
    'of': {
        'pt-BR': 'de', 'en': 'of', 'es': 'de', 'fr': 'sur', 'de': 'von', 'it': 'di',
        'nl': 'van', 'sv': 'av', 'no': 'av', 'pl': 'z', 'id': 'dari',
        'ja': 'の', 'ko': '의', 'th': 'จาก', 'vi': 'của',
    },
    'next': {
        'pt-BR': 'Próxima', 'en': 'Next', 'es': 'Siguiente', 'fr': 'Suivant', 'de': 'Weiter', 'it': 'Avanti',
        'nl': 'Volgende', 'sv': 'Nästa', 'no': 'Neste', 'pl': 'Następny', 'id': 'Berikutnya',
        'ja': '次へ', 'ko': '다음', 'th': 'ถัดไป', 'vi': 'Tiếp theo',
    },
    'finish': {
        'pt-BR': 'Finalizar', 'en': 'Finish', 'es': 'Finalizar', 'fr': 'Terminer', 'de': 'Beenden', 'it': 'Finire',
        'nl': 'Voltooien', 'sv': 'Avsluta', 'no': 'Fullfør', 'pl': 'Zakończ', 'id': 'Selesai',
        'ja': '終了', 'ko': '완료', 'th': 'เสร็จสิ้น', 'vi': 'Hoàn thành',
    },
    
    # Quiz Results
    'your_result': {
        'pt-BR': 'Seu Resultado', 'en': 'Your Result', 'es': 'Tu Resultado', 'fr': 'Votre Résultat', 'de': 'Ihr Ergebnis', 'it': 'Il tuo Risultato',
        'nl': 'Jouw Resultaat', 'sv': 'Ditt Resultat', 'no': 'Ditt Resultat', 'pl': 'Twój Wynik', 'id': 'Hasil Anda',
        'ja': 'あなたの結果', 'ko': '당신의 결과', 'th': 'ผลลัพธ์ของคุณ', 'vi': 'Kết quả của bạn',
    },
    'you_scored': {
        'pt-BR': 'Você acertou', 'en': 'You scored', 'es': 'Acertaste', 'fr': 'Vous avez obtenu', 'de': 'Sie haben erreicht', 'it': 'Hai segnato',
        'nl': 'Je scoorde', 'sv': 'Du fick', 'no': 'Du fikk', 'pl': 'Zdobyłeś', 'id': 'Anda mencetak',
        'ja': 'あなたのスコア', 'ko': '당신의 점수', 'th': 'คุณได้คะแนน', 'vi': 'Bạn đã đạt',
    },
    'correct_answers': {
        'pt-BR': 'respostas corretas', 'en': 'correct answers', 'es': 'respuestas correctas', 'fr': 'réponses correctes', 'de': 'richtige Antworten', 'it': 'risposte corrette',
        'nl': 'juiste antwoorden', 'sv': 'rätta svar', 'no': 'riktige svar', 'pl': 'poprawne odpowiedzi', 'id': 'jawaban benar',
        'ja': '正解', 'ko': '정답', 'th': 'คำตอบที่ถูกต้อง', 'vi': 'câu trả lời đúng',
    },
    'try_again': {
        'pt-BR': 'Tentar Novamente', 'en': 'Try Again', 'es': 'Intentar de Nuevo', 'fr': 'Réessayer', 'de': 'Erneut versuchen', 'it': 'Riprova',
        'nl': 'Probeer opnieuw', 'sv': 'Försök igen', 'no': 'Prøv igjen', 'pl': 'Spróbuj ponownie', 'id': 'Coba Lagi',
        'ja': 'もう一度試す', 'ko': '다시 시도', 'th': 'ลองอีกครั้ง', 'vi': 'Thử lại',
    },
    'back_to_category': {
        'pt-BR': 'Voltar para Categoria', 'en': 'Back to Category', 'es': 'Volver a Categoría', 'fr': 'Retour à la Catégorie', 'de': 'Zurück zur Kategorie', 'it': 'Torna alla Categoria',
        'nl': 'Terug naar Categorie', 'sv': 'Tillbaka till Kategori', 'no': 'Tilbake til Kategori', 'pl': 'Powrót do Kategorii', 'id': 'Kembali ke Kategori',
        'ja': 'カテゴリーに戻る', 'ko': '카테고리로 돌아가기', 'th': 'กลับไปที่หมวดหมู่', 'vi': 'Quay lại Danh mục',
    },
    'review_answers': {
        'pt-BR': 'Revisar Respostas', 'en': 'Review Answers', 'es': 'Revisar Respuestas', 'fr': 'Réviser les Réponses', 'de': 'Antworten überprüfen', 'it': 'Rivedi le Risposte',
        'nl': 'Antwoorden bekijken', 'sv': 'Granska Svar', 'no': 'Gjennomgå Svar', 'pl': 'Przejrzyj Odpowiedzi', 'id': 'Tinjau Jawaban',
        'ja': '回答を確認', 'ko': '답변 검토', 'th': 'ตรวจสอบคำตอบ', 'vi': 'Xem lại Câu trả lời',
    },
    'your_answer': {
        'pt-BR': 'Sua resposta', 'en': 'Your answer', 'es': 'Tu respuesta', 'fr': 'Votre réponse', 'de': 'Ihre Antwort', 'it': 'La tua risposta',
        'nl': 'Jouw antwoord', 'sv': 'Ditt svar', 'no': 'Ditt svar', 'pl': 'Twoja odpowiedź', 'id': 'Jawaban Anda',
        'ja': 'あなたの回答', 'ko': '당신의 답변', 'th': 'คำตอบของคุณ', 'vi': 'Câu trả lời của bạn',
    },
    'correct_answer': {
        'pt-BR': 'Resposta correta', 'en': 'Correct answer', 'es': 'Respuesta correcta', 'fr': 'Réponse correcte', 'de': 'Richtige Antwort', 'it': 'Risposta corretta',
        'nl': 'Juiste antwoord', 'sv': 'Rätt svar', 'no': 'Riktig svar', 'pl': 'Poprawna odpowiedź', 'id': 'Jawaban benar',
        'ja': '正解', 'ko': '정답', 'th': 'คำตอบที่ถูกต้อง', 'vi': 'Câu trả lời đúng',
    },
    
    # Footer
    'footer_languages_title': {
        'pt-BR': 'Quizzes para todos os idiomas', 'en': 'Quizzes for all languages', 'es': 'Quizzes para todos los idiomas', 
        'fr': 'Quiz pour toutes les langues', 'de': 'Quiz für alle sprachen', 'it': 'Quiz per tutte le lingue',
        'nl': 'Quizzen voor alle talen', 'sv': 'Frågesporter för alla språk', 'no': 'Quizer for alle språk', 'pl': 'Quizy dla wszystkich języków', 'id': 'Kuis untuk semua bahasa',
        'ja': 'すべての言語のクイズ', 'ko': '모든 언어를 위한 퀴즈', 'th': 'แบบทดสอบสำหรับทุกภาษา', 'vi': 'Câu đố cho mọi ngôn ngữ',
    },
    'footer_languages_subtitle': {
        'pt-BR': 'Mais de 7.000 quizzes em 6 idiomas diferentes', 'en': 'Over 7,000 quizzes in 6 different languages', 'es': 'Más de 7.000 quizzes en 6 idiomas diferentes', 
        'fr': 'Plus de 7 000 quiz en 6 langues différentes', 'de': 'Über 7.000 Quiz in 6 verschiedenen Sprachen', 'it': 'Oltre 7.000 quiz in 6 lingue diverse',
        'nl': 'Meer dan 7.000 quizzen in 6 verschillende talen', 'sv': 'Över 7 000 frågesporter på 6 olika språk', 'no': 'Over 7 000 quizer på 6 forskjellige språk', 
        'pl': 'Ponad 7000 quizów w 6 różnych językach', 'id': 'Lebih dari 7.000 kuis dalam 6 bahasa berbeda',
        'ja': '6つの異なる言語で7,000以上のクイズ', 'ko': '6개 언어로 된 7,000개 이상의 퀴즈', 'th': 'แบบทดสอบมากกว่า 7,000 รายการใน 6 ภาษา', 'vi': 'Hơn 7.000 câu đố bằng 6 ngôn ngữ khác nhau',
    },
    'navigation': {
        'pt-BR': 'Navegação', 'en': 'Navigation', 'es': 'Navegación', 'fr': 'Navigation', 'de': 'Navigation', 'it': 'Navigazione',
        'nl': 'Navigatie', 'sv': 'Navigering', 'no': 'Navigasjon', 'pl': 'Nawigacja', 'id': 'Navigasi',
        'ja': 'ナビゲーション', 'ko': '탐색', 'th': 'การนำทาง', 'vi': 'Điều hướng',
    },
    'home': {
        'pt-BR': 'Início', 'en': 'Home', 'es': 'Inicio', 'fr': 'Accueil', 'de': 'Startseite', 'it': 'Home',
        'nl': 'Home', 'sv': 'Hem', 'no': 'Hjem', 'pl': 'Strona główna', 'id': 'Beranda',
        'ja': 'ホーム', 'ko': '홈', 'th': 'หน้าแรก', 'vi': 'Trang chủ',
    },
    'categories': {
        'pt-BR': 'Categorias', 'en': 'Categories', 'es': 'Categorías', 'fr': 'Catégories', 'de': 'Kategorien', 'it': 'Categorie',
        'nl': 'Categorieën', 'sv': 'Kategorier', 'no': 'Kategorier', 'pl': 'Kategorie', 'id': 'Kategori',
        'ja': 'カテゴリー', 'ko': '카테고리', 'th': 'หมวดหมู่', 'vi': 'Danh mục',
    },
    'account': {
        'pt-BR': 'Conta', 'en': 'Account', 'es': 'Cuenta', 'fr': 'Compte', 'de': 'Konto', 'it': 'Account',
        'nl': 'Account', 'sv': 'Konto', 'no': 'Konto', 'pl': 'Konto', 'id': 'Akun',
        'ja': 'アカウント', 'ko': '계정', 'th': 'บัญชี', 'vi': 'Tài khoản',
    },
    'legal': {
        'pt-BR': 'Legal', 'en': 'Legal', 'es': 'Legal', 'fr': 'Légal', 'de': 'Rechtliches', 'it': 'Legale',
        'nl': 'Juridisch', 'sv': 'Juridisk', 'no': 'Juridisk', 'pl': 'Prawne', 'id': 'Hukum',
        'ja': '法的情報', 'ko': '법적 고지', 'th': 'กฎหมาย', 'vi': 'Pháp lý',
    },
    'terms_of_use': {
        'pt-BR': 'Termos de Uso', 'en': 'Terms of Use', 'es': 'Términos de Uso', 'fr': "Conditions d'Utilisation", 'de': 'Nutzungsbedingungen', 'it': "Termini d'Uso",
        'nl': 'Gebruiksvoorwaarden', 'sv': 'Användarvillkor', 'no': 'Bruksvilkår', 'pl': 'Warunki użytkowania', 'id': 'Ketentuan Penggunaan',
        'ja': '利用規約', 'ko': '이용 약관', 'th': 'ข้อกำหนดการใช้งาน', 'vi': 'Điều khoản sử dụng',
    },
    'privacy': {
        'pt-BR': 'Privacidade', 'en': 'Privacy', 'es': 'Privacidad', 'fr': 'Confidentialité', 'de': 'Datenschutz', 'it': 'Privacy',
        'nl': 'Privacy', 'sv': 'Integritet', 'no': 'Personvern', 'pl': 'Prywatność', 'id': 'Privasi',
        'ja': 'プライバシー', 'ko': '개인정보 보호', 'th': 'ความเป็นส่วนตัว', 'vi': 'Quyền riêng tư',
    },
    'contact': {
        'pt-BR': 'Contato', 'en': 'Contact', 'es': 'Contacto', 'fr': 'Contact', 'de': 'Kontakt', 'it': 'Contatto',
        'nl': 'Contact', 'sv': 'Kontakt', 'no': 'Kontakt', 'pl': 'Kontakt', 'id': 'Kontak',
        'ja': 'お問い合わせ', 'ko': '연락처', 'th': 'ติดต่อ', 'vi': 'Liên hệ',
    },
    'footer_description': {
        'pt-BR': 'A melhor plataforma de quizzes do Brasil. Aprenda, desafie e divirta-se com nossos quizzes interativos!', 
        'en': 'The best quiz platform. Learn, challenge yourself and have fun with our interactive quizzes!', 
        'es': 'La mejor plataforma de quizzes. ¡Aprende, desafíate y diviértete con nuestros quizzes interactivos!', 
        'fr': 'La meilleure plateforme de quiz. Apprenez, défiez-vous et amusez-vous avec nos quiz interactifs!', 
        'de': 'Die beste Quiz-Plattform. Lernen, fordern Sie sich heraus und haben Sie Spaß mit unseren interaktiven Quiz!', 
        'it': 'La migliore piattaforma di quiz. Impara, sfidati e divertiti con i nostri quiz interattivi!',
        'nl': 'Het beste quizplatform. Leer, daag jezelf uit en heb plezier met onze interactieve quizzen!', 
        'sv': 'Den bästa frågesporten. Lär dig, utmana dig själv och ha kul med våra interaktiva frågesporter!', 
        'no': 'Den beste quizplattformen. Lær, utfordre deg selv og ha det gøy med våre interaktive quizer!', 
        'pl': 'Najlepsza platforma quizów. Ucz się, rzuć sobie wyzwanie i baw się naszymi interaktywnymi quizami!', 
        'id': 'Platform kuis terbaik. Belajar, tantang diri Anda dan bersenang-senang dengan kuis interaktif kami!',
        'ja': '最高のクイズプラットフォーム。学び、挑戦し、インタラクティブなクイズで楽しもう！', 
        'ko': '최고의 퀴즈 플랫폼. 배우고, 도전하고, 인터랙티브 퀴즈로 즐기세요!', 
        'th': 'แพลตฟอร์มแบบทดสอบที่ดีที่สุด เรียนรู้ ท้าทายตัวเอง และสนุกกับแบบทดสอบแบบอินเทอร์แอกทีฟของเรา!', 
        'vi': 'Nền tảng câu đố tốt nhất. Học hỏi, thách thức bản thân và vui chơi với các câu đố tương tác của chúng tôi!',
    },
    'all_rights_reserved': {
        'pt-BR': 'Todos os direitos reservados.', 'en': 'All rights reserved.', 'es': 'Todos los derechos reservados.', 
        'fr': 'Tous droits réservés.', 'de': 'Alle Rechte vorbehalten.', 'it': 'Tutti i diritti riservati.',
        'nl': 'Alle rechten voorbehouden.', 'sv': 'Alla rättigheter förbehållna.', 'no': 'Alle rettigheter reservert.', 
        'pl': 'Wszelkie prawa zastrzeżone.', 'id': 'Hak cipta dilindungi.',
        'ja': '全著作権所有。', 'ko': '모든 권리 보유.', 'th': 'สงวนลิขสิทธิ์', 'vi': 'Đã đăng ký bản quyền.',
    },
    
    # User Profile
    'statistics': {
        'pt-BR': 'Estatísticas', 'en': 'Statistics', 'es': 'Estadísticas', 'fr': 'Statistiques', 'de': 'Statistiken', 'it': 'Statistiche',
        'nl': 'Statistieken', 'sv': 'Statistik', 'no': 'Statistikk', 'pl': 'Statystyki', 'id': 'Statistik',
        'ja': '統計', 'ko': '통계', 'th': 'สถิติ', 'vi': 'Thống kê',
    },
    'total_attempts': {
        'pt-BR': 'Tentativas Totais', 'en': 'Total Attempts', 'es': 'Intentos Totales', 'fr': 'Tentatives Totales', 'de': 'Gesamtversuche', 'it': 'Tentativi Totali',
        'nl': 'Totaal Pogingen', 'sv': 'Totalt Försök', 'no': 'Totale Forsøk', 'pl': 'Łączna liczba prób', 'id': 'Total Percobaan',
        'ja': '総試行回数', 'ko': '총 시도 횟수', 'th': 'ความพยายามทั้งหมด', 'vi': 'Tổng số lần thử',
    },
    'accuracy_rate': {
        'pt-BR': 'Taxa de Acerto', 'en': 'Accuracy Rate', 'es': 'Tasa de Acierto', 'fr': 'Taux de Précision', 'de': 'Genauigkeitsrate', 'it': 'Tasso di Precisione',
        'nl': 'Nauwkeurigheidspercentage', 'sv': 'Noggrannhet', 'no': 'Nøyaktighet', 'pl': 'Wskaźnik dokładności', 'id': 'Tingkat Akurasi',
        'ja': '正解率', 'ko': '정확도', 'th': 'อัตราความแม่นยำ', 'vi': 'Tỷ lệ chính xác',
    },
    'perfect_quizzes': {
        'pt-BR': 'Quizzes Perfeitos', 'en': 'Perfect Quizzes', 'es': 'Quizzes Perfectos', 'fr': 'Quiz Parfaits', 'de': 'Perfekte Quiz', 'it': 'Quiz Perfetti',
        'nl': 'Perfecte Quizzen', 'sv': 'Perfekta Frågesporter', 'no': 'Perfekte Quizer', 'pl': 'Doskonałe Quizy', 'id': 'Kuis Sempurna',
        'ja': 'パーフェクトクイズ', 'ko': '완벽한 퀴즈', 'th': 'แบบทดสอบที่สมบูรณ์แบบ', 'vi': 'Câu đố hoàn hảo',
    },
    'explore': {
        'pt-BR': 'Explorar', 'en': 'Explore', 'es': 'Explorar', 'fr': 'Explorer', 'de': 'Erkunden', 'it': 'Esplora',
        'nl': 'Verkennen', 'sv': 'Utforska', 'no': 'Utforsk', 'pl': 'Odkryj', 'id': 'Jelajahi',
        'ja': '探索', 'ko': '탐색', 'th': 'สำรวจ', 'vi': 'Khám phá',
    },
    'no_categories_available': {
        'pt-BR': 'Nenhuma categoria disponível no momento.', 'en': 'No categories available at the moment.', 'es': 'No hay categorías disponibles en este momento.', 
        'fr': 'Aucune catégorie disponible pour le moment.', 'de': 'Derzeit keine Kategorien verfügbar.', 'it': 'Nessuna categoria disponibile al momento.',
        'nl': 'Momenteel geen categorieën beschikbaar.', 'sv': 'Inga kategorier tillgängliga för tillfället.', 'no': 'Ingen kategorier tilgjengelig for øyeblikket.', 
        'pl': 'Brak dostępnych kategorii w tym momencie.', 'id': 'Tidak ada kategori yang tersedia saat ini.',
        'ja': '現在利用可能なカテゴリーはありません。', 'ko': '현재 사용 가능한 카테고리가 없습니다.', 'th': 'ไม่มีหมวดหมู่ที่พร้อมใช้งานในขณะนี้', 'vi': 'Hiện tại không có danh mục nào.',
    },
    'cta_title': {
        'pt-BR': 'Pronto para testar seus conhecimentos?', 'en': 'Ready to test your knowledge?', 'es': '¿Listo para probar tus conocimientos?', 
        'fr': 'Prêt à tester vos connaissances?', 'de': 'Bereit, Ihr Wissen zu testen?', 'it': 'Pronto a testare le tue conoscenze?',
        'nl': 'Klaar om je kennis te testen?', 'sv': 'Redo att testa din kunskap?', 'no': 'Klar for å teste kunnskapen din?', 
        'pl': 'Gotowy sprawdzić swoją wiedzę?', 'id': 'Siap menguji pengetahuan Anda?',
        'ja': 'あなたの知識をテストする準備はできましたか？', 'ko': '지식을 테스트할 준비가 되셨나요?', 'th': 'พร้อมที่จะทดสอบความรู้ของคุณหรือยัง?', 'vi': 'Sẵn sàng kiểm tra kiến thức của bạn?',
    },
    'cta_description': {
        'pt-BR': 'Junte-se a milhares de usuários e descubra o quanto você realmente sabe. É grátis, divertido e viciante!', 
        'en': 'Join thousands of users and discover how much you really know. It\'s free, fun and addictive!', 
        'es': 'Únete a miles de usuarios y descubre cuánto realmente sabes. ¡Es gratis, divertido y adictivo!', 
        'fr': 'Rejoignez des milliers d\'utilisateurs et découvrez ce que vous savez vraiment. C\'est gratuit, amusant et addictif!', 
        'de': 'Schließen Sie sich Tausenden von Benutzern an und entdecken Sie, wie viel Sie wirklich wissen. Es ist kostenlos, unterhaltsam und macht süchtig!', 
        'it': 'Unisciti a migliaia di utenti e scopri quanto sai davvero. È gratis, divertente e coinvolgente!',
        'nl': 'Sluit je aan bij duizenden gebruikers en ontdek hoeveel je echt weet. Het is gratis, leuk en verslavend!', 
        'sv': 'Gå med tusentals användare och upptäck hur mycket du verkligen vet. Det är gratis, roligt och beroendeframkallande!', 
        'no': 'Bli med tusenvis av brukere og oppdag hvor mye du virkelig vet. Det er gratis, gøy og vanedannende!', 
        'pl': 'Dołącz do tysięcy użytkowników i odkryj, ile naprawdę wiesz. To darmowe, zabawne i uzależniające!', 
        'id': 'Bergabunglah dengan ribuan pengguna dan temukan seberapa banyak yang Anda ketahui. Gratis, menyenangkan, dan adiktif!',
        'ja': '何千人ものユーザーに参加して、あなたが本当にどれだけ知っているかを発見してください。無料で、楽しく、中毒性があります！', 
        'ko': '수천 명의 사용자와 함께 당신이 정말로 얼마나 알고 있는지 발견하세요. 무료이며 재미있고 중독성이 있습니다!', 
        'th': 'เข้าร่วมกับผู้ใช้หลายพันคนและค้นพบว่าคุณรู้มากแค่ไหนจริงๆ ฟรี สนุก และติดใจ!', 
        'vi': 'Tham gia cùng hàng nghìn người dùng và khám phá bạn thực sự biết bao nhiêu. Miễn phí, vui vẻ và gây nghiện!',
    },
    'start_journey': {
        'pt-BR': 'Começar minha jornada', 'en': 'Start my journey', 'es': 'Comenzar mi viaje', 'fr': 'Commencer mon voyage', 'de': 'Meine Reise beginnen', 'it': 'Inizia il mio viaggio',
        'nl': 'Begin mijn reis', 'sv': 'Börja min resa', 'no': 'Start min reise', 'pl': 'Rozpocznij moją podróż', 'id': 'Mulai perjalanan saya',
        'ja': '私の旅を始める', 'ko': '내 여정 시작', 'th': 'เริ่มต้นการเดินทางของฉัน', 'vi': 'Bắt đầu hành trình của tôi',
    },
    'explore_quizzes': {
        'pt-BR': 'Explorar quizzes', 'en': 'Explore quizzes', 'es': 'Explorar quizzes', 'fr': 'Explorer les quiz', 'de': 'Quiz erkunden', 'it': 'Esplora quiz',
        'nl': 'Verken quizzen', 'sv': 'Utforska frågesporter', 'no': 'Utforsk quizer', 'pl': 'Odkryj quizy', 'id': 'Jelajahi kuis',
        'ja': 'クイズを探索', 'ko': '퀴즈 탐색', 'th': 'สำรวจแบบทดสอบ', 'vi': 'Khám phá câu đố',
    },
    
    # Home Page - Category Cards
    'your_progress': {
        'pt-BR': 'Seu Progresso', 'en': 'Your Progress', 'es': 'Tu Progreso', 'fr': 'Votre Progrès', 'de': 'Ihr Fortschritt', 'it': 'Il tuo Progresso',
        'nl': 'Jouw Voortgang', 'sv': 'Din Framsteg', 'no': 'Din Fremgang', 'pl': 'Twój Postęp', 'id': 'Kemajuan Anda',
        'ja': 'あなたの進捗', 'ko': '당신의 진행 상황', 'th': 'ความคืบหน้าของคุณ', 'vi': 'Tiến độ của bạn',
    },
    'completed': {
        'pt-BR': 'completos', 'en': 'completed', 'es': 'completados', 'fr': 'terminés', 'de': 'abgeschlossen', 'it': 'completati',
        'nl': 'voltooid', 'sv': 'slutförda', 'no': 'fullført', 'pl': 'ukończone', 'id': 'selesai',
        'ja': '完了', 'ko': '완료', 'th': 'เสร็จสิ้น', 'vi': 'hoàn thành',
    },
    'coming_soon': {
        'pt-BR': '🔜 Em breve!', 'en': '🔜 Coming soon!', 'es': '🔜 ¡Próximamente!', 'fr': '🔜 Bientôt!', 'de': '🔜 Demnächst!', 'it': '🔜 Prossimamente!',
        'nl': '🔜 Binnenkort!', 'sv': '🔜 Kommer snart!', 'no': '🔜 Kommer snart!', 'pl': '🔜 Wkrótce!', 'id': '🔜 Segera hadir!',
        'ja': '🔜 近日公開！', 'ko': '🔜 곧 출시!', 'th': '🔜 เร็วๆ นี้!', 'vi': '🔜 Sắp ra mắt!',
    },
    'start_journey_button': {
        'pt-BR': 'Iniciar Jornada 🚀', 'en': 'Start Journey 🚀', 'es': 'Iniciar Viaje 🚀', 'fr': 'Commencer le Voyage 🚀', 'de': 'Reise starten 🚀', 'it': 'Inizia il Viaggio 🚀',
        'nl': 'Start Reis 🚀', 'sv': 'Starta Resa 🚀', 'no': 'Start Reise 🚀', 'pl': 'Rozpocznij Podróż 🚀', 'id': 'Mulai Perjalanan 🚀',
        'ja': '旅を始める 🚀', 'ko': '여정 시작 🚀', 'th': 'เริ่มการเดินทาง 🚀', 'vi': 'Bắt đầu Hành trình 🚀',
    },
    'category_complete': {
        'pt-BR': '✨ Categoria 100% completa!', 'en': '✨ Category 100% complete!', 'es': '✨ ¡Categoría 100% completa!', 'fr': '✨ Catégorie 100% complète!', 'de': '✨ Kategorie 100% abgeschlossen!', 'it': '✨ Categoria 100% completa!',
        'nl': '✨ Categorie 100% voltooid!', 'sv': '✨ Kategori 100% slutförd!', 'no': '✨ Kategori 100% fullført!', 'pl': '✨ Kategoria 100% ukończona!', 'id': '✨ Kategori 100% selesai!',
        'ja': '✨ カテゴリー100%完了！', 'ko': '✨ 카테고리 100% 완료!', 'th': '✨ หมวดหมู่เสร็จสิ้น 100%!', 'vi': '✨ Danh mục hoàn thành 100%!',
    },
    'continue_journey': {
        'pt-BR': '🎯 Continue sua jornada!', 'en': '🎯 Continue your journey!', 'es': '🎯 ¡Continúa tu viaje!', 'fr': '🎯 Continuez votre voyage!', 'de': '🎯 Setze deine Reise fort!', 'it': '🎯 Continua il tuo viaggio!',
        'nl': '🎯 Ga door met je reis!', 'sv': '🎯 Fortsätt din resa!', 'no': '🎯 Fortsett reisen din!', 'pl': '🎯 Kontynuuj swoją podróż!', 'id': '🎯 Lanjutkan perjalanan Anda!',
        'ja': '🎯 旅を続けよう！', 'ko': '🎯 여정을 계속하세요!', 'th': '🎯 ดำเนินการเดินทางต่อ!', 'vi': '🎯 Tiếp tục hành trình của bạn!',
    },
    'new_challenge': {
        'pt-BR': '⚡ Novo desafio disponível!', 'en': '⚡ New challenge available!', 'es': '⚡ ¡Nuevo desafío disponible!', 'fr': '⚡ Nouveau défi disponible!', 'de': '⚡ Neue Herausforderung verfügbar!', 'it': '⚡ Nuova sfida disponibile!',
        'nl': '⚡ Nieuwe uitdaging beschikbaar!', 'sv': '⚡ Ny utmaning tillgänglig!', 'no': '⚡ Ny utfordring tilgjengelig!', 'pl': '⚡ Nowe wyzwanie dostępne!', 'id': '⚡ Tantangan baru tersedia!',
        'ja': '⚡ 新しいチャレンジ！', 'ko': '⚡ 새 도전 가능!', 'th': '⚡ ความท้าทายใหม่!', 'vi': '⚡ Thách thức mới!',
    },
    'review_quizzes': {
        'pt-BR': 'Revisar Quizzes 🔄', 'en': 'Review Quizzes 🔄', 'es': 'Revisar Quizzes 🔄', 'fr': 'Réviser les Quiz 🔄', 'de': 'Quiz überprüfen 🔄', 'it': 'Rivedi Quiz 🔄',
        'nl': 'Quizzen bekijken 🔄', 'sv': 'Granska Frågesporter 🔄', 'no': 'Gjennomgå Quizer 🔄', 'pl': 'Przejrzyj Quizy 🔄', 'id': 'Tinjau Kuis 🔄',
        'ja': 'クイズ復習 🔄', 'ko': '퀴즈 복습 🔄', 'th': 'ทบทวนแบบทดสอบ 🔄', 'vi': 'Xem lại Câu đố 🔄',
    },
    'continue_playing': {
        'pt-BR': 'Continuar Jogando 🎮', 'en': 'Continue Playing 🎮', 'es': 'Seguir Jugando 🎮', 'fr': 'Continuer à Jouer 🎮', 'de': 'Weiterspielen 🎮', 'it': 'Continua a Giocare 🎮',
        'nl': 'Doorgaan met Spelen 🎮', 'sv': 'Fortsätt Spela 🎮', 'no': 'Fortsett å Spille 🎮', 'pl': 'Kontynuuj Grę 🎮', 'id': 'Lanjutkan Bermain 🎮',
        'ja': 'プレイ続行 🎮', 'ko': '계속 플레이 🎮', 'th': 'เล่นต่อ 🎮', 'vi': 'Tiếp tục Chơi 🎮',
    },
    
    # User Profile - Dashboard
    'quizzes_completed': {
        'pt-BR': 'Quizzes Realizados', 'en': 'Quizzes Completed', 'es': 'Quizzes Completados', 'fr': 'Quiz Terminés', 'de': 'Quiz Abgeschlossen', 'it': 'Quiz Completati',
        'nl': 'Quizzen Voltooid', 'sv': 'Frågesporter Slutförda', 'no': 'Quizer Fullført', 'pl': 'Quizy Ukończone', 'id': 'Kuis Diselesaikan',
        'ja': '完了したクイズ', 'ko': '완료된 퀴즈', 'th': 'แบบทดสอบที่เสร็จสิ้น', 'vi': 'Câu đố đã hoàn thành',
    },
    'badges_earned': {
        'pt-BR': 'Badges Conquistadas', 'en': 'Badges Earned', 'es': 'Insignias Ganadas', 'fr': 'Badges Gagnés', 'de': 'Abzeichen Verdient', 'it': 'Badge Guadagnate',
        'nl': 'Badges Verdiend', 'sv': 'Märken Förtjänade', 'no': 'Merker Opptjent', 'pl': 'Odznaki Zdobyte', 'id': 'Lencana Diperoleh',
        'ja': '獲得したバッジ', 'ko': '획득한 배지', 'th': 'เหรียญที่ได้รับ', 'vi': 'Huy hiệu đã đạt được',
    },
    'my_achievements': {
        'pt-BR': 'Minhas Conquistas', 'en': 'My Achievements', 'es': 'Mis Logros', 'fr': 'Mes Réalisations', 'de': 'Meine Erfolge', 'it': 'I Miei Successi',
        'nl': 'Mijn Prestaties', 'sv': 'Mina Framgångar', 'no': 'Mine Prestasjoner', 'pl': 'Moje Osiągnięcia', 'id': 'Pencapaian Saya',
        'ja': '私の成果', 'ko': '내 성과', 'th': 'ความสำเร็จของฉัน', 'vi': 'Thành tích của tôi',
    },
    'my_results': {
        'pt-BR': 'Meus Resultados', 'en': 'My Results', 'es': 'Mis Resultados', 'fr': 'Mes Résultats', 'de': 'Meine Ergebnisse', 'it': 'I Miei Risultati',
        'nl': 'Mijn Resultaten', 'sv': 'Mina Resultat', 'no': 'Mine Resultater', 'pl': 'Moje Wyniki', 'id': 'Hasil Saya',
        'ja': '私の結果', 'ko': '내 결과', 'th': 'ผลลัพธ์ของฉัน', 'vi': 'Kết quả của tôi',
    },
    'complete_quizzes_for_amazing_badges': {
        'pt-BR': 'Complete quizzes para conquistar badges incríveis', 'en': 'Complete quizzes to earn amazing badges', 'es': 'Completa quizzes para ganar insignias increíbles', 'fr': 'Complétez des quiz pour gagner des badges incroyables', 'de': 'Vervollständige Quiz, um erstaunliche Abzeichen zu verdienen', 'it': 'Completa i quiz per guadagnare badge fantastici',
        'nl': 'Voltooi quizzen om geweldige badges te verdienen', 'sv': 'Slutför frågesporter för att tjäna fantastiska märken', 'no': 'Fullfør quizer for å tjene fantastiske merker', 'pl': 'Ukończ quizy, aby zdobyć niesamowite odznaki', 'id': 'Selesaikan kuis untuk mendapatkan lencana luar biasa',
        'ja': '素晴らしいバッジを獲得するためにクイズを完了', 'ko': '놀라운 배지를 얻기 위해 퀴즈 완료', 'th': 'ทำแบบทดสอบให้เสร็จเพื่อรับเหรียญที่น่าทึ่ง', 'vi': 'Hoàn thành câu đố để kiếm được huy hiệu tuyệt vời',
    },
    'no_achievements_yet': {
        'pt-BR': 'Nenhuma conquista ainda', 'en': 'No achievements yet', 'es': 'Aún no hay logros', 'fr': 'Aucune réalisation pour le moment', 'de': 'Noch keine Erfolge', 'it': 'Nessun successo ancora',
        'nl': 'Nog geen prestaties', 'sv': 'Inga framgångar än', 'no': 'Ingen prestasjoner ennå', 'pl': 'Brak osiągnięć', 'id': 'Belum ada pencapaian',
        'ja': 'まだ成果なし', 'ko': '아직 성과 없음', 'th': 'ยังไม่มีผลงาน', 'vi': 'Chưa có thành tích',
    },
    'complete_quizzes_for_exclusive_badges': {
        'pt-BR': 'Complete quizzes e alcance boas pontuações para conquistar badges exclusivas!', 'en': 'Complete quizzes and achieve good scores to earn exclusive badges!', 'es': '¡Completa quizzes y alcanza buenas puntuaciones para ganar insignias exclusivas!', 'fr': 'Complétez des quiz et obtenez de bons scores pour gagner des badges exclusifs!', 'de': 'Vervollständige Quiz und erreiche gute Punkte, um exklusive Abzeichen zu verdienen!', 'it': 'Completa i quiz e ottieni buoni punteggi per guadagnare badge esclusivi!',
        'nl': 'Voltooi quizzen en behaal goede scores om exclusieve badges te verdienen!', 'sv': 'Slutför frågesporter och uppnå bra poäng för att tjäna exklusiva märken!', 'no': 'Fullfør quizer og oppnå gode poeng for å tjene eksklusive merker!', 'pl': 'Ukończ quizy i osiągnij dobre wyniki, aby zdobyć ekskluzywne odznaki!', 'id': 'Selesaikan kuis dan capai skor bagus untuk mendapatkan lencana eksklusif!',
        'ja': 'クイズを完了して良いスコアを達成し、限定バッジを獲得しましょう！', 'ko': '퀴즈를 완료하고 좋은 점수를 달성하여 독점 배지를 획득하세요!', 'th': 'ทำแบบทดสอบให้เสร็จและได้คะแนนดีเพื่อรับเหรียญพิเศษ!', 'vi': 'Hoàn thành câu đố và đạt điểm cao để kiếm được huy hiệu độc quyền!',
    },
    'start_earning': {
        'pt-BR': 'Começar a Conquistar', 'en': 'Start Earning', 'es': 'Comenzar a Ganar', 'fr': 'Commencer à Gagner', 'de': 'Verdienen Beginnen', 'it': 'Inizia a Guadagnare',
        'nl': 'Begin met Verdienen', 'sv': 'Börja Tjäna', 'no': 'Begynn å Tjene', 'pl': 'Zacznij Zarabiać', 'id': 'Mulai Menghasilkan',
        'ja': '獲得を開始', 'ko': '획득 시작', 'th': 'เริ่มรับรางวัล', 'vi': 'Bắt đầu Kiếm',
    },
    'all': {
        'pt-BR': 'Todos', 'en': 'All', 'es': 'Todos', 'fr': 'Tous', 'de': 'Alle', 'it': 'Tutti',
        'nl': 'Alle', 'sv': 'Alla', 'no': 'Alle', 'pl': 'Wszystkie', 'id': 'Semua',
        'ja': 'すべて', 'ko': '모두', 'th': 'ทั้งหมด', 'vi': 'Tất cả',
    },
    
    # Quiz Play
    'playing': {
        'pt-BR': 'Jogando', 'en': 'Playing', 'es': 'Jugando', 'fr': 'En train de jouer', 'de': 'Spielen', 'it': 'Giocando',
        'nl': 'Spelen', 'sv': 'Spelar', 'no': 'Spiller', 'pl': 'Gracie', 'id': 'Bermain',
        'ja': 'プレイ中', 'ko': '플레이 중', 'th': 'กำลังเล่น', 'vi': 'Đang chơi',
    },
    'progress': {
        'pt-BR': 'Progresso', 'en': 'Progress', 'es': 'Progreso', 'fr': 'Progrès', 'de': 'Fortschritt', 'it': 'Progresso',
        'nl': 'Voortgang', 'sv': 'Framsteg', 'no': 'Fremgang', 'pl': 'Postęp', 'id': 'Kemajuan',
        'ja': '進捗', 'ko': '진행률', 'th': 'ความคืบหน้า', 'vi': 'Tiến độ',
    },
    'question': {
        'pt-BR': 'Questão', 'en': 'Question', 'es': 'Pregunta', 'fr': 'Question', 'de': 'Frage', 'it': 'Domanda',
        'nl': 'Vraag', 'sv': 'Fråga', 'no': 'Spørsmål', 'pl': 'Pytanie', 'id': 'Pertanyaan',
        'ja': '質問', 'ko': '질문', 'th': 'คำถาม', 'vi': 'Câu hỏi',
    },
    'finish_quiz': {
        'pt-BR': 'Finalizar Quiz', 'en': 'Finish Quiz', 'es': 'Finalizar Quiz', 'fr': 'Terminer le Quiz', 'de': 'Quiz beenden', 'it': 'Termina Quiz',
        'nl': 'Quiz voltooien', 'sv': 'Avsluta Quiz', 'no': 'Fullfør Quiz', 'pl': 'Zakończ Quiz', 'id': 'Selesaikan Kuis',
        'ja': 'クイズ終了', 'ko': '퀴즈 완료', 'th': 'เสร็จสิ้นแบบทดสอบ', 'vi': 'Hoàn thành Câu đố',
    },
    'you_are_playing': {
        'pt-BR': 'Você está jogando', 'en': 'You are playing', 'es': 'Estás jugando', 'fr': 'Vous jouez', 'de': 'Sie spielen', 'it': 'Stai giocando',
        'nl': 'Je speelt', 'sv': 'Du spelar', 'no': 'Du spiller', 'pl': 'Grasz', 'id': 'Anda sedang bermain',
        'ja': 'あなたはプレイ中です', 'ko': '당신은 플레이 중입니다', 'th': 'คุณกำลังเล่น', 'vi': 'Bạn đang chơi',
    },
    
    # Theme Detail
    'questions': {
        'pt-BR': 'questões', 'en': 'questions', 'es': 'preguntas', 'fr': 'questions', 'de': 'Fragen', 'it': 'domande',
        'nl': 'vragen', 'sv': 'frågor', 'no': 'spørsmål', 'pl': 'pytania', 'id': 'pertanyaan',
        'ja': '質問', 'ko': '질문', 'th': 'คำถาม', 'vi': 'câu hỏi',
    },
    'available_achievements': {
        'pt-BR': 'Conquistas Disponíveis', 'en': 'Available Achievements', 'es': 'Logros Disponibles', 'fr': 'Réalisations Disponibles', 'de': 'Verfügbare Erfolge', 'it': 'Successi Disponibili',
        'nl': 'Beschikbare Prestaties', 'sv': 'Tillgängliga Framgångar', 'no': 'Tilgjengelige Prestasjoner', 'pl': 'Dostępne Osiągnięcia', 'id': 'Pencapaian Tersedia',
        'ja': '利用可能な成果', 'ko': '사용 가능한 성과', 'th': 'ความสำเร็จที่มี', 'vi': 'Thành tích có sẵn',
    },
    'earned': {
        'pt-BR': 'conquistadas', 'en': 'earned', 'es': 'ganadas', 'fr': 'gagnées', 'de': 'verdient', 'it': 'guadagnate',
        'nl': 'verdiend', 'sv': 'förtjänade', 'no': 'opptjent', 'pl': 'zdobyte', 'id': 'diperoleh',
        'ja': '獲得', 'ko': '획득', 'th': 'ได้รับ', 'vi': 'đạt được',
    },
    'quizzes': {
        'pt-BR': 'Quizzes', 'en': 'Quizzes', 'es': 'Quizzes', 'fr': 'Quiz', 'de': 'Quiz', 'it': 'Quiz',
        'nl': 'Quizzen', 'sv': 'Frågesporter', 'no': 'Quizer', 'pl': 'Quizy', 'id': 'Kuis',
        'ja': 'クイズ', 'ko': '퀴즈', 'th': 'แบบทดสอบ', 'vi': 'Câu đố',
    },
    'play': {
        'pt-BR': 'Jogar', 'en': 'Play', 'es': 'Jugar', 'fr': 'Jouer', 'de': 'Spielen', 'it': 'Giocare',
        'nl': 'Spelen', 'sv': 'Spela', 'no': 'Spill', 'pl': 'Graj', 'id': 'Main',
        'ja': 'プレイ', 'ko': '플레이', 'th': 'เล่น', 'vi': 'Chơi',
    },
    'no_content_available_yet': {
        'pt-BR': 'Nenhum conteúdo disponível ainda', 'en': 'No content available yet', 'es': 'Aún no hay contenido disponible', 'fr': 'Aucun contenu disponible pour le moment', 'de': 'Noch kein Inhalt verfügbar', 'it': 'Nessun contenuto disponibile ancora',
        'nl': 'Nog geen inhoud beschikbaar', 'sv': 'Inget innehåll tillgängligt än', 'no': 'Ingen innhold tilgjengelig ennå', 'pl': 'Brak dostępnej treści', 'id': 'Belum ada konten tersedia',
        'ja': 'まだコンテンツがありません', 'ko': '아직 사용 가능한 콘텐츠가 없습니다', 'th': 'ยังไม่มีเนื้อหา', 'vi': 'Chưa có nội dung nào',
    },
    'coming_soon_new_content': {
        'pt-BR': 'Em breve, novos quizzes e subcategorias estarão disponíveis aqui!', 'en': 'Coming soon, new quizzes and subcategories will be available here!', 'es': '¡Próximamente, nuevos quizzes y subcategorías estarán disponibles aquí!', 'fr': 'Bientôt, de nouveaux quiz et sous-catégories seront disponibles ici!', 'de': 'Bald werden hier neue Quiz und Unterkategorien verfügbar sein!', 'it': 'Presto, nuovi quiz e sottocategorie saranno disponibili qui!',
        'nl': 'Binnenkort zullen hier nieuwe quizzen en subcategorieën beschikbaar zijn!', 'sv': 'Snart kommer nya frågesporter och underkategorier att vara tillgängliga här!', 'no': 'Snart vil nye quizer og underkategorier være tilgjengelige her!', 'pl': 'Wkrótce nowe quizy i podkategorie będą dostępne tutaj!', 'id': 'Segera, kuis dan subkategori baru akan tersedia di sini!',
        'ja': 'まもなく、新しいクイズとサブカテゴリがここで利用可能になります！', 'ko': '곧 새로운 퀴즈와 하위 카테고리가 여기에서 사용 가능해집니다!', 'th': 'เร็วๆ นี้ แบบทดสอบและหมวดหมู่ย่อยใหม่จะพร้อมใช้งานที่นี่!', 'vi': 'Sắp có các câu đố và danh mục con mới sẽ có sẵn ở đây!',
    },
    'home': {
        'pt-BR': 'Início', 'en': 'Home', 'es': 'Inicio', 'fr': 'Accueil', 'de': 'Startseite', 'it': 'Home',
        'nl': 'Home', 'sv': 'Hem', 'no': 'Hjem', 'pl': 'Strona główna', 'id': 'Beranda',
        'ja': 'ホーム', 'ko': '홈', 'th': 'หน้าแรก', 'vi': 'Trang chủ',
    },
    
    # Palavras não traduzidas encontradas nos templates
    'inactive': {
        'pt-BR': 'Inativo', 'en': 'Inactive', 'es': 'Inactivo', 'fr': 'Inactif', 'de': 'Inaktiv', 'it': 'Inattivo',
        'nl': 'Inactief', 'sv': 'Inaktiv', 'no': 'Inaktiv', 'pl': 'Nieaktywny', 'id': 'Tidak aktif',
        'ja': '非アクティブ', 'ko': '비활성', 'th': 'ไม่ใช้งาน', 'vi': 'Không hoạt động',
    },
    'quiz_inactive': {
        'pt-BR': 'Quiz Inativo', 'en': 'Quiz Inactive', 'es': 'Quiz Inactivo', 'fr': 'Quiz Inactif', 'de': 'Quiz Inaktiv', 'it': 'Quiz Inattivo',
        'nl': 'Quiz Inactief', 'sv': 'Quiz Inaktiv', 'no': 'Quiz Inaktiv', 'pl': 'Quiz Nieaktywny', 'id': 'Kuis Tidak aktif',
        'ja': 'クイズ非アクティブ', 'ko': '퀴즈 비활성', 'th': 'แบบทดสอบไม่ใช้งาน', 'vi': 'Câu đố không hoạt động',
    },
    'items': {
        'pt-BR': 'itens', 'en': 'items', 'es': 'elementos', 'fr': 'éléments', 'de': 'Elemente', 'it': 'elementi',
        'nl': 'items', 'sv': 'objekt', 'no': 'elementer', 'pl': 'elementy', 'id': 'item',
        'ja': 'アイテム', 'ko': '항목', 'th': 'รายการ', 'vi': 'mục',
    },
    'coming_soon': {
        'pt-BR': 'Em breve', 'en': 'Coming soon', 'es': 'Próximamente', 'fr': 'Bientôt', 'de': 'Demnächst', 'it': 'Prossimamente',
        'nl': 'Binnenkort', 'sv': 'Kommer snart', 'no': 'Kommer snart', 'pl': 'Wkrótce', 'id': 'Segera hadir',
        'ja': '近日公開', 'ko': '곧 출시', 'th': 'เร็วๆ นี้', 'vi': 'Sắp ra mắt',
    },
    'time': {
        'pt-BR': 'Tempo', 'en': 'Time', 'es': 'Tiempo', 'fr': 'Temps', 'de': 'Zeit', 'it': 'Tempo',
        'nl': 'Tijd', 'sv': 'Tid', 'no': 'Tid', 'pl': 'Czas', 'id': 'Waktu',
        'ja': '時間', 'ko': '시간', 'th': 'เวลา', 'vi': 'Thời gian',
    },
    'played_on': {
        'pt-BR': 'Jogado em', 'en': 'Played on', 'es': 'Jugado el', 'fr': 'Joué le', 'de': 'Gespielt am', 'it': 'Giocato il',
        'nl': 'Gespeeld op', 'sv': 'Spelade den', 'no': 'Spilt den', 'pl': 'Grane', 'id': 'Dimainkan pada',
        'ja': 'プレイ日', 'ko': '플레이 날짜', 'th': 'เล่นเมื่อ', 'vi': 'Chơi vào',
    },
    'at': {
        'pt-BR': 'às', 'en': 'at', 'es': 'a las', 'fr': 'à', 'de': 'um', 'it': 'alle',
        'nl': 'om', 'sv': 'kl', 'no': 'kl', 'pl': 'o', 'id': 'pada',
        'ja': 'に', 'ko': '에', 'th': 'ที่', 'vi': 'lúc',
    },
    'hits': {
        'pt-BR': 'ACERTOS', 'en': 'HITS', 'es': 'ACIERTOS', 'fr': 'TOUCHÉS', 'de': 'TREFFER', 'it': 'COLPI',
        'nl': 'RAKERS', 'sv': 'TRÄFFAR', 'no': 'TREFF', 'pl': 'TRAFIONY', 'id': 'HIT',
        'ja': 'ヒット', 'ko': '히트', 'th': 'ฮิต', 'vi': 'Lượt truy cập',
    },
    'rate': {
        'pt-BR': 'TAXA', 'en': 'RATE', 'es': 'TASA', 'fr': 'TAUX', 'de': 'RATE', 'it': 'TASSO',
        'nl': 'TARIEVEN', 'sv': 'TAXA', 'no': 'RATE', 'pl': 'STAWKA', 'id': 'TINGKAT',
        'ja': 'レート', 'ko': '비율', 'th': 'อัตรา', 'vi': 'Tỷ lệ',
    },
    'try_again': {
        'pt-BR': 'Tentar novamente', 'en': 'Try again', 'es': 'Intentar de nuevo', 'fr': 'Réessayer', 'de': 'Erneut versuchen', 'it': 'Riprova',
        'nl': 'Probeer opnieuw', 'sv': 'Försök igen', 'no': 'Prøv igjen', 'pl': 'Spróbuj ponownie', 'id': 'Coba lagi',
        'ja': 'もう一度試す', 'ko': '다시 시도', 'th': 'ลองอีกครั้ง', 'vi': 'Thử lại',
    },
    'explore_quizzes': {
        'pt-BR': 'Explorar Quizzes', 'en': 'Explore Quizzes', 'es': 'Explorar Quizzes', 'fr': 'Explorer les Quiz', 'de': 'Quiz erkunden', 'it': 'Esplora Quiz',
        'nl': 'Verken Quizzen', 'sv': 'Utforska Frågesporter', 'no': 'Utforsk Quizer', 'pl': 'Odkryj Quizy', 'id': 'Jelajahi Kuis',
        'ja': 'クイズを探索', 'ko': '퀴즈 탐색', 'th': 'สำรวจแบบทดสอบ', 'vi': 'Khám phá Câu đố',
    },
    'no_quiz_completed_yet': {
        'pt-BR': 'Nenhum quiz realizado ainda', 'en': 'No quiz completed yet', 'es': 'Aún no se ha completado ningún quiz', 'fr': 'Aucun quiz terminé pour le moment', 'de': 'Noch kein Quiz abgeschlossen', 'it': 'Nessun quiz completato ancora',
        'nl': 'Nog geen quiz voltooid', 'sv': 'Ingen frågesport slutförd än', 'no': 'Ingen quiz fullført ennå', 'pl': 'Brak ukończonych quizów', 'id': 'Belum ada kuis yang diselesaikan',
        'ja': 'まだ完了したクイズはありません', 'ko': '아직 완료된 퀴즈가 없습니다', 'th': 'ยังไม่มีแบบทดสอบที่เสร็จสิ้น', 'vi': 'Chưa có câu đố nào hoàn thành',
    },
    'start_learning_journey': {
        'pt-BR': 'Comece sua jornada de aprendizado agora!', 'en': 'Start your learning journey now!', 'es': '¡Comienza tu viaje de aprendizaje ahora!', 'fr': 'Commencez votre voyage d\'apprentissage maintenant!', 'de': 'Beginnen Sie jetzt Ihre Lernreise!', 'it': 'Inizia il tuo viaggio di apprendimento ora!',
        'nl': 'Begin nu je leerreis!', 'sv': 'Börja din lärresa nu!', 'no': 'Start din læringsreise nå!', 'pl': 'Rozpocznij swoją podróż edukacyjną teraz!', 'id': 'Mulai perjalanan belajar Anda sekarang!',
        'ja': '今すぐ学習の旅を始めましょう！', 'ko': '지금 학습 여정을 시작하세요!', 'th': 'เริ่มต้นการเดินทางเรียนรู้ของคุณตอนนี้!', 'vi': 'Bắt đầu hành trình học tập của bạn ngay bây giờ!',
    },
    'save_progress': {
        'pt-BR': 'Salvar Progresso', 'en': 'Save Progress', 'es': 'Guardar Progreso', 'fr': 'Sauvegarder le Progrès', 'de': 'Fortschritt speichern', 'it': 'Salva Progresso',
        'nl': 'Voortgang opslaan', 'sv': 'Spara framsteg', 'no': 'Lagre fremgang', 'pl': 'Zapisz postęp', 'id': 'Simpan kemajuan',
        'ja': '進捗を保存', 'ko': '진행률 저장', 'th': 'บันทึกความคืบหน้า', 'vi': 'Lưu tiến độ',
    },
    'create_account_login_description': {
        'pt-BR': 'Crie uma conta ou faça login para acompanhar seu progresso, ver seu histórico de pontuações e competir no ranking.', 'en': 'Create an account or log in to track your progress, view your score history and compete in the ranking.', 'es': 'Crea una cuenta o inicia sesión para rastrear tu progreso, ver tu historial de puntuaciones y competir en el ranking.', 'fr': 'Créez un compte ou connectez-vous pour suivre vos progrès, voir votre historique de scores et participer au classement.', 'de': 'Erstellen Sie ein Konto oder melden Sie sich an, um Ihren Fortschritt zu verfolgen, Ihre Punktverlauf anzuzeigen und im Ranking zu konkurrieren.', 'it': 'Crea un account o accedi per tracciare i tuoi progressi, visualizzare la cronologia dei punteggi e competere nella classifica.',
        'nl': 'Maak een account aan of log in om je voortgang bij te houden, je scoregeschiedenis te bekijken en mee te doen aan de ranking.', 'sv': 'Skapa ett konto eller logga in för att spåra din framsteg, visa din poänghistorik och tävla i ranking.', 'no': 'Opprett en konto eller logg inn for å spore fremgangen din, se poenghistorikken din og konkurrere i ranking.', 'pl': 'Utwórz konto lub zaloguj się, aby śledzić swoje postępy, przeglądać historię wyników i konkurować w rankingu.', 'id': 'Buat akun atau masuk untuk melacak kemajuan Anda, melihat riwayat skor Anda dan bersaing di peringkat.',
        'ja': 'アカウントを作成するかログインして、進捗を追跡し、スコア履歴を表示し、ランキングで競争してください。', 'ko': '계정을 만들거나 로그인하여 진행 상황을 추적하고, 점수 기록을 보고, 순위에서 경쟁하세요.', 'th': 'สร้างบัญชีหรือเข้าสู่ระบบเพื่อติดตามความคืบหน้าของคุณ ดูประวัติคะแนนของคุณ และแข่งขันในอันดับ', 'vi': 'Tạo tài khoản hoặc đăng nhập để theo dõi tiến độ của bạn, xem lịch sử điểm số và cạnh tranh trong bảng xếp hạng.',
    },
    'save_results_achievements': {
        'pt-BR': 'Salvar seus resultados e conquistas', 'en': 'Save your results and achievements', 'es': 'Guardar tus resultados y logros', 'fr': 'Sauvegarder vos résultats et réalisations', 'de': 'Speichern Sie Ihre Ergebnisse und Erfolge', 'it': 'Salva i tuoi risultati e successi',
        'nl': 'Bewaar je resultaten en prestaties', 'sv': 'Spara dina resultat och framgångar', 'no': 'Lagre dine resultater og prestasjoner', 'pl': 'Zapisz swoje wyniki i osiągnięcia', 'id': 'Simpan hasil dan pencapaian Anda',
        'ja': '結果と成果を保存', 'ko': '결과와 성과 저장', 'th': 'บันทึกผลลัพธ์และความสำเร็จของคุณ', 'vi': 'Lưu kết quả và thành tích của bạn',
    },
    'compete_global_ranking': {
        'pt-BR': 'Competir no ranking global', 'en': 'Compete in global ranking', 'es': 'Competir en el ranking global', 'fr': 'Participer au classement mondial', 'de': 'Im globalen Ranking konkurrieren', 'it': 'Competere nella classifica globale',
        'nl': 'Concurreren in wereldwijde ranking', 'sv': 'Tävla i global ranking', 'no': 'Konkurrere i global ranking', 'pl': 'Konkurować w globalnym rankingu', 'id': 'Bersaing di peringkat global',
        'ja': 'グローバルランキングで競争', 'ko': '글로벌 순위에서 경쟁', 'th': 'แข่งขันในอันดับโลก', 'vi': 'Cạnh tranh trong bảng xếp hạng toàn cầu',
    },
    'earn_badges_rewards': {
        'pt-BR': 'Ganhar badges e recompensas', 'en': 'Earn badges and rewards', 'es': 'Ganar insignias y recompensas', 'fr': 'Gagner des badges et des récompenses', 'de': 'Abzeichen und Belohnungen verdienen', 'it': 'Guadagnare badge e ricompense',
        'nl': 'Badges en beloningen verdienen', 'sv': 'Tjäna märken och belöningar', 'no': 'Tjene merker og belønninger', 'pl': 'Zarabiaj odznaki i nagrody', 'id': 'Dapatkan lencana dan hadiah',
        'ja': 'バッジと報酬を獲得', 'ko': '배지와 보상 획득', 'th': 'รับเหรียญและรางวัล', 'vi': 'Kiếm huy hiệu và phần thưởng',
    },
    'track_evolution': {
        'pt-BR': 'Acompanhar sua evolução', 'en': 'Track your evolution', 'es': 'Rastrear tu evolución', 'fr': 'Suivre votre évolution', 'de': 'Verfolgen Sie Ihre Entwicklung', 'it': 'Traccia la tua evoluzione',
        'nl': 'Volg je evolutie', 'sv': 'Spåra din utveckling', 'no': 'Spor din evolusjon', 'pl': 'Śledź swoją ewolucję', 'id': 'Lacak evolusi Anda',
        'ja': '進化を追跡', 'ko': '진화 추적', 'th': 'ติดตามการพัฒนาของคุณ', 'vi': 'Theo dõi sự tiến hóa của bạn',
    },
    'create_account': {
        'pt-BR': 'Criar conta', 'en': 'Create account', 'es': 'Crear cuenta', 'fr': 'Créer un compte', 'de': 'Konto erstellen', 'it': 'Crea account',
        'nl': 'Account aanmaken', 'sv': 'Skapa konto', 'no': 'Opprett konto', 'pl': 'Utwórz konto', 'id': 'Buat akun',
        'ja': 'アカウント作成', 'ko': '계정 만들기', 'th': 'สร้างบัญชี', 'vi': 'Tạo tài khoản',
    },
    'enter': {
        'pt-BR': 'Entrar', 'en': 'Enter', 'es': 'Entrar', 'fr': 'Entrer', 'de': 'Eingeben', 'it': 'Entra',
        'nl': 'Invoeren', 'sv': 'Ange', 'no': 'Skriv inn', 'pl': 'Wprowadź', 'id': 'Masuk',
        'ja': '入力', 'ko': '입력', 'th': 'เข้า', 'vi': 'Nhập',
    },
    'share': {
        'pt-BR': 'Compartilhar', 'en': 'Share', 'es': 'Compartir', 'fr': 'Partager', 'de': 'Teilen', 'it': 'Condividi',
        'nl': 'Delen', 'sv': 'Dela', 'no': 'Del', 'pl': 'Udostępnij', 'id': 'Bagikan',
        'ja': '共有', 'ko': '공유', 'th': 'แชร์', 'vi': 'Chia sẻ',
    },
    'tweet': {
        'pt-BR': 'Tweetar', 'en': 'Tweet', 'es': 'Tuitear', 'fr': 'Tweeter', 'de': 'Twittern', 'it': 'Twittare',
        'nl': 'Tweeten', 'sv': 'Tweeta', 'no': 'Tweet', 'pl': 'Tweetnij', 'id': 'Tweet',
        'ja': 'ツイート', 'ko': '트윗', 'th': 'ทวีต', 'vi': 'Tweet',
    },
    'position': {
        'pt-BR': 'Posição', 'en': 'Position', 'es': 'Posición', 'fr': 'Position', 'de': 'Position', 'it': 'Posizione',
        'nl': 'Positie', 'sv': 'Position', 'no': 'Posisjon', 'pl': 'Pozycja', 'id': 'Posisi',
        'ja': '位置', 'ko': '위치', 'th': 'ตำแหน่ง', 'vi': 'Vị trí',
    },
    'beaten': {
        'pt-BR': 'Superados', 'en': 'Beaten', 'es': 'Superados', 'fr': 'Battus', 'de': 'Geschlagen', 'it': 'Battuti',
        'nl': 'Verslagen', 'sv': 'Slagna', 'no': 'Slått', 'pl': 'Pokonani', 'id': 'Dikalahkan',
        'ja': '打ち負かした', 'ko': '이긴', 'th': 'เอาชนะ', 'vi': 'Đánh bại',
    },
    'you_may_also_like': {
        'pt-BR': 'Você também pode gostar', 'en': 'You may also like', 'es': 'También te puede gustar', 'fr': 'Vous pourriez aussi aimer', 'de': 'Das könnte Ihnen auch gefallen', 'it': 'Potrebbe piacerti anche',
        'nl': 'Je vindt dit misschien ook leuk', 'sv': 'Du kanske också gillar', 'no': 'Du liker kanskje også', 'pl': 'Może Ci się też spodobać', 'id': 'Anda mungkin juga menyukai',
        'ja': 'こちらもおすすめ', 'ko': '이것도 좋아할 수 있습니다', 'th': 'คุณอาจชอบด้วย', 'vi': 'Bạn cũng có thể thích',
    },
    'products_selected_for_you': {
        'pt-BR': 'Produtos selecionados especialmente para você', 'en': 'Products selected especially for you', 'es': 'Productos seleccionados especialmente para ti', 'fr': 'Produits sélectionnés spécialement pour vous', 'de': 'Speziell für Sie ausgewählte Produkte', 'it': 'Prodotti selezionati appositamente per te',
        'nl': 'Producten speciaal voor jou geselecteerd', 'sv': 'Produkter valda speciellt för dig', 'no': 'Produkter valgt spesielt for deg', 'pl': 'Produkty wybrane specjalnie dla Ciebie', 'id': 'Produk yang dipilih khusus untuk Anda',
        'ja': 'あなたのために特別に選ばれた製品', 'ko': '당신을 위해 특별히 선택된 제품', 'th': 'ผลิตภัณฑ์ที่เลือกมาเป็นพิเศษสำหรับคุณ', 'vi': 'Sản phẩm được chọn đặc biệt cho bạn',
    },
    'view_product': {
        'pt-BR': 'Ver produto', 'en': 'View product', 'es': 'Ver producto', 'fr': 'Voir le produit', 'de': 'Produkt anzeigen', 'it': 'Visualizza prodotto',
        'nl': 'Bekijk product', 'sv': 'Visa produkt', 'no': 'Se produkt', 'pl': 'Zobacz produkt', 'id': 'Lihat produk',
        'ja': '製品を見る', 'ko': '제품 보기', 'th': 'ดูผลิตภัณฑ์', 'vi': 'Xem sản phẩm',
    },
    'answer_review': {
        'pt-BR': 'Revisão das Respostas', 'en': 'Answer Review', 'es': 'Revisión de Respuestas', 'fr': 'Révision des Réponses', 'de': 'Antwortüberprüfung', 'it': 'Revisione delle Risposte',
        'nl': 'Antwoordbeoordeling', 'sv': 'Svarsgranskning', 'no': 'Svarsoppgjør', 'pl': 'Przegląd odpowiedzi', 'id': 'Tinjauan Jawaban',
        'ja': '回答の確認', 'ko': '답변 검토', 'th': 'การตรวจสอบคำตอบ', 'vi': 'Xem lại câu trả lời',
    },
    'see_questions_check_answers': {
        'pt-BR': 'Veja as questões e confira suas respostas', 'en': 'See the questions and check your answers', 'es': 'Ve las preguntas y revisa tus respuestas', 'fr': 'Voir les questions et vérifier vos réponses', 'de': 'Sehen Sie die Fragen und überprüfen Sie Ihre Antworten', 'it': 'Vedi le domande e controlla le tue risposte',
        'nl': 'Bekijk de vragen en controleer je antwoorden', 'sv': 'Se frågorna och kontrollera dina svar', 'no': 'Se spørsmålene og sjekk svarene dine', 'pl': 'Zobacz pytania i sprawdź swoje odpowiedzi', 'id': 'Lihat pertanyaan dan periksa jawaban Anda',
        'ja': '質問を見て、回答を確認してください', 'ko': '질문을 보고 답변을 확인하세요', 'th': 'ดูคำถามและตรวจสอบคำตอบของคุณ', 'vi': 'Xem các câu hỏi và kiểm tra câu trả lời của bạn',
    },
    'correct': {
        'pt-BR': 'Correto', 'en': 'Correct', 'es': 'Correcto', 'fr': 'Correct', 'de': 'Richtig', 'it': 'Corretto',
        'nl': 'Correct', 'sv': 'Rätt', 'no': 'Riktig', 'pl': 'Poprawny', 'id': 'Benar',
        'ja': '正解', 'ko': '정답', 'th': 'ถูกต้อง', 'vi': 'Đúng',
    },
    'incorrect': {
        'pt-BR': 'Incorreto', 'en': 'Incorrect', 'es': 'Incorrecto', 'fr': 'Incorrect', 'de': 'Falsch', 'it': 'Sbagliato',
        'nl': 'Onjuist', 'sv': 'Fel', 'no': 'Feil', 'pl': 'Niepoprawny', 'id': 'Salah',
        'ja': '不正解', 'ko': '틀림', 'th': 'ไม่ถูกต้อง', 'vi': 'Sai',
    },
    'new_achievement_unlocked': {
        'pt-BR': 'Nova Conquista Desbloqueada!', 'en': 'New Achievement Unlocked!', 'es': '¡Nuevo Logro Desbloqueado!', 'fr': 'Nouvelle Réalisation Débloquée!', 'de': 'Neuer Erfolg freigeschaltet!', 'it': 'Nuovo Successo Sbloccato!',
        'nl': 'Nieuwe Prestatie Ontgrendeld!', 'sv': 'Ny Framgång Upplåst!', 'no': 'Ny Prestasjon Låst Opp!', 'pl': 'Nowe Osiągnięcie Odblokowane!', 'id': 'Pencapaian Baru Terbuka!',
        'ja': '新しい成果が解除されました！', 'ko': '새로운 성과가 잠금 해제되었습니다!', 'th': 'ความสำเร็จใหม่ปลดล็อกแล้ว!', 'vi': 'Thành tích mới đã được mở khóa!',
    },
    'new_achievements': {
        'pt-BR': 'Novas Conquistas!', 'en': 'New Achievements!', 'es': '¡Nuevos Logros!', 'fr': 'Nouvelles Réalisations!', 'de': 'Neue Erfolge!', 'it': 'Nuovi Successi!',
        'nl': 'Nieuwe Prestaties!', 'sv': 'Nya Framgångar!', 'no': 'Nye Prestasjoner!', 'pl': 'Nowe Osiągnięcia!', 'id': 'Pencapaian Baru!',
        'ja': '新しい成果！', 'ko': '새로운 성과!', 'th': 'ความสำเร็จใหม่!', 'vi': 'Thành tích mới!',
    },
    'congratulations_earned': {
        'pt-BR': 'Parabéns! Você conquistou', 'en': 'Congratulations! You earned', 'es': '¡Felicidades! Ganaste', 'fr': 'Félicitations! Vous avez gagné', 'de': 'Herzlichen Glückwunsch! Sie haben verdient', 'it': 'Congratulazioni! Hai guadagnato',
        'nl': 'Gefeliciteerd! Je hebt verdiend', 'sv': 'Grattis! Du tjänade', 'no': 'Gratulerer! Du tjente', 'pl': 'Gratulacje! Zarobiłeś', 'id': 'Selamat! Anda mendapat',
        'ja': 'おめでとうございます！獲得しました', 'ko': '축하합니다! 획득했습니다', 'th': 'ยินดีด้วย! คุณได้รับ', 'vi': 'Chúc mừng! Bạn đã kiếm được',
    },
    'new_badge': {
        'pt-BR': 'uma nova badge', 'en': 'a new badge', 'es': 'una nueva insignia', 'fr': 'un nouveau badge', 'de': 'ein neues Abzeichen', 'it': 'un nuovo badge',
        'nl': 'een nieuwe badge', 'sv': 'ett nytt märke', 'no': 'et nytt merke', 'pl': 'nową odznakę', 'id': 'lencana baru',
        'ja': '新しいバッジ', 'ko': '새로운 배지', 'th': 'เหรียญใหม่', 'vi': 'huy hiệu mới',
    },
    'new_badges': {
        'pt-BR': 'novas badges', 'en': 'new badges', 'es': 'nuevas insignias', 'fr': 'nouveaux badges', 'de': 'neue Abzeichen', 'it': 'nuovi badge',
        'nl': 'nieuwe badges', 'sv': 'nya märken', 'no': 'nye merker', 'pl': 'nowe odznaki', 'id': 'lencana baru',
        'ja': '新しいバッジ', 'ko': '새로운 배지들', 'th': 'เหรียญใหม่', 'vi': 'huy hiệu mới',
    },
    'continue': {
        'pt-BR': 'Continuar', 'en': 'Continue', 'es': 'Continuar', 'fr': 'Continuer', 'de': 'Fortsetzen', 'it': 'Continua',
        'nl': 'Doorgaan', 'sv': 'Fortsätt', 'no': 'Fortsett', 'pl': 'Kontynuuj', 'id': 'Lanjutkan',
        'ja': '続ける', 'ko': '계속', 'th': 'ดำเนินการต่อ', 'vi': 'Tiếp tục',
    },
    'new': {
        'pt-BR': 'NOVO', 'en': 'NEW', 'es': 'NUEVO', 'fr': 'NOUVEAU', 'de': 'NEU', 'it': 'NUOVO',
        'nl': 'NIEUW', 'sv': 'NY', 'no': 'NY', 'pl': 'NOWY', 'id': 'BARU',
        'ja': '新着', 'ko': '새로운', 'th': 'ใหม่', 'vi': 'MỚI',
    },
    'share_achievement': {
        'pt-BR': 'Compartilhe sua conquista!', 'en': 'Share your achievement!', 'es': '¡Comparte tu logro!', 'fr': 'Partagez votre réalisation!', 'de': 'Teilen Sie Ihren Erfolg!', 'it': 'Condividi il tuo successo!',
        'nl': 'Deel je prestatie!', 'sv': 'Dela din framgång!', 'no': 'Del din prestasjon!', 'pl': 'Udostępnij swoje osiągnięcie!', 'id': 'Bagikan pencapaian Anda!',
        'ja': '成果を共有しましょう！', 'ko': '성과를 공유하세요!', 'th': 'แชร์ความสำเร็จของคุณ!', 'vi': 'Chia sẻ thành tích của bạn!',
    },
    'view_all_achievements': {
        'pt-BR': 'Ver todas as suas conquistas', 'en': 'View all your achievements', 'es': 'Ver todos tus logros', 'fr': 'Voir toutes vos réalisations', 'de': 'Alle Ihre Erfolge anzeigen', 'it': 'Visualizza tutti i tuoi successi',
        'nl': 'Bekijk al je prestaties', 'sv': 'Visa alla dina framgångar', 'no': 'Se alle prestasjonene dine', 'pl': 'Zobacz wszystkie swoje osiągnięcia', 'id': 'Lihat semua pencapaian Anda',
        'ja': 'すべての成果を表示', 'ko': '모든 성과 보기', 'th': 'ดูความสำเร็จทั้งหมดของคุณ', 'vi': 'Xem tất cả thành tích của bạn',
    },
    'go_to_profile': {
        'pt-BR': 'Ir para o Perfil', 'en': 'Go to Profile', 'es': 'Ir al Perfil', 'fr': 'Aller au Profil', 'de': 'Zum Profil gehen', 'it': 'Vai al Profilo',
        'nl': 'Ga naar Profiel', 'sv': 'Gå till Profil', 'no': 'Gå til Profil', 'pl': 'Przejdź do Profilu', 'id': 'Pergi ke Profil',
        'ja': 'プロフィールに移動', 'ko': '프로필로 이동', 'th': 'ไปที่โปรไฟล์', 'vi': 'Đi đến Hồ sơ',
    },
}


def translate(key, language='pt-BR', default=None):
    """
    Obtém a tradução de uma chave para o idioma especificado
    
    Args:
        key: Chave da tradução
        language: Código do idioma (pt, en, es, fr, de, it, pt-BR, nl, sv, no, pl, id, ja, ko, th, vi)
        default: Valor padrão caso a tradução não exista
    
    Returns:
        String traduzida ou a chave original se não encontrada
    """
    if key in TRANSLATIONS:
        translations = TRANSLATIONS[key]
        
        # Tenta primeiro com o código completo (ex: pt-BR)
        if language in translations:
            return translations[language]
        
        # Se não encontrar, tenta com o código base (ex: pt de pt-BR)
        base_lang = language.split('-')[0] if '-' in language else language
        if base_lang in translations:
            return translations[base_lang]
        
        # Fallback para pt-BR
        return translations.get('pt-BR', default or key)
    
    return default or key
