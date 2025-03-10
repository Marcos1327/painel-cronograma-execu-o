import pandas as pd
import streamlit as st
import os
import requests
from io import BytesIO

# sharepoint_link = r'https://justicaeleitoral.sharepoint.com/_layouts/15/download.aspx?uniqueid=EYNnHN9IGYxAlqxSL0TB6aUBerWcuMCF06D3NIeWJwEsHg?e=e7k5oY'
caminho_excel = r'D:\Users\marcos.fernandes\OneDrive - TRIBUNAL SUPERIOR ELEITORAL\Documentos\Excel\Backups PCA\Cronograma de Execução do PCA 2025 - versão 22 (baixado em 24.02.2025).xlsx'
caminho_excel_casa = r'C:\Users\Marcos\OneDrive - TRIBUNAL SUPERIOR ELEITORAL\Documentos\Excel\Backups PCA\Cronograma de Execução do PCA 2025 - versão 22 (baixado em 24.02.2025).xlsx'
googledrive_download = r'https://drive.google.com/uc?export=download&id=1REqKfYOmD0YMS-yZArxgzXnvhJxa5mr9'

googledrive_download2 = r'https://drive.google.com/uc?export=download&id=1m3XoJcrfZWPchdU2za70bjZewNlIzJVl'

response = requests.get(googledrive_download2)

if response.status_code == 200:
    tabela = pd.read_excel(BytesIO(response.content), sheet_name="Contratações", header=1)
else:
    print(f"Erro ao baixar o arquivo. Código de status: {response.status_code}")    

tabela["Data de Conclusão Planejada*"] = pd.to_datetime(tabela['Data de Conclusão Planejada*'], format='%d/%m/%Y', errors='coerce')
tabela["Qtde de Entregas para a Conclusão"] = tabela["Qtde de Entregas para a Conclusão"].astype(str)
tabela["Dias Úteis para a Data de Conclusão Planejada"] = tabela["Dias Úteis para a Data de Conclusão Planejada"].astype(str)
tabela["Dias Úteis na Entrega Atual"] = tabela["Dias Úteis na Entrega Atual"].astype(str)
tabela["Prazo da Entrega Atual"] = tabela["Prazo da Entrega Atual"].astype(str)

for i in range(0,38):
    coluna = f"Data Planejada {i:02d}"
    if coluna in tabela.columns:
        tabela[coluna] = tabela[coluna].astype(str)
    else:
        print(f"Coluna '{coluna}' não foi encontrada")   

# tabela["Quantidade em Dia"] = tabela["Cumprimento do Prazo na Entrega Atual"].apply(lambda x: (x == "Em dia"))
# quantidadeContratacoesEmDia = tabela[tabela["Quantidade em Dia"] == True].shape[0]

# tabela["Quantidade em Atraso"] = tabela["Cumprimento do Prazo na Entrega Atual"].apply(lambda x: (x == "Atrasada"))
# quantidadeContratacoesEmAtraso = tabela[tabela["Quantidade em Atraso"] == True].shape[0]


