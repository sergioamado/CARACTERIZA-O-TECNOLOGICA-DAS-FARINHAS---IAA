import streamlit as st
import pandas as pd
from graficos import Graficos

# App principal
st.title("Análise Gráfica das Amostras")
# Upload do arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

graficos = Graficos()

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, decimal=',')
    st.write("Primeiras linhas dos dados carregados:", df.head())

    st.sidebar.title("Selecione o Gráfico")
    grafico_opcao = st.sidebar.selectbox(
        "Escolha o tipo de gráfico",
        ["Gráfico de Pizza", "Gráfico de Barras", "Gráfico de Comparação", "Gráfico Individual por Linha"]
    )

    if grafico_opcao == "Gráfico de Pizza":
        pizza_tipo = st.sidebar.radio("Deseja gerar o gráfico por:", ("Coluna", "Linha"))
        if pizza_tipo == "Coluna":
            coluna = st.sidebar.selectbox("Escolha a coluna para o gráfico de pizza", df.columns)
            graficos.grafico_pizza_coluna(df, coluna)
        elif pizza_tipo == "Linha":
            linha = st.sidebar.selectbox("Escolha a linha para o gráfico de pizza", df.index)
            graficos.grafico_pizza_linha(df, linha)

    elif grafico_opcao == "Gráfico de Barras":
        linha = st.sidebar.selectbox("Escolha a linha para o eixo X", df.index)
        colunas = st.sidebar.multiselect("Escolha as colunas para o eixo Y", df.columns)
        if colunas:
            graficos.grafico_barras(df, linha, colunas)
        else:
            st.error("Por favor, selecione pelo menos uma coluna para gerar o gráfico.")

    elif grafico_opcao == "Gráfico de Comparação":
        linhas = st.sidebar.multiselect("Escolha as linhas para comparação", df.index)
        coluna = st.sidebar.selectbox("Escolha a coluna para comparação", df.columns)
        if linhas and coluna:
            graficos.grafico_comparativo(df, linhas, coluna)
        else:
            st.error("Por favor, selecione pelo menos uma linha e uma coluna para gerar o gráfico.")

    elif grafico_opcao == "Gráfico Individual por Linha":
        linhas = st.sidebar.multiselect("Escolha as linhas para comparação", df.index)
        colunas = st.sidebar.multiselect("Escolha as colunas para análise", df.columns)
        if linhas and colunas:
            graficos.grafico_individual_por_linha(df, linhas, colunas)
        else:
            st.error("Por favor, selecione pelo menos uma linha e uma coluna para gerar os gráficos.")
