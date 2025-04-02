import streamlit as st
# from Dataset.dados import quantidadeContratacoesEmDia, quantidadeContratacoesEmAtraso
from Graficos.graficosPrazo import grafico_contratacoes_em_dia, grafico_contratacoes_em_atraso, grafico_entregas_em_dia, grafico_entregas_em_atraso, grafico_conclusao_estimada_por_mes

def exibir_aba_dashboard_prazo(tabela, contratacoesEmDia, contratacoesEmAtraso, entregasEmDia, entregasEmAtraso, objetoPorMes):
    coluna1, coluna2 = st.columns(2)

    tabela["Quantidade em Dia"] = tabela["Cumprimento do Prazo na Entrega Atual"].apply(lambda x: (x == "Em dia"))
    quantidadeContratacoesEmDia = tabela[tabela["Quantidade em Dia"] == True].shape[0]

    tabela["Quantidade em Atraso"] = tabela["Cumprimento do Prazo na Entrega Atual"].apply(lambda x: (x == "Atrasada"))
    quantidadeContratacoesEmAtraso = tabela[tabela["Quantidade em Atraso"] == True].shape[0]

    with coluna1:
        with st.container(border=True):
         st.metric("Quantidade Total de Contratações em Dia", quantidadeContratacoesEmDia)
         
        with st.container(border=True):
           st.plotly_chart(grafico_contratacoes_em_dia(contratacoesEmDia), use_container_width=True) 

        with st.container(border=True):
          st.plotly_chart(grafico_entregas_em_dia(entregasEmDia), use_container_width=True)   

    with coluna2:
       with st.container(border=True):
        st.metric("Quantidade Total de Contratações em Atraso", quantidadeContratacoesEmAtraso)

       with st.container(border=True):
        st.plotly_chart(grafico_contratacoes_em_atraso(contratacoesEmAtraso), use_container_width=True)

       with st.container(border=True):
         st.plotly_chart(grafico_entregas_em_atraso(entregasEmAtraso), use_container_width=True)

    with st.container(border=True):
        st.plotly_chart(grafico_conclusao_estimada_por_mes(objetoPorMes), use_container_width=True)