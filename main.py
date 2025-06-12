import streamlit as st
import base64
from PIL import Image
import time

st.set_page_config(layout="wide", page_title="Portal Comercial Travelex", page_icon="📊")

# Função para estilo customizado com hover animado
def local_css():
    st.markdown("""
        <style>
            .section-title {
                font-size: 26px;
                font-weight: bold;
                margin-top: 40px;
                color: #00205B;
                display: flex;
                align-items: center;
            }
            .section-title img {
                margin-right: 10px;
            }
            .resource-box {
                padding: 15px 20px;
                margin-bottom: 12px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                transition: all 0.3s ease;
                border-left: 5px solid #00205B;
                display: block;
                text-decoration: none;
            }
            .resource-box:hover {
                transform: scale(1.015);
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }
            .search-box input {
                padding: 10px;
                border-radius: 10px;
                border: 1px solid #ccc;
                width: 100%;
            }
            .header-container {
                background-color: white;
                padding: 20px 40px;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                margin-bottom: 30px;
                display: flex;
                align-items: center;
            }
            .header-logo {
                height: 42px;
                margin-right: 20px;
            }
            .header-text {
                display: flex;
                flex-direction: column;
            }
        </style>
    """, unsafe_allow_html=True)

local_css()

# Cabeçalho com logo
col1, col2 = st.columns([1, 10])
with col1:
    st.image("https://i.imgur.com/H9Xj7nd.png", width=100)
with col2:
    st.markdown("""
        <div class="header-container">
            <div class="header-text">
                <h2 style="margin: 0; color: #00205B;">Central de Planejamento Comercial</h2>
                <span style="color: #6c757d;">Travelex Bank · Tudo o que você precisa em um só lugar.</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 🔍 Barra de busca
st.markdown("""
### 🔍 Pesquisar
<div style="display: flex; gap: 10px; align-items: center;">
    <input type="text" placeholder="Buscar dashboards, formulários ou materiais" style="flex: 1; padding: 10px; border: 1px solid #ccc; border-radius: 8px;"/>
    <button style="padding: 10px 15px; background-color: #fff; color: #00205B; border: 1px solid #00205B; border-radius: 8px;">
        🔍 Buscar
    </button>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Função para gerar seção
def section(title, emoji, links):
    st.markdown(f"""<div class='section-title'>{emoji} {title}</div>""", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, (nome, url) in enumerate(links):
        link_html = f"<a href='{url}' target='_blank' class='resource-box'>{nome}</a>"
        if i % 2 == 0:
            col1.markdown(link_html, unsafe_allow_html=True)
        else:
            col2.markdown(link_html, unsafe_allow_html=True)

# Seções do portal
section("Dashboards Comerciais", "📊", [
    ("📌 Gestão Comercial – Market Share", "https://app.powerbi.com/links/VrFjeMY32s"),
    ("📈 Telemetria", "https://app.powerbi.com/links/DN8vawnQyN"),
    ("🔍 Raio X", "https://app.powerbi.com/links/r_cCxY0hQF"),
    ("📊 Resultados vs Meta", "https://app.powerbi.com/links/5tOpR8JJh4")
])

section("Formulários", "📝", [
    ("📄 Migração de Carteira", "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4..."),
    ("📄 Extração de CAM57", "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...")
])

section("Materiais", "📚", [
    ("📁 Treinamentos e Manuais", "https://seulink.com/treinamentos")
])

section("Área de Crédito", "🏢", [
    ("📝 Proposta de Crédito", "https://forms.office.com/pages/responsepage.aspx?id=creditform1"),
    ("🌱 Formulário ESG", "https://forms.office.com/pages/responsepage.aspx?id=esgform2"),
    ("📊 New Dashboard - Crédito", "https://app.powerbi.com/links/newcreditdashboard")
])
