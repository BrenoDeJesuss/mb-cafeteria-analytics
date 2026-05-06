from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def gerar_insight_ia(mes, total_vendido, media_diaria):
    """
    Envia os dados resumidos para o Llama 3 e retorna uma análise estratégica.
    """
    try:
        # 1. Inicializa o modelo local
        llm = OllamaLLM(model="llama3")

        # 2. Prepara o molde da pergunta (Prompt)
        template = ChatPromptTemplate.from_messages([
            ("system", "Você é um consultor de negócios sênior especializado em cafeterias."),
            ("user", (
                "Analise os resultados de {mes} de 2026: "
                "Faturamento Total: R$ {total:.2f}. "
                "Média Diária: R$ {media:.2f}. "
                "Escreva um insight curto (máximo 4 frases) sobre esse desempenho "
                "e sugira uma ação prática para o dono da cafeteria."
            ))
        ])

        # 3. Cria a corrente e executa
        chain = template | llm
        resposta = chain.invoke({
            "mes": mes,
            "total": total_vendido,
            "media": media_diaria
        })
        
        return resposta
    except Exception as e:
        return f"Erro ao consultar a IA: {e}"