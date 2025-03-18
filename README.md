```markdown
# Exemplo de Integração com a API OpenAI

Este projeto demonstra como fazer uma integração básica com a API da OpenAI para realizar consultas ao modelo GPT.

## Estrutura do Projeto

```
.
├── exemplos
│   └── exemplos_04.py
├── .env
└── requirements.txt
```

## Pré-requisitos

- Python 3.7 ou superior
- Uma chave de API válida da OpenAI

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API:
```
OPEN_AI_API_KEY=sua_chave_aqui
```

## Conteúdo do requirements.txt
```
python-dotenv==1.0.0
requests==2.31.0
```

## Código Exemplo

```python:exemplos/exemplos_04.py
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.openai.com/v1/chat/completions"

openai_api_key = os.getenv("OPEN_AI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "Olá, Qual é o preço do Etherum atualmente?"}]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json()["choices"][0]["message"]["content"])
```

## Explicação do Código

### 1. Importações
```python
import requests  # Para fazer requisições HTTP
import json     # Para manipulação de dados JSON
import os       # Para variáveis de ambiente
from dotenv import load_dotenv  # Para carregar variáveis do arquivo .env
```

### 2. Configuração do Ambiente
```python
load_dotenv()  # Carrega as variáveis do arquivo .env
url = "https://api.openai.com/v1/chat/completions"  # URL da API da OpenAI
openai_api_key = os.getenv("OPEN_AI_API_KEY")  # Obtém a chave da API das variáveis de ambiente
```

### 3. Configuração dos Headers
```python
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}
```
Os headers são necessários para autenticação e especificação do tipo de conteúdo.

### 4. Preparação dos Dados
```python
data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "Olá, Qual é o preço do Etherum atualmente?"}]
}
```
Define o modelo a ser usado e a mensagem para a API.

### 5. Requisição e Resposta
```python
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json()["choices"][0]["message"]["content"])
```
Envia a requisição POST e imprime a resposta do modelo.

## Como Executar

1. Certifique-se de que todas as dependências estão instaladas
2. Verifique se o arquivo `.env` está configurado corretamente
3. Execute o script:
```bash
python exemplos/exemplos_04.py
```

## Observações Importantes

- Mantenha sua chave API segura e nunca a compartilhe
- O modelo "gpt-4o-mini" usado no exemplo deve ser substituído por um modelo válido da OpenAI
- Certifique-se de ter créditos suficientes em sua conta OpenAI
- Trate possíveis erros de API em um ambiente de produção

## Tratamento de Erros

O código exemplo é básico e não inclui tratamento de erros. Em um ambiente de produção, você deve adicionar try/catch para lidar com:
- Erros de conexão
- Respostas de erro da API
- Problemas com a chave API
- Limites de taxa excedidos
```

Este README fornece uma documentação completa para entender e executar o exemplo_04.py, incluindo instalação, configuração e explicações detalhadas de cada parte do código.
