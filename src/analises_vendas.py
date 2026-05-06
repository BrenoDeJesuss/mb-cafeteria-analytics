def calcular_total_vendido(vendas):
    return vendas["valor_vendido"].sum()


def calcular_media_diaria(vendas):
    return vendas["valor_vendido"].mean()


def encontrar_maior_venda(vendas):
    indice_maior_venda = vendas["valor_vendido"].idxmax()
    return vendas.loc[indice_maior_venda]


def encontrar_menor_venda(vendas):
    indice_menor_venda = vendas["valor_vendido"].idxmin()
    return vendas.loc[indice_menor_venda]
