# ☕ MB Cafeteria Analytics & AI Consulting

[![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Llama3-white?style=for-the-badge)](https://ollama.com/)

Um ecossistema de inteligência de dados projetado para pequenas empresas. Este projeto automatiza a extração de dados financeiros de planilhas complexas, gera visualizações de tendências e utiliza **IA Local (Llama 3)** para fornecer consultoria estratégica em tempo real.

---

## 🚀 O que este projeto faz?

- **Extração Dinâmica:** Localiza e extrai dados de vendas de múltiplos meses dentro de um único arquivo Excel, sem a necessidade de formatação prévia manual.
- **Data Cleaning & Engineering:** Processamento automatizado com Pandas para tratar valores nulos, converter tipos de dados e calcular indicadores financeiros (Faturamento Total, Média Diária, Outliers).
- **Dashboard Interativo:** Visualização clara de tendências diárias através de gráficos de linha e métricas comparativas.
- **Consultoria com IA Local:** Integração com **Llama 3** via Ollama para analisar o desempenho do mês e sugerir ações práticas de negócio (ex: gestão de estoque, horários de pico).

## 🧠 O Diferencial: Privacidade Total
Diferente de dashboards que usam APIs de nuvem (como OpenAI), este projeto roda um modelo de linguagem **100% local**. Isso significa que os dados financeiros da empresa **nunca saem da máquina do usuário**, garantindo conformidade com privacidade e segurança de dados.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.14
- **Interface:** Streamlit
- **Manipulação de Dados:** Pandas, OpenPyXL
- **Inteligência Artificial:** LangChain & Ollama (Llama 3)
- **Ambiente:** Linux (Fedora)

---

## ⚙️ Como rodar o projeto

### 1. Pré-requisitos
Certifique-se de ter o **Ollama** instalado e o modelo Llama 3 baixado:
```bash
ollama pull llama3

2. Instalação

Clone o repositório e instale as dependências:
Bash

git clone [https://github.com/BrenoDeJesuss/mb-cafeteria-analytics.git](https://github.com/BrenoDeJesuss/mb-cafeteria-analytics.git)
cd mb-cafeteria-analytics
pip install -r requirements.txt

3. Execução

Inicie o dashboard:
Bash

streamlit run financeiro.py

📂 Estrutura do Projeto
Plaintext

├── datasets/             # Planilhas de dados brutos
├── src/                  # Módulos de lógica (Extração, Limpeza, IA)
├── financeiro.py         # Arquivo principal (Interface Streamlit)
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação

Desenvolvido por Breno de Jesus

Focado em transformar dados brutos em decisões inteligentes.


---

### Por que esse README é "foda"?

1.  **Badges Profissionais:** No topo, ele já mostra as tecnologias (`Python`, `Streamlit`, `Ollama`) com selos coloridos. Isso passa autoridade imediata.
2.  **Foco no Negócio:** Ele explica *por que* o projeto é útil (privacidade, automação, estratégia), não apenas o que o código faz.
3.  **Privacidade como Destaque:** No mundo dos dados, enfatizar que a IA é local e segura é um diferencial enorme.
4.  **Organização:** Instruções claras de como qualquer pessoa pode baixar e rodar o seu trabalho.

**Dica final:** Depois de colar isso no arquivo e salvar, faça o commit:
```bash
git add README.md
git commit -m "Docs: Adicionando documentação detalhada"
git push
