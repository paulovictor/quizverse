# 🚀 PLANO DE MIGRAÇÃO: Quiz UUID → Slug Primary Key

## 📋 **ANÁLISE INICIAL**

### **Modelos que referenciam Quiz:**
1. **Question** → `quiz = ForeignKey(Quiz)`
2. **QuizAttempt** → `quiz = ForeignKey(Quiz)`
3. **UserAnswer** → `attempt = ForeignKey(QuizAttempt)` (indireto)

### **Arquivos que usam quiz.id/quiz.pk:**
1. `quizzes/tests/unit/test_models_theme.py` - linha 197
2. `quizzes/tests/unit/test_models_quiz.py` - linha 80
3. `setup/create_quiz.py` - linha 374

### **URLs que usam quiz_slug:**
- `quiz_detail.html` - já usa `quiz.slug`
- `quiz_play.html` - já usa `quiz.slug`
- `quiz_result.html` - já usa `quiz.slug`

---

## 🎯 **ESTRATÉGIA DE MIGRAÇÃO**

### **FASE 1: PREPARAÇÃO**
1. ✅ Verificar se todos os quizzes têm slug único
2. ✅ Atualizar scripts de criação para garantir slugs únicos
3. ✅ Atualizar testes para usar slug ao invés de id

### **FASE 2: MIGRAÇÃO DO MODELO**
1. ✅ Alterar modelo Quiz para usar slug como primary key
2. ✅ Atualizar foreign keys para usar `to_field='slug'`
3. ✅ Criar migração que remove UUID e define slug como PK

### **FASE 3: ATUALIZAÇÃO DE CÓDIGO**
1. ✅ Atualizar views que usam quiz.id
2. ✅ Atualizar templates que referenciam quiz.id
3. ✅ Atualizar scripts de fixture
4. ✅ Atualizar testes

### **FASE 4: DEPLOY E TESTE**
1. ✅ Aplicar migração em produção
2. ✅ Verificar funcionamento
3. ✅ Limpar código desnecessário

---

## 📝 **PLANO DETALHADO STEP-BY-STEP**

### **STEP 1: Verificar e Corrigir Slugs Existentes**
```bash
# Verificar se todos os quizzes têm slug
python manage.py shell -c "
from quizzes.models import Quiz
quizzes_sem_slug = Quiz.objects.filter(slug__isnull=True)
print(f'Quizzes sem slug: {quizzes_sem_slug.count()}')
"
```

### **STEP 2: Atualizar Scripts de Criação**
- ✅ Modificar `setup/create_quiz.py` para garantir slugs únicos
- ✅ Atualizar `setup/create_questions.py` se necessário

### **STEP 3: Atualizar Testes**
- ✅ Corrigir `test_models_theme.py` linha 197
- ✅ Corrigir `test_models_quiz.py` linha 80
- ✅ Verificar outros testes que usam quiz.id

### **STEP 4: Atualizar Modelo Quiz**
```python
# Em quizzes/models.py
class Quiz(models.Model):
    # Remover: id = models.UUIDField(primary_key=True, ...)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, primary_key=True)  # ← Mudança aqui
    # ... resto dos campos
```

### **STEP 5: Atualizar Foreign Keys**
```python
# Em quizzes/models.py
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', to_field='slug')

class QuizAttempt(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts', to_field='slug')
```

### **STEP 6: Criar Migração**
```bash
# Remover todas as migrações existentes
rm quizzes/migrations/0*.py

# Criar nova migração inicial
python manage.py makemigrations quizzes --name initial_with_slug_pk
```

### **STEP 7: Atualizar Views**
- ✅ Verificar se views usam quiz.id (provavelmente não)
- ✅ Confirmar que URLs já usam quiz.slug

### **STEP 8: Atualizar Scripts de Fixture**
- ✅ Modificar `setup/create_quiz.py` para usar quiz.slug
- ✅ Testar exportação de fixtures

### **STEP 9: Testes Locais**
```bash
# Executar todos os testes
make test

# Verificar funcionamento básico
python manage.py runserver
```

### **STEP 10: Deploy em Produção**
```bash
# Fazer backup do banco
heroku pg:backups:capture

# Deploy
git add .
git commit -m "feat: migrate Quiz primary key from UUID to slug"
git push heroku main

# Verificar se migração foi aplicada
heroku run python manage.py showmigrations
```

---

## ⚠️ **PONTOS DE ATENÇÃO**

### **1. Dependências em Cascata**
- Question → Quiz (FK)
- QuizAttempt → Quiz (FK)
- UserAnswer → QuizAttempt → Quiz (FK indireto)

### **2. Fixtures Existentes**
- Verificar se fixtures de quiz usam UUIDs
- Atualizar para usar slugs

### **3. URLs e Views**
- Confirmar que URLs já usam `quiz_slug`
- Verificar se views acessam quiz.id

### **4. Testes**
- Atualizar todos os testes que usam quiz.id
- Verificar factories de teste

---

## 🔄 **ORDEM DE EXECUÇÃO**

1. **Preparação** (Steps 1-3)
2. **Modelo** (Steps 4-6)
3. **Código** (Steps 7-8)
4. **Testes** (Step 9)
5. **Deploy** (Step 10)

---

## 📊 **ESTIMATIVA DE TEMPO**

- **Preparação**: 30 min
- **Modelo**: 45 min
- **Código**: 30 min
- **Testes**: 30 min
- **Deploy**: 15 min
- **Total**: ~2.5 horas

---

## 🎯 **RESULTADO ESPERADO**

- ✅ Quiz usa slug como primary key
- ✅ Foreign keys funcionam corretamente
- ✅ Fixtures usam slugs
- ✅ URLs continuam funcionando
- ✅ Testes passam
- ✅ Produção funciona normalmente

---

## 📋 **CHECKLIST FINAL**

- [ ] Todos os quizzes têm slug único
- [ ] Scripts de criação atualizados
- [ ] Testes corrigidos
- [ ] Modelo Quiz atualizado
- [ ] Foreign keys com to_field='slug'
- [ ] Migração criada
- [ ] Views verificadas
- [ ] Scripts de fixture atualizados
- [ ] Testes locais passando
- [ ] Deploy em produção
- [ ] Verificação pós-deploy
