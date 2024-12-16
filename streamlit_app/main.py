# streamlit_app/main.py
import streamlit as st
import requests
import json
import os
import matplotlib.pyplot as plt

API_URL = "http://localhost:8000"

st.title("Análise de Partidas de Futebol")

match_id = st.text_input("Insira o ID da Partida:", value="1085911")

if st.button("Buscar Partida"):
    summary_response = requests.post(f"{API_URL}/match_summary", json={"match_id": int(match_id)})
    if summary_response.status_code == 200:
        summary = summary_response.json()["summary"]
        st.subheader("Sumarização da Partida")
        st.write(summary)
    else:
        st.error("Erro ao obter a sumarização da partida.")

    player_id = st.text_input("Insira o ID do Jogador para ver o perfil:", value="6789")
    if st.button("Buscar Perfil do Jogador"):
        profile_response = requests.post(f"{API_URL}/player_profile", json={"match_id": int(match_id), "player_id": int(player_id)})
        if profile_response.status_code == 200:
            profile = profile_response.json()
            st.subheader("Perfil do Jogador")
            st.json(profile)
            stats = {
                "Passes": profile["passes"],
                "Finalizações": profile["finalizations"],
                "Dispossessions": profile["dispossessions"],
                "Minutos Jogados": profile["minutes_played"]
            }
            fig, ax = plt.subplots()
            ax.bar(stats.keys(), stats.values(), color='skyblue')
            ax.set_ylabel('Quantidade')
            ax.set_title(f'Estatísticas de {profile["name"]}')
            st.pyplot(fig)
        else:
            st.error("Erro ao obter o perfil do jogador.")

    style = st.selectbox("Escolha o estilo da narração:", ["Formal", "Humorístico", "Técnico"])
    if st.button("Gerar Narração"):
        narration_response = requests.post(f"{API_URL}/narrate_match", json={"match_id": int(match_id), "style": style})
        if narration_response.status_code == 200:
            narrative = narration_response.json()["narrative"]
            st.subheader("Narração da Partida")
            st.write(narrative)
        else:
            st.error("Erro ao gerar a narrativa da partida.")
