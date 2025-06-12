import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
import requests
import os

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portal Comercial Travelex", layout="wide", page_icon="📊")

# CONTADOR DE ACESSO (salvo no .streamlit/contador.txt)
contador_path = os.path.join(".streamlit", "contador.txt")
if not os.path.exists(contador_path):
    with open(contador_path, "w") as f:
        f.write("0")

with open(contador_path, "r+") as f:
    total_acessos = int(f.read()) + 1
    f.seek(0)
    f.write(str(total_acessos))

# FUNÇÃO PARA CARREGAR ANIMAÇÃO LOTTIE
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# URL da animação Lottie
lottie_welcome = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_vf1gk5ha.json")

# ESTILO CUSTOMIZADO
st.markdown("""
    <style>
        body {
            background-color: #F5F7FA;
        }
        .main {
            background-color: #F5F7FA;
        }
        .block-container {
            padding: 2rem;
        }
        h1, h2, h3 {
            color: #00205B;
        }
        .card {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            margin-bottom: 1.5rem;
        }
        .card:hover {
            box-shadow: 0 6px 18px rgba(0,0,0,0.1);
            transform: translateY(-4px);
        }
        .section-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: #00205B;
        }
        a {
            color: #0072CE;
            font-weight: 500;
            text-decoration: none;
        }
        a:hover {
            color: #005bb5;
        }
        .center-logo {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# LOGO E TÍTULO
st.markdown('<div class="center-logo">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 9])
with col1:
    st.image("logo_travelex.png", width=100)
with col2:
    st.markdown("## Portal Comercial Travelex")
    st.caption("Tudo o que você precisa, centralizado e fácil de acessar.")
st.markdown('</div>', unsafe_allow_html=True)

# AVISO NO TOPO
st.info("🔔 Atualização: Adicionamos o novo relatório de Telemetria!")

# MENU LATERAL
with st.sidebar:
    selected = option_menu(
        "Seções",
        ["🏠 Início", "📊 Dashboards", "📄 Formulários", "📚 Materiais"],
        icons=["house", "bar-chart", "file-earmark-text", "folder"],
        menu_icon="cast",
        default_index=0
    )

# CONTEÚDO DAS SEÇÕES
if selected == "🏠 Início":
    st.markdown("### 👋 Bem-vindo(a) ao Portal Comercial Travelex")
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_welcome, height=200, speed=1)
    with col2:
        st.markdown(
            "Use o menu lateral para navegar entre dashboards, formulários e materiais. "
            "Esse portal está em constante evolução para melhor servir o time comercial."
        )

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

    for i, dashboard in enumerate(dashboards):
        with cols[i % 2]:
            st.markdown(f"""
                <a href="{dashboard['link']}" target="_blank" style="text-decoration: none;">
                    <div class="card" style="margin: 1rem 0; transition: 0.3s ease; border: 1px solid #e0e0e0;">
                        <h4 style="margin: 0;">{dashboard['nome']}</h4>
                    </div>
                </a>
            """, unsafe_allow_html=True)

elif selected == "📄 Formulários":
    st.markdown("### 📄 Formulários Úteis")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("📝 [Pedidos de Migração de Carteira](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...)")
        st.markdown("📝 [Pedidos de Extração de CAM57](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...)")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "📚 Materiais":
    st.markdown("### 📚 Materiais e Documentos")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("📂 *(Esta seção pode conter links para treinamentos, manuais, apresentações internas etc. Me envie o que quiser que eu coloco aqui!)*")
        st.markdown('</div>', unsafe_allow_html=True)

# RODAPÉ
st.markdown("---")
st.caption("Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank")
st.markdown(f"<sub>🔒 Acesso: somente uso interno | 🧾 Dados de uso sendo monitorados | 📊 Total de acessos: <b>{total_acessos}</b></sub>", unsafe_allow_html=True)
