import streamlit as st
from streamlit_option_menu import option_menu

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portal Comercial Travelex", layout="wide", page_icon="📊")

# ESTILO FORÇADO TRAVELEX
st.markdown("""
    <style>
        body, .main, .block-container {
            background-color: #F5F7FA;
        }

        h1, h2, h3, h4 {
            color: #00205B !important;
        }

        .st-emotion-cache-6qob1r, .css-10trblm { /* títulos */
            color: #00205B !important;
        }

        .st-emotion-cache-1avcm0n.ezrtsby0 {
            background-color: #E4002B !important;
        }

        .st-emotion-cache-1v0mbdj, .st-emotion-cache-16txtl3 {
            color: #00205B !important;
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

        .center-logo img {
            max-height: 60px;
            width: auto;
            object-fit: contain;
        }

        .footer {
            font-size: 0.85rem;
            color: gray;
            text-align: left;
            padding-top: 1.5rem;
        }

        a {
            color: #00205B;
            text-decoration: none;
        }

        a:hover {
            color: #E4002B;
        }

        .search-box {
            margin-top: 15px;
            margin-bottom: 25px;
        }
    </style>
""", unsafe_allow_html=True)

# LOGO E TÍTULO
st.markdown('<div class="center-logo">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 9])
with col1:
    st.image("logo_travelex.png")
with col2:
    st.markdown("## Portal Comercial Travelex")
    st.caption("Tudo o que você precisa, centralizado e fácil de acessar.")
st.markdown('</div>', unsafe_allow_html=True)

# ALERTA DE ATUALIZAÇÃO
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

# BARRA DE BUSCA (aperfeiçoada)
search_term = st.text_input("🔎 Buscar algo no portal:", "").lower()

# RESULTADOS DE BUSCA FLEXÍVEL
def buscar_resultados(term):
    banco = {
        "Gestão Comercial – Market Share": "https://app.powerbi.com/links/VrFjeMY32s",
        "Telemetria": "https://app.powerbi.com/links/DN8VawnQyN",
        "Raio X": "https://app.powerbi.com/links/r_cCxY0hQF",
        "Resultados vs Meta": "https://app.powerbi.com/links/5tOpR8JJh4",
        "Pedidos de Migração de Carteira": "https://forms.office.com/pages/responsepage.aspx?id=...",
        "Pedidos de Extração de CAM57": "https://forms.office.com/pages/responsepage.aspx?id=..."
    }
    resultados = [f"- [{k}]({v})" for k, v in banco.items() if term in k.lower()]
    return resultados

if search_term:
    st.markdown("### 🔍 Resultados da Busca:")
    resultados = buscar_resultados(search_term)
    if resultados:
        for item in resultados:
            st.markdown(item)
    else:
        st.warning("Nenhum resultado encontrado.")

# CONTEÚDO PRINCIPAL (apenas se não estiver buscando)
if not search_term:
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
            st.markdown("- [Pedidos de Migração de Carteira](https://forms.office.com/pages/responsepage.aspx?id=...)")
            st.markdown("- [Pedidos de Extração de CAM57](https://forms.office.com/pages/responsepage.aspx?id=...)")
            st.markdown('</div>', unsafe_allow_html=True)

    elif selected == "📚 Materiais":
        st.markdown("### 📚 Materiais e Documentos")
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("*(Esta seção pode conter links para treinamentos, manuais, apresentações internas etc. Me envie o que quiser que eu coloco aqui!)*")
            st.markdown('</div>', unsafe_allow_html=True)

# RODAPÉ
st.markdown("---")
st.markdown(
    '<div class="footer">Desenvolvido pela área de Planejamento Comercial '
    '(Gestão Felipe Von Pressentin) – Travelex Bank<br>'
    '🔒 Acesso: somente uso interno | 📊 Dados de uso sendo monitorados | 📈 Total de acessos: <strong>1234</strong></div>',
    unsafe_allow_html=True
)
