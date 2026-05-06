from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3")

template = ChatPromptTemplate.from_messages([
    ("system", "Você é um consultor financeiro especialista em cafeterias brasileiras."),
    ("user", "Analise este dado de venda: {venda}. O que você pode me dizer sobre este desempenho?")
])

chain = template | model

# 4. Simulamos um dado que viria do seu Pandas
dado_venda = "Data: 05/05/2026, Valor Vendido: R$ 2.500,00, Meta Diária: R$ 1.800,00"

# 5. Executamos passando o dado
resposta = chain.invoke({"venda": dado_venda})

print("\n--- Insight do Consultor IA ---")
print(resposta)