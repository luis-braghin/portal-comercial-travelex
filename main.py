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
        }
        .block-container {
            padding: 2rem 3rem;
        }
        h1, h2, h3, h4 {
            color: #00205B;
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
    st.markdown("## 📈 Meta do Mês")
    st.markdown("""
        <div class="metric-block">
            <h2 style="margin:0;">🎯 75%</h2>
            <p style="margin:0;">Meta atingida até agora</p>
        </div>
    """, unsafe_allow_html=True)

    # DASHBOARDS
    st.markdown("## 📊 Dashboards Comerciais")
    dash_cols = st.columns(2)
    with dash_cols[0]:
        st.markdown("""
            <a href="https://app.powerbi.com/links/VrFjeMY32s" target="_blank">
                <div class="card">
                    <h4>📌 Gestão Comercial – Market Share</h4>
                </div>
            </a>
        """, unsafe_allow_html=True)
        st.markdown("""
            <a href="https://app.powerbi.com/links/r_cCxY0hQF" target="_blank">
                <div class="card">
                    <h4>🩺 Raio X</h4>
                </div>
            </a>
        """, unsafe_allow_html=True)
    with dash_cols[1]:
        st.markdown("""
            <a href="https://app.powerbi.com/links/DN8VawnQyN" target="_blank">
                <div class="card">
                    <h4>📡 Telemetria</h4>
                </div>
            </a>
        """, unsafe_allow_html=True)
        st.markdown("""
            <a href="https://app.powerbi.com/links/5tOpR8JJh4" target="_blank">
                <div class="card">
                    <h4>📊 Resultados vs Meta</h4>
                </div>
            </a>
        """, unsafe_allow_html=True)

    # FORMULÁRIOS
    st.markdown("## 📝 Formulários Úteis")
    form_cols = st.columns(2)
    with form_cols[0]:
        st.markdown("""
            <a href="https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4..." target="_blank">
                <div class="card">
                    <h4>📄 Migração de Carteira</h4>
                </div>
            </a>
        """, unsafe_allow_html=True)
    with form_cols[1]:
        st.markdown("""
            <a href="https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4..." target="_blank">
                <div class="card">
                    <h4>📄 Extração de CAM57</h4>
                </div>
            </a>
        """, unsafe_allow_html=True)

    # MATERIAIS
    st.markdown("## 📚 Materiais")
    st.markdown("""
        <div class="card">
            <h4>📁 Esta seção pode conter links para treinamentos, manuais, apresentações internas etc.</h4>
            <p>Me envie o que quiser que eu coloco aqui!</p>
        </div>
    """, unsafe_allow_html=True)

# OUTRAS SEÇÕES
elif selected == "📊 Dashboards":
    st.markdown("### 📊 Dashboards Comerciais")
    dashboards = [
        {"nome": "Gestão Comercial – Market Share", "link": "https://app.powerbi.com/links/VrFjeMY32s"},
        {"nome": "Telemetria", "link": "https://app.powerbi.com/links/DN8VawnQyN"},
        {"nome": "Raio X", "link": "https://app.powerbi.com/links/r_cCxY0hQF"},
        {"nome": "Resultados vs Meta", "link": "https://app.powerbi.com/links/5tOpR8JJh4"},
    ]
    col1, col2 = st.columns(2)
    for i, dash in enumerate(dashboards):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
                <a href="{dash['link']}" target="_blank">
                    <div class="card">
                        <h4>{dash['nome']}</h4>
                    </div>
                </a>
            """, unsafe_allow_html=True)

elif selected == "📄 Formulários":
    st.markdown("### 📄 Formulários Úteis")
    st.markdown("""
        <a href="https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4..." target="_blank">
            <div class="card">
                <h4>📝 Pedidos de Migração de Carteira</h4>
            </div>
        </a>
    """, unsafe_allow_html=True)
    st.markdown("""
        <a href="https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4..." target="_blank">
            <div class="card">
                <h4>📑 Pedidos de Extração de CAM57</h4>
            </div>
        </a>
    """, unsafe_allow_html=True)

elif selected == "📚 Materiais":
    st.markdown("### 📚 Materiais e Documentos")
    st.markdown("""
        <div class="card">
            <p>📂 *(Envie os links ou materiais que deseja adicionar aqui)*</p>
        </div>
    """, unsafe_allow_html=True)

# RODAPÉ
st.markdown("---")
st.caption("Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank")
st.markdown(f"<sub>🔒 Acesso: somente uso interno | 🧾 Dados de uso sendo monitorados | 📊 Total de acessos: <b>{total_acessos}</b></sub>", unsafe_allow_html=True)
