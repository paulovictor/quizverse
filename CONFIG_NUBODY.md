# ⚙️ Configuração para nubody.com.br

## 🌐 Configurar Domínio Personalizado no Heroku

### 1. Adicionar domínio ao Heroku

```bash
# Adicionar domínio principal
heroku domains:add nubody.com.br

# Adicionar subdomínio www (opcional)
heroku domains:add www.nubody.com.br
```

### 2. Configurar ALLOWED_HOSTS

```bash
heroku config:set ALLOWED_HOSTS='nubody.com.br,www.nubody.com.br,.herokuapp.com'
```

### 3. Obter DNS target do Heroku

```bash
heroku domains
```

Você verá algo como:
```
=== seu-app Custom Domains
Domain Name        DNS Target
─────────────────  ─────────────────────────────────
nubody.com.br      xxx-yyy-zzz.herokudns.com
www.nubody.com.br  xxx-yyy-zzz.herokudns.com
```

### 4. Configurar DNS no seu provedor (Registro.br, Cloudflare, etc)

**Para nubody.com.br (domínio raiz):**

Opção A - CNAME (se o provedor permitir):
```
Tipo: CNAME
Nome: @
Valor: xxx-yyy-zzz.herokudns.com
```

Opção B - ALIAS/ANAME:
```
Tipo: ALIAS ou ANAME
Nome: @
Valor: xxx-yyy-zzz.herokudns.com
```

**Para www.nubody.com.br:**
```
Tipo: CNAME
Nome: www
Valor: xxx-yyy-zzz.herokudns.com
```

### 5. Atualizar Site no Django Admin

Acesse: `https://nubody.com.br/admin/sites/site/1/change/`

- **Domain name:** `nubody.com.br`
- **Display name:** `Quiz App - Nubody`

### 6. Atualizar Social Auth Redirect URIs

**Google Console:**
- Adicione: `https://nubody.com.br/accounts/google/login/callback/`
- Adicione: `https://www.nubody.com.br/accounts/google/login/callback/`

**Facebook Developers:**
- Adicione: `https://nubody.com.br/accounts/facebook/login/callback/`
- Adicione: `https://www.nubody.com.br/accounts/facebook/login/callback/`

## 🔒 SSL/HTTPS

O Heroku fornece SSL automático! Após configurar o domínio, o HTTPS estará ativo automaticamente. 🎉

## ✅ Verificar configuração

```bash
# Ver variáveis de ambiente
heroku config

# Ver domínios configurados
heroku domains

# Testar o site
curl -I https://nubody.com.br
```

## 📝 Checklist Final

- [ ] Domínio adicionado no Heroku
- [ ] ALLOWED_HOSTS configurado
- [ ] DNS configurado no provedor
- [ ] Site atualizado no Django Admin
- [ ] Redirect URIs atualizados (Google/Facebook)
- [ ] SSL funcionando (HTTPS)
- [ ] Testado em: nubody.com.br e www.nubody.com.br

## 🚀 Propagação DNS

Após configurar o DNS, pode levar de **alguns minutos a 48 horas** para propagar mundialmente.

Verifique em: https://www.whatsmydns.net/#CNAME/nubody.com.br

## 💡 Dica

Se você usa Cloudflare, ative o "proxy" (nuvem laranja) para CDN e proteção DDoS!

