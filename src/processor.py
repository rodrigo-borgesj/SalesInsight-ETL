from config import JSON_PATH
import json
import pandas as pd


def carregar_arquivo():
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def processar_dados():
    dados = carregar_arquivo()

    if not dados:
        return pd.DataFrame()
    
    df = pd.DataFrame(dados)

    #df["cpf"] = df["cpf"].str.replace(".", "").str.replace("-", "")
    df["cpf"] = df["cpf"].str.replace(r"\D", "", regex=True)
    df["data"] = pd.to_datetime(df["data"])
    df["valor"] = pd.to_numeric(df["valor"])

    return df