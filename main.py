import streamlit as st
from streamlit_option_menu import option_menu
import base64

# CONFIG
st.set_page_config(
    page_title="Portal de Planejamento Comercial",
    layout="wide",
    page_icon="logo_travelex.png"
)

# ENCODE DE IMAGEM

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64("logo_travelex.png")

# CSS MODERNO VISUAL
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    .main-container {
        max-width: 1400px;
        margin: auto;
    }

    .custom-card {
        border-left: 6px solid #00205B;
        background: #ffffff;
        padding: 18px 22px;
        border-radius: 12px;
        margin: 12px 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.06);
        transition: transform 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    }

    .custom-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    }

    .highlight-box {
        background: linear-gradient(90deg, #e8f0fe, #f1f5fc);
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.05);
        margin-bottom: 35px;
    }

    .section-title {
        font-size: 26px;
        font-weight: 700;
        color: #00205B;
        margin-top: 40px;
        margin-bottom: 10px;
    }

    .info-text {
        font-size: 16px;
        color: #4a4a4a;
    }

    .metric-box {
        background: linear-gradient(to right, #f6f9ff, #e8eefc);
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        color: #00205B;
        font-size: 24px;
        font-weight: 700;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
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
conteudos = {
    "📊 Dashboards Comerciais": [
        ("📌 Gestião Comercial – Market Share", "https://app.powerbi.com/links/VrFjeMY32s"),
        ("📡 Telemetria 🆕", "https://app.powerbi.com/links/DN8VawnQyN"),
        ("🔍 Raio X", "https://app.powerbi.com/links/r_cCxY0hQF"),
        ("📈 Resultados vs Meta", "https://app.powerbi.com/links/5tOpR8JJh4"),
    ],
    "📄 Formulários": [
        ("📄 Migração de Carteira", "https://forms.office.com/pages/responsepage.aspx?id=1"),
        ("📄 Extração de CAM57", "https://forms.office.com/pages/responsepage.aspx?id=2")
    ],
    "📚 Materiais": [
        ("📁 Treinamentos e Manuais", "https://example.com/materials")
    ],
    "🏢 Área de Crédito": [
        ("🧾 Proposta de Crédito", "https://forms.office.com/pages/responsepage.aspx?id=creditform"),
        ("🌱 Formulário ESG", "https://forms.office.com/pages/responsepage.aspx?id=esgform"),
        ("📊 Dashboard Crédito", "https://app.powerbi.com/links/newcreditdash")
    ]
}
eventos = [
    "🔔 Reunião Trimestral - 20 de Junho",
    "🧠 Workshop Estratégico - 27 de Junho",
    "📊 Atualização Power BI - 01 de Julho"
]

# FUNÇÃO PARA CARDS

def mostrar_bloco(titulo, lista):
    st.markdown(f"<div class='section-title'>{titulo}</div>", unsafe_allow_html=True)
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
    <div class='highlight-box'>
        <div style="display: flex; align-items: center;">
            <img src='data:image/png;base64,{logo_base64}' width='60' style='margin-right: 20px;'>
            <div>
                <h1 style='margin: 0; color: #00205B;'>Portal de Planejamento Comercial</h1>
                <p class='info-text'>Travelex Bank · Tudo o que você precisa em um só lugar.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.info("🔔 Atualização: Adicionamos o novo relatório de Telemetria!")

    st.markdown("<div class='section-title'>📉 Meta do Mês</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class="metric-box">
            🎯 <strong>X%</strong><br>
            <span style="font-size: 14px; font-weight: normal">Meta atingida até agora</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>🗓️ Próximos Eventos</div>", unsafe_allow_html=True)
    with st.container():
        for evento in eventos:
            st.markdown(f"- {evento}")

    for secao, blocos in conteudos.items():
        mostrar_bloco(secao, blocos)

    st.markdown("</div>", unsafe_allow_html=True)

# SEÇÕES
else:
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    secao_nome = next((k for k in conteudos.keys() if selected in k or k.endswith(selected)), None)
    if secao_nome:
        mostrar_bloco(secao_nome, conteudos[secao_nome])
    else:
        st.warning("Nenhum conteúdo encontrado para esta seção.")
    st.markdown("</div>", unsafe_allow_html=True)

# RODAPÉ
st.markdown("""<br><hr><div style='text-align:center; font-size:13px; color:#6c757d;'>
    Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank<br>
    🔒 Acesso: somente uso interno | 📊 Dados de uso sendo monitorados
</div>""", unsafe_allow_html=True)
