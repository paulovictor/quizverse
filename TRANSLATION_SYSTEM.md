# 🌍 Sistema de Tradução - Quizverso

## Visão Geral

Implementamos um **sistema de tradução simples e eficiente** usando **Template Tags customizadas** e **dicionários Python**.

---

## 📁 Arquivos Principais

### 1. `/quizzes/translations.py`
- **Dicionário central** com todas as traduções
- Estrutura: `{'chave': {'pt-BR': 'texto', 'en': 'text', ...}}`
- Função `translate(key, language, default)` para buscar traduções

### 2. `/quizzes/templatetags/icon_tags.py`
- Template tag `{% t 'chave' %}` - usa idioma do contexto automaticamente
- Filtro `|translate:language` - traduz com idioma específico

---

## 🚀 Como Usar nos Templates

### Opção 1: Template Tag (Recomendado)
```django
{% load icon_tags %}

<h1>{% t 'welcome_title' %}</h1>
<p>{% t 'welcome_subtitle' %}</p>
```
**Vantagem:** Usa automaticamente o `current_language` do contexto

### Opção 2: Filtro
```django
{% load icon_tags %}

<h1>{{ 'welcome_title'|translate:current_language }}</h1>
```
**Vantagem:** Mais explícito, útil para traduzir variáveis

---

## ➕ Adicionar Novas Traduções

### Passo 1: Adicione no dicionário `TRANSLATIONS`

```python
# quizzes/translations.py

TRANSLATIONS = {
    # ... outras traduções
    'nova_chave': {
        'pt-BR': 'Texto em Português',
        'en': 'Text in English',
        'es': 'Texto en Español',
        'fr': 'Texte en Français',
        'de': 'Text auf Deutsch',
        'it': 'Testo in Italiano',
    },
}
```

### Passo 2: Use no template

```django
{% t 'nova_chave' %}
```

**Pronto!** Não precisa reiniciar o servidor (em desenvolvimento).

---

## 🎯 Idiomas Suportados

| Código | Idioma | Emoji |
|--------|--------|-------|
| `pt-BR` | Português (Brasil) | 🇧🇷 |
| `en` | English | 🇺🇸 |
| `es` | Español | 🇪🇸 |
| `fr` | Français | 🇫🇷 |
| `de` | Deutsch | 🇩🇪 |
| `it` | Italiano | 🇮🇹 |

---

## 📝 Templates Já Traduzidos

✅ **base.html** - Header, Footer, Language Selector  
✅ **home.html** - Hero, Stats, Categories, CTA

### Templates para Traduzir:
- [ ] `theme_detail.html` - Página de categoria
- [ ] `quiz_detail.html` - Detalhes do quiz
- [ ] `quiz_play.html` - Gameplay
- [ ] `quiz_result.html` - Resultados
- [ ] `user_profile.html` - Perfil do usuário

---

## 🔧 Como Funciona

1. **Usuário seleciona idioma** no footer (language cards)
2. **JavaScript** envia POST para `/set-language/`
3. **View** salva idioma na `session`
4. **Helper** `get_user_language(request)` busca idioma da sessão
5. **Context** em todas as views inclui `current_language` e `language_stats`
6. **Templates** usam `{% t 'chave' %}` que busca tradução automaticamente

---

## 💡 Exemplos Práticos

### Exemplo 1: Traduzir texto estático
```django
<!-- Antes -->
<h1>Bem-vindo ao Quizverso</h1>

<!-- Depois -->
<h1>{% t 'welcome_title' %}</h1>
```

### Exemplo 2: Traduzir com variáveis
```django
<!-- Se a tradução tem placeholder -->
<p>{% t 'you_scored' %} {{ score }} {% t 'correct_answers' %}</p>
```

### Exemplo 3: Traduzir botões
```django
<button>{% t 'start_quiz' %}</button>
<a href="#">{% t 'back_to_category' %}</a>
```

---

## ⚙️ Contexto Global

Todas as views incluem automaticamente:

```python
context = {
    # ... outros dados
    'current_language': 'pt-BR',  # Idioma atual do usuário
    'language_stats': {           # Contadores por idioma
        'pt_BR': 150,
        'en': 80,
        'es': 45,
        # ...
    },
}
```

---

## 🎨 Boas Práticas

### ✅ Faça:
- Use chaves descritivas: `'start_quiz'` em vez de `'btn1'`
- Mantenha traduções curtas e claras
- Use a mesma chave para o mesmo conceito
- Agrupe traduções relacionadas

### ❌ Evite:
- Hardcoded texto nos templates
- Chaves muito longas: `'welcome_to_our_amazing_platform_title'`
- Traduções com HTML embutido
- Duplicar traduções similares

---

## 🚀 Expandir o Sistema

### Para adicionar novo idioma:

1. Adicione em `models.py`:
```python
LANGUAGE_CHOICES = [
    # ... existentes
    ('ja', 'Japanese'),  # Novo
]
```

2. Adicione traduções para todas as chaves em `translations.py`

3. Adicione language card no `base.html` footer

---

## 📊 Estatísticas

- **Chaves de tradução:** ~60
- **Idiomas:** 6
- **Templates traduzidos:** 2/7
- **Cobertura:** ~30%

---

## 🔮 Futuro

### Melhorias Possíveis:
1. **Script de validação** - verificar se todas as chaves têm todos os idiomas
2. **Interface de admin** - gerenciar traduções no Django Admin
3. **Importar/Exportar** - JSON/CSV para tradutores externos
4. **Pluralização** - suporte a singular/plural
5. **Fallback** - usar inglês se tradução não existir

---

## 🆘 Troubleshooting

### Tradução não aparece?
1. Verifique se a chave existe em `TRANSLATIONS`
2. Confirme que `current_language` está no contexto
3. Veja se carregou `{% load icon_tags %}`
4. Limpe o cache do navegador

### Idioma não muda?
1. Verifique console do navegador (F12)
2. Confirme que a sessão está ativa
3. Teste em janela anônima

---

**Criado em:** Outubro 2025  
**Versão:** 1.0  
**Sistema:** Django + Custom Template Tags

