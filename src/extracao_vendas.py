import pandas as pd

def localizar_e_extrair_mes(df, nome_mes_alvo, ano_alvo=2026):
   
    nome_mes_alvo = nome_mes_alvo.upper()
    ano_alvo = str(ano_alvo)
    linha_inicio = None

    for i, row in df.iterrows():
     
        if str(row[0]).upper() == "MÊS" and str(row[1]).upper() == nome_mes_alvo:
            
            linha_abaixo = df.iloc[i + 1]
            if str(linha_abaixo[1]) == ano_alvo:
                linha_inicio = i
                break
    
    if linha_inicio is None:
        raise ValueError(f"Mês {nome_mes_alvo} do ano {ano_alvo} não encontrado!")

    
    idx_dados = linha_inicio + 6
    
    vendas_esquerda = df.iloc[idx_dados : idx_dados + 16, [0, 1]].copy()
    vendas_direita = df.iloc[idx_dados : idx_dados + 16, [2, 3]].copy()

    return vendas_esquerda, vendas_direita