import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Executor de Script", layout="centered")

st.title("🚀 Executor de Scripts de Carga")

st.markdown("""
Este app executa scripts Python de carga (ex: MySQL → Oracle).  
Selecione abaixo qual script deseja rodar.
""")

# Lista de scripts disponíveis
scripts_disponiveis = [
    "carga_tb_instituicao.py",
    "carga_tb_perfil_inst.py",
    "carga_rl_perfil_icao_opcao.py"
]

# Caixa de seleção
script_selecionado = st.selectbox("Selecione o script para executar:", scripts_disponiveis)

# Botão para executar
if st.button("Executar Script Selecionado"):
    with st.spinner(f"Executando {script_selecionado}..."):
        try:
            resultado = subprocess.run(
                ["python", script_selecionado],
                capture_output=True,
                text=True
            )

            # Exibe saída padrão
            if resultado.stdout:
                st.subheader("Saída (stdout):")
                st.code(resultado.stdout, language="bash")

            # Exibe erro, se houver
            if resultado.stderr:
                st.subheader("Erros (stderr):")
                st.code(resultado.stderr, language="bash")

        except Exception as e:
            st.error(f"Erro ao executar o script: {e}")
