# ETLProjectAPIExtract

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
