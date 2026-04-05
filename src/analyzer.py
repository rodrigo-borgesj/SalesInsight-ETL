import sqlite3
import pandas as pd
from config import DB_PATH

def conexao(comando_sql):
    connect = sqlite3.connect(DB_PATH)
    df = pd.read_sql(comando_sql, connect, parse_dates=['data'])
    connect.close()
    return df

def ranking_faturamento():
    df = conexao("SELECT * FROM vendas")
    ranking = df.groupby('cliente')['valor'].sum().sort_values(ascending=False)
    return ranking

def ranking_produto():
    df = conexao("SELECT * FROM vendas")
    return df['produto'].value_counts()

def ranking_mes():
    df = conexao("SELECT * FROM vendas")
    return df.groupby(df['data'].dt.month_name())['valor'].sum().sort_values(ascending=False)