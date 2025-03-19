Criarei um README abrangente explicando ambos os arquivos e suas funcionalidades.

```markdown
# Sistema de monitoramento de preços de Bitcoin

Este projeto consiste em dois componentes principais: um pipeline de dados que coleta preços de Bitcoin da API da Coinbase e os armazena em um banco de dados PostgreSQL, e um painel Streamlit que visualiza esses dados em tempo real.

## Estrutura do projeto

```
├── src/
│ └── pipeline_04.py
├── app/
│ └── dashboard_00.py
└── .env
```

## Componentes

### 1. Pipeline de dados (pipeline_04.py)

O componente pipeline é responsável por coletar, transformar e armazenar dados de preços de Bitcoin.

#### Principais recursos:

- **Configuração do ambiente**
- Usa `python-dotenv` para gerenciar variáveis ​​de ambiente
- Configura o Logfire para registro abrangente
- Configura a conexão do banco de dados PostgreSQL

- **Configuração do banco de dados**
- Usa o SQLAlchemy ORM para operações de banco de dados
- Cria automaticamente as tabelas necessárias se elas não existirem

- **Funções de coleta de dados**
- `extract_dados_bitcoin()`: Obtém dados de preço do Bitcoin em tempo real da API da Coinbase
- `transform_dados_bitcoin()`: Transforma dados brutos da API em formato estruturado
- `salvar_dados_postgres()`: Salva os dados processados ​​no banco de dados PostgreSQL

- **Fluxo de execução**
- Executa continuamente com intervalos de 15 segundos
- Inclui tratamento de erros e desligamento normal com CTRL+C
- Registra todas as operações e possíveis erros

### 2. Painel (dashboard_00.py)

Um baseado em Streamlit painel da web que visualiza os dados de preço do Bitcoin coletados.

#### Principais recursos:

- **Visualização de dados**
- Atualizações de preços em tempo real
- Gráfico de preços históricos
- Exibição de estatísticas importantes

- **Componentes**
- Visualização de tabela de dados recentes
- Gráfico de linhas mostrando a evolução dos preços
- Métricas mostrando os preços atuais, máximos e mínimos

- **Integração de banco de dados**
- Conexão direta com o banco de dados PostgreSQL
- Atualização automática de dados
- Tratamento de erros para problemas de conexão com o banco de dados

## Detalhes técnicos

### Dependências

- Python 3.x
- PostgreSQL
- Bibliotecas:
- `requests`: Para chamadas de API
- `sqlalchemy`: ORM de banco de dados
- `logfire`: Sistema de registro
- `streamlit`: Estrutura de painel
- `pandas`: Manipulação de dados
- `psycopg2`: Adaptador PostgreSQL
- `python-dotenv`: Gerenciamento de ambiente

### Variáveis ​​de ambiente

Variáveis ​​necessárias em `.env` arquivo:
```
POSTGRES_USER=seu_usuário
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=seu_banco_de_dados
POSTGRES_HOST=seu_host
POSTGRES_PORT=sua_porta
```

## Uso

1. **Configurando o Pipeline**
```bash
python src/pipeline_04.py
```
Isso começará a coletar dados de preço do Bitcoin a cada 15 segundos.

2. **Executando o Dashboard**
```bash
streamlit run app/dashboard_00.py
```
Isso iniciará o painel da web em sua máquina local.

## Fluxo de dados

1. O pipeline coleta dados da API da Coinbase
2. Os dados são transformados e marcados com data e hora
3. Os dados processados ​​são armazenados no PostgreSQL
4. O painel lê do PostgreSQL
5. As visualizações são atualizadas em tempo real

## Tratamento de erros

- Ambos os componentes incluem tratamento de erros abrangente
- Chamadas de API com falha ou operações de banco de dados são registradas
- O pipeline tenta novamente automaticamente após erros
- O painel exibe mensagens de erro amigáveis

## Registro

- Sistema de registro abrangente usando Logfire
- Rastreia chamadas de API, operações de banco de dados e erros
- Inclui registro de consulta SQL
- Registros de data e hora para todas as operações

## Melhores práticas

- Uso de variáveis ​​de ambiente para dados confidenciais
- Separação de preocupações (coleta de dados vs. visualização)
- Tratamento de erros e registro adequados
- Estrutura de código limpa com responsabilidades de função claras
- Gerenciamento de conexão de banco de dados
- Criação automatizada de tabelas
- Processamento e visualização de dados em tempo real

Este projeto fornece uma solução completa para monitorar preços de Bitcoin com atualizações em tempo real e capacidades de visualização.