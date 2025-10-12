# Implementação do Sistema de Quiz

## 📋 Estrutura Implementada

### Models Criados

1. **Theme** (Tema)
   - UUID, title, description, slug, active
   - Exemplo: "flamengo", "harrypotter"

2. **Quiz** (Quiz)
   - UUID, theme (FK), title, slug, description
   - difficulty (fácil/médio/difícil)
   - time_limit, active, order
   - Exemplo: "quiz-1", "quiz-sonserina"

3. **Question** (Pergunta)
   - UUID, quiz (FK), text, explanation
   - order, points

4. **Answer** (Alternativa)
   - UUID, question (FK), text, is_correct, order

5. **QuizAttempt** (Tentativa)
   - UUID, user (FK nullable), quiz (FK)
   - session_key (para anônimos)
   - question_order (JSONField) - ordem randomizada
   - started_at, completed_at, score, max_score

6. **UserAnswer** (Resposta do Usuário)
   - UUID, attempt (FK), question (FK), selected_answer (FK)
   - is_correct, points_earned, answered_at

## 🎯 Funcionalidades Implementadas

### ✅ Perguntas Aleatórias
- A ordem das perguntas é randomizada quando o quiz é iniciado
- A ordem é salva no QuizAttempt.question_order
- Garante que o usuário vê as mesmas perguntas na mesma ordem durante toda a tentativa

### ✅ Alternativas Aleatórias
- As alternativas também são embaralhadas ao exibir cada pergunta

### ✅ Sistema de Pontuação
- Cada pergunta tem um valor de pontos
- Score é calculado automaticamente ao finalizar
- Percentual de acerto é exibido

### ✅ Usuários Anônimos + Login Posterior
- Usuários não logados podem fazer o quiz
- Ao finalizar, é exibida uma opção para fazer login
- Após login, a tentativa pode ser associada ao usuário (via claim_attempt)

### ✅ Histórico de Tentativas
- Usuários logados veem suas 5 últimas tentativas

## 📍 URLs Implementadas

```
/flamengo/                              → Lista quizzes do tema
/flamengo/quiz-1/                       → Detalhes do quiz
/flamengo/quiz-1/start/                 → Iniciar quiz (POST)
/attempt/<uuid>/play/                   → Jogar quiz
/attempt/<uuid>/answer/                 → Enviar resposta (POST/AJAX)
/attempt/<uuid>/finish/                 → Finalizar quiz
/attempt/<uuid>/resultado/              → Ver resultado
/attempt/<uuid>/claim/                  → Associar ao usuário (POST)
```

## 🎨 Templates Criados

1. **theme_detail.html** - Lista quizzes do tema
2. **quiz_detail.html** - Detalhes e botão para iniciar
3. **quiz_play.html** - Interface para responder perguntas
4. **quiz_result.html** - Resultado com revisão e prompt de login

## 🔐 Permissões

- Apenas o usuário que criou a tentativa pode acessá-la
- Para anônimos, verifica session_key
- Para logados, verifica user

## 🎭 Admin

Todos os models têm interfaces admin completas com:
- Inlines (Answer dentro de Question, Question dentro de Quiz)
- Filtros e busca
- Campos readonly onde apropriado
- Visualização de tentativas e respostas

## 🚀 Como Usar

### 1. Criar um Superuser (se não tiver)
```bash
uv run python manage.py createsuperuser
```

### 2. Iniciar o Servidor
```bash
uv run python manage.py runserver
```

### 3. Acessar o Admin
```
http://localhost:8000/admin/
```

### 4. Criar Conteúdo
1. Crie um **Theme** (ex: slug="flamengo", title="Flamengo")
2. Crie um **Quiz** associado ao theme (ex: slug="quiz-1")
3. Adicione **Questions** ao quiz
4. Adicione **Answers** a cada question (marque uma como is_correct=True)

### 5. Testar
```
http://localhost:8000/flamengo/
http://localhost:8000/flamengo/quiz-1/
```

## 🔍 Recursos Especiais

### Randomização
- `QuizAttempt.initialize_question_order()` - randomiza perguntas
- `random.shuffle(answers)` na view - randomiza alternativas

### Auto-cálculo
- `UserAnswer.save()` - calcula is_correct e points_earned automaticamente
- `QuizAttempt.get_score_percentage()` - calcula percentual

### Segurança
- CSRF token em todos os forms
- Verificação de permissão em todas as views
- Session-based para anônimos

## 📊 Próximas Melhorias Possíveis

- [ ] Sistema de autenticação completo (login/register)
- [ ] Timer funcional para quizzes com time_limit
- [ ] Ranking de melhores pontuações
- [ ] Badges e conquistas
- [ ] Compartilhamento de resultados
- [ ] Modo multiplayer/competitivo
- [ ] Estatísticas detalhadas por tema
- [ ] Export de resultados (PDF/CSV)
- [ ] API REST para mobile
- [ ] PWA support

## 🐛 Observações

- O botão "Fazer Login e Salvar" no resultado atualmente mostra um alert
- Para implementar login completo, adicione django.contrib.auth.urls e templates de login
- A funcionalidade claim_attempt já está implementada e funcional

