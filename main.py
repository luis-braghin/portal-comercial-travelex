import streamlit as st
from streamlit_option_menu import option_menu
import re

# Contador de acessos (simples)
if "access_count" not in st.session_state:
    st.session_state.access_count = 0
st.session_state.access_count += 1

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portal Comercial Travelex", layout="wide", page_icon="📊")

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
    st.image("logo_travelex.png", width=90)
with col2:
    st.markdown("## Portal Comercial Travelex")
    st.caption("Tudo o que você precisa, centralizado e fácil de acessar.")
st.markdown('</div>', unsafe_allow_html=True)

# MENU LATERAL
with st.sidebar:
    selected = option_menu(
        "Seções",
        ["🏠 Início", "📊 Dashboards", "📄 Formulários", "📚 Materiais"],
        icons=["house", "bar-chart", "file-earmark-text", "folder"],
        menu_icon="cast",
        default_index=0
    )

# AVISO TOPO
st.info("🔔 Atualização: Adicionamos o novo relatório de Telemetria!")

# DADOS
dashboards = {
    "Gestão Comercial – Market Share": "https://app.powerbi.com/links/VrFjeMY32s",
    "Telemetria": "https://app.powerbi.com/links/DN8VawnQyN",
    "Raio X": "https://app.powerbi.com/links/r_cCxY0hQF",
    "Resultados vs Meta": "https://app.powerbi.com/links/5tOpR8JJh4"
}
formularios = {
    "Pedidos de Migração de Carteira": "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4d0eK42lIfQ7vVodaBv4SADNOrM5qGKC6CrhUODZPTUtHWU4xTTFDWTcwQkRIRlk0QVVNNS4u",
    "Pedidos de Extração de CAM57": "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4d0eK42lIfQ7vVhiVOkKoYqdBqDjlbS0O0SNUQTZMVUVEVk42U1JaRjlLNEFXWVFNWEZGNS4u"
}

materiais = {
    # Adicione aqui quando quiser
}

# FILTRAGEM (apenas na aba Início)
def buscar_itens(query, itens):
    return {k: v for k, v in itens.items() if re.search(query, k, re.IGNORECASE)}

# SEÇÕES
if selected == "🏠 Início":
    st.markdown("### 👋 Bem-vindo(a) ao Portal Comercial Travelex")
    st.markdown("Use o menu lateral para navegar entre dashboards, formulários e materiais. Esse portal está em constante evolução para melhor servir o time comercial.")

    search_term = st.text_input("🔎 Buscar algo no portal:")
    if search_term:
        st.subheader("🔗 Resultados da Busca")
        resultados = {
            "Dashboards": buscar_itens(search_term, dashboards),
            "Formulários": buscar_itens(search_term, formularios),
            "Materiais": buscar_itens(search_term, materiais)
        }
        for secao, links in resultados.items():
            if links:
                st.markdown(f"#### {secao}")
                for nome, url in links.items():
                    st.markdown(f"- [{nome}]({url})")

elif selected == "📊 Dashboards":
    st.markdown("### 📊 Dashboards Comerciais")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        for nome, url in dashboards.items():
            st.markdown(f"- [{nome}]({url})")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "📄 Formulários":
    st.markdown("### 📄 Formulários Úteis")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        for nome, url in formularios.items():
            st.markdown(f"- [{nome}]({url})")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "📚 Materiais":
    st.markdown("### 📚 Materiais e Documentos")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("*(Esta seção pode conter links para treinamentos, manuais, apresentações internas etc. Me envie o que quiser que eu coloco aqui!)*")
        st.markdown('</div>', unsafe_allow_html=True)

# RODAPÉ
st.markdown("---")
st.caption("""
Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank  
🔒 Acesso: somente uso interno | 📊 Dados de uso sendo monitorados | 📈 Total de acessos: **{:,}**
""".format(st.session_state.access_count))
