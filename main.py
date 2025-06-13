
import streamlit as st
import base64
from streamlit_option_menu import option_menu

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Portal de Planejamento Comercial",
    layout="wide",
    page_icon="logo_travelex.png"
)

# Função para converter imagem em base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_path = "logo_travelex.png"
logo_base64 = get_base64_of_bin_file(logo_path)

# SIDEBAR
with st.sidebar:
    st.markdown(f"""
    <div style='text-align: center; background-color: #002b5b; padding: 20px; border-radius: 10px;'>
        <img src='data:image/png;base64,{logo_base64}' width='150'>
    </div>
    """, unsafe_allow_html=True)

    selected = option_menu(
        "Seções",
        ["Início", "Dashboards", "Formulários", "Materiais", "Crédito"],
        icons=["house", "bar-chart", "file-earmark-text", "folder", "building"],
        menu_icon="cast",
        default_index=0
    )

# CABEÇALHO
st.markdown(f"""
<div style='background-color: #ffffff; padding: 30px 20px 10px 20px; border-radius: 10px;
             box-shadow: 0px 0px 10px rgba(0,0,0,0.05); display: flex; align-items: center; margin-bottom: 25px;'>
    <img src='data:image/png;base64,{logo_base64}' width='60' style='margin-right: 20px;'>
    <div>
        <h1 style='margin: 0; color: #002B5B;'>Portal de Planejamento Comercial</h1>
        <p style='margin-top: 5px; color: #6c757d;'>Travelex Bank · Tudo o que você precisa em um só lugar.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# NOTIFICAÇÃO
st.markdown("""
<div style="background-color: #e6f0fb; border-radius: 8px; padding: 10px 20px; margin-top: 10px;">
    🔔 Atualização: Adicionamos o novo relatório de Telemetria!
</div>
""", unsafe_allow_html=True)

# INÍCIO
if selected == "Início":
    # PESQUISA
    st.markdown("### 🔎 Pesquisar")
    col1, col2 = st.columns([8, 1])
    with col1:
        query = st.text_input("", placeholder="Buscar dashboards, formulários ou materiais")
    with col2:
        st.markdown("""
        <div style="margin-top: 34px;">
            <button style="background-color: white; border: 1px solid #002B5B;
            border-radius: 6px; padding: 8px 12px; cursor: pointer;">
                🔍 Buscar
            </button>
        </div>
        """, unsafe_allow_html=True)

    # META DO MÊS
    st.markdown("### 📈 Meta do Mês")
    st.markdown("""
    <div style="background-color: #f0f4fb; padding: 8px; border-radius: 8px; text-align: center; color: #00205B;">
        <div style="font-size: 28px; font-weight: bold;">🎯 X%</div>
        <div style="font-size: 13px;">Meta atingida até agora</div>
    </div>
    """, unsafe_allow_html=True)

    # EVENTOS
    st.markdown("### 🗓️ Próximos Eventos")
    st.markdown("""
    <ul style='line-height: 1.7; font-size: 15px;'>
        <li>🔔 Reunião Trimestral - 20 de Junho</li>
        <li>🧠 Workshop Estratégico - 27 de Junho</li>
        <li>📊 Atualização Power BI - 01 de Julho</li>
    </ul>
    """, unsafe_allow_html=True)

    # CONTEÚDO
    secoes = {
        "📊 Dashboards Comerciais": [
            ("📌 Gestão Comercial – Market Share", "#"),
            ("🧭 Telemetria", "#"),
            ("🔎 Raio X", "#"),
            ("📈 Resultados vs Meta", "#")
        ],
        "📄 Formulários": [
            ("📄 Migração de Carteira", "#"),
            ("📄 Extração de CAM57", "#")
        ],
        "📚 Materiais": [
            ("📁 Treinamentos e Manuais", "#")
        ],
        "🏢 Crédito": [
            ("🧾 Proposta de Crédito", "#"),
            ("🌱 Formulário ESG", "#"),
            ("📊 New Dashboard - Crédito", "#")
        ]
    }

    for secao, links in secoes.items():
        st.markdown(f"""
        <div style="border-left: 6px solid #002B5B; background-color: #f5f7fa; padding: 8px 15px;
                    border-radius: 6px; font-weight: bold; font-size: 16px; color: #002B5B; margin-top: 30px;">
            {secao}
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        metade = len(links) // 2 + len(links) % 2
        for col, chunk in zip([col1, col2], [links[:metade], links[metade:]]):
            with col:
                for nome, url in chunk:
                    st.markdown(f"""
                    <a href="{url}" target="_blank" style="text-decoration: none;">
                        <div style="border: 1px solid #003366; padding: 12px 20px;
                        border-radius: 10px; margin: 10px 0; background-color: #fff;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.05); transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out; cursor: pointer;">
                            {nome}
                        </div>
                    </a>
                    """, unsafe_allow_html=True)

# RODAPÉ
st.markdown("""
<br><br>
<div style="text-align: center; font-size: 13px; color: #6c757d;">
    Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank<br>
    🔒 Acesso: somente uso interno | 📋 Dados de uso sendo monitorados
</div>
""", unsafe_allow_html=True)
