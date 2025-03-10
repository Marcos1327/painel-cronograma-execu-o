import plotly.express as px
import streamlit as st
from Utils.utils import quebrar_texto
from Utils.constantes import COR_TEXTO_GRAFICO, COR_FUNDO_GRAFICO, COR_BLOCO_GRAFICO, CUMPRIMENTO_PRAZO_ENTREGA_ATUAL, ARTEFATO_ENTREGA_ATUAL, CATEGORIA_OBJETO, STATUS, TITULO_OBJETO, UNIDADE_REQUISITANTE, VALOR_ANUAL_ESTIMADO, DATA_CONCLUSAO_ESTIMADA


def grafico_contratacoes_em_dia(contratacoesEmDia):

    grafico = px.bar(
        contratacoesEmDia,
        x = UNIDADE_REQUISITANTE,
        y = CUMPRIMENTO_PRAZO_ENTREGA_ATUAL,
        text = CUMPRIMENTO_PRAZO_ENTREGA_ATUAL,
        color = UNIDADE_REQUISITANTE,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    grafico.update_layout(
        title=dict(text='Contratações em Dia', x=0.02, font=dict(size=22)),
        showlegend = False,
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


def grafico_contratacoes_em_atraso(contratacoesEmAtraso):
    grafico = px.bar(
        contratacoesEmAtraso,
        x = UNIDADE_REQUISITANTE,
        y = CUMPRIMENTO_PRAZO_ENTREGA_ATUAL,
        text = CUMPRIMENTO_PRAZO_ENTREGA_ATUAL,
        color = UNIDADE_REQUISITANTE,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    grafico.update_layout(
        title=dict(text='Contratações em Atraso', x=0.02, font=dict(size=22)),
        showlegend = False,
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


def grafico_entregas_em_dia(entregasEmDia):

    entregasEmDia[ARTEFATO_ENTREGA_ATUAL] = entregasEmDia[ARTEFATO_ENTREGA_ATUAL].apply(quebrar_texto)

    grafico = px.bar(
        entregasEmDia,
        x = ARTEFATO_ENTREGA_ATUAL,
        y = CUMPRIMENTO_PRAZO_ENTREGA_ATUAL,
        text = CUMPRIMENTO_PRAZO_ENTREGA_ATUAL,
        color = ARTEFATO_ENTREGA_ATUAL,
        color_discrete_sequence = px.colors.qualitative.Set2
    )

    grafico.update_layout(
        title=dict(text='Entregas em Dia', x=0.02, font=dict(size=22)),
        showlegend = False,
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

def grafico_entregas_em_atraso(entregasEmAtraso):

    # entregasEmAtraso[ARTEFATO_ENTREGA_ATUAL] = entregasEmAtraso[ARTEFATO_ENTREGA_ATUAL].apply(quebrar_texto)

    grafico = px.bar(
        entregasEmAtraso,
        x = CUMPRIMENTO_PRAZO_ENTREGA_ATUAL,
        y = ARTEFATO_ENTREGA_ATUAL,
        orientation='h',
        text = CUMPRIMENTO_PRAZO_ENTREGA_ATUAL,
        color = ARTEFATO_ENTREGA_ATUAL,
        color_discrete_sequence = px.colors.qualitative.Set2
    )

    grafico.update_layout(
        title=dict(text='Entregas em Atraso', x=0.02, font=dict(size=22)),
        showlegend = False,
    )

    grafico.update_traces(
        textposition = 'outside',
        width=0.7,
        textfont=dict(size=14, color= COR_TEXTO_GRAFICO)
    )

    grafico.update_xaxes(
        showticklabels=True,
        visible=False,
        title= "",
        tickfont=dict(size=14, color= COR_TEXTO_GRAFICO)
    )

    grafico.update_yaxes(
        showgrid=False,
        title="",
        visible=True,
        tickfont=dict(color= COR_TEXTO_GRAFICO)
    )       

    return grafico


def grafico_conclusao_estimada_por_mes(objetoPorMes):

    grafico = px.bar(
        objetoPorMes,
        x = 'Mês',
        y = CUMPRIMENTO_PRAZO_ENTREGA_ATUAL,
        text = CUMPRIMENTO_PRAZO_ENTREGA_ATUAL,
        color= 'Mês',
        color_discrete_sequence = px.colors.qualitative.Set2
    )

    grafico.update_layout(
        title=dict(text='Planejamento de Conclusão das Contratações', x=0.02, font=dict(size=22)),
        showlegend = False,
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