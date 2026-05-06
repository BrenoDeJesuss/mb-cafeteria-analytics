import pandas as pd

from src.configuracoes import CAMINHO_PLANILHA, NOME_ABA_PRINCIPAL


def carregar_planilha_financeira():
    df = pd.read_excel(
        CAMINHO_PLANILHA,
        sheet_name=NOME_ABA_PRINCIPAL,
        header=None,
    )

    return df
