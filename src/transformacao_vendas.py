import pandas as pd


def unir_partes_vendas(vendas_esquerda, vendas_direita):
    vendas_esquerda = vendas_esquerda.copy()
    vendas_direita = vendas_direita.copy()

    vendas_esquerda.columns = ["data", "valor_vendido"]
    vendas_direita.columns = ["data", "valor_vendido"]

    vendas_unificadas = pd.concat(
        [vendas_esquerda, vendas_direita],
        ignore_index=True,
    )

    return vendas_unificadas

def limpar_vendas_diarias(vendas):
    vendas = vendas.copy()

    vendas["data"] = pd.to_datetime(vendas["data"])
    vendas["valor_vendido"] = pd.to_numeric(
        vendas["valor_vendido"],
        errors="coerce",
    ).fillna(0)

    vendas = vendas[vendas["valor_vendido"] > 0]

    vendas = vendas.sort_values("data")
    vendas = vendas.reset_index(drop=True)

    return vendas