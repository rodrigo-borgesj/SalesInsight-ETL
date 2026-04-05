from src.processor import processar_dados
from src.database import inicializar_banco
from src.analyzer import ranking_faturamento, ranking_produto, ranking_mes
from src.visualizer import grafico_faturamento, grafico_produto, grafico_mes

# 1. SINCRONIZAÇÃO (Obrigatório para o banco funcionar)
df_inicial = processar_dados()
inicializar_banco(df_inicial)

while True:
    print("\n--- ANALISE DE VENDAS ---")
    print("[1] Relatório de Vendas (Texto)")
    print("[2] Ver Gráficos (Visual)")
    print("[3] Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite apenas números.")
        continue

    if opcao == 1:
        print("\n--- Relatório de Vendas (Texto) ---")
        print("[1] Faturamento")
        print("[2] Produto")
        print("[3] Mês")
        print("[4] Retornar")

        try:
            sub_opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite apenas números.")
            continue

        if sub_opcao == 1:
            print(ranking_faturamento())

        elif sub_opcao == 2:
            print(ranking_produto())

        elif sub_opcao == 3:
            print(ranking_mes())

        elif sub_opcao == 4:
            pass
    
    elif opcao == 2:
        print("\n--- Ver Gráficos (Visual) ---")
        print("[1] Faturamento")
        print("[2] Produto")
        print("[3] Mês")
        print("[4] Retornar")

        try:
            sub_opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite apenas números.")
            continue

        if sub_opcao == 1:
            grafico_faturamento()

        elif sub_opcao == 2:
            grafico_produto()

        elif sub_opcao == 3:
            grafico_mes()

        elif sub_opcao == 4:
            pass
 
    elif opcao == 3:
        print("Saindo.....")
        break