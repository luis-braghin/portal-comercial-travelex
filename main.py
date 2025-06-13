import streamlit as st
from streamlit_option_menu import option_menu
import base64
import os

# CONFIG INICIAL
st.set_page_config(page_title="Portal Comercial Travelex", layout="wide")

# CONTADOR DE ACESSO
contador_path = os.path.join(".streamlit", "contador.txt")
if not os.path.exists(contador_path):
    with open(contador_path, "w") as f:
        f.write("0")
with open(contador_path, "r+") as f:
    total_acessos = int(f.read()) + 1
    f.seek(0)
    f.write(str(total_acessos))

# FUNÇÃO PARA IMAGEM DA LOGO
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64_of_bin_file("logo_travelex.png")

# CSS
st.markdown("""
<style>
    .card {
        background-color: white;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        transition: all 0.2s ease-in-out;
        font-size: 16px;
    }
    .card:hover {
        box-shadow: 0 6px 14px rgba(0,0,0,0.15);
        transform: scale(1.02);
    }
    .metric-block {
        background-color: #00205B;
        padding: 1.2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }
    h2.section-title {
        background-color: #002B5B;
        color: white;
        padding: 10px 16px;
        border-radius: 8px;
        font-size: 18px;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# SIDEBAR COM OPTION MENU
with st.sidebar:
    st.image(f"data:image/png;base64,{logo_base64}", width=150)
    selected = option_menu(
        "Seções",
        ["🏠 Início", "📊 Dashboards", "📄 Formulários", "📚 Materiais", "🏢 Crédito"],
        icons=["house", "bar-chart", "file-earmark-text", "folder", "building"],
        default_index=0
    )

# DADOS
dashboards = [
    ("📌 Gestão Comercial – Market Share", "https://app.powerbi.com/links/VrFjeMY32s"),
    ("🧭 Telemetria", "https://app.powerbi.com/links/DN8VawnQyN"),
    ("🔎 Raio X", "https://app.powerbi.com/links/r_cCxY0hQF"),
    ("📈 Resultados vs Meta", "https://app.powerbi.com/links/5tOpR8JJh4")
]

formularios = [
    ("📄 Migração de Carteira", "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4..."),
    ("📄 Extração de CAM57", "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...")
]

materiais = [
    ("📁 Treinamentos e Manuais", "https://example.com/materials")
]

credito = [
    ("🧾 Proposta de Crédito", "https://forms.office.com/pages/responsepage.aspx?id=creditform"),
    ("🌱 Formulário ESG", "https://forms.office.com/pages/responsepage.aspx?id=esgform"),
    ("📊 New Dashboard - Crédito", "https://app.powerbi.com/links/newcreditdash")
]

eventos = [
    ("🔔 Reunião Trimestral - 20 de Junho"),
    ("🧠 Workshop Estratégico - 27 de Junho"),
    ("📊 Atualização Power BI - 01 de Julho")
]

# CABEÇALHO AJUSTADO
st.markdown(f"""
<div style='background-color: #ffffff; padding: 30px 20px; border-radius: 10px;
box-shadow: 0px 0px 10px rgba(0,0,0,0.05); display: flex; align-items: center; margin-bottom: 20px;'>
    <img src='data:image/png;base64,{logo_base64}' width='60' style='margin-right: 20px;'>
    <div>
        <h1 style='margin-bottom: 0px; color: #002B5B;'>Portal de Planejamento Comercial</h1>
        <p style='margin-top: 5px; color: #6c757d;'>Travelex Bank · Tudo o que você precisa em um só lugar.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# NOTIFICAÇÃO
st.info("🔔 Atualização: Adicionamos o novo relatório de Telemetria!")


# CONTEÚDO POR SEÇÃO
if selected == "🏠 Início":
# Se não estiver buscando, mostra todos os blocos normalmente
if not query:
    # Meta
    st.markdown("### 📈 Meta do Mês")
    st.markdown("""
    <div class="metric-block">
        🎯 X%<br>
        <small>Meta atingida até agora</small>
    </div>
    """, unsafe_allow_html=True)

    # Eventos
    st.markdown("### 📅 Próximos Eventos")
    for evento in eventos:
        st.markdown(f"- {evento}")

# Resultados filtrados por busca
exibiu_resultado = False

# Dashboards
dash_filtered = [(n, l) for (n, l) in dashboards if query in n.lower()]
if dash_filtered:
    exibiu_resultado = True
    st.markdown('<h2 class="section-title">📊 Dashboards Comerciais</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, (nome, link) in enumerate(dash_filtered):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

# Formulários
form_filtered = [(n, l) for (n, l) in formularios if query in n.lower()]
if form_filtered:
    exibiu_resultado = True
    st.markdown('<h2 class="section-title">📄 Formulários</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, (nome, link) in enumerate(form_filtered):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

# Materiais
mat_filtered = [(n, l) for (n, l) in materiais if query in n.lower()]
if mat_filtered:
    exibiu_resultado = True
    st.markdown('<h2 class="section-title">📚 Materiais</h2>', unsafe_allow_html=True)
    for nome, link in mat_filtered:
        st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

# Crédito
cred_filtered = [(n, l) for (n, l) in credito if query in n.lower()]
if cred_filtered:
    exibiu_resultado = True
    st.markdown('<h2 class="section-title">🏢 Área de Crédito</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, (nome, link) in enumerate(cred_filtered):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

# Caso não encontre nenhum resultado
if query and not exibiu_resultado:
    st.warning("🔎 Nenhum resultado encontrado para sua busca.")

    # Meta
    st.markdown("### 📈 Meta do Mês")
    st.markdown("""
    <div class="metric-block">
        🎯 X%<br>
        <small>Meta atingida até agora</small>
    </div>
    """, unsafe_allow_html=True)

    # Eventos
    st.markdown("### 📅 Próximos Eventos")
    for evento in eventos:
        st.markdown(f"- {evento}")

    # Dashboards
    st.markdown('<h2 class="section-title">📊 Dashboards Comerciais</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, (nome, link) in enumerate(dashboards):
        if query in nome.lower():
            with (col1 if i % 2 == 0 else col2):
                st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

    # Formulários
    st.markdown('<h2 class="section-title">📄 Formulários</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, (nome, link) in enumerate(formularios):
        if query in nome.lower():
            with (col1 if i % 2 == 0 else col2):
                st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

    # Materiais
    st.markdown('<h2 class="section-title">📚 Materiais</h2>', unsafe_allow_html=True)
    for nome, link in materiais:
        if query in nome.lower():
            st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

    # Crédito
    st.markdown('<h2 class="section-title">🏢 Área de Crédito</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, (nome, link) in enumerate(credito):
        if query in nome.lower():
            with (col1 if i % 2 == 0 else col2):
                st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

elif selected == "📊 Dashboards":
    st.markdown("### 📊 Dashboards Comerciais")
    for nome, link in dashboards:
        st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

elif selected == "📄 Formulários":
    st.markdown("### 📄 Formulários Úteis")
    for nome, link in formularios:
        st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

elif selected == "📚 Materiais":
    st.markdown("### 📚 Materiais e Documentos")
    for nome, link in materiais:
        st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

elif selected == "🏢 Crédito":
    st.markdown("### 🏢 Área de Crédito")
    for nome, link in credito:
        st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

# RODAPÉ
st.markdown("---")
st.caption("Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank")
st.markdown(f"<sub>🔒 Acesso: somente uso interno | 🧾 Dados de uso sendo monitorados | 📊 Total de acessos: <b>{total_acessos}</b></sub>", unsafe_allow_html=True)
