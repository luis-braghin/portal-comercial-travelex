import streamlit as st
from streamlit_option_menu import option_menu
import os
import base64

# CONFIGURAÇÕES
st.set_page_config(
    page_title="Portal de Planejamento Comercial",
    layout="wide",
    page_icon="logo_travelex.png"
)

# FUNÇÃO PARA ENCODE DE IMAGEM
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64("logo_travelex.png")

# CSS PERSONALIZADO
st.markdown(f"""
<style>
    .custom-card {{
        border: 1px solid #00205B;
        padding: 12px 20px;
        border-radius: 10px;
        margin: 10px 0;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        cursor: pointer;
    }}
    .custom-card:hover {{
        transform: scale(1.02);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    .metric-box {{
        background-color: #E8EEF7;
        color: #00205B;
        text-align: center;
        padding: 14px;
        font-size: 18px;
        border-radius: 10px;
    }}
    .header {{
        background-color: white;
        padding: 30px 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.image(f"data:image/png;base64,{logo_base64}", width=180)
    selected = option_menu(
        "Seções",
        ["🏠 Início", "📊 Dashboards", "📄 Formulários", "📚 Materiais", "🏢 Crédito"],
        icons=["house", "bar-chart", "file-earmark-text", "book", "building"],
        menu_icon="cast",
        default_index=0
    )

# DADOS
dashboards = [
    ("📌 Gestão Comercial – Market Share", "https://app.powerbi.com/links/VrFjeMY32s"),
    ("📡 Telemetria", "https://app.powerbi.com/links/DN8VawnQyN"),
    ("🔍 Raio X", "https://app.powerbi.com/links/r_cCxY0hQF"),
    ("📈 Resultados vs Meta", "https://app.powerbi.com/links/5tOpR8JJh4"),
]
formularios = [
    ("📄 Migração de Carteira", "https://forms.office.com/pages/responsepage.aspx?id=1"),
    ("📄 Extração de CAM57", "https://forms.office.com/pages/responsepage.aspx?id=2")
]
materiais = [
    ("📁 Treinamentos e Manuais", "https://example.com/materials")
]
credito = [
    ("🧾 Proposta de Crédito", "https://forms.office.com/pages/responsepage.aspx?id=creditform"),
    ("🌱 Formulário ESG", "https://forms.office.com/pages/responsepage.aspx?id=esgform"),
    ("📊 Dashboard Crédito", "https://app.powerbi.com/links/newcreditdash")
]
eventos = [
    ("🔔 Reunião Trimestral - 20 de Junho"),
    ("🧠 Workshop Estratégico - 27 de Junho"),
    ("📊 Atualização Power BI - 01 de Julho")
]

# FUNÇÃO PARA EXIBIR SEÇÕES
def mostrar_bloco(titulo, lista, margin_top=30):
    st.markdown(f"""<div style="margin-top: {margin_top}px;"><h3>{titulo}</h3></div>""", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, (nome, link) in enumerate(lista):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
                <a href="{link}" target="_blank" style="text-decoration: none;">
                    <div class="custom-card">{nome}</div>
                </a>
            """, unsafe_allow_html=True)

# INÍCIO
if selected == "🏠 Início":
    st.markdown(f"""
    <div class='header'>
        <div style="display: flex; align-items: center;">
            <img src='data:image/png;base64,{logo_base64}' width='60' style='margin-right: 20px;'>
            <div>
                <h1 style='margin: 0; color: #00205B;'>Portal de Planejamento Comercial</h1>
                <p style='margin: 0; color: #6c757d;'>Travelex Bank · Tudo o que você precisa em um só lugar.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.info("🔔 Atualização: Adicionamos o novo relatório de Telemetria!")

    # Espaço após alerta
    st.markdown("<br>", unsafe_allow_html=True)

    # META
    st.markdown("### 📉 Meta do Mês")
    st.markdown("""
        <div class="metric-box">
            🎯 <strong>X%</strong><br>
            <span style="font-size: 13px;">Meta atingida até agora</span>
        </div>
    """, unsafe_allow_html=True)

    # EVENTOS
    st.markdown("<div style='margin-top:30px;'><h3>🗓️ Próximos Eventos</h3></div>", unsafe_allow_html=True)
    for evento in eventos:
        st.markdown(f"- {evento}")

    # Espaçamento menor antes dos dashboards
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

    mostrar_bloco("📊 Dashboards Comerciais", dashboards)
    mostrar_bloco("📄 Formulários", formularios)
    mostrar_bloco("📚 Materiais", materiais)
    mostrar_bloco("🏢 Área de Crédito", credito)

# OUTRAS SEÇÕES
def render_secao(titulo, dados):
    st.markdown(f"### {titulo}")
    col1, col2 = st.columns(2)
    for i, (nome, link) in enumerate(dados):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
                <a href="{link}" target="_blank" style="text-decoration: none;">
                    <div class="custom-card">{nome}</div>
                </a>
            """, unsafe_allow_html=True)

if selected == "📊 Dashboards":
    render_secao("📊 Dashboards Comerciais", dashboards)
elif selected == "📄 Formulários":
    render_secao("📄 Formulários", formularios)
elif selected == "📚 Materiais":
    render_secao("📚 Materiais", materiais)
elif selected == "🏢 Crédito":
    render_secao("🏢 Área de Crédito", credito)

# RODAPÉ
st.markdown("""<br><hr><div style='text-align:center; font-size:13px; color:#6c757d;'>
    Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank<br>
    🔒 Acesso: somente uso interno | 📊 Dados de uso sendo monitorados
</div>""", unsafe_allow_html=True)
