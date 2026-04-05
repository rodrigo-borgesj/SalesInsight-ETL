import sqlite3
import pandas as pd
from config import DB_PATH

def inicializar_banco(df):
    connect = sqlite3.connect(DB_PATH)
    df.to_sql("vendas", connect, if_exists="replace", index=False)
    connect.close()
