import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Frota de veículos", layout="wide", page_icon="🚗")

df = pd.read_csv("numero_veiculos.csv")

df_filtrado = df[
    (df["id_municipio_nome"].isin(["Belo Horizonte", "Betim", "Contagem"])) &
    (df["mes"] == 12) &
    (df["ano"] == 2025)
].copy()

df_filtrado = df_filtrado[["id_municipio_nome", "tipo_veiculo", "quantidade"]]
df_filtrado = df_filtrado[df_filtrado["quantidade"] > 0]

st.title("Painel Streamlit da frota de veículos")
st.header("Belo Horizonte, Betim e Contagem — dezembro de 2025")

opcao = st.sidebar.radio("Escolha o que ver", ["Tabela", "Gráficos"])

if opcao == "Tabela":
    st.dataframe(df_filtrado, hide_index=True)
else:
    for cidade in ["Belo Horizonte", "Betim", "Contagem"]:
        dados_cidade = df_filtrado[df_filtrado["id_municipio_nome"] == cidade]
        fig = px.pie(
            dados_cidade,
            names="tipo_veiculo",
            values="quantidade",
            title=f"Frota de veículos em {cidade}",
        )
        st.plotly_chart(fig)

