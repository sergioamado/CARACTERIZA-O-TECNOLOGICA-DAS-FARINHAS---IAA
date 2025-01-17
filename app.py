import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Funções de gráficos (já fornecidas)
def grafico_pizza(dados, coluna_analisada):
    dados_agrupados = dados[coluna_analisada].value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(
        dados_agrupados,
        labels=dados_agrupados.index,
        autopct='%1.1f%%',
        startangle=90,
        labeldistance=1.1
    )
    ax.set_title(f'Distribuição por {coluna_analisada}', fontsize=16)
    st.pyplot(fig)

def grafico_barras(dados, coluna_analisada):
    dados_agrupados = dados[coluna_analisada].value_counts()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(dados_agrupados.index, dados_agrupados.values, color='skyblue')
    ax.set_title(f'Distribuição de {coluna_analisada}', fontsize=14)
    ax.set_xlabel(coluna_analisada, fontsize=12)
    ax.set_ylabel('Quantidade', fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

def grafico_comparativo(dados, colunas):
    # Permitir que o usuário escolha as colunas para comparação
    colunas_selecionadas = st.sidebar.multiselect(
        "Escolha as colunas para comparar",
        options=colunas,
        default=colunas
    )
    
    if not colunas_selecionadas:
        st.error("Por favor, selecione pelo menos uma coluna para comparar.")
        return

    fig, ax = plt.subplots(figsize=(12, 8))
    for coluna in colunas_selecionadas:
        ax.plot(dados[coluna], marker='o', label=coluna)

    ax.set_title(f'Comparação entre Colunas', fontsize=20)
    ax.set_xlabel('Índice', fontsize=12)
    ax.set_ylabel('Valores', fontsize=12)
    ax.legend(loc='best', fontsize=10)
    ax.grid(True)
    st.pyplot(fig)

def grafico_individual_por_coluna(dados, coluna_comparacao='amostra'):
    colunas = dados.columns
    for coluna in colunas:
        if coluna != coluna_comparacao:
            st.markdown(f"### Gráfico para {coluna}")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(dados[coluna_comparacao], dados[coluna], marker='o', color='green')
            ax.set_title(f'{coluna_comparacao} vs {coluna}', fontsize=14)
            ax.set_xlabel(coluna_comparacao, fontsize=12)
            ax.set_ylabel(coluna, fontsize=12)
            ax.grid(True)
            st.pyplot(fig)

# Carregar os dados CSV
st.title("Análise Gráfica das Amostras")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Lê o CSV
    df = pd.read_csv(uploaded_file, decimal=',')
    
    # Exibir as primeiras linhas para conferirmos os dados
    st.write("Primeiras linhas dos dados carregados:", df.head())
    
    # Opções de gráficos
    st.sidebar.title("Selecione o Gráfico")
    grafico_opcao = st.sidebar.selectbox(
        "Escolha o tipo de gráfico",
        ["Gráfico de Pizza", "Gráfico de Barras", "Gráfico de Comparação", "Gráfico Individual por Coluna"]
    )
    
    # Condicional para exibir o gráfico escolhido
    if grafico_opcao == "Gráfico de Pizza":
        coluna = st.sidebar.selectbox("Escolha a coluna para o gráfico de pizza", df.columns)
        grafico_pizza(df, coluna)

    elif grafico_opcao == "Gráfico de Barras":
        coluna = st.sidebar.selectbox("Escolha a coluna para o gráfico de barras", df.columns)
        grafico_barras(df, coluna)

    elif grafico_opcao == "Gráfico de Comparação":
        # Permitir que o usuário escolha todas as colunas disponíveis
        colunas = df.columns.tolist()
        grafico_comparativo(df, colunas)

    elif grafico_opcao == "Gráfico Individual por Coluna":
        grafico_individual_por_coluna(df)
