import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Gerenciador de Dados - Planilha PET")

# Upload do arquivo Excel
uploaded_file = st.file_uploader("Carregue sua planilha Excel", type=["xlsx"])

if uploaded_file:
    try:
        # Tentar ler o arquivo Excel com a biblioteca 'openpyxl'
        df = pd.read_excel(uploaded_file, engine='openpyxl')
        
        # Mostrar os dados na tela
        st.write("Dados carregados:")
        st.dataframe(df)

        # Adicionar novos registros
        st.subheader("Adicionar Novo Registro")
        cols = df.columns.tolist()
        novo_dado = {col: st.text_input(col, "") for col in cols}
        
        if st.button("Adicionar Registro"):
            # Adicionar o registro ao DataFrame
            df = df.append(novo_dado, ignore_index=True)
            st.success("Registro adicionado com sucesso!")
        
        # Opção para baixar os dados atualizados
        st.download_button(
            label="Baixar Planilha Atualizada",
            data=df.to_excel(index=False),
            file_name="planilha_atualizada.xlsx"
        )
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
