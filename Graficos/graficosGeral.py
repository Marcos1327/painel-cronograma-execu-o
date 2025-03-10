import plotly.express as px
import streamlit as st
from Utils.utils import quebrar_texto
from Utils.constantes import COR_TEXTO_GRAFICO, COR_FUNDO_GRAFICO, COR_BLOCO_GRAFICO, CUMPRIMENTO_PRAZO_ENTREGA_ATUAL, ARTEFATO_ENTREGA_ATUAL, CATEGORIA_OBJETO, STATUS, TITULO_OBJETO, UNIDADE_REQUISITANTE, VALOR_ANUAL_ESTIMADO

def grafico_valor_por_unidade_requisitante(valorPorUnidadeRequisitante):

    valorPorUnidadeRequisitante['Valor Formatado'] = valorPorUnidadeRequisitante['Valor Anual Estimado*'].apply( lambda x: f"R$ {x:,.0f}".replace(",", ".").replace('X', '.'))

    grafico = px.bar(
        valorPorUnidadeRequisitante,
        x = VALOR_ANUAL_ESTIMADO,
        y = UNIDADE_REQUISITANTE,
        orientation='h',
        text = 'Valor Formatado',
        color = UNIDADE_REQUISITANTE,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    grafico.update_layout(
        title=dict(text='Valor Anual das Contratações', x=0.02, font=dict(size=22)),
        uniformtext_minsize=10,
        uniformtext_mode='hide',
        showlegend=False,
        # paper_bgcolor=COR_BLOCO_GRAFICO, #Muda a cor do fundo do bloco onde está inserido o gráfico
        plot_bgcolor=COR_FUNDO_GRAFICO, #Muda a cor do fundo do gráfico
        margin=dict(l=20, r=20, t=75, b=20),
    )

    grafico.update_traces(
        textfont=dict(size=14, color= COR_TEXTO_GRAFICO)
    )

    grafico.update_xaxes(
        showticklabels=False,
        visible=False,
        tickfont=dict(color= COR_TEXTO_GRAFICO)
    )

    grafico.update_yaxes(
        showgrid=False,
        title="",
        tickfont=dict(size=14, color= COR_TEXTO_GRAFICO)
    )
    
    return grafico

def grafico_qtde_contratacoes_por_entrega(qtdeContratacoesPorEntrega):

    grafico = px.bar(
        qtdeContratacoesPorEntrega,
        x = CUMPRIMENTO_PRAZO_ENTREGA_ATUAL,
        y = ARTEFATO_ENTREGA_ATUAL,
        orientation='h',
        text = CUMPRIMENTO_PRAZO_ENTREGA_ATUAL,
        color = ARTEFATO_ENTREGA_ATUAL,
        color_discrete_sequence=px.colors.qualitative.Set2        
    )

    grafico.update_layout(
        title=dict(text='Quantidade de Contratações por Entrega', x=0.02, font=dict(size=22)),
        showlegend=False,
        height = 1026
    )

    grafico.update_traces(
        width=0.9,
        textfont=dict(size= 14, color= COR_TEXTO_GRAFICO)
    )

    grafico.update_xaxes(
        showticklabels=False,
        visible=False,
        tickfont=dict(color= COR_TEXTO_GRAFICO)
    )

    grafico.update_yaxes(
        showgrid=False,
        title="",
        tickfont=dict(size=14, color= COR_TEXTO_GRAFICO)
    )

    return grafico

def grafico_valor_por_categoria(valorPorCategoria):

    valorPorCategoria['Valor Formatado'] = valorPorCategoria[VALOR_ANUAL_ESTIMADO].apply( lambda x: f"R$ {x:,.0f}".replace(",", ".").replace('X', '.'))
    valorPorCategoria[CATEGORIA_OBJETO] = valorPorCategoria[CATEGORIA_OBJETO].apply(quebrar_texto)

    grafico = px.bar(
        valorPorCategoria,
        x = CATEGORIA_OBJETO,
        y = VALOR_ANUAL_ESTIMADO,
        text = 'Valor Formatado',
        color = CATEGORIA_OBJETO,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    grafico.update_layout(
        title=dict(text='Valor Anual por Categoria', x=0.02, font=dict(size=22)),
        showlegend=False,
        margin=dict(l=20, t=50),
        height = 530,
    )

    grafico.update_traces(
        textposition='outside',
        width=0.9,
        textfont=dict(size=14, color= COR_TEXTO_GRAFICO)
    )

    grafico.update_xaxes(
        showticklabels=True,
        visible=True,
        title= "",
        tickfont=dict(size=13, color= COR_TEXTO_GRAFICO),
    )

    grafico.update_yaxes(
        showgrid=False,
        title="",
        visible=False,
        tickfont=dict(color= COR_TEXTO_GRAFICO)
    )

    return grafico

def grafico_ranking_cinco_maiores_contratacoes(rankingPorContratacoes):

    rankingPorContratacoes['Valor Formatado'] = rankingPorContratacoes[VALOR_ANUAL_ESTIMADO].apply( lambda x: f"R$ {x:,.0f}".replace(",", ".").replace('X', '.'))
    rankingPorContratacoes[TITULO_OBJETO] = rankingPorContratacoes[TITULO_OBJETO].fillna('Vazio')
    rankingPorContratacoes[TITULO_OBJETO] = rankingPorContratacoes[TITULO_OBJETO].apply(quebrar_texto)

    grafico = px.bar(
        rankingPorContratacoes,
        x = TITULO_OBJETO,
        y = VALOR_ANUAL_ESTIMADO,
        text = 'Valor Formatado',
        color = TITULO_OBJETO,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    grafico.update_layout(
        title=dict(text='5 Maiores Valores Anuais de Contratações', x=0.02, font=dict(size=22)),
        showlegend = False,
        height = 502,
        
    )

    grafico.update_traces(
        textposition = 'outside',
        width=0.7,
        textfont=dict(size=14, color= COR_TEXTO_GRAFICO)
    )

    grafico.update_xaxes(
        showticklabels=True,
        visible=True,
        title= "",
        tickfont=dict(size=14, color= COR_TEXTO_GRAFICO)
    )    

    grafico.update_yaxes(
        showgrid=False,
        title="",
        visible=False,
        tickfont=dict(color= COR_TEXTO_GRAFICO)
    )

    return grafico

def grafico_contratacoes_por_status(contratacoesPorStatus):

    grafico = px.bar(
        contratacoesPorStatus,
        x = STATUS,
        y = TITULO_OBJETO,
        text = TITULO_OBJETO,
        color = STATUS,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    grafico.update_layout(
        title=dict(text='Status das Contratações', x=0.02, font=dict(size=22)),
        showlegend = False,
        margin=dict(l=20, t=50),
        height = 500,
        
    )

    grafico.update_traces(
        textposition = 'outside',
        width=0.7,
        textfont=dict(size=14, color= COR_TEXTO_GRAFICO)
    )

    grafico.update_xaxes(
        showticklabels=True,
        visible=True,
        title= "",
        tickfont=dict(size=14, color= COR_TEXTO_GRAFICO)
    )    

    grafico.update_yaxes(
        showgrid=False,
        title="",
        visible=False,
        tickfont=dict(color= COR_TEXTO_GRAFICO)
    )

    return grafico
