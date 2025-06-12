import streamlit as st
from streamlit_option_menu import option_menu
import os
from PIL import Image

# CONFIGURANDO A PÁGINA
st.set_page_config(
    page_title="Portal Comercial Travelex",
    layout="wide",
    page_icon="📊"
)

# CSS PERSONALIZADO
st.markdown("""
    <style>
    .main {
        background-color: #F5F7FA;
    }
    .block-container {
        padding: 2rem 4rem;
    }
    h1, h2, h3, h4 {
        color: #00205B;
    }
    .section-title {
        font-size: 1.6rem;
        font-weight: 600;
        margin-top: 3rem;
        margin-bottom: 1rem;
        color: #00205B;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .card {
        background-color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        transition: transform 0.2s ease;
    }
    .card:hover {
        transform: scale(1.01);
    }
    .search-section {
        margin-bottom: 2rem;
    }
    .header-wrapper {
        background: white;
        padding: 1rem 2rem 2rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-radius: 12px;
    }
    .search-bar-wrapper {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .stTextInput>div>input {
        border: 1px solid #00205B;
        border-radius: 6px;
        padding: 0.5rem;
    }
    .stButton>button {
        background-color: white;
        border: 1px solid #00205B;
        border-radius: 6px;
        color: #00205B;
    }
    </style>
""", unsafe_allow_html=True)

# CONTADOR DE ACESSO
contador_path = os.path.join(".streamlit", "contador.txt")
os.makedirs(".streamlit", exist_ok=True)
if not os.path.exists(contador_path):
    with open(contador_path, "w") as f:
        f.write("0")

with open(contador_path, "r+") as f:
    total_acessos = int(f.read()) + 1
    f.seek(0)
    f.write(str(total_acessos))

# SIDEBAR
with st.sidebar:
    selected = option_menu(
        "Seções",
        ["🏠 Início", "📊 Dashboards", "📄 Formulários", "📚 Materiais", "🏦 Área de Crédito"],
        icons=["house", "bar-chart", "file-earmark-text", "folder", "building"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"background-color": "#00205B"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin": "5px 0"},
            "nav-link-selected": {"background-color": "#004C99"},
        }
    )

# CABEÇALHO
st.markdown('<div class="header-wrapper">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 9])
with col1:
    st.image("logo_travelex.png", width=110)
with col2:
    st.markdown("## Central de Planejamento Comercial")
    st.caption("Travelex Bank · Tudo o que você precisa em um só lugar.")
st.markdown('</div>', unsafe_allow_html=True)

# BARRA DE BUSCA
st.markdown("<div class='section-title'>🔍 Pesquisar</div>", unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns([10, 1])
    with col1:
        search_query = st.text_input("", placeholder="Buscar dashboards, formulários ou materiais")
    with col2:
        st.button("🔎 Buscar")

# BLOCOS DE CONTEÚDO

st.markdown("<div class='section-title'>📊 Dashboards Comerciais</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='card'>📌 [Gestão Comercial – Market Share](https://app.powerbi.com/links/VrFjeMY32s)</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🔎 [Raio X](https://app.powerbi.com/links/r_cCxY0hQF)</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'>📈 [Telemetria](https://app.powerbi.com/links/DN8VawnQyN)</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>📊 [Resultados vs Meta](https://app.powerbi.com/links/5tOpR8JJh4)</div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>📝 Formulários</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='card'>📄 [Migração de Carteira](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...)</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'>🧾 [Extração de CAM57](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...)</div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>📚 Materiais</div>", unsafe_allow_html=True)
st.markdown("<div class='card'>📁 [Treinamentos e Manuais](#)</div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>🏦 Área de Crédito</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='card'>📝 [Proposta de Crédito](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...)</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>📊 [New Dashboard - Crédito](https://app.powerbi.com/links/creditdashboard)</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'>🌱 [Formulário ESG](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...)</div>", unsafe_allow_html=True)

# RODAPÉ
st.markdown("---")
st.caption("Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank")
st.markdown(f"<sub>🔒 Acesso: somente uso interno | 🧾 Dados de uso sendo monitorados | 📊 Total de acessos: <b>{total_acessos}</b></sub>", unsafe_allow_html=True)
