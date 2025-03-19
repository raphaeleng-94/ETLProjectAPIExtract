import time
import requests
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

from database import Base, Bitcoin

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis separadas do arquivo .env (sem SSL)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)


# Cria o engine da conexão com o banco de dados
engine = create_engine(DATABASE_URL)
# Cria o sessionmaker
SessionLocal = sessionmaker(bind=engine)

def criar_tabela():
    """Cria a tabela no banco de dados, se não existir"""
    Base.metadata.create_all(engine)
    print("Tabela criada|verificada com sucesso")

def extract_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    dados = response.json()
    return dados

def transform_dados_bitcoin(dados):
    valor = dados["data"]["amount"]
    moeda = dados["data"]["currency"]
    criptomoeda = dados["data"]["base"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dados_transformados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }

    return dados_transformados

def salvar_dados_postgres(dados):
    """Salva os dados no banco de dados PostgreSQL"""
    session = SessionLocal()
    novo_registro = Bitcoin(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print(f"[{dados['timestamp']}] Dados salvos com sucesso no PostgreSQL!")

if __name__ == "__main__":
    criar_tabela()
    print("Iniciando o pipeline com atualização a cada 15 segundos...(CTRL+C para interromper)")
    while True:
        try:
            # Extração dos dados
            dados = extract_dados_bitcoin()
            if dados:
                dados_transformados = transform_dados_bitcoin(dados)
                print("Dados Tratados:", dados_transformados)
                salvar_dados_postgres(dados_transformados)
            time.sleep(15)
        except KeyboardInterrupt:
            print("\nPipeline interrompido pelo usuário")
            break
        except Exception as e:
            print(f"\nErro ao processar dados: {e}")
            time.sleep(15)
    
