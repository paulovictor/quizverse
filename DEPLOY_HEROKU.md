# 🚀 Deploy no Heroku - Guia Completo

## ✅ Arquivos já criados:
- ✅ `Procfile` - Configura o servidor Gunicorn
- ✅ `runtime.txt` - Define a versão do Python
- ✅ `requirements.txt` - Lista todas as dependências
- ✅ `.gitignore` - Ignora arquivos desnecessários
- ✅ `settings.py` - Configurado para produção

## 📋 Pré-requisitos

1. **Conta no Heroku** - https://signup.heroku.com/
2. **Heroku CLI instalado** - https://devcenter.heroku.com/articles/heroku-cli
3. **Git instalado**

## 🔧 Passo a Passo

### 1. Instalar Heroku CLI (se ainda não tiver)

**Mac:**
```bash
brew tap heroku/brew && brew install heroku
```

**Windows:**
Baixe o instalador: https://devcenter.heroku.com/articles/heroku-cli

**Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

### 2. Fazer login no Heroku

```bash
heroku login
```

### 3. Inicializar Git (se ainda não tiver)

```bash
cd /Users/paulo/work/quiz
git init
git add .
git commit -m "Initial commit - Quiz App"
```

### 4. Criar app no Heroku

```bash
heroku create seu-quiz-app-nome
```

Ou deixe o Heroku gerar um nome aleatório:
```bash
heroku create
```

### 5. Adicionar PostgreSQL

```bash
heroku addons:create heroku-postgresql:essential-0
```

### 6. Configurar variáveis de ambiente

```bash
# Gerar uma nova SECRET_KEY segura
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Configurar no Heroku (substitua NOVA_SECRET_KEY pela gerada acima)
heroku config:set SECRET_KEY='NOVA_SECRET_KEY_AQUI'
heroku config:set DEBUG=False

# Configure seu domínio personalizado (exemplo: nubody.com.br)
# Se usar domínio personalizado:
heroku config:set ALLOWED_HOSTS='nubody.com.br,www.nubody.com.br,.herokuapp.com'

# OU se usar apenas Heroku:
heroku config:set ALLOWED_HOSTS='.herokuapp.com'
```

### 7. Deploy!

```bash
git push heroku main
```

Ou se sua branch principal é `master`:
```bash
git push heroku master
```

### 8. Executar migrações

```bash
heroku run python manage.py migrate
```

### 9. Criar superuser

```bash
heroku run python manage.py createsuperuser
```

### 10. Coletar arquivos estáticos

```bash
heroku run python manage.py collectstatic --noinput
```

### 11. Popular dados de exemplo (opcional)

```bash
heroku run python populate_sample_data.py
heroku run python populate_products.py
```

### 12. Abrir o app!

```bash
heroku open
```

## 🔗 URLs Importantes

Depois do deploy, suas URLs serão:
- **Home:** `https://seu-app.herokuapp.com/`
- **Admin:** `https://seu-app.herokuapp.com/admin/`
- **Login:** `https://seu-app.herokuapp.com/accounts/login/`

## 🐛 Comandos Úteis

### Ver logs
```bash
heroku logs --tail
```

### Executar comandos Django
```bash
heroku run python manage.py comando
```

### Reiniciar app
```bash
heroku restart
```

### Ver informações do app
```bash
heroku info
```

### Abrir console Python
```bash
heroku run python manage.py shell
```

## 🔒 Configurar Login Social (Google/Facebook)

### 1. Atualizar redirect URIs nos consoles

**Google Console:**
- Adicione: `https://seu-app.herokuapp.com/accounts/google/login/callback/`

**Facebook Developers:**
- Adicione: `https://seu-app.herokuapp.com/accounts/facebook/login/callback/`

### 2. Atualizar Site no Django Admin

Acesse: `https://seu-app.herokuapp.com/admin/sites/site/1/change/`
- **Domain name:** `seu-app.herokuapp.com`
- **Display name:** `Quiz App`

### 3. Adicionar Social Applications

Acesse: `https://seu-app.herokuapp.com/admin/socialaccount/socialapp/`

Adicione Google e Facebook com as credenciais corretas.

## ⚡ Deploy Automático com GitHub (Opcional)

1. Conecte seu repositório GitHub ao Heroku
2. No dashboard do Heroku, vá em **Deploy**
3. Conecte ao GitHub
4. Ative **Automatic Deploys** da branch main

## 📊 Monitoramento

### Ver uso de recursos
```bash
heroku ps
```

### Ver addons
```bash
heroku addons
```

### Ver banco de dados
```bash
heroku pg:info
```

## 🆘 Troubleshooting

### App não está respondendo
```bash
heroku logs --tail
heroku restart
```

### Erro de banco de dados
```bash
heroku pg:reset DATABASE_URL
heroku run python manage.py migrate
```

### Limpar cache
```bash
heroku repo:purge_cache -a seu-app-nome
```

## 💰 Custos

- **Dyno básico:** ~$5-7/mês
- **PostgreSQL Essential:** ~$5/mês
- **Total:** ~$10-12/mês

Ou use o free tier (com limitações):
```bash
heroku ps:scale web=1
```

## 🎉 Pronto!

Seu Quiz App agora está no ar! 🚀

Acesse: https://seu-app.herokuapp.com

