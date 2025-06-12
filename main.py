import streamlit as st
from streamlit_option_menu import option_menu
import os

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portal Comercial Travelex", layout="wide", page_icon="📊")

# CONTADOR DE ACESSO
contador_path = os.path.join(".streamlit", "contador.txt")
if not os.path.exists(contador_path):
    with open(contador_path, "w") as f:
        f.write("0")

with open(contador_path, "r+") as f:
    total_acessos = int(f.read()) + 1
    f.seek(0)
    f.write(str(total_acessos))

# ESTILO
st.markdown("""
    <style>
        body {
            background-color: #F5F7FA;
        }
        .main {
            background-color: #F5F7FA;
        }
        .block-container {
            padding: 2rem 3rem;
        }
        .sidebar .sidebar-content {
            background-color: #00205B;
        }
        .css-1d391kg {
            background-color: #00205B !important;
        }
        .card {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            margin-bottom: 1.5rem;
            transition: 0.3s;
        }
        .card:hover {
            box-shadow: 0 6px 18px rgba(0,0,0,0.1);
            transform: translateY(-4px);
        }
        h1, h2, h3, h4, h5 {
            color: #00205B;
        }
        .metric-card {
            background-color: #DDE7F2;
            border-radius: 12px;
            padding: 1.2rem;
            text-align: center;
            color: #00205B;
        }
    </style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    selected = option_menu(
        "Seções",
        ["🏠 Início", "📊 Dashboards", "📄 Formulários", "📚 Materiais"],
        icons=["house", "bar-chart", "file-earmark-text", "folder"],
        menu_icon="cast",
        default_index=0
    )

# LOGO E TÍTULO
st.markdown('<div style="display:flex;align-items:center;gap:20px;margin-bottom:20px;">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 9])
with col1:
    st.image("logo_travelex.png", width=100)
with col2:
    st.markdown("## Central de Planejamento Comercial")
    st.caption("Travelex Bank · Tudo o que você precisa em um só lugar.")
st.markdown("</div>", unsafe_allow_html=True)

# ALERTA
st.info("🔔 Atualização: Adicionamos o novo relatório de Telemetria!")

# CONTEÚDO
if selected == "🏠 Início":
    # Bloco de meta do mês
    st.markdown("### 📈 Meta do Mês")
    with st.container():
        st.markdown('<div class="metric-card"><h2>75%</h2><p>Meta atingida até agora</p></div>', unsafe_allow_html=True)

    # Dashboards
    st.markdown("### 📊 Dashboards Comerciais")
    dash1, dash2 = st.columns(2)
    with dash1:
        st.markdown('<div class="card">📈 [Gestão Comercial – Market Share](https://app.powerbi.com/links/VrFjeMY32s)</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">📊 [Raio X](https://app.powerbi.com/links/r_cCxY0hQF)</div>', unsafe_allow_html=True)
    with dash2:
        st.markdown('<div class="card">📡 [Telemetria](https://app.powerbi.com/links/DN8VawnQyN)</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">📋 [Resultados vs Meta](https://app.powerbi.com/links/5tOpR8JJh4)</div>', unsafe_allow_html=True)

    # Formulários
    st.markdown("### 📄 Formulários Úteis")
    form1, form2 = st.columns(2)
    with form1:
        st.markdown('<div class="card">📝 [Migração de Carteira](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...)</div>', unsafe_allow_html=True)
    with form2:
        st.markdown('<div class="card">📑 [Extração de CAM57](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...)</div>', unsafe_allow_html=True)

    # Materiais
    st.markdown("### 📚 Materiais")
    st.markdown('<div class="card">📂 Esta seção pode conter links para treinamentos, manuais, apresentações internas etc. Me envie o que quiser que eu coloco aqui!</div>', unsafe_allow_html=True)

elif selected == "📊 Dashboards":
    st.markdown("### 📊 Dashboards Comerciais")
    dashboards = [
        {"nome": "Gestão Comercial – Market Share", "link": "https://app.powerbi.com/links/VrFjeMY32s"},
        {"nome": "Telemetria", "link": "https://app.powerbi.com/links/DN8VawnQyN"},
        {"nome": "Raio X", "link": "https://app.powerbi.com/links/r_cCxY0hQF"},
        {"nome": "Resultados vs Meta", "link": "https://app.powerbi.com/links/5tOpR8JJh4"},
    ]
    col1, col2 = st.columns(2)
    cols = [col1, col2]
    for i, dash in enumerate(dashboards):
        with cols[i % 2]:
            st.markdown(f'<div class="card">🔗 [{dash["nome"]}]({dash["link"]})</div>', unsafe_allow_html=True)

elif selected == "📄 Formulários":
    st.markdown("### 📄 Formulários Úteis")
    st.markdown('<div class="card">📝 [Pedidos de Migração de Carteira](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...)</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📑 [Pedidos de Extração de CAM57](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...)</div>', unsafe_allow_html=True)

elif selected == "📚 Materiais":
    st.markdown("### 📚 Materiais e Documentos")
    st.markdown('<div class="card">📂 *(Envie os materiais que quiser adicionar aqui)*</div>', unsafe_allow_html=True)

# RODAPÉ
st.markdown("---")
st.caption("Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank")
st.markdown(f"<sub>🔒 Acesso: somente uso interno | 🧾 Dados de uso sendo monitorados | 📊 Total de acessos: <b>{total_acessos}</b></sub>", unsafe_allow_html=True)
