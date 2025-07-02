import streamlit as st
import subprocess

st.title("Executar Carga")

# Botão para rodar o script externo
if st.button("Executar teste_conexao.py"):
    with st.spinner("Executando..."):
        result = subprocess.run(
            ["python", "teste_conexao.py"],
            capture_output=True,
            text=True
        )
        if result.stdout:
            st.success("Saída:")
            st.code(result.stdout)
        if result.stderr:
            st.error("Erro:")
            st.code(result.stderr)
