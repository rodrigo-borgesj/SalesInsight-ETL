SalesInsight-ETL/
│
├── data/                       # Onde ficam os arquivos de dados
│   ├── raw/                    # JSON original (vendas_brutas.json)
│   └── processed/              # Banco SQLite e CSVs gerados
│
├── src/                        # Código-fonte do projeto
│   ├── __init__.py
│   ├── database.py             # Funções de SQL (Criar tabelas, Inserir)
│   ├── processor.py            # Lógica de Limpeza com Pandas e JSON
│   ├── analyzer.py             # Cálculos de Ranking, Agrupamentos e Médias
│   └── visualizer.py           # Geração de gráficos com Matplotlib
│
├── tests/                      # (Opcional) Testes unitários
│
├── main.py                     # O Maestro: Menu de interação com o usuário
├── config.py                   # Caminhos de arquivos (DB_PATH, JSON_PATH)
├── requirements.txt            # Lista de bibliotecas (pandas, matplotlib)
└── README.md                   # A "vitrine" do seu projeto no GitHub