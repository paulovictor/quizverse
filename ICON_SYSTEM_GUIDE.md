# 🎨 Sistema de Ícones SVG - Guia de Uso

## ✅ Sistema Implementado!

O sistema de ícones SVG foi totalmente implementado e está pronto para uso!

## 📂 Estrutura Criada

```
quizzes/
├── static/
│   └── icons/
│       ├── trophy.svg       # Troféu/Esportes
│       ├── soccer.svg        # Futebol
│       ├── gamepad.svg       # Games/Videogames
│       ├── book.svg          # Livros/Conhecimento
│       ├── film.svg          # Filmes/Cinema
│       └── music.svg         # Música
│
├── templatetags/
│   ├── __init__.py
│   └── icon_tags.py          # Template tag para renderizar ícones
│
└── models.py                 # Campo icon_svg adicionado ao Theme
```

## 🚀 Como Usar

### 1. No Django Admin

Ao editar um Tema, você verá o campo:
- **icon_svg**: Nome do arquivo SVG - ex: `trophy`, `soccer`, `gamepad`, `book`, `film`, `music`

**Exemplo:**
- icon_svg: `soccer`
- icon_svg: `trophy`
- icon_svg: `gamepad`

Se deixar vazio, será exibido um ícone de livro (📚) como placeholder.

### 2. Nos Templates

**Carregar a template tag:**
```django
{% load icon_tags %}
```

**Renderizar ícone:**
```django
{# Renderizar ícone SVG #}
{% render_icon theme %}

{# Com classe CSS customizada #}
{% render_icon theme 'icon-large' %}
```

### 3. Verificar se tem SVG

```django
{% if theme|has_svg_icon %}
    <p>Este tema tem ícone SVG!</p>
{% endif %}
```

## 📝 Ícones Disponíveis

Crie o arquivo SVG em `quizzes/static/icons/` e use o nome (sem .svg):

| Arquivo | Nome para usar | Sugestão de uso |
|---------|---------------|-----------------|
| `trophy.svg` | `trophy` | Campeonatos, vitórias |
| `soccer.svg` | `soccer` | Futebol |
| `gamepad.svg` | `gamepad` | Videogames |
| `book.svg` | `book` | Conhecimento, cultura |
| `film.svg` | `film` | Cinema, filmes |
| `music.svg` | `music` | Música |

## ➕ Adicionar Novos Ícones

1. Crie ou encontre um SVG
2. **IMPORTANTE**: Use `currentColor` no SVG (não cores fixas)
3. Salve em `quizzes/static/icons/nome-do-icone.svg`
4. No admin, use `nome-do-icone` (sem .svg)

**Exemplo de SVG correto:**
```xml
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <path d="..." stroke="currentColor" stroke-width="2"/>
</svg>
```

❌ **NÃO use:**
```xml
<path stroke="#3b82f6"/>  <!-- Cor fixa -->
```

✅ **USE:**
```xml
<path stroke="currentColor"/>  <!-- Herda a cor do CSS -->
```

## 🎨 Personalizar Cores via CSS

```css
.my-icon {
    color: #ff0000; /* O SVG vai usar essa cor */
}
```

## 📋 Checklist de Implementação

- [x] Estrutura de diretórios criada
- [x] Campo `icon_svg` adicionado ao modelo
- [x] Migração criada e aplicada
- [x] Template tag criada
- [x] 6 ícones SVG de exemplo
- [x] CSS para ícones adicionado
- [ ] Atualizar templates existentes (opcional)
- [ ] Adicionar mais ícones conforme necessário

## 🔄 Sistema Simplificado

O sistema funciona de forma direta:
- Se `icon_svg` estiver preenchido → usa o SVG especificado
- Se `icon_svg` estiver vazio → mostra um placeholder (📚)

## 🎯 Próximos Passos

1. **Testar**: Edite um tema no admin e adicione `trophy` no campo icon_svg
2. **Visualizar**: Vá para a página do tema e veja o ícone SVG
3. **Criar mais**: Adicione mais SVGs conforme necessário
4. **Atualizar templates**: Use `{% render_icon theme %}` nos templates

## 📚 Recursos para SVGs

- **Heroicons**: https://heroicons.com/ (gratuito, MIT)
- **Lucide**: https://lucide.dev/ (gratuito, ISC)
- **Feather Icons**: https://feathericons.com/ (gratuito, MIT)
- **Flaticon**: https://www.flaticon.com/ (grátis com atribuição)

## ⚠️ Importante

- **NÃO salve SVGs no banco de dados**
- **SEMPRE use `currentColor`** nos SVGs
- **Mantenha SVGs simples** (< 5KB)
- **Use nomes descritivos** para os arquivos

## 🐛 Troubleshooting

**Ícone não aparece:**
1. Verifique se o arquivo existe em `quizzes/static/icons/`
2. Verifique o nome (sem .svg)
3. Rode `python manage.py collectstatic` se estiver em produção

**Ícone está com cor errada:**
- Certifique-se de usar `currentColor` no SVG
- O SVG herda a cor do elemento pai via CSS

---

**Sistema implementado por:** Cursor AI
**Data:** 2025
**Status:** ✅ Pronto para produção

