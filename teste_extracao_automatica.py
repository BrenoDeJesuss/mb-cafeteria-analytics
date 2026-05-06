import pandas as pd
from src.carregamento import carregar_planilha_financeira
from src.extracao_vendas import localizar_e_extrair_mes
from src.transformacao_vendas import unir_partes_vendas

def testar_sistema():
    print("--- INICIANDO TESTE DE EXTRAÇÃO AUTOMÁTICA ---")
    
    # 1. Carrega o arquivo bruto
    try:
        df_bruto = carregar_planilha_financeira()
        print("✅ Arquivo carregado com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao carregar arquivo: {e}")
        return

    # 2. Tenta extrair um mês específico (Ex: MARÇO)
    mes_para_teste = "MARÇO"
    print(f"🔍 Buscando o mês de {mes_para_teste}...")
    
    try:
        v_esq, v_dir = localizar_e_extrair_mes(df_bruto, "MARÇO", ano_alvo=2026)
        print(f"✅ Marcador de {mes_para_teste} localizado!")
        
        # 3. Une as partes para ver se os dados fazem sentido
        df_unificado = unir_partes_vendas(v_esq, v_dir)
        
        print("\n--- AMOSTRA DOS DADOS EXTRAÍDOS ---")
        # Mostra as primeiras e últimas linhas para conferir as datas
        print(df_unificado.head(5))
        print("...")
        print(df_unificado.tail(5))
        
        print(f"\n📊 Total de linhas capturadas: {len(df_unificado)}")
        
    except Exception as e:
        print(f"❌ Falha na extração: {e}")

if __name__ == "__main__":
    testar_sistema()