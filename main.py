import streamlit as st
from streamlit_option_menu import option_menu
import os

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Portal Comercial Travelex",
    layout="wide",
    page_icon="logo_travelex.png"  # Coloque seu favicon na raiz
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

# DADOS GLOBAIS
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
eventos = [
    ("📅 Reunião Comercial", "18/06/2025", "Apresentação de resultados semestrais."),
    ("🧠 Workshop CRM", "25/06/2025", "Capacitação para uso da nova plataforma."),
    ("🚀 Lançamento de Campanha", "01/07/2025", "Nova campanha de captação será iniciada."),
]

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
        .header {
            background-color: white;
            padding: 1.5rem 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            margin-bottom: 2rem;
        }
        .card {
            background-color: white;
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            transition: all 0.2s ease-in-out;
            font-size: 16px;
        }
        .card:hover {
            box-shadow: 0 6px 14px rgba(0,0,0,0.15);
            transform: scale(1.02);
        }
        .metric-block {
            background-color: #00205B;
            padding: 1.5rem;
            border-radius: 16px;
            color: white;
            text-align: center;
            margin-top: 2rem;
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
        }
        .metric-block img {
            height: 50px;
        }
        .event-block {
            background-color: #ffffff;
            border-left: 5px solid #0072CE;
            padding: 1rem;
            border-radius: 12px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.08);
            margin-bottom: 1rem;
        }
        .search-container {
            display: flex;
            gap: 0.5rem;
            align-items: center;
            margin-bottom: 1.5rem;
        }
        .search-container input {
            flex: 1;
            padding: 0.6rem;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
        }
        .search-container button {
            background-color: #00205B;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1rem;
            cursor: pointer;
        }
        /* Sidebar dark mode */
        section[data-testid="stSidebar"] {
            background-color: #00205B !important;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    selected = option_menu(
        "Seções",
        ["🏠 Início", "📊 Dashboards", "📄 Formulários", "📚 Materiais"],
        icons=["house", "bar-chart", "file-earmark-text", "folder"],
        menu_icon="cast",
        default_index=0
    )

# CABEÇALHO
st.markdown('<div class="header">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 9])
with col1:
    st.image("logo_travelex.png", width=100)
with col2:
    st.markdown("## Central de Planejamento Comercial")
    st.caption("Travelex Bank · Tudo o que você precisa em um só lugar.")
st.markdown('</div>', unsafe_allow_html=True)

# AVISO
st.info("🔔 Atualização: Adicionamos o novo relatório de Telemetria!")

# INÍCIO
if selected == "🏠 Início":
    st.markdown("### 🔎 Pesquisar")
    col_search = st.columns([6, 1])
    search = col_search[0].text_input("", placeholder="Buscar dashboards, formulários ou materiais").lower()
    col_search[1].button("🔍 Buscar")

    # META DO MÊS
    st.markdown("## 📈 Meta do Mês")
    st.markdown("""
        <div class="metric-block">
            <img src="https://img.icons8.com/ios-filled/100/ffffff/combo-chart.png"/>
            <div>
                <h2 style="margin:0;">🎯 75%</h2>
                <p style="margin:0;">Meta atingida até agora</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # EVENTOS
    st.markdown("## 📅 Próximos Eventos")
    st.markdown("<div style='margin-top:3rem'></div>", unsafe_allow_html=True)
    for titulo, data, desc in eventos:
        st.markdown(f"""
            <div class="event-block">
                <strong>{titulo}</strong> – <em>{data}</em><br>
                <span>{desc}</span>
            </div>
        """, unsafe_allow_html=True)

    # DASHBOARDS
    st.markdown("## 📊 Dashboards Comerciais")
    st.markdown("<div style='margin-top:3rem'></div>", unsafe_allow_html=True)
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
    st.markdown("<div style='margin-top:3rem'></div>", unsafe_allow_html=True)
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
    st.markdown("<div style='margin-top:3rem'></div>", unsafe_allow_html=True)
    for nome, link in materiais:
        if search in nome.lower():
            st.markdown(f"""
                <a href="{link}" target="_blank">
                    <div class="card">{nome}</div>
                </a>
            """, unsafe_allow_html=True)

# OUTRAS SEÇÕES
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
