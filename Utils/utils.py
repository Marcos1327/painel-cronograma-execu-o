import streamlit as st

def format_number(value, prefix=''):
    for unit in ['', '']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        
        # value /= 1000

        formatted_value = f'{value:,.0f}'.replace(',', '.')
        
    return f'{prefix} {formatted_value}' #Milhões


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def quebrar_texto(texto, max_caracteres=20): #31

    if len(texto) <= max_caracteres:
        return texto
    
    meio_texto = len(texto) // 2

    for i in range(meio_texto, 0, -1):
        if texto[i] == " ":
            texto_quebrado = texto[:i] + "<br>" + texto[i+1:]
            return texto_quebrado
        
    return texto

def quebrar_texto2(texto, max_caracteres=20): #31

    if len(texto) <= max_caracteres:
        return texto
    
    meio_texto = len(texto) // 2

    for i in range(meio_texto, 0, -1):
        if texto[i] == " ":
            texto_quebrado = texto[:i] + "<br>" + texto[i+1:]
            break

    else:
        return texto
    
    print(len(texto_quebrado))

    if len(texto_quebrado) > 12:
        meio_segunda_parte = len(texto_quebrado) // 2
        for j in range(meio_segunda_parte, 0, -1):
            if texto_quebrado[j] == " ":
                texto_quebrado = texto_quebrado[:j] + "<br>" + texto_quebrado[j+1:]
                break
    print(texto_quebrado)
        
    return texto_quebrado

quebrar_texto2("Despacho pela Inicialização da Contratação")    



################ Cria uma borda a partir de um retangulo ########################
# shapes=[
#     dict(
#         type="rect",
#         xref="paper",
#         yref="paper",
#         x0=-0.1,
#         y0=0,
#         x1=1,
#         y1=1.2,
#         line=dict(color="white", width=2),
#         fillcolor="rgba(0,0,0,0)"
#     )
# ],