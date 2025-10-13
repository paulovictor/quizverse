# Configuração DNS para quizverso.com

## ✅ Status no Heroku
- Domínios adicionados com sucesso
- ALLOWED_HOSTS atualizado
- Aplicação reiniciada (v23)

## 📋 Configurações DNS no Registrador

Configure os seguintes registros DNS no painel do seu registrador de domínio (ex: Registro.br, GoDaddy, Cloudflare, etc):

### 1. Domínio Principal (quizverso.com)
**Tipo:** ALIAS ou ANAME (se suportado) ou A
**Nome/Host:** @ (ou deixe em branco)
**Valor/Target:** `fitted-cucumber-dkk141hbfuooxdymyref6f1s.herokudns.com`
**TTL:** 3600 (ou padrão)

> ⚠️ **Nota:** Alguns registradores não suportam ALIAS/ANAME. Neste caso, use CNAME apontando para o domínio do Heroku, ou consulte a documentação do seu registrador.

### 2. Subdomínio WWW (www.quizverso.com)
**Tipo:** CNAME
**Nome/Host:** www
**Valor/Target:** `metaphysical-lake-rgjartn03ixrhpl0vuyzxsuj.herokudns.com`
**TTL:** 3600 (ou padrão)

## 🔒 SSL/HTTPS
O Heroku gerencia automaticamente os certificados SSL gratuitos via Let's Encrypt. Após configurar o DNS:
1. Aguarde a propagação DNS (pode levar até 48h, geralmente 1-2h)
2. O Heroku emitirá automaticamente o certificado SSL
3. Seu site estará disponível via HTTPS

## ✓ Verificar Configuração
Para verificar se o DNS está propagado, use:
```bash
# Verificar domínio principal
heroku domains:wait 'quizverso.com' -a quiz-webapp

# Verificar www
heroku domains:wait 'www.quizverso.com' -a quiz-webapp
```

Ou use ferramentas online como:
- https://dnschecker.org/
- https://www.whatsmydns.net/

## 📊 Domínios Ativos na Aplicação

1. **quizverso.com** → fitted-cucumber-dkk141hbfuooxdymyref6f1s.herokudns.com
2. **www.quizverso.com** → metaphysical-lake-rgjartn03ixrhpl0vuyzxsuj.herokudns.com
3. **nubody.com.br** → secret-loon-mwfwidzmf0z3zlk97q7xdm9e.herokudns.com
4. **www.nubody.com.br** → defined-llama-nojwysigvc3nno45cpmiku49.herokudns.com
5. **quiz-webapp-a6102da847af.herokuapp.com** (domínio original do Heroku)

## 🔧 Comandos Úteis

```bash
# Listar todos os domínios
heroku domains -a quiz-webapp

# Ver configurações DNS
heroku config:get ALLOWED_HOSTS -a quiz-webapp

# Aguardar certificado SSL
heroku certs:auto:wait -a quiz-webapp
```

## 📝 Próximos Passos

1. ✅ Acessar o painel do seu registrador de domínio (quizverso.com)
2. ✅ Adicionar os registros DNS acima
3. ⏳ Aguardar propagação (1-2 horas geralmente)
4. ✅ Testar acesso: https://quizverso.com e https://www.quizverso.com
5. ✅ Verificar SSL automático do Heroku

## ⚠️ Importante
- **NÃO DELETE** os registros antigos até confirmar que os novos estão funcionando
- Mantenha backup das configurações DNS antigas
- Teste ambos os domínios (com e sem www) após configuração

