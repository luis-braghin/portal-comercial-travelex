import streamlit as st
from streamlit_option_menu import option_menu

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portal Comercial Travelex", layout="wide", page_icon="📊")

# ESTILO CUSTOMIZADO + RESPONSIVIDADE
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
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            margin-bottom: 1.5rem;
        }
        a {
            color: #0072CE;
            font-weight: 500;
            text-decoration: none;
        }
        a:hover {
            color: #005bb5;
        }
        .sidebar-logo {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        @media screen and (max-width: 768px) {
            .block-container {
                padding: 1rem;
            }
            .card {
                padding: 1rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# MENU LATERAL COM LOGO
# LOGO na sidebar com imagem local
with st.sidebar:
    st.markdown(
        """
        <div style='text-align: center; margin-bottom: 20px;'>
            <img src='logo_travelex.png' width='160'>
        </div>
        """,
        unsafe_allow_html=True
    )

    selected = option_menu(
        "Seções",
        ["🏠 Início", "📊 Dashboards", "📄 Formulários", "📚 Materiais"],
        icons=["house", "bar-chart", "file-earmark-text", "folder"],
        menu_icon="cast",
        default_index=0
    )

# TÍTULO
st.markdown("## Portal Comercial Travelex")
st.caption("Tudo o que você precisa, centralizado e fácil de acessar.")

# CONTEÚDO DAS SEÇÕES
if selected == "🏠 Início":
    st.markdown("### 👋 Bem-vindo(a) ao Portal Comercial Travelex")
    st.markdown(
        "Use o menu lateral para navegar entre dashboards, formulários e materiais. "
        "Esse portal está em constante evolução para melhor servir o time comercial."
    )

elif selected == "📊 Dashboards":
    st.markdown("### 📊 Dashboards Comerciais")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("- [Gestão Comercial – Market Share](https://app.powerbi.com/links/VrFjeMY32s)")
        st.markdown("- [Telemetria](https://app.powerbi.com/links/DN8VawnQyN)")
        st.markdown("- [Raio X](https://app.powerbi.com/links/r_cCxY0hQF)")
        st.markdown("- [Resultados vs Meta](https://app.powerbi.com/links/5tOpR8JJh4)")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "📄 Formulários":
    st.markdown("### 📄 Formulários Úteis")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("- [Pedidos de Migração de Carteira](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4d0eK42lIfQ7vVodaBv4SADNOrM5qGKC6CrhUODZPTUtHWU4xTTFDWTcwQkRIRlk0QVVNNS4u)")
        st.markdown("- [Pedidos de Extração de CAM57](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4d0eK42lIfQ7vVhiVOkKoYqdBqDjlbS0O0SNUQTZMVUVEVk42U1JaRjlLNEFXWVFNWEZGNS4u)")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "📚 Materiais":
    st.markdown("### 📚 Materiais e Documentos")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("*(Esta seção pode conter links para treinamentos, manuais, apresentações internas etc. Me envie o que quiser que eu coloco aqui!)*")
        st.markdown('</div>', unsafe_allow_html=True)

# RODAPÉ ATUALIZADO
st.markdown("---")
st.caption("Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank")
