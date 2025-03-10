import streamlit as st
import plotly.express as px
from Dataset.dados import tabela
from Abas.dataset import exibir_aba_dataset
from Insights.insights import gerar_insights_derivados
from Abas.dashboardGeral import exibir_aba_dashboard_geral
from Abas.dashboardPrazo import exibir_aba_dashboard_prazo
from Filtros.filtros import aplicar_filtro

st.set_page_config(page_title='Painel Cronograma PCA - 2025', page_icon=':bar_chart:',layout='wide')
st.title("Cronograma de Execução - PCA 2025")
st.sidebar.title("Filtros")

tabela = aplicar_filtro(tabela)

valorPorUnidadeRequisitante, qtdeContratacoesPorEntrega, valorPorCategoria, rankingPorContratacoes, contratacoesPorStatus, contratacoesEmDia, contratacoesEmAtraso, entregasEmDia, entregasEmAtraso, objetosPorMes = gerar_insights_derivados(tabela)
aba1, aba2, aba3 = st.tabs(['Cronograma de Execução PCA - 2025', 'Dashboard Geral', 'Dashboard de Prazos'])

with aba1:
    exibir_aba_dataset(tabela)

with aba2:
    exibir_aba_dashboard_geral(tabela, valorPorUnidadeRequisitante, qtdeContratacoesPorEntrega, valorPorCategoria, rankingPorContratacoes, contratacoesPorStatus)

with aba3:
    exibir_aba_dashboard_prazo(tabela, contratacoesEmDia, contratacoesEmAtraso, entregasEmDia, entregasEmAtraso, objetosPorMes)
