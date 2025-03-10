import streamlit as st

def exibir_aba_dataset(tabela):
    st.dataframe(tabela, height=500)


# def get_file(senha_correta):

#     senha = st.sidebar.text_input("Digite a senha para fazer upload do arquivo:", type="password")

#     if senha == senha_correta:
#         st.sidebar.success("Acesso Permitido")

#         uploaded_file = st.sidebar.file_uploader("Choose a file",type=["xlsx"])

#         return uploaded_file
#     else:
#         if senha:
#             st.sidebar.error("Acesso Negado. Você não tem permissão para fazer upload do arquivo")
#     return None