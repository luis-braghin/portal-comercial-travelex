import streamlit as st
from streamlit_option_menu import option_menu

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portal Comercial Travelex", layout="wide", page_icon="📊")

# VISITAS NA SESSÃO
if "visits" not in st.session_state:
    st.session_state["visits"] = 1
else:
    st.session_state["visits"] += 1

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
        .alert-info {
            background-color: #e0ecf9;
            color: #00205B;
            padding: 12px 20px;
            border-left: 5px solid #0072CE;
            border-radius: 8px;
            margin-bottom: 20px;
            font-size: 0.95rem;
        }
        .search-box input {
            padding: 0.5rem;
            font-size: 0.9rem;
            width: 100%;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        .card {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            margin-bottom: 1.5rem;
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

# ALERTA NO TOPO
st.markdown('<div class="alert-info">🔔 Atualização: Adicionamos o novo relatório de Telemetria!</div>', unsafe_allow_html=True)

# MENU LATERAL
with st.sidebar:
    selected = option_menu(
        "Seções",
        ["🏠 Início", "📊 Dashboards", "📄 Formulários", "📚 Materiais"],
        icons=["house", "bar-chart", "file-earmark-text", "folder"],
        menu_icon="cast",
        default_index=0
    )

# Função de busca
def search_links(termo, links_dict):
    results = []
    for nome, url in links_dict.items():
        if termo.lower() in nome.lower():
            results.append(f"- [{nome}]({url})")
    return results

# CONTEÚDO DAS SEÇÕES
if selected == "🏠 Início":
    st.markdown("### 👋 Bem-vindo(a) ao Portal Comercial Travelex")
    st.markdown(
        "Use o menu lateral para navegar entre dashboards, formulários e materiais. "
        "Esse portal está em constante evolução para melhor servir o time comercial."
    )
    st.markdown(f"**Número de visitas nesta sessão:** {st.session_state['visits']}")

elif selected == "📊 Dashboards":
    st.markdown("### 📊 Dashboards Comerciais")
    dashboards = {
        "Gestão Comercial – Market Share": "https://app.powerbi.com/links/VrFjeMY32s",
        "Telemetria": "https://app.powerbi.com/links/DN8VawnQyN",
        "Raio X": "https://app.powerbi.com/links/r_cCxY0hQF",
        "Resultados vs Meta": "https://app.powerbi.com/links/5tOpR8JJh4"
    }

    search = st.text_input("🔍 Buscar dashboards:", key="busca_dash")
    results = search_links(search, dashboards) if search else dashboards.values()

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        for linha in (results if isinstance(results, list) else dashboards):
            if isinstance(linha, str):
                st.markdown(linha)
            else:
                st.markdown(f"- [{linha}]({dashboards[linha]})")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "📄 Formulários":
    st.markdown("### 📄 Formulários Úteis")
    formularios = {
        "Pedidos de Migração de Carteira": "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4d0eK42lIfQ7vVodaBv4SADNOrM5qGKC6CrhUODZPTUtHWU4xTTFDWTcwQkRIRlk0QVVNNS4u",
        "Pedidos de Extração de CAM57": "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4d0eK42lIfQ7vVhiVOkKoYqdBqDjlbS0O0SNUQTZMVUVEVk42U1JaRjlLNEFXWVFNWEZGNS4u"
    }

    search = st.text_input("🔍 Buscar formulários:", key="busca_forms")
    results = search_links(search, formularios) if search else formularios.values()

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        for linha in (results if isinstance(results, list) else formularios):
            if isinstance(linha, str):
                st.markdown(linha)
            else:
                st.markdown(f"- [{linha}]({formularios[linha]})")
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
