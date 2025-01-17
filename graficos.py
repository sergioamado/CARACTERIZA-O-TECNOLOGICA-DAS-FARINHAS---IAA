import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Gráfico de Pizza
def grafico_pizza(dados, coluna_analisada):
    # Contar os valores únicos na coluna analisada
    dados_agrupados = dados[coluna_analisada].value_counts()

    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(8, 8))  # Aumentar o tamanho do gráfico
    ax.pie(
        dados_agrupados,
        labels=dados_agrupados.index,
        autopct='%1.1f%%',
        startangle=90,
        labeldistance=1.1  # Ajustar a posição dos rótulos para evitar sobreposição
    )
    ax.set_title(f'Distribuição por {coluna_analisada}', fontsize=16)

    # Exibir no Streamlit
    st.pyplot(fig)

# Gráfico de Barras
def grafico_barras(dados, coluna_analisada):
    # Contar os valores únicos na coluna analisada
    dados_agrupados = dados[coluna_analisada].value_counts()

    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(10, 5))  # Tamanho ajustado para barras
    ax.bar(dados_agrupados.index, dados_agrupados.values, color='skyblue')
    ax.set_title(f'Distribuição de {coluna_analisada}', fontsize=14)
    ax.set_xlabel(coluna_analisada, fontsize=12)
    ax.set_ylabel('Quantidade', fontsize=12)
    ax.tick_params(axis='x', rotation=45)  # Rotacionar rótulos para melhor visualização

    # Exibir no Streamlit
    st.pyplot(fig)

# Gráfico de Comparação com a Amostra
def grafico_comparativo(dados, colunas, coluna_comparacao='Amostra'):
    # Criar o gráfico para cada coluna comparada com 'Amostra'
    fig, ax = plt.subplots(figsize=(12, 8))  # Tamanho ajustado
    for coluna in colunas:
        if coluna != coluna_comparacao:  # Não comparar com a própria coluna
            ax.plot(dados[coluna_comparacao], dados[coluna], marker='o', label=coluna)

    ax.set_title(f'Comparação com {coluna_comparacao}', fontsize=16)
    ax.set_xlabel(coluna_comparacao, fontsize=14)
    ax.set_ylabel('Valores', fontsize=14)
    ax.legend(loc='best', fontsize=12)
    ax.grid(True)

    # Exibir no Streamlit
    st.pyplot(fig)

# Gráfico Individual para Cada Coluna
def grafico_individual_por_coluna(dados, coluna_comparacao='Amostra'):
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