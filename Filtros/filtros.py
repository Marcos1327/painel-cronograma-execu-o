import streamlit as st
import pandas as pd
from Utils.constantes import UNIDADE_REQUISITANTE, UNIDADE_SUBORDINADA, MODALIDADE, PRIORIDADE, STATUS

# Colocar .dropna() antes do .unique() para retirar valores vazios

def aplicar_filtro(tabela):
    st.markdown("""
        <style>
            .st-cf{
                cursor: pointer
            }
        </style>    
    """, unsafe_allow_html=True)

    filtro_unidade_requisitante = st.sidebar.multiselect('Unidade Requisitante', sorted(tabela[UNIDADE_REQUISITANTE].unique()), placeholder='Unidade Requisitante', label_visibility='hidden')

    if filtro_unidade_requisitante:
        tabela_filtrada = tabela[tabela[UNIDADE_REQUISITANTE].isin(filtro_unidade_requisitante)]
    else:
        tabela_filtrada = tabela
   
    filtro_subunidade = st.sidebar.multiselect('Subunidades', sorted(tabela_filtrada[UNIDADE_SUBORDINADA].fillna('vazio').unique()), placeholder='Subunidade', label_visibility='hidden')

    if filtro_subunidade:
        tabela_filtrada = tabela_filtrada[tabela_filtrada[UNIDADE_SUBORDINADA].isin(filtro_subunidade)]

    filtro_por_modalidade = st.sidebar.multiselect('Modalidade', sorted(tabela_filtrada[MODALIDADE].fillna('vazio').unique()), placeholder='Modalidade', label_visibility='hidden')

    filtro_por_prioridade = st.sidebar.multiselect('Prioridade', sorted(tabela_filtrada[PRIORIDADE].fillna('vazio').unique()), placeholder='Prioridade', label_visibility='hidden')

    filtro_por_status = st.sidebar.multiselect('Status', sorted(tabela_filtrada['Status'].fillna('vazio').unique()), placeholder='Status', label_visibility='hidden')

    if filtro_unidade_requisitante:
        tabela = tabela[tabela[UNIDADE_REQUISITANTE].isin(filtro_unidade_requisitante)]

    if filtro_subunidade:
        tabela = tabela[tabela[UNIDADE_SUBORDINADA].isin(filtro_subunidade)]  

    if filtro_por_modalidade:
        tabela = tabela[tabela[MODALIDADE].isin(filtro_por_modalidade)]

    if filtro_por_prioridade:
        tabela = tabela[tabela[PRIORIDADE].isin(filtro_por_prioridade)]          

    if filtro_por_status:
        tabela = tabela[tabela[STATUS].isin(filtro_por_status)]

    return tabela