
import streamlit as st
from PIL import Image

# ---- Configuração da página ----
st.set_page_config(page_title="Portal Comercial Travelex", page_icon="📊", layout="wide")

# ---- Logo da Travelex ----
col1, col2 = st.columns([0.1, 0.9])
with col1:
    logo = Image.open("logo_travelex.png")
    st.image(logo, width=80)
with col2:
    st.title("Portal Comercial Travelex")
    st.caption("Tudo o que você precisa, centralizado e fácil de acessar.")

# ---- Aviso ----
st.info("🔔 Atualização: Adicionamos o novo relatório de Telemetria!", icon="🔔")

# ---- Painel de Acesso Rápido ----
st.markdown("## 👋 Bem-vindo(a) ao Portal Comercial Travelex")
st.write("Use os cartões abaixo para navegar entre dashboards, formulários e materiais.")

# ---- Layout em Cartões ----
col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.subheader("📊 Dashboards Comerciais")
        st.markdown("- [Gestão Comercial – Market Share](https://example.com)")
        st.markdown("- [Telemetria](https://example.com)")
        st.markdown("- [Raio X](https://example.com)")
        st.markdown("- [Resultados vs Meta](https://example.com)")

with col2:
    with st.container():
        st.subheader("📄 Formulários Úteis")
        st.markdown("- [Pedidos de Migração de Carteira](https://example.com)")
        st.markdown("- [Pedidos de Extração de CAM57](https://example.com)")

st.markdown("---")

# ---- Rodapé com contador de acessos ----
if "contador" not in st.session_state:
    st.session_state.contador = 0
st.session_state.contador += 1

st.markdown(
    f"""
    <div style='font-size: 12px; color: gray; text-align: left'>
        Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank <br>
        🔒 Acesso: somente uso interno |
        📑 Dados de uso sendo monitorados |
        📊 Total de acessos: <b>{st.session_state.contador}</b>
    </div>
    """,
    unsafe_allow_html=True
)
