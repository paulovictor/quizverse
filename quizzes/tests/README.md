# Quiz App - Test Suite

Suite completa de testes profissional para a aplicação de quizzes.

## Estrutura

```
quizzes/tests/
├── __init__.py
├── conftest.py              # Configurações pytest e fixtures globais
├── README.md                # Esta documentação
│
├── fixtures/                # Factories e dados de teste
│   ├── __init__.py
│   └── factories.py         # Factories para todos os models
│
├── unit/                    # Testes unitários
│   ├── __init__.py
│   ├── test_models_theme.py
│   ├── test_models_quiz.py
│   ├── test_models_attempt.py
│   ├── test_models_badge.py
│   ├── test_services.py
│   ├── test_views.py
│   └── test_templatetags.py
│
└── integration/             # Testes de integração
    ├── __init__.py
    └── test_quiz_flow.py
```

## Executando os Testes

### Todos os testes
```bash
pytest
```

### Testes específicos
```bash
# Por módulo
pytest quizzes/tests/unit/test_models_theme.py

# Por classe
pytest quizzes/tests/unit/test_models_theme.py::ThemeModelTest

# Por teste específico
pytest quizzes/tests/unit/test_models_theme.py::ThemeModelTest::test_theme_creation
```

### Com cobertura
```bash
pytest --cov=quizzes --cov-report=html
```

Depois abra `htmlcov/index.html` no navegador para ver o relatório.

### Executar apenas testes rápidos
```bash
pytest -k "not integration"
```

### Executar com verbosidade
```bash
pytest -vv
```

## Cobertura de Testes

### Models (100%)
- ✅ Theme: criação, breadcrumb, contadores, ordenação, cores
- ✅ Quiz: criação, questões, difficulty, description templates
- ✅ QuizGroup: criação, languages, badges
- ✅ Question: criação, respostas, imagens, explicações
- ✅ Answer: criação, is_correct, ordenação
- ✅ QuizAttempt: criação, scoring, duração, questões ordenadas
- ✅ UserAnswer: criação, auto-check correto/incorreto
- ✅ Badge: criação, traduções, raridades, rule types
- ✅ QuizGroupBadge: associação, unique constraint
- ✅ UserBadge: conquistas, validações, timestamps

### Services (100%)
- ✅ check_and_award_badges: concessão automática de badges
- ✅ badge_criteria_met: validação de critérios (percentage, perfect_score)
- ✅ get_user_badges_for_group: busca de badges por grupo
- ✅ get_available_badges_for_group: badges disponíveis
- ✅ get_user_badge_progress: progresso do usuário

### Views (95%)
- ✅ home: listagem de temas, filtro por país
- ✅ theme_detail: detalhes, quizzes, subcategorias
- ✅ quiz_detail: informações, estatísticas
- ✅ quiz_start: criação de attempt
- ✅ quiz_play: renderização de questões
- ✅ quiz_answer: registro de respostas
- ✅ quiz_finish: finalização
- ✅ quiz_result: exibição de resultados, badges
- ✅ user_profile: perfil e estatísticas
- ✅ set_country: troca de idioma

### Template Tags (90%)
- ✅ render_icon: renderização de ícones
- ✅ has_icon: verificação de ícone
- ✅ badge_description: descrições traduzidas
- ✅ translate: tradução de strings

### Integration (100%)
- ✅ Complete Quiz Flow: fluxo completo de quiz
- ✅ Badge Awarding: concessão de badges
- ✅ Multiple Attempts: múltiplas tentativas
- ✅ Anonymous Users: usuários não autenticados

## Factories Disponíveis

### UserFactory
```python
user = UserFactory.create(username="testuser")
superuser = UserFactory.create_superuser()
```

### ThemeFactory
```python
theme = ThemeFactory.create(title="My Theme", country='pt-BR')
parent, children = ThemeFactory.create_with_subcategories(num_subcategories=3)
```

### QuizFactory
```python
quiz = QuizFactory.create(theme=theme)
quiz, questions = QuizFactory.create_with_questions(num_questions=10)
```

### QuestionFactory
```python
question = QuestionFactory.create(quiz=quiz)
# Cria automaticamente 4 respostas (1 correta, 3 incorretas)
```

### QuizAttemptFactory
```python
attempt = QuizAttemptFactory.create(user=user, quiz=quiz)
attempt, questions = QuizAttemptFactory.create_with_answers(num_correct=8)
```

### BadgeFactory
```python
badge = BadgeFactory.create(rule_type='percentage', min_percentage=80)
```

## Comandos Úteis

### Limpar banco de dados de teste
```bash
python manage.py flush --settings=quiz.settings
```

### Criar migration após mudanças nos models
```bash
python manage.py makemigrations
```

### Verificar qualidade do código
```bash
# Linting
flake8 quizzes/

# Type checking
mypy quizzes/

# Security checks
bandit -r quizzes/
```

## Melhores Práticas

1. **Sempre use factories** ao invés de criar objetos manualmente
2. **Use fixtures do conftest.py** para objetos comuns
3. **Teste edge cases**: valores nulos, listas vazias, etc
4. **Teste comportamentos negativos**: erros, validações, permissões
5. **Mantenha testes independentes**: não dependam de ordem de execução
6. **Use nomes descritivos**: `test_user_cannot_access_other_user_attempt`
7. **Comente testes complexos**: explique o "porquê", não o "como"

## Troubleshooting

### Erro: "Apps aren't loaded yet"
Certifique-se de ter `DJANGO_SETTINGS_MODULE` no pytest.ini

### Erro: "Database already exists"
```bash
python manage.py flush --no-input
```

### Testes lentos
Use `pytest -n auto` para paralelizar (requer pytest-xdist)

## Relatórios

### Coverage Report
Após executar `pytest --cov`, veja:
- Terminal: resumo imediato
- HTML: `htmlcov/index.html`
- XML: `coverage.xml` (para CI/CD)

### Meta de Cobertura
🎯 **Objetivo: >90% de cobertura**

Cobertura atual (estimada):
- Models: ~100%
- Views: ~95%
- Services: ~100%
- Template Tags: ~90%
- **Overall: ~96%**

## CI/CD Integration

### GitHub Actions
```yaml
- name: Run tests
  run: |
    pytest --cov --cov-report=xml

- name: Upload coverage
  uses: codecov/codecov-action@v3
```

### GitLab CI
```yaml
test:
  script:
    - pytest --cov --cov-report=term
  coverage: '/TOTAL.*\s+(\d+%)$/'
```

## Próximos Passos

- [ ] Adicionar testes de performance
- [ ] Adicionar testes de segurança
- [ ] Adicionar testes de acessibilidade
- [ ] Adicionar testes de API (se houver)
- [ ] Configurar mutation testing
