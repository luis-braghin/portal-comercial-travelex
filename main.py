import streamlit as st
from streamlit_option_menu import option_menu
import base64

# CONFIG
st.set_page_config(
    page_title="Portal de Planejamento Comercial",
    layout="wide",
    page_icon="logo_travelex.png"
)

# IMAGEM
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64("logo_travelex.png")

# CSS MODERNO
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    .custom-card {
        border: none;
        padding: 18px 22px;
        border-radius: 12px;
        margin: 12px 0;
        background: linear-gradient(135deg, #ffffff, #f3f7fd);
        box-shadow: 0 3px 10px rgba(0,0,0,0.06);
        transition: transform 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
        cursor: pointer;
    }

    .custom-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    }

    .metric-box {
        background: linear-gradient(90deg, #E8EEF7, #f4f7fc);
        color: #00205B;
        text-align: center;
        padding: 20px;
        font-size: 20px;
        font-weight: 600;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        margin-bottom: 30px;
    }

    .section-highlight {
        background: linear-gradient(to right, #f6f9ff, #e4ecf9);
        border-radius: 12px;
        padding: 20px 30px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        margin-bottom: 30px;
    }

    .header {
        background: linear-gradient(to right, #ffffff, #f3f3f3);
        padding: 30px 20px;
        border-radius: 12px;
        margin-bottom: 30px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    .main-container {
        max-width: 1400px;
        margin: auto;
    }

    .nav-link {
        transition: 0.3s;
    }

    .nav-link:hover {
        color: #00205B !important;
        font-weight: 600;
    }
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

# CONTEÚDO
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
materiais = [("📁 Treinamentos e Manuais", "https://example.com/materials")]
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

def mostrar_bloco(titulo, lista, margin_top=30):
    st.markdown(f"""<div style="margin-top: {margin_top}px;"><h3 style="color:#00205B;">{titulo}</h3></div>""", unsafe_allow_html=True)
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
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

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
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 📉 Meta do Mês", unsafe_allow_html=True)
    st.markdown("""
        <div class="metric-box">
            🎯 <strong>X%</strong><br>
            <span style="font-size: 14px;">Meta atingida até agora</span>
        </div>
    """, unsafe_allow_html=True)

    # EVENTOS
    st.markdown("<div class='section-highlight'><h4 style='margin-top:0;'>🗓️ Próximos Eventos</h4>", unsafe_allow_html=True)
    for evento in eventos:
        st.markdown(f"- {evento}")
    st.markdown("</div>", unsafe_allow_html=True)

    mostrar_bloco("📊 Dashboards Comerciais", dashboards, margin_top=10)
    mostrar_bloco("📄 Formulários", formularios)
    mostrar_bloco("📚 Materiais", materiais)
    mostrar_bloco("🏢 Área de Crédito", credito)

    st.markdown("</div>", unsafe_allow_html=True)  # Fecha main-container

# OUTRAS SEÇÕES
def render_secao(titulo, dados):
    st.markdown(f"<div class='main-container'><h3>{titulo}</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, (nome, link) in enumerate(dados):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
                <a href="{link}" target="_blank" style="text-decoration: none;">
                    <div class="custom-card">{nome}</div>
                </a>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

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
