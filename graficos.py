import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class Graficos:
    @staticmethod
    def grafico_pizza_coluna(dados, coluna_analisada):
        # Gráfico de pizza baseado em uma coluna
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
    def grafico_pizza_linha(dados, linha_analisada):
        # Seleciona a linha como uma Series
        dados_linha = dados.iloc[linha_analisada]
        
        # Filtra apenas valores numéricos da linha
        dados_numericos = dados_linha[dados_linha.apply(lambda x: isinstance(x, (int, float)))]
        
        if dados_numericos.empty:
            st.error("A linha selecionada não contém valores numéricos suficientes para gerar um gráfico de pizza.")
            return

        # Criação do gráfico de pizza
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(
            dados_numericos,
            labels=dados_numericos.index,
            autopct='%1.1f%%',
            startangle=90,
            labeldistance=1.1
        )
        ax.set_title(f"Distribuição de valores na linha {linha_analisada}", fontsize=16)
        st.pyplot(fig)

    @staticmethod
    def grafico_barras(dados, linha, colunas):
        # Gráfico de barras: Eixo X = linha, Eixo Y = valores das colunas selecionadas
        dados_linha = dados.loc[linha, colunas]
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(dados_linha.index, dados_linha.values, color='skyblue')
        ax.set_title(f'Valores da Linha {linha}', fontsize=14)
        ax.set_xlabel('Colunas', fontsize=12)
        ax.set_ylabel('Valores', fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

    @staticmethod
    def grafico_comparativo(dados, linhas, coluna):
        # Gráfico comparativo entre linhas para uma coluna específica
        fig, ax = plt.subplots(figsize=(12, 8))
        for linha in linhas:
            valores = dados.loc[linha, coluna]
            ax.plot(valores, marker='o', label=f'Linha {linha}')

        ax.set_title(f'Comparação entre Linhas para a Coluna {coluna}', fontsize=20)
        ax.set_xlabel('Índice', fontsize=12)
        ax.set_ylabel('Valores', fontsize=12)
        ax.legend(loc='best', fontsize=10)
        ax.grid(True)
        st.pyplot(fig)

    @staticmethod
    def grafico_individual_por_linha(dados, linhas, colunas):
        # Gráficos individuais: Comparação entre as linhas escolhidas para várias colunas
        for linha in linhas:
            st.markdown(f"### Gráfico para Linha {linha}")
            fig, ax = plt.subplots(figsize=(10, 5))
            valores = dados.loc[linha, colunas]
            ax.plot(valores.index, valores.values, marker='o', color='green')
            ax.set_title(f'Linha {linha} para Colunas Selecionadas', fontsize=14)
            ax.set_xlabel('Colunas', fontsize=12)
            ax.set_ylabel('Valores', fontsize=12)
            ax.grid(True)
            st.pyplot(fig)
