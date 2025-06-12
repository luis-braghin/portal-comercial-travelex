import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portal Comercial Travelex", layout="wide", page_icon="📊")

# ESTILO CUSTOMIZADO COM CORES TRAVELEX
st.markdown("""
    <style>
        body, .main {
            background-color: #F5F7FA;
        }
        .block-container {
            padding: 2rem;
        }
        h1, h2, h3, .st-emotion-cache-10trblm, .st-emotion-cache-1avcm0n {
            color: #00205B;
        }
        .css-1d391kg {
            background-color: #00205B !important;
        }
        .css-1v0mbdj, .st-emotion-cache-1v0mbdj {
            background-color: #E4002B !important;
            color: white !important;
        }
        .css-1x8cf1d, .st-emotion-cache-1x8cf1d {
            color: white !important;
        }
        a {
            color: #0072CE;
            font-weight: 500;
            text-decoration: none;
        }
        a:hover {
            color: #005bb5;
        }
        .card {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            margin-bottom: 1.5rem;
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

# MENSAGEM DE ATUALIZAÇÃO
st.info("\U0001F6A8 Atualização: Adicionamos o novo relatório de Telemetria!")

# MENU LATERAL
with st.sidebar:
    selected = option_menu(
        "Seções",
        ["\U0001F3E0 Início", "\U0001F4CA Dashboards", "\U0001F4C4 Formulários", "\U0001F4DA Materiais"],
        icons=["house", "bar-chart", "file-earmark-text", "folder"],
        menu_icon="cast",
        default_index=0
    )

# CONTEÚDO DAS SEÇÕES
if selected == "\U0001F3E0 Início":
    st.markdown("### \U0001F44B Bem-vindo(a) ao Portal Comercial Travelex")
    st.markdown(
        "Use o menu lateral para navegar entre dashboards, formulários e materiais. "
        "Esse portal está em constante evolução para melhor servir o time comercial."
    )

elif selected == "\U0001F4CA Dashboards":
    st.markdown("### \U0001F4CA Dashboards Comerciais")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("- [Gestão Comercial – Market Share](https://app.powerbi.com/links/VrFjeMY32s)")
        st.markdown("- [Telemetria](https://app.powerbi.com/links/DN8VawnQyN)")
        st.markdown("- [Raio X](https://app.powerbi.com/links/r_cCxY0hQF)")
        st.markdown("- [Resultados vs Meta](https://app.powerbi.com/links/5tOpR8JJh4)")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "\U0001F4C4 Formulários":
    st.markdown("### \U0001F4C4 Formulários Úteis")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("- [Pedidos de Migração de Carteira](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4d0eK42lIfQ7vVodaBv4SADNOrM5qGKC6CrhUODZPTUtHWU4xTTFDWTcwQkRIRlk0QVVNNS4u)")
        st.markdown("- [Pedidos de Extração de CAM57](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4d0eK42lIfQ7vVhiVOkKoYqdBqDjlbS0O0SNUQTZMVUVEVk42U1JaRjlLNEFXWVFNWEZGNS4u)")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "\U0001F4DA Materiais":
    st.markdown("### \U0001F4DA Materiais e Documentos")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("*(Esta seção pode conter links para treinamentos, manuais, apresentações internas etc. Me envie o que quiser que eu coloco aqui!)*")
        st.markdown('</div>', unsafe_allow_html=True)

# RODAPÉ ATUALIZADO COM ANALYTICS BÁSICO
st.markdown("---")
st.caption("Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank")

# CONTADOR DE VISITAS (simples)
count_file = "counter.txt"
if not os.path.exists(count_file):
    with open(count_file, "w") as f:
        f.write("0")
with open(count_file, "r") as f:
    count = int(f.read().strip()) + 1
with open(count_file, "w") as f:
    f.write(str(count))
st.caption(f"\U0001F4C8 Total de acessos: {count}")
