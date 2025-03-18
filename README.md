# ETLProjectAPIExtract

# Projeto ETL com Python

Este é um projeto de ETL (Extract, Transform, Load) desenvolvido em Python para extrair, transformar e carregar dados utilizando a biblioteca requests.

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-projeto.git
cd nome-do-projeto
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 📦 Estrutura do Projeto

projeto/
│
├── src/
│ ├── extract.py # Módulo de extração de dados
│ ├── transform.py # Módulo de transformação
│ └── load.py # Módulo de carregamento
│
├── config/
│ └── config.py # Configurações do projeto
│
├── tests/ # Testes unitários
│
├── requirements.txt # Dependências do projeto
└── README.md

## 🚀 Como usar

1. Configure as variáveis de ambiente necessárias (se aplicável)
2. Execute o script principal:

```bash
python src/main.py
```

## 📝 Exemplo de Uso

```python
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

# Extrair dados
raw_data = extract_data('https://api.exemplo.com/dados')

# Transformar dados
transformed_data = transform_data(raw_data)

# Carregar dados
load_data(transformed_data, 'destino.csv')
```

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [Pandas](https://pandas.pydata.org/) (opcional para manipulação de dados)

## ✒️ Autores

* **Raphael Amorim** - *Desenvolvimento Inicial* - [raphaeleng-94](https://github.com/raphaeleng-94)

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.
