import streamlit as st
from src.carregamento import carregar_planilha_financeira
from src.extracao_vendas import localizar_e_extrair_mes
from src.processamento_vendas import processar_vendas_mes
from src.ia_consultor import gerar_insight_ia

# Configuração da Página
st.set_page_config(page_title="Dashboard MB Cafeteria", layout="wide")

def exibir_resultado_mes(nome_mes, resultado_mes):
    """Renderiza os indicadores, gráficos e tabelas de um mês no Streamlit"""
    st.header(f"📅 {nome_mes}")
    
    # --- GRÁFICO DE TENDÊNCIA ---
    # Mostra a oscilação das vendas ao longo dos dias
    st.write("**📈 Tendência de Vendas Diárias:**")
    st.line_chart(
        resultado_mes["vendas_limpa"].set_index("data")["valor_vendido"],
        color="#FF4B4B" # Um vermelho sutil para destacar
    )
    
    # Métricas Principais
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Vendido", f"R$ {resultado_mes['total_vendido']:,.2f}")
    with col2:
        st.metric("Média Diária", f"R$ {resultado_mes['media_diaria']:,.2f}")

    # Tabelas de Destaque
    col_tabela1, col_tabela2 = st.columns(2)
    with col_tabela1:
        st.write("**🏆 Maior venda do mês:**")
        st.dataframe(resultado_mes["maior_venda"].to_frame().T, hide_index=True)
    
    with col_tabela2:
        st.write("**📉 Menor venda do mês:**")
        st.dataframe(resultado_mes["menor_venda"].to_frame().T, hide_index=True)

    # DataFrame completo (expansível)
    with st.expander(f"Ver lista detalhada de {nome_mes}"):
        st.dataframe(resultado_mes["vendas_limpa"], use_container_width=True)


# --- INÍCIO DO APP ---
st.title("☕ Painel Financeiro - MB Cafeteria")

# 1. Carregamento dos dados
base_bruta = carregar_planilha_financeira()

# 2. Configuração da Automação
meses_para_analise = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL"]
ano_alvo = 2026

# Dicionário para armazenar os resultados
resultados_acumulados = {}

# 3. Loop de Processamento e Exibição
for mes in meses_para_analise:
    try:
        resultado = processar_vendas_mes(
            base_bruta,
            lambda df, m=mes: localizar_e_extrair_mes(df, m, ano_alvo=ano_alvo)
        )
        
        resultados_acumulados[mes] = resultado
        exibir_resultado_mes(f"{mes.capitalize()} / {ano_alvo}", resultado)
        st.markdown("---")
        
    except Exception as e:
        st.warning(f"⚠️ Não foi possível processar {mes}: {e}")

# --- ESPAÇO DA INTELIGÊNCIA ARTIFICIAL ---
st.subheader("💡 Consultoria Estratégica (Llama 3)")

if st.button("Gerar Análise com IA"):
    if resultados_acumulados:
        ultimo_mes_nome = list(resultados_acumulados.keys())[-1]
        dados_ultimo_mes = resultados_acumulados[ultimo_mes_nome]
        
        with st.spinner(f"O Llama 3 está analisando {ultimo_mes_nome}..."):
            insight = gerar_insight_ia(
                mes=ultimo_mes_nome,
                total_vendido=dados_ultimo_mes["total_vendido"],
                media_diaria=dados_ultimo_mes["media_diaria"]
            )
            
            with st.chat_message("assistant"):
                st.write(insight)
    else:
        st.error("Nenhum dado disponível para análise.")