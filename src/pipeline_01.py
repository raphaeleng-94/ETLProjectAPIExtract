import time
import requests
from tinydb import TinyDB
from datetime import datetime

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

def salvar_dados_tinydb(dados, db_name ="bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print(f"Dados salvos em {db_name}")

if __name__ == "__main__":
    while True:
        # Extração dos dados
        dados = extract_dados_bitcoin()
        # Transformação dos dados
        dados_transformados = transform_dados_bitcoin(dados)
        # Salvar os dados
        salvar_dados_tinydb(dados_transformados)
        time.sleep(15)
    
