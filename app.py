import streamlit as st
import subprocess

st.title("Executar Carga")

# Botão para rodar o script externo
if st.button("Executar carga_rl_perfil_icao_opcao.py"):
    with st.spinner("Executando..."):
        result = subprocess.run(
            ["python", "carga_rl_perfil_icao_opcao.py"],
            capture_output=True,
            text=True
        )
        if result.stdout:
            st.success("Saída:")
            st.code(result.stdout)
        if result.stderr:
            st.error("Erro:")
            st.code(result.stderr)
