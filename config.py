import os

# Raiz do Projeto
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 

# Pasta de Dados
RAW_DATA_DIR = os.path.join(ROOT_DIR, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(ROOT_DIR, "data", "processed")

# Caminhos dos Arquivos Especificos
JSON_PATH = os.path.join(RAW_DATA_DIR, "vendas_brutas.json")
DB_PATH = os.path.join(PROCESSED_DATA_DIR, "vendas.db")

# Criar as pastas automaticamente se não existirem
os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)