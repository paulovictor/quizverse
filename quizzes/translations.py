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
    
    # Home Page
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
        'pt-BR': 'perguntas', 'en': 'questions', 'es': 'preguntas', 'fr': 'questions', 'de': 'Fragen', 'it': 'domande',
        'nl': 'vragen', 'sv': 'frågor', 'no': 'spørsmål', 'pl': 'pytania', 'id': 'pertanyaan',
        'ja': '質問', 'ko': '질문', 'th': 'คำถาม', 'vi': 'câu hỏi',
    },
    'subcategories': {
        'pt-BR': 'subcategorias', 'en': 'subcategories', 'es': 'subcategorías', 'fr': 'sous-catégories', 'de': 'Unterkategorien', 'it': 'sottocategorie',
        'nl': 'subcategorieën', 'sv': 'underkategorier', 'no': 'underkategorier', 'pl': 'podkategorie', 'id': 'subkategori',
        'ja': 'サブカテゴリー', 'ko': '하위 카테고리', 'th': 'หมวดหมู่ย่อย', 'vi': 'danh mục con',
    },
    
    # Quiz Detail
    'questions': {
        'pt-BR': 'perguntas', 'en': 'questions', 'es': 'preguntas', 'fr': 'questions', 'de': 'Fragen', 'it': 'domande',
        'nl': 'vragen', 'sv': 'frågor', 'no': 'spørsmål', 'pl': 'pytania', 'id': 'pertanyaan',
        'ja': '質問', 'ko': '질문', 'th': 'คำถาม', 'vi': 'câu hỏi',
    },
    'estimated_time': {
        'pt-BR': 'min', 'en': 'min', 'es': 'min', 'fr': 'min', 'de': 'Min', 'it': 'min',
        'nl': 'min', 'sv': 'min', 'no': 'min', 'pl': 'min', 'id': 'mnt',
        'ja': '分', 'ko': '분', 'th': 'นาที', 'vi': 'phút',
    },
    'difficulty': {
        'pt-BR': 'Dificuldade', 'en': 'Difficulty', 'es': 'Dificultad', 'fr': 'Difficulté', 'de': 'Schwierigkeit', 'it': 'Difficoltà',
        'nl': 'Moeilijkheidsgraad', 'sv': 'Svårighetsgrad', 'no': 'Vanskelighetsgrad', 'pl': 'Trudność', 'id': 'Kesulitan',
        'ja': '難易度', 'ko': '난이도', 'th': 'ความยาก', 'vi': 'Độ khó',
    },
    'start_quiz': {
        'pt-BR': 'Iniciar Quiz', 'en': 'Start Quiz', 'es': 'Iniciar Quiz', 'fr': 'Commencer le Quiz', 'de': 'Quiz starten', 'it': 'Inizia Quiz',
        'nl': 'Quiz starten', 'sv': 'Starta Quiz', 'no': 'Start Quiz', 'pl': 'Rozpocznij Quiz', 'id': 'Mulai Kuis',
        'ja': 'クイズ開始', 'ko': '퀴즈 시작', 'th': 'เริ่มแบบทดสอบ', 'vi': 'Bắt đầu Câu đố',
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
        'pt-BR': 'Pergunta', 'en': 'Question', 'es': 'Pregunta', 'fr': 'Question', 'de': 'Frage', 'it': 'Domanda',
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
