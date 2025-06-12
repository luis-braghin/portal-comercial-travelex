import streamlit as st
from streamlit_option_menu import option_menu
import os

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portal Comercial Travelex", layout="wide", page_icon="📊")

# CONTADOR DE ACESSO
contador_path = os.path.join(".streamlit", "contador.txt")
if not os.path.exists(contador_path):
    with open(contador_path, "w") as f:
        f.write("0")

with open(contador_path, "r+") as f:
    total_acessos = int(f.read()) + 1
    f.seek(0)
    f.write(str(total_acessos))

# ESTILO CUSTOMIZADO
st.markdown("""
    <style>
        body {
            background-color: #F5F7FA;
        }
        .main {
            background-color: #F5F7FA;
            font-size: 16px;
        }
        .block-container {
            padding: 2rem 3rem;
        }
        h1, h2, h3, h4 {
            color: #00205B;
            font-size: 20px;
        }
        a {
            text-decoration: none;
        }
        a:hover {
            opacity: 0.9;
        }
        .card {
            background-color: white;
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            transition: 0.3s;
            font-size: 16px;
        }
        .card:hover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transform: translateY(-2px);
        }
        .metric-block {
            background-color: #00205B;
            padding: 1.5rem;
            border-radius: 16px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
        }
        .search-box input {
            width: 100%;
            padding: 0.6rem;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# MENU LATERAL
with st.sidebar:
    selected = option_menu(
        "Seções",
        ["🏠 Início", "📊 Dashboards", "📄 Formulários", "📚 Materiais"],
        icons=["house", "bar-chart", "file-earmark-text", "folder"],
        menu_icon="cast",
        default_index=0
    )

# LOGO E TÍTULO
st.markdown('<div style="display:flex;align-items:center;gap:20px;margin-bottom:20px;">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 9])
with col1:
    st.image("logo_travelex.png", width=100)
with col2:
    st.markdown("## Central de Planejamento Comercial")
    st.caption("Travelex Bank · Tudo o que você precisa em um só lugar.")
st.markdown("</div>", unsafe_allow_html=True)

# AVISO NO TOPO
st.info("🔔 Atualização: Adicionamos o novo relatório de Telemetria!")

# INÍCIO
if selected == "🏠 Início":
    # BARRA DE BUSCA
    st.markdown("### 🔎 Pesquisar")
    search = st.text_input("Digite para buscar em dashboards, formulários ou materiais:", "").lower()

    # META DO MÊS
    st.markdown("## 📈 Meta do Mês")
    st.markdown("""
        <div class="metric-block">
            <h2 style="margin:0;">🎯 75%</h2>
            <p style="margin:0;">Meta atingida até agora</p>
        </div>
    """, unsafe_allow_html=True)

    # DADOS
    dashboards = [
        ("📌 Gestão Comercial – Market Share", "https://app.powerbi.com/links/VrFjeMY32s"),
        ("📡 Telemetria", "https://app.powerbi.com/links/DN8VawnQyN"),
        ("🩺 Raio X", "https://app.powerbi.com/links/r_cCxY0hQF"),
        ("📊 Resultados vs Meta", "https://app.powerbi.com/links/5tOpR8JJh4"),
    ]
    formularios = [
        ("📄 Migração de Carteira", "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4..."),
        ("📄 Extração de CAM57", "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4..."),
    ]
    materiais = [
        ("📁 Treinamentos e Manuais", "#"),
    ]

    # DASHBOARDS
    st.markdown("## 📊 Dashboards Comerciais")
    dash_cols = st.columns(2)
    for i, (nome, link) in enumerate(dashboards):
        if search in nome.lower():
            with dash_cols[i % 2]:
                st.markdown(f"""
                    <a href="{link}" target="_blank">
                        <div class="card">{nome}</div>
                    </a>
                """, unsafe_allow_html=True)

    # FORMULÁRIOS
    st.markdown("## 📝 Formulários Úteis")
    form_cols = st.columns(2)
    for i, (nome, link) in enumerate(formularios):
        if search in nome.lower():
            with form_cols[i % 2]:
                st.markdown(f"""
                    <a href="{link}" target="_blank">
                        <div class="card">{nome}</div>
                    </a>
                """, unsafe_allow_html=True)

    # MATERIAIS
    st.markdown("## 📚 Materiais")
    for nome, link in materiais:
        if search in nome.lower():
            st.markdown(f"""
                <a href="{link}" target="_blank">
                    <div class="card">{nome}</div>
                </a>
            """, unsafe_allow_html=True)

# OUTRAS SEÇÕES (mantidas simples)
elif selected == "📊 Dashboards":
    st.markdown("### 📊 Dashboards Comerciais")
    for nome, link in dashboards:
        st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

elif selected == "📄 Formulários":
    st.markdown("### 📄 Formulários Úteis")
    for nome, link in formularios:
        st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

elif selected == "📚 Materiais":
    st.markdown("### 📚 Materiais e Documentos")
    for nome, link in materiais:
        st.markdown(f'<a href="{link}" target="_blank"><div class="card">{nome}</div></a>', unsafe_allow_html=True)

# RODAPÉ
st.markdown("---")
st.caption("Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank")
st.markdown(f"<sub>🔒 Acesso: somente uso interno | 🧾 Dados de uso sendo monitorados | 📊 Total de acessos: <b>{total_acessos}</b></sub>", unsafe_allow_html=True)
