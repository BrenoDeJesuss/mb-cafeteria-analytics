def extrair_vendas_fevereiro_2026(df):
    vendas_esquerda = df.iloc[3961:3976, [0, 1]]
    vendas_direita = df.iloc[3961:3974, [2, 3]]

    return vendas_esquerda, vendas_direita

def extrair_vendas_marco_2026(df):
    vendas_esquerda = df.iloc[4209:4225, [0, 1]]
    vendas_direta = df.iloc[4209:4226, [2, 3]]

    return vendas_esquerda, vendas_direta