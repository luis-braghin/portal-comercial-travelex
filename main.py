# Integra todas as melhorias pedidas, com organização modular e foco em layout profissional

import streamlit as st
from streamlit_option_menu import option_menu
import os

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Portal Comercial Travelex",
    layout="wide",
    page_icon="logo_travelex.png"
)

# CONTADOR DE ACESSO
contador_path = os.path.join(".streamlit", "contador.txt")
if not os.path.exists(contador_path):
    with open(contador_path, "w") as f:
        f.write("0")

with open(contador_path, "r+") as f:
    total_acessos = int(f.read()) + 1
    f.seek(0)
    f.write(str(total_acessos))

# DADOS
SECOES = {
    "📊 Dashboards Comerciais": [
        ("📌 Gestão Comercial – Market Share", "https://app.powerbi.com/links/VrFjeMY32s"),
        ("📡 Telemetria", "https://app.powerbi.com/links/DN8VawnQyN"),
        ("🩺 Raio X", "https://app.powerbi.com/links/r_cCxY0hQF"),
        ("📊 Resultados vs Meta", "https://app.powerbi.com/links/5tOpR8JJh4")
    ],
    "📝 Formulários ": [
        ("📄 Migração de Carteira", "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4..."),
        ("📄 Extração de CAM57", "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...")
    ],
    "📚 Materiais": [
        ("📁 Treinamentos e Manuais", "#")
    ],
    "🏦 Área de Crédito": [
        ("📝 Proposta de Crédito", "https://forms.office.com/pages/responsepage.aspx?id=credito..."),
        ("🌱 Formulário ESG", "https://forms.office.com/pages/responsepage.aspx?id=esg..."),
        ("📊 New Dashboard - Crédito", "https://app.powerbi.com/links/newdashboardcredito")
    ]
}

EVENTOS = [
    ("📅 Reunião Comercial", "18/06/2025", "Apresentação de resultados semestrais."),
    ("🧠 Workshop CRM", "25/06/2025", "Capacitação para uso da nova plataforma."),
    ("🚀 Lçto Campanha", "01/07/2025", "Nova campanha de captação será iniciada.")
]

# CSS CUSTOMIZADO (será inserido depois como st.markdown)
CUSTOM_CSS = """
<style>
    body, .main {
        background-color: #F5F7FA;
        font-size: 16px;
    }
    .block-container {
        padding: 2rem 3rem;
    }
    h1, h2, h3 {
        color: #00205B;
    }
    section[data-testid="stSidebar"] {
        background-color: #00205B !important;
        color: white;
    }
    .header {
        background: white;
        padding: 1rem 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .search-bar {
        display: flex;
        gap: 10px;
        margin-bottom: 2rem;
        align-items: center;
    }
    .search-bar input {
        flex: 1;
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 8px;
    }
    .card {
        background-color: white;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        transition: 0.3s;
        margin-bottom: 1rem;
    }
    .card:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }
    .metric {
        background-color: #00205B;
        color: white;
        border-radius: 10px;
        padding: 1rem 2rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1rem;
        font-size: 18px;
        margin-bottom: 2rem;
    }
    .event {
        border-left: 5px solid #0072CE;
        padding-left: 1rem;
        margin-bottom: 1rem;
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    selected = option_menu(
        "Seções",
        ["🏠 Início"] + list(SECOES.keys()),
        icons=["house"] + ["bar-chart", "file-earmark-text", "folder", "bank"],
        menu_icon="cast",
        default_index=0
    )

# CABEÇALHO
st.markdown('<div class="header">', unsafe_allow_html=True)
st.image("logo_travelex.png", width=100)
st.markdown("""
    <div>
        <h2>Central de Planejamento Comercial</h2>
        <p style='color: gray;'>Travelex Bank · Tudo o que você precisa em um só lugar.</p>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# CONTEÚDO PRINCIPAL
if selected == "🏠 Início":
    # BARRA DE BUSCA
    st.markdown("### 🔎 Pesquisar")
    col_search = st.columns([7, 1])
    search = col_search[0].text_input("", placeholder="Buscar dashboards, formulários ou materiais").lower()
    col_search[1].button("🔍 Buscar")

    # META DO MÊS
    st.markdown("### 📈 Meta do Mês")
    st.markdown("""
        <div class="metric">
            <span>🎯</span> <strong>75%</strong>
            <span style='font-size:14px;'>Meta atingida</span>
        </div>
    """, unsafe_allow_html=True)

    # EVENTOS
    st.markdown("### 📅 Próximos Eventos")
    for titulo, data, desc in EVENTOS:
        st.markdown(f"<div class='event'><strong>{titulo}</strong> - <em>{data}</em><br>{desc}</div>", unsafe_allow_html=True)

    # SEÇÕES DINÂMICAS
    for titulo, links in SECOES.items():
        st.markdown(f"### {titulo}")
        cols = st.columns(2)
        for i, (nome, link) in enumerate(links):
            if search in nome.lower():
                with cols[i % 2]:
                    st.markdown(f"<a href='{link}' target='_blank'><div class='card'>{nome}</div></a>", unsafe_allow_html=True)

else:
    # OUTRAS SEÇÕES
    st.markdown(f"### {selected}")
    links = SECOES.get(selected, [])
    cols = st.columns(2)
    for i, (nome, link) in enumerate(links):
        with cols[i % 2]:
            st.markdown(f"<a href='{link}' target='_blank'><div class='card'>{nome}</div></a>", unsafe_allow_html=True)

# RODAPÉ
st.markdown("---")
st.caption("Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank")
st.markdown(f"<sub>🔒 Acesso: somente uso interno | 🧾 Dados de uso sendo monitorados | 📊 Total de acessos: <b>{total_acessos}</b></sub>", unsafe_allow_html=True)
