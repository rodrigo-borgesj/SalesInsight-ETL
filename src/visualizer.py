import matplotlib.pyplot as plt
from src.analyzer import ranking_faturamento, ranking_mes, ranking_produto

def gerar_grafico(dados, tipo, titulo, xtexto, ytexto):
    if dados.empty:
        print(f"Sem dados para gerar o gráfico: {titulo}")
        return

    plt.figure(figsize=(10, 6))

    dados.plot(kind=tipo, ax=plt.gca(), color='skyblue')

    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.xlabel(xtexto)
    plt.ylabel(ytexto)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7) # Adiciona linhas de grade sutis
    plt.tight_layout()
    plt.show()

def grafico_faturamento():
    grafico = ranking_faturamento()
    gerar_grafico(grafico, "bar", "Faturamento por Cliente", "Cliente", "Valor")

def grafico_produto():
    grafico = ranking_produto()
    gerar_grafico(grafico, "bar", "Produtos mais Vendidos", "Produto", "Quantidade")

def grafico_mes():
    grafico = ranking_mes()
    gerar_grafico(grafico, "bar", "Melhor Mês", "Mês", "Valor")