import streamlit as st
from Utils.utils import format_number
from Graficos.graficosGeral import grafico_valor_por_unidade_requisitante, grafico_qtde_contratacoes_por_entrega, grafico_valor_por_categoria, grafico_ranking_cinco_maiores_contratacoes, grafico_contratacoes_por_status
from Utils.constantes import QTDE_ENTREGAS_PARA_CONCLUSAO, VALOR_ANUAL_ESTIMADO


def exibir_aba_dashboard_geral(tabela, valorPorUnidadeRequisitante, qtdeContratacoesPorEntrega, valorPorCategoria, rankingPorContratacoes, contratacoesPorStatus):
    coluna1, coluna2 = st.columns(2)

    st.markdown("""
        <style>
            .st-emotion-cache-1wivap2 {
                display: flex;
                justify-content: center        
            }
            .st-emotion-cache-q49buc {
                display: flex;
                justify-content: center
            }

            .st-emotion-cache-17c4ue {
                    display: flex;
                    justify-content: center
                } 

            .st-emotion-cache-gy4uc {
                    display: flex;
                    justify-content: center
                }           
        </style>    
    """, unsafe_allow_html=True)

    with coluna1: 
        with st.container(border=True):
            st.metric("Quantidade Total de Contratações", tabela[QTDE_ENTREGAS_PARA_CONCLUSAO].count())

        with st.container(border=True):
            st.plotly_chart(grafico_qtde_contratacoes_por_entrega(qtdeContratacoesPorEntrega), use_container_width=True)
        
        with st.container(border=True):
            st.plotly_chart(grafico_ranking_cinco_maiores_contratacoes(rankingPorContratacoes), use_container_width=True)

        

    with coluna2: 
        with st.container(border=True):
            st.metric('Valor Total das Contratações', format_number(tabela[VALOR_ANUAL_ESTIMADO].sum(), 'R$'))

        with st.container(border=True):
            st.plotly_chart(grafico_valor_por_unidade_requisitante(valorPorUnidadeRequisitante), use_container_width=True)

        with st.container(border=True):
            st.plotly_chart(grafico_valor_por_categoria(valorPorCategoria), use_container_width=True)

        with st.container(border=True):
            st.plotly_chart(grafico_contratacoes_por_status(contratacoesPorStatus), use_container_width=True)

        
