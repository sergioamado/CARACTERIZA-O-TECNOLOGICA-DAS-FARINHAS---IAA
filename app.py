import streamlit as st
import pandas as pd
from graficos import Graficos

st.title("Análise Gráfica das Amostras")
graficos = Graficos()
# Upload do arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, decimal=',')
    st.write("Primeiras linhas dos dados carregados:", df.head())

    st.sidebar.title("Selecione o Gráfico")
    grafico_opcao = st.sidebar.selectbox(
        "Escolha o tipo de gráfico",
        ["Gráfico de Pizza", "Gráfico de Barras", "Gráfico de Comparação", "Gráfico Individual por Coluna"]
    )

    if grafico_opcao == "Gráfico de Pizza":
        # Certifique-se de que uma coluna é selecionada
        coluna = st.sidebar.selectbox("Escolha a coluna para o gráfico de pizza", df.columns)
        if coluna:
            Graficos.grafico_pizza(df, coluna)
        else:
            st.error("Por favor, selecione uma coluna para gerar o gráfico de pizza.")

    elif grafico_opcao == "Gráfico de Barras":
        coluna = st.sidebar.selectbox("Escolha a coluna para o gráfico de barras", df.columns)
        if coluna:
            Graficos.grafico_barras(df, coluna)
        else:
            st.error("Por favor, selecione uma coluna para gerar o gráfico de barras.")

    elif grafico_opcao == "Gráfico de Comparação":
        colunas = df.columns.tolist()
        if colunas:
            Graficos.grafico_comparativo(df, colunas)
        else:
            st.error("Por favor, selecione pelo menos uma coluna para comparação.")

    elif grafico_opcao == "Gráfico Individual por Coluna":
        if not df.empty:
            Graficos.grafico_individual_por_coluna(df)
        else:
            st.error("Os dados carregados estão vazios.")
