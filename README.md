# Football Match Analysis Application

## Descrição
Aplicação para análise de partidas de futebol, permitindo gerar perfis de jogadores, sumarizar eventos e criar narrativas personalizadas.

## Configuração do Ambiente
1. Crie e ative o ambiente virtual
2. Instale as dependências: `pip install -r requirements.txt`
3. Crie um arquivo `.env` com sua chave OpenAI: `OPENAI_API_KEY=YOUR_KEY`

## Execução
- API: `uvicorn app.api:app --reload`
- Interface: `streamlit run streamlit_app/main.py`
