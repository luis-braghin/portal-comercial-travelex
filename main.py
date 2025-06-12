import streamlit as st

# Configurações da página
st.set_page_config(page_title="Portal Comercial Travelex", layout="wide")

# Contador de acessos
if "access_count" not in st.session_state:
    if "count" not in st.session_state:
        st.session_state.count = 0
    st.session_state.count += 1
    with open("access_count.txt", "a") as f:
        f.write("1\n")

with open("access_count.txt", "r") as f:
    total_accesses = len(f.readlines())

# Cores da Travelex
PRIMARY_COLOR = "#051f49"
SECONDARY_COLOR = "#ffffff"
HIGHLIGHT_COLOR = "#e30613"

# Logo e título
st.markdown(
    f"""
    <div style='display: flex; align-items: center; gap: 10px; margin-bottom: 10px;'>
        <img src='https://i.ibb.co/jhfSPML/logo-travelex.png' width='80'/>
        <h1 style='color:{PRIMARY_COLOR}; margin: 0;'>Portal Comercial Travelex</h1>
    </div>
    <p style='color: gray; font-size: 18px;'>Tudo o que você precisa, centralizado e fácil de acessar.</p>
    """,
    unsafe_allow_html=True
)

# Alerta de atualização
st.markdown(
    f"""
    <div style='background-color: #dceafd; padding: 10px 15px; border-radius: 8px; margin-top: 10px;'>
        <b>🔔 Atualização:</b> Adicionamos o novo relatório de Telemetria!
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Cards das seções
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Dashboards Comerciais")
    st.markdown(
        """
        - [Gestão Comercial – Market Share](https://app.powerbi.com/view?r=XXXX)
        - [Telemetria](https://app.powerbi.com/view?r=YYYY)
        - [Raio X](https://app.powerbi.com/view?r=ZZZZ)
        - [Resultados vs Meta](https://app.powerbi.com/view?r=AAAA)
        """
    )

with col2:
    st.markdown("### 📝 Formulários Úteis")
    st.markdown(
        """
        - [Pedidos de Migração de Carteira](https://forms.office.com/r/abc)
        - [Pedidos de Extração de CAM57](https://forms.office.com/r/xyz)
        """
    )

# Espaço
st.markdown("")

with st.container():
    st.markdown("### 📂 Materiais")
    st.markdown(
        """
        - [Apresentação Institucional](https://drive.google.com/drive/abc)
        - [Treinamentos Comerciais](https://drive.google.com/drive/xyz)
        """
    )

st.markdown("---")

# Rodapé
st.markdown(
    f"""
    <div style="text-align: center; font-size: 14px; color: gray;">
        Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank <br>
        🔒 Acesso: somente uso interno |
        📋 Dados de uso sendo monitorados |
        📊 Total de acessos: <b>{total_accesses}</b>
    </div>
    """,
    unsafe_allow_html=True
)
