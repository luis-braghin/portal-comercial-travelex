
import streamlit as st

st.set_page_config(
    page_title="Central de Planejamento - Travelex",
    layout="wide",
    page_icon="📊"
)

# Custom CSS para identidade visual da Travelex
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        h1, h2, h3 {
            color: #00205B;
        }
        a {
            text-decoration: none;
            color: #0072CE;
            font-weight: 500;
        }
        a:hover {
            color: #005bb5;
        }
        .st-expander > summary {
            font-size: 1.1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Logo e título
col1, col2 = st.columns([1, 9])
with col1:
    st.image("logo.png", width=80)
with col2:
    st.markdown("## Central de Planejamento Comercial")
    st.markdown("#### Travelex Bank · Tudo o que você precisa em um só lugar.")

st.markdown("---")

# Layout em duas colunas principais
col_dash, col_form = st.columns(2)

with col_dash:
    with st.expander("📊 Dashboards Comerciais", expanded=True):
        st.markdown("- [Gestão Comercial – Market Share](https://app.powerbi.com/links/VrFjeMY32s?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&pbi_source=linkShare&bookmarkGuid=bc82c15b-c9b4-4549-b54b-30bd002fa59b)")
        st.markdown("- [Telemetria](https://app.powerbi.com/links/DN8VawnQyN?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&pbi_source=linkShare&bookmarkGuid=f27b74bf-26e7-4a81-8aa9-2c27c7e7c9ad)")
        st.markdown("- [Raio X](https://app.powerbi.com/links/r_cCxY0hQF?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&pbi_source=linkShare&bookmarkGuid=72639833-4ddb-4fed-8449-067afe9d0927)")
        st.markdown("- [Resultados vs Meta](https://app.powerbi.com/links/5tOpR8JJh4?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&pbi_source=linkShare)")

with col_form:
    with st.expander("📄 Formulários Úteis", expanded=True):
        st.markdown("- [Pedidos de Migração de Carteira](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4d0eK42lIfQ7vVodaBv4SADNOrM5qGKC6CrhUODZPTUtHWU4xTTFDWTcwQkRIRlk0QVVNNS4u&origin=lprLink&route=shorturl)")
        st.markdown("- [Pedidos de Extração de CAM57](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4d0eK42lIfQ7vVhiVOkKoYqdBqDjlbS0O0SNUQTZMVUVEVk42U1JaRjlLNEFXWVFNWEZGNS4u&origin=lprLink&route=shorturl)")

st.markdown("---")
st.caption("Desenvolvido pela área de Planejamento Comercial – Travelex Bank")
