# Guia de Traduções de Badges

## Visão Geral

O sistema de badges agora suporta traduções para múltiplos idiomas. Cada badge pode ter descrições traduzidas para diferentes países/idiomas.

## Como Funciona

### 1. Modelo Badge Atualizado

- **Campo `description`**: Descrição padrão (fallback)
- **Campo `description_translations`**: JSON com traduções por idioma
- **Método `get_description(language)`**: Retorna descrição traduzida

### 2. Uso nos Templates

```django
<!-- Antes -->
{{ badge.description }}

<!-- Agora -->
{{ badge|badge_description:current_language }}
```

### 3. Django Admin

No admin (`/admin/quizzes/badge/`), você pode:

- **Ver quantas traduções** cada badge tem na listagem
- **Editar traduções** no campo "Traduções" 
- **Preview das traduções** em tempo real
- **Validação automática** do JSON

## Formato das Traduções

```json
{
  "pt-BR": "Acerte todos os 150 Pokémon! Maestria absoluta da Geração 1.",
  "en-US": "Get all 150 Pokémon correct! Absolute mastery of Generation 1.",
  "es-MX": "¡Acierta todos los 150 Pokémon! Maestría absoluta de la Generación 1.",
  "de-DE": "Errate alle 150 Pokémon! Absolute Meisterschaft der 1. Generation.",
  "fr-FR": "Trouvez tous les 150 Pokémon! Maîtrise absolue de la Génération 1."
}
```

## Códigos de Idioma Suportados

- `pt-BR` - Português (Brasil)
- `en-US`, `en-CA`, `en-GB`, `en-IN`, `en-PH`, `en-AU`, `en-NZ` - Inglês
- `es-MX`, `es-ES`, `es-AR`, `es-CO` - Espanhol
- `de-DE` - Alemão
- `fr-FR` - Francês
- `it-IT` - Italiano
- `nl-NL` - Holandês
- `sv-SE` - Sueco
- `no-NO` - Norueguês
- `pl-PL` - Polonês
- `id-ID` - Indonésio
- `ja-JP` - Japonês
- `ko-KR` - Coreano
- `th-TH` - Tailandês
- `vi-VN` - Vietnamita

## Como Adicionar Traduções

### 1. Via Django Admin

1. Acesse `/admin/quizzes/badge/`
2. Clique em uma badge
3. No campo "Traduções", adicione o JSON
4. Salve

### 2. Via Script Python

```python
from quizzes.models import Badge

badge = Badge.objects.get(title="🟠 Amber Pikachu")
badge.description_translations = {
    "pt-BR": "Acerte todos os 150 Pokémon!",
    "en-US": "Get all 150 Pokémon correct!",
    "es-MX": "¡Acierta todos los 150 Pokémon!"
}
badge.save()
```

## Fallback Automático

Se não houver tradução para o idioma solicitado, o sistema automaticamente usa:

1. A tradução do idioma solicitado
2. Se não existir, usa o campo `description` (fallback)

## Templates Atualizados

Os seguintes templates foram atualizados para usar o novo sistema:

- `theme_detail.html` - Tooltip das badges
- `user_profile.html` - Descrição das badges conquistadas  
- `quiz_result.html` - Celebração de novas badges

## Exemplo de Uso

```python
# No Python
badge = Badge.objects.get(title="🟠 Amber Pikachu")
print(badge.get_description("pt-BR"))  # "Acerte todos os 150 Pokémon!"
print(badge.get_description("en-US"))  # "Get all 150 Pokémon correct!"
print(badge.get_description("xx-XX"))  # Fallback para description
```

```django
<!-- No template -->
{{ badge|badge_description:current_language }}
```

## Migração Concluída

✅ **Migração aplicada**: Campo `description_translations` adicionado
✅ **Dados migrados**: 9 badges existentes migradas para o novo formato
✅ **Templates atualizados**: 3 templates usando o novo sistema
✅ **Admin configurado**: Interface para editar traduções
✅ **Badges Pokémon**: 5 badges com traduções para 25 idiomas

## Próximos Passos

1. **Teste o sistema**: Acesse diferentes países e veja as traduções
2. **Adicione mais traduções**: Use o admin para adicionar traduções em outros idiomas
3. **Crie novas badges**: Use o novo sistema desde o início
4. **Monitore performance**: O sistema usa cache automático do Django
