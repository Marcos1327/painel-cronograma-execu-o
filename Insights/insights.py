import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Dataset.dados import tabela as tb
from Utils.constantes import UNIDADE_REQUISITANTE, VALOR_ANUAL_ESTIMADO, ARTEFATO_ENTREGA_ATUAL, CUMPRIMENTO_PRAZO_ENTREGA_ATUAL, CATEGORIA_OBJETO, TITULO_OBJETO, STATUS, DATA_CONCLUSAO_ESTIMADA

def gerar_insights_derivados(tabela):

    # ____________________________________________ DataFrame DASHBOARD GERAL ____________________________________________

    #DataFrame Valor por Unidade Requisitante
    valorPorUnidadeRequisitante = tabela.groupby(UNIDADE_REQUISITANTE)[[VALOR_ANUAL_ESTIMADO]].sum().sort_values(VALOR_ANUAL_ESTIMADO, ascending=False)
    valorPorUnidadeRequisitante = valorPorUnidadeRequisitante.reset_index()

    #DataFrame Quantidade de Contratações por entrega
    qtdeContratacoesPorEntrega = tabela.groupby(ARTEFATO_ENTREGA_ATUAL)[[CUMPRIMENTO_PRAZO_ENTREGA_ATUAL]].count().sort_values(CUMPRIMENTO_PRAZO_ENTREGA_ATUAL, ascending=False)
    qtdeContratacoesPorEntrega = qtdeContratacoesPorEntrega.reset_index()

    #DataFrame Valor por Categoria do Objeto
    valorPorCategoria = tabela.groupby(CATEGORIA_OBJETO)[[VALOR_ANUAL_ESTIMADO]].sum().sort_values(VALOR_ANUAL_ESTIMADO, ascending=False)
    valorPorCategoria = valorPorCategoria.reset_index()

    #DataFrame Ranking das Cinco Maiores Contratações 
    rankingPorContratacoes = tabela[[TITULO_OBJETO, VALOR_ANUAL_ESTIMADO]].sort_values(VALOR_ANUAL_ESTIMADO, ascending=False).head(5)

    #DataFrame Contratações por Status
    contratacoesPorStatus = tabela.groupby(STATUS)[[TITULO_OBJETO]].count().sort_values(TITULO_OBJETO, ascending=False)
    contratacoesPorStatus = contratacoesPorStatus.reset_index()

    # ____________________________________________ DataFrame DASHBOARD PRAZO ____________________________________________

    #DataFrame Contratações em Dia
    filtroEmDia = tabela[CUMPRIMENTO_PRAZO_ENTREGA_ATUAL] == "Em dia"
    contratacoesEmDia = tabela[filtroEmDia].groupby(UNIDADE_REQUISITANTE)[[CUMPRIMENTO_PRAZO_ENTREGA_ATUAL]].count().sort_values(CUMPRIMENTO_PRAZO_ENTREGA_ATUAL, ascending=False)
    contratacoesEmDia = contratacoesEmDia.reset_index()

    #DataFrame Contratações em Atraso
    filtroEmAtraso = tabela[CUMPRIMENTO_PRAZO_ENTREGA_ATUAL] == "Atrasada"
    contratacoesEmAtraso = tabela[filtroEmAtraso].groupby(UNIDADE_REQUISITANTE)[[CUMPRIMENTO_PRAZO_ENTREGA_ATUAL]].count().sort_values(CUMPRIMENTO_PRAZO_ENTREGA_ATUAL, ascending=False)
    contratacoesEmAtraso = contratacoesEmAtraso.reset_index()

    #DataFrame Entregas em Dia
    filtroEntregasEmdia = tabela[CUMPRIMENTO_PRAZO_ENTREGA_ATUAL] == "Em dia"
    entregasEmDia = tabela[filtroEntregasEmdia].groupby(ARTEFATO_ENTREGA_ATUAL)[[CUMPRIMENTO_PRAZO_ENTREGA_ATUAL]].count().sort_values(CUMPRIMENTO_PRAZO_ENTREGA_ATUAL, ascending=False)
    entregasEmDia = entregasEmDia.reset_index()

    #DataFrame Entregas em Atraso
    filtroEntregasEmAtraso = tabela[CUMPRIMENTO_PRAZO_ENTREGA_ATUAL] == "Atrasada"
    entregasEmAtraso = tabela[filtroEntregasEmAtraso].groupby(ARTEFATO_ENTREGA_ATUAL)[[CUMPRIMENTO_PRAZO_ENTREGA_ATUAL]].count().sort_values(CUMPRIMENTO_PRAZO_ENTREGA_ATUAL, ascending=False).head(14)
    entregasEmAtraso = entregasEmAtraso.reset_index()

    #DataFrame Conclusão das contratações por mês

    date = tabela[tabela["Data de Conclusão Planejada*"].dt.year == 2025]

    meses_abreviados = {
        1: "jan", 2: "fev", 3: "mar", 4: "abr", 5: "mai", 6: "jun",
        7: "jul", 8: "ago", 9: "set", 10: "out", 11: "nov", 12: "dez"
    } 

    tabela.loc[:,'Mês'] = date[DATA_CONCLUSAO_ESTIMADA].dt.month.map(meses_abreviados)

    tabela['Numero_Mes'] = tabela[DATA_CONCLUSAO_ESTIMADA].dt.month

    objetosPorMês = tabela.groupby(["Mês", "Numero_Mes"])[[CUMPRIMENTO_PRAZO_ENTREGA_ATUAL]].count()
    objetosPorMês = objetosPorMês.reset_index()

    objetosPorMês = objetosPorMês.sort_values("Numero_Mes")

    objetosPorMês = objetosPorMês.drop(columns=["Numero_Mes"])

    return valorPorUnidadeRequisitante, qtdeContratacoesPorEntrega, valorPorCategoria, rankingPorContratacoes, contratacoesPorStatus, contratacoesEmDia, contratacoesEmAtraso, entregasEmDia, entregasEmAtraso, objetosPorMês


# gerar_insights_derivados(tb)

