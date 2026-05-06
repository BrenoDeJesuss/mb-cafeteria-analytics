from src.transformacao_vendas import unir_partes_vendas, limpar_vendas_diarias
from src.analises_vendas import (
    calcular_total_vendido,
    calcular_media_diaria,
    encontrar_maior_venda,
    encontrar_menor_venda,
)


def processar_vendas_mes(base_bruta, funcao_extracao):
    vendas_esquerda, vendas_direita = funcao_extracao(base_bruta)

    vendas = unir_partes_vendas(
        vendas_esquerda,
        vendas_direita,
    )

    vendas_limpa = limpar_vendas_diarias(vendas)

    total_vendido = calcular_total_vendido(vendas_limpa)
    media_diaria = calcular_media_diaria(vendas_limpa)
    maior_venda = encontrar_maior_venda(vendas_limpa)
    menor_venda = encontrar_menor_venda(vendas_limpa)

    return {
        "vendas_limpa": vendas_limpa,
        "total_vendido": total_vendido,
        "media_diaria": media_diaria,
        "maior_venda": maior_venda,
        "menor_venda": menor_venda,
    }
