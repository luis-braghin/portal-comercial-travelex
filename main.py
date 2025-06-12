import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Portal Comercial Travelex",
    page_icon="🏦",
    layout="wide",
)

# === SIDEBAR ===
with st.sidebar:
    # Tenta exibir o logo (precisa estar na mesma pasta no GitHub)
    try:
        st.image("logo_travelex.png", width=180)
    except:
        st.warning("⚠️ Logo não encontrado (logo_travelex.png)")

    st.markdown("## 🖥️ Seções")
    menu = st.radio("",
        ["🏠 Início", "📊 Dashboards", "📄 Formulários", "📁 Materiais"],
        label_visibility="collapsed"
    )

# === CONTEÚDO PRINCIPAL ===
st.markdown("<br>", unsafe_allow_html=True)

if menu == "🏠 Início":
    st.title("Portal Comercial Travelex")
    st.caption("Tudo o que você precisa, centralizado e fácil de acessar.")
    st.markdown("### 👋 Bem-vindo(a) ao Portal Comercial Travelex")
    st.write(
        "Use o menu lateral para navegar entre dashboards, formulários e materiais. "
        "Esse portal está em constante evolução para melhor servir o time comercial."
    )

elif menu == "📊 Dashboards":
    st.subheader("📊 Dashboards Comerciais")
    st.markdown("- [**Gestão Comercial – Market Share**](https://app.powerbi.com/links/VrFjeMY32s)")
    st.markdown("- [**Telemetria**](https://app.powerbi.com/links/DN8VawnQyN)")
    st.markdown("- [**Raio X**](https://app.powerbi.com/links/r_cCxY0hQF)")
    st.markdown("- [**Resultados vs Meta**](https://app.powerbi.com/links/5tOpR8JJh4)")

elif menu == "📄 Formulários":
    st.subheader("📄 Formulários Úteis")
    st.markdown("- [**Pedidos de Migração de Carteira**](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...)")
    st.markdown("- [**Pedidos de Extração de CAM57**](https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...)")

elif menu == "📁 Materiais":
    st.subheader("📁 Materiais e Documentos")
    st.info("_Esta seção pode conter links para treinamentos, manuais, apresentações internas etc. Me envie o que quiser que eu coloco aqui!_")

# === RODAPÉ ===
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: gray;'>"
    "Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank"
    "</p>",
    unsafe_allow_html=True
)
