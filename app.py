import streamlit as st
import pandas as pd
import pyautogui
import time
import webbrowser
import urllib.parse
import sys
import os

ARQUIVO_PROCESSADOS = "telefones_processados.txt"  # Arquivo com telefones já enviados

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0

st.title("Gerador de Mensagens Automáticas - WhatsApp Web")

# Verificar permissões no macOS
if sys.platform == 'darwin':  # macOS
    st.sidebar.subheader("⚠️ Permissões Necessárias")
    st.sidebar.markdown("""
    ### Para o envio automático funcionar:
    1. Abra Preferências do Sistema
    2. Vá em Privacidade e Segurança
    3. Clique em Acessibilidade
    4. Clique no cadeado para fazer alterações
    5. Marque a caixa do Terminal ou do aplicativo que está rodando o script

    Se não aparecer na lista:
    1. Clique no + (mais)
    2. Navegue até Applications
    3. Selecione Terminal ou o aplicativo que está usando
    """)

# Configurações de tempo na sidebar
st.sidebar.subheader("Configurações")
tempo_carregamento = st.sidebar.slider(
    "Tempo de espera para carregamento (segundos)",
    min_value=20,
    max_value=40,
    value=25,
    help="Tempo de espera após abrir cada link"
)

# Área para templates de mensagem
st.subheader("Templates de Mensagem")
st.write("Use {nome} para inserir o nome da pessoa na mensagem")

# Lista de templates de mensagem
if 'message_templates' not in st.session_state:
    st.session_state.message_templates = ["Olá, me chamo José Henrique, este número é do CNPJ: {nome}, correto? Atuo com soluções em eneriga solar. Sabia que é possível reduzir sua conta de luz para apenas R$50,00 por mês? Posso disponibilizar um orçamento com um especialista sem compromisso?"]

# Função para adicionar novo template
def add_template():
    st.session_state.message_templates.append("")

# Mostrar e editar templates existentes
templates_to_remove = []
for i, template in enumerate(st.session_state.message_templates):
    col1, col2 = st.columns([4, 1])
    with col1:
        new_template = st.text_input(f"Template {i+1}", value=template, key=f"template_{i}")
        st.session_state.message_templates[i] = new_template
    with col2:
        if st.button("Remover", key=f"remove_{i}"):
            templates_to_remove.append(i)

# Remover templates marcados para remoção
for i in sorted(templates_to_remove, reverse=True):
    st.session_state.message_templates.pop(i)

# Botão para adicionar novo template
if st.button("Adicionar Novo Template"):
    add_template()

# Criar duas colunas para o layout do upload e início
col1, col2 = st.columns([2, 1])

with col1:
    # Upload do arquivo CSV
    uploaded_file = st.file_uploader("Faça upload do CSV (colunas: telefone,nome)", type=["csv"])

with col2:
    # Botão de início (só aparece quando houver arquivo)
    start_button = None
    if uploaded_file:
        start_button = st.button("▶️ Iniciar Envio de Mensagens")

# Verificar se há arquivo carregado
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if not "telefone" in df.columns or not "nome" in df.columns:
        st.error("CSV deve conter as colunas 'telefone' e 'nome'")
        st.stop()

    st.success("✅ CSV carregado com sucesso!")

    # Lê os telefones já processados anteriormente
    if os.path.exists(ARQUIVO_PROCESSADOS):
        with open(ARQUIVO_PROCESSADOS, "r") as f:
            telefones_enviados = set(l.strip() for l in f if l.strip())
    else:
        telefones_enviados = set()

    # Filtra o DataFrame para NÃO enviar para números já processados
    df_filtrado = df[~df['telefone'].astype(str).isin(telefones_enviados)]
    if df_filtrado.empty:
        st.info("Todos os telefones deste arquivo já foram processados!")
        st.stop()

    # Alterna templates entre os contatos restantes
    all_links = []
    templates = [t for t in st.session_state.message_templates if t.strip()]
    n_templates = len(templates)
    if n_templates == 0:
        st.error("Adicione pelo menos um template de mensagem!")
        st.stop()

    contatos_para_enviar = []
    for i, (_, row) in enumerate(df_filtrado.iterrows()):
        try:
            template = templates[i % n_templates]
            message = template.format(nome=row['nome'])
            encoded_message = urllib.parse.quote(message)
            link = f"https://web.whatsapp.com/send/?phone={str(row['telefone'])}&text={encoded_message}"
            all_links.append((link, str(row['telefone'])))
            contatos_para_enviar.append(str(row['telefone']))
        except Exception as e:
            st.error(f"Erro ao processar template: {str(e)}")
            st.stop()

    with st.expander("Ver links gerados"):
        for link, _ in all_links:
            st.write(link)

    if start_button:
        st.warning("⚠️ IMPORTANTE: Mantenha o Google Chrome como janela ativa!")
        st.warning("⚠️ Não interaja com o navegador durante o processo.")
        progress_bar = st.progress(0)
        status_text = st.empty()

        processados_com_sucesso = []

        for idx, (link, telefone) in enumerate(all_links, 1):
            try:
                status_text.text(f"Processando mensagem {idx} de {len(all_links)}...")

                # Abrir link no navegador
                webbrowser.open_new_tab(link)

                # Esperar o carregamento inicial
                time.sleep(tempo_carregamento)

                # Pressionar Enter para enviar
                pyautogui.press('enter')
                time.sleep(3)

                # Fechar a aba atual
                if sys.platform == "darwin":
                    pyautogui.hotkey('command', 'w')
                else:
                    pyautogui.hotkey('ctrl', 'w')

                # Esperar antes de prosseguir
                time.sleep(3)

                # Atualizar barra de progresso
                progress_bar.progress(idx / len(all_links))

                # Marca como processado com sucesso
                processados_com_sucesso.append(telefone)

            except Exception as e:
                st.error(f"Erro ao processar mensagem {idx}: {str(e)}")
                st.stop()

        # Adiciona números processados ao arquivo (apenas novos)
        if processados_com_sucesso:
            with open(ARQUIVO_PROCESSADOS, "a") as f:
                for telefone in processados_com_sucesso:
                    f.write(f"{telefone}\n")

        status_text.text("✅ Processo concluído!")
        st.success(f"Todas as {len(processados_com_sucesso)} mensagens foram processadas!")
