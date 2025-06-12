import streamlit as st
import base64

# CONFIGURAÇÕES INICIAIS
st.set_page_config(page_title="Portal Comercial Travelex", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_path = "logo_travelex.png"
logo_base64 = get_base64_of_bin_file(logo_path)

# CSS PERSONALIZADO
st.markdown(f"""
<style>
    html {{ scroll-behavior: smooth; }}
    .sidebar-links a {{
        color: white;
        display: block;
        padding: 8px 0;
        text-decoration: none;
    }}
    .sidebar-links a:hover {{ text-decoration: underline; }}
    .custom-card {{
        border: 1px solid #003366;
        padding: 12px 20px;
        border-radius: 10px;
        margin: 10px 0;
        background-color: #fff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        cursor: pointer;
    }}
    .custom-card:hover {{
        transform: scale(1.03);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown(f"""
    <div style='text-align: center; background-color: #002b5b; padding: 20px; border-radius: 10px;'>
        <img src='data:image/png;base64,{logo_base64}' width='150'>
    </div>
    <div class="sidebar-links" style='color: white; margin-top: 20px;'>
        <h4>Seções</h4>
        <a href="#inicio">🏠 Início</a>
        <a href="#dashboards">📊 Dashboards</a>
        <a href="#formularios">📄 Formulários</a>
        <a href="#materiais">📚 Materiais</a>
        <a href="#credito">🏢 Crédito</a>
    </div>
    """, unsafe_allow_html=True)

# CABEÇALHO
st.markdown(f"""
<div id="inicio" style='background-color: #ffffff; padding: 30px 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.05); display: flex; align-items: center;'>
    <img src='data:image/png;base64,{logo_base64}' width='60' style='margin-right: 20px;'>
    <div>
        <h1 style='margin-bottom: 0px; color: #002B5B;'>Central de Planejamento Comercial</h1>
        <p style='margin-top: 5px; color: #6c757d;'>Travelex Bank · Tudo o que você precisa em um só lugar.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# NOTIFICAÇÃO
st.markdown("""
<div style="background-color: #e6f0fb; border-radius: 8px; padding: 10px 20px; margin-top: 20px;">
    🔔 Atualização: Adicionamos o novo relatório de Telemetria!
</div>
""", unsafe_allow_html=True)

# BARRA DE PESQUISA
col1, col2 = st.columns([9, 1])
with col1:
    query = st.text_input("Pesquisar", placeholder="Buscar dashboards, formulários ou materiais")
with col2:
    st.markdown("""
    <div style="padding-top: 30px;">
        <button style="background-color: white; border: 1px solid #002B5B; border-radius: 6px; padding: 6px 12px; cursor: pointer;">
            🔍 Buscar
        </button>
    </div>
    """, unsafe_allow_html=True)

# ESPAÇAMENTO
st.markdown("<div style='margin-top: 25px'></div>", unsafe_allow_html=True)

# META DO MÊS (DISCRETA)
st.markdown("""
<h3 style='color: #002B5B; font-size: 18px;'>📉 Meta do Mês</h3>
<div style="background-color: #E8EEF7; padding: 14px; border-radius: 10px; text-align: center; color: #002B5B; font-size: 16px;">
    🎯 X%<br>
    <span style="font-size: 13px;">Meta atingida até agora</span>
</div>
""", unsafe_allow_html=True)

# ESPAÇAMENTO
st.markdown("<div style='margin-top: 25px'></div>", unsafe_allow_html=True)

# PRÓXIMOS EVENTOS
st.markdown("""
<h3 style='color: #002B5B; font-size: 18px;'>🗓️ Próximos Eventos</h3>
<ul style='line-height: 1.7; font-size: 15px;'>
    <li>🔔 Reunião Trimestral - 20 de Junho</li>
    <li>🧠 Workshop Estratégico - 27 de Junho</li>
    <li>📊 Atualização Power BI - 01 de Julho</li>
</ul>
""", unsafe_allow_html=True)

# DADOS DAS SEÇÕES
secoes = {
    "📊 Dashboards Comerciais": [
        ("📌 Gestão Comercial – Market Share", "https://app.powerbi.com/links/VrFjeMY32s"),
        ("🧭 Telemetria", "https://app.powerbi.com/links/DN8VawnQyN"),
        ("🔎 Raio X", "https://app.powerbi.com/links/r_cCxY0hQF"),
        ("📈 Resultados vs Meta", "https://app.powerbi.com/links/5tOpR8JJh4")
    ],
    "📄 Formulários": [
        ("📄 Migração de Carteira", "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4..."),
        ("📄 Extração de CAM57", "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4...")
    ],
    "📚 Materiais": [
        ("📁 Treinamentos e Manuais", "https://example.com/materials")
    ],
    "🏢 Área de Crédito": [
        ("🧾 Proposta de Crédito", "https://forms.office.com/pages/responsepage.aspx?id=creditform"),
        ("🌱 Formulário ESG", "https://forms.office.com/pages/responsepage.aspx?id=esgform"),
        ("📊 New Dashboard - Crédito", "https://app.powerbi.com/links/newcreditdash")
    ]
}

anchors = ["dashboards", "formularios", "materiais", "credito"]

# LOOP DAS SEÇÕES
for i, (secao, links) in enumerate(secoes.items()):
    st.markdown(f"""
    <div id="{anchors[i]}" style="background-color: #002B5B; color: white; padding: 10px 15px; border-radius: 8px; font-size: 18px; margin-top: 40px;">
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
                    <div class="custom-card">
                        <span style="display: block;">{nome}</span>
                    </div>
                </a>
                """, unsafe_allow_html=True)

# RODAPÉ
st.markdown("""
<br><br>
<div style="text-align: center; font-size: 13px; color: #6c757d;">
    Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank<br>
    🔒 Acesso: somente uso interno | 📋 Dados de uso sendo monitorados | 📊 Total de acessos: <b>23</b>
</div>
""", unsafe_allow_html=True)
