import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

class Graficos:
    @staticmethod
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

    @staticmethod
    def grafico_barras(dados, coluna_analisada):
        dados_agrupados = dados[coluna_analisada].value_counts()
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(dados_agrupados.index, dados_agrupados.values, color='skyblue')
        ax.set_title(f'Distribuição de {coluna_analisada}', fontsize=14)
        ax.set_xlabel(coluna_analisada, fontsize=12)
        ax.set_ylabel('Quantidade', fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

    @staticmethod
    def grafico_comparativo(dados, colunas):
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

    @staticmethod
    def grafico_individual_por_coluna(dados):
        colunas = dados.columns
        coluna_comparacao = st.sidebar.selectbox(
            "Escolha a coluna de comparação", options=colunas
        )
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
