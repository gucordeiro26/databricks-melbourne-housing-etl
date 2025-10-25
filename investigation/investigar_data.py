import pandas as pd

# --- AÇÃO NECESSÁRIA: Verifique se o nome do arquivo abaixo está correto ---
caminho_csv = "MELBOURNE_HOUSE_PRICES_LESS.csv"

print("--- Teste de Leitura Focada no Arquivo CSV ---")
try:
    # Vamos tentar ler o arquivo CSV. O erro, se houver, deve acontecer aqui.
    print("Tentando ler o arquivo CSV...")
    df_csv = pd.read_csv(caminho_csv)
    print("SUCESSO: O arquivo CSV foi lido na memória sem erros de parsing.")

    # Se a leitura deu certo, agora procuramos a data
    print("\nProcurando pela data '3/09/2016'...")
    # Forçamos a coluna 'Date' a ser do tipo string para a comparação ser exata
    df_csv['Date'] = df_csv['Date'].astype(str)
    linha_problematica = df_csv[df_csv['Date'] == '3/09/2016']
    
    if not linha_problematica.empty:
        print("\n>>> SUCESSO: Data '3/09/2016' ENCONTRADA no arquivo CSV!")
        print("Conteúdo da linha:")
        print(linha_problematica.to_string())
    else:
        print("\n>>> INFO: Data '3/09/2016' NÃO encontrada no arquivo CSV.")

except Exception as e:
    # Se qualquer erro acontecer durante a tentativa de ler o arquivo, ele será capturado aqui.
    print("\n" + "*"*25)
    print("!!! ERRO DETALHADO AO LER O CSV:")
    print(e)
    print("*"*25)
    print("\nO erro acima é a causa do problema. Por favor, me envie esta mensagem completa.")