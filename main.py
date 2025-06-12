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

        .css-6qob1r.e1fqkh3o2 {  /* título principal */
            color: #00205B;
        }

        h1, h2, h3, h4 {
            color: #00205B;
        }

        .st-emotion-cache-1avcm0n.ezrtsby0 { /* barra lateral ativa */
            background-color: #E4002B !important;
        }

        .css-1d391kg { /* botões do menu */
            color: #00205B;
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
    st.image("logo_travelex.png", width=100)
with col2:
    st.markdown("## Portal Comercial Travelex")
    st.caption("Tudo o que você precisa, centralizado e fácil de acessar.")
st.markdown('</div>', unsafe_allow_html=True)

# BARRA DE ALERTA
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

# BARRA DE BUSCA GLOBAL
search_term = st.text_input("🔎 Buscar algo no portal:", "", key="busca").lower()

# FUNÇÃO DE BUSCA SIMPLES
def exibir_resultado_busca():
    results = []
    if "migração" in search_term:
        results.append("- [Pedidos de Migração de Carteira](https://forms.office.com/pages/responsepage.aspx?id=...)")
    if "cam57" in search_term:
        results.append("- [Pedidos de Extração de CAM57](https://forms.office.com/pages/responsepage.aspx?id=...)")
    if "market" in search_term or "gestão" in search_term:
        results.append("- [Gestão Comercial – Market Share](https://app.powerbi.com/links/VrFjeMY32s)")
    if "telemetria" in search_term:
        results.append("- [Telemetria](https://app.powerbi.com/links/DN8VawnQyN)")
    if "raio" in search_term:
        results.append("- [Raio X](https://app.powerbi.com/links/r_cCxY0hQF)")
    if "meta" in search_term:
        results.append("- [Resultados vs Meta](https://app.powerbi.com/links/5tOpR8JJh4)")
    
    if results:
        st.markdown("### Resultados da busca:")
        for item in results:
            st.markdown(item)
    elif search_term:
        st.warning("Nenhum resultado encontrado.")

if search_term:
    exibir_resultado_busca()

# CONTEÚDO DAS SEÇÕES
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

# RODAPÉ COM INDICADOR DE USO
st.markdown("---")
st.markdown(
    '<div class="footer">Desenvolvido pela área de Planejamento Comercial '
    '(Gestão Felipe Von Pressentin) – Travelex Bank<br>'
    '🔒 Acesso: somente uso interno | 📊 Dados de uso sendo monitorados | 👁 Total de acessos: <strong>1234</strong></div>',
    unsafe_allow_html=True
)
