# Guia - Extrair URLs do Cloudinary

Script para recuperar todas as URLs de arquivos de uma pasta no Cloudinary.

## 📋 Informações que você precisa fornecer:

### 1. **Credenciais do Cloudinary**

Acesse: https://console.cloudinary.com/console/settings/security

Você precisará de:
- `Cloud Name` (nome da conta)
- `API Key` 
- `API Secret`

### 2. **Nome da Pasta**

Exemplo:
- `pokemon`
- `images/pokemon`
- `quiz/icons`

### 3. **Tipo de Recurso** (opcional)

- `image` - Apenas imagens (padrão)
- `video` - Apenas vídeos
- `raw` - Arquivos raw (PDFs, etc.)

### 4. **Formato de Saída** (opcional)

- `json` - JSON completo com metadados (padrão)
- `csv` - Formato CSV
- `urls_only` - Apenas URLs (uma por linha)
- `list` - Lista Python

---

## 🚀 Como Usar

### Opção 1: Variáveis de Ambiente (Recomendado)

```bash
# Configurar credenciais
export CLOUDINARY_CLOUD_NAME=seu_cloud_name
export CLOUDINARY_API_KEY=sua_api_key
export CLOUDINARY_API_SECRET=seu_api_secret

# Instalar dependência
pip install cloudinary

# Executar script
python cloudinary_get_urls.py
```

### Opção 2: Editar o Script Diretamente

Abra `cloudinary_get_urls.py` e edite:

```python
# Suas credenciais
CLOUD_NAME = 'seu_cloud_name'
API_KEY = 'sua_api_key'
API_SECRET = 'seu_api_secret'

# Pasta para buscar
FOLDER_NAME = 'sua_pasta'

# Tipo de recurso
RESOURCE_TYPE = 'image'  # ou 'video', 'raw'

# Formato de saída
OUTPUT_FORMAT = 'json'  # ou 'csv', 'urls_only', 'list'
```

---

## 📊 Formatos de Saída

### JSON (Padrão)
```json
[
  {
    "public_id": "pokemon/001_bulbasaur",
    "format": "png",
    "width": 475,
    "height": 475,
    "bytes": 203394,
    "url": "https://res.cloudinary.com/..."
  }
]
```

### CSV
```csv
public_id,format,width,height,bytes,url
pokemon/001_bulbasaur,png,475,475,203394,https://...
pokemon/002_ivysaur,png,475,475,202762,https://...
```

### URLs Only
```
https://res.cloudinary.com/.../pokemon/001_bulbasaur.png
https://res.cloudinary.com/.../pokemon/002_ivysaur.png
https://res.cloudinary.com/.../pokemon/003_venusaur.png
```

---

## 🎨 Transformações (Opcional)

Para gerar URLs com transformações específicas, edite:

```python
# Exemplo: Redimensionar para 300x300
TRANSFORMATIONS = {
    'width': 300,
    'height': 300,
    'crop': 'fill'
}

# Exemplo: Adicionar marca d'água
TRANSFORMATIONS = {
    'overlay': 'logo',
    'width': 50,
    'gravity': 'south_east'
}

# Exemplo: Formato WebP otimizado
TRANSFORMATIONS = {
    'fetch_format': 'auto',
    'quality': 'auto'
}
```

Documentação: https://cloudinary.com/documentation/image_transformations

---

## 💡 Exemplos de Uso

### 1. Extrair todas as imagens de uma pasta

```python
FOLDER_NAME = 'pokemon'
RESOURCE_TYPE = 'image'
OUTPUT_FORMAT = 'json'
```

### 2. Apenas URLs (sem metadados)

```python
FOLDER_NAME = 'icons'
OUTPUT_FORMAT = 'urls_only'
```

### 3. Limitar a 100 resultados

```python
FOLDER_NAME = 'images'
MAX_RESULTS = 100
```

### 4. URLs com redimensionamento

```python
FOLDER_NAME = 'photos'
TRANSFORMATIONS = {'width': 800, 'height': 600, 'crop': 'fill'}
OUTPUT_FORMAT = 'urls_only'
```

---

## 🔧 Troubleshooting

### Erro: "Biblioteca 'cloudinary' não está instalada"

```bash
pip install cloudinary
```

### Erro: "Credenciais não configuradas"

Verifique se:
1. As variáveis de ambiente estão definidas
2. Ou as constantes no script estão preenchidas
3. O Cloud Name está correto

### Erro: "Nenhum recurso encontrado"

Verifique:
1. O nome da pasta está correto (case-sensitive)
2. A pasta contém arquivos do tipo especificado
3. Suas credenciais têm permissão de leitura

### Erro de autenticação

Verifique:
1. API Key e Secret estão corretos
2. As credenciais não expiraram
3. A conta Cloudinary está ativa

---

## 📝 Saída do Script

O script gera um arquivo com o seguinte padrão:

```
cloudinary_urls_pokemon.json  # Para formato JSON
cloudinary_urls_pokemon.csv   # Para formato CSV
cloudinary_urls_pokemon.txt   # Para urls_only ou list
```

---

## 🔐 Segurança

**IMPORTANTE:** 

- ❌ **NÃO** commite credenciais no git
- ✅ Use variáveis de ambiente
- ✅ Adicione `cloudinary_*.json` no `.gitignore`
- ✅ Use `.env` para desenvolvimento local

Exemplo `.env`:
```env
CLOUDINARY_CLOUD_NAME=seu_cloud_name
CLOUDINARY_API_KEY=sua_api_key
CLOUDINARY_API_SECRET=seu_api_secret
```

E carregue com `python-dotenv`:
```python
from dotenv import load_dotenv
load_dotenv()
```

---

## 📚 Recursos

- **Documentação Cloudinary:** https://cloudinary.com/documentation
- **API Reference:** https://cloudinary.com/documentation/admin_api
- **Python SDK:** https://github.com/cloudinary/pycloudinary

---

**Criado para facilitar a migração e backup de assets do Cloudinary**

