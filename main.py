import streamlit as st
import base64
from PIL import Image

st.set_page_config(page_title="Portal Comercial Travelex", layout="wide")

# Função para carregar imagens como base64 para uso inline em HTML
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Logo
logo_path = "logo_travelex.png"
logo_base64 = get_base64_of_bin_file(logo_path)

# Sidebar com cor de fundo personalizada
with st.sidebar:
    st.markdown(
        f"""
        <div style='text-align: center; background-color: #002b5b; padding: 20px; border-radius: 10px;'>
            <img src='data:image/png;base64,{logo_base64}' width='150'>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <div style='color: white;'>
        <h4>Seções</h4>
        <ul style='list-style: none; padding-left: 0;'>
            <li><a href="#inicio" style='color: white;'>🏠 Início</a></li>
            <li><a href="#dashboards" style='color: white;'>📊 Dashboards</a></li>
            <li><a href="#formularios" style='color: white;'>📄 Formulários</a></li>
            <li><a href="#materiais" style='color: white;'>📚 Materiais</a></li>
            <li><a href="#credito" style='color: white;'>🏢 Área de Crédito</a></li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Cabeçalho com fundo e logo centralizada
st.markdown(
    f"""
    <div id="inicio" style='background-color: #ffffff; padding: 30px 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.05); display: flex; align-items: center;'>
        <img src='data:image/png;base64,{logo_base64}' width='60' style='margin-right: 20px;'>
        <div>
            <h1 style='margin-bottom: 0px; color: #002B5B;'>Central de Planejamento Comercial</h1>
            <p style='margin-top: 5px; color: #6c757d;'>Travelex Bank · Tudo o que você precisa em um só lugar.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""<br>""", unsafe_allow_html=True)

# Barra de busca
col1, col2 = st.columns([9, 1])
with col1:
    query = st.text_input("🔎 Pesquisar", placeholder="Buscar dashboards, formulários ou materiais")
with col2:
    st.markdown("""
    <div style="padding-top: 14px;">
        <button style="background-color: white; border: 1px solid #002B5B; border-radius: 6px; padding: 6px 12px; cursor: pointer;">
            🔍 Buscar
        </button>
    </div>
    """, unsafe_allow_html=True)

# Exemplo de seções com cards clicáveis e separados
secoes = {
    "📊 Dashboards Comerciais": [
        ("📌 Gestão Comercial – Market Share", "https://app.powerbi.com/links/VrFjeMY32s"),
        ("🧭 Telemetria", "https://app.powerbi.com/links/DN8VawnQyN"),
        ("🔎 Raio X", "https://app.powerbi.com/links/r_cCxY0hQF"),
        ("📈 Resultados vs Meta", "https://app.powerbi.com/links/5tOpR8JJh4")
    ],
    "📝 Formulários": [
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

for i, (secao, links) in enumerate(secoes.items()):
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown(f"<h3 id='{anchors[i]}'>{secao}</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    metade = len(links) // 2 + len(links) % 2
    with col1:
        for nome, url in links[:metade]:
            st.markdown(
                f"""
                <a href="{url}" target="_blank" style="text-decoration: none;">
                    <div style="border: 1px solid #003366; padding: 12px 20px; border-radius: 10px; margin: 10px 0; background-color: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.05); transition: transform 0.2s; cursor: pointer;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)';">
                        {nome}
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )
    with col2:
        for nome, url in links[metade:]:
            st.markdown(
                f"""
                <a href="{url}" target="_blank" style="text-decoration: none;">
                    <div style="border: 1px solid #003366; padding: 12px 20px; border-radius: 10px; margin: 10px 0; background-color: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.05); transition: transform 0.2s; cursor: pointer;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)';">
                        {nome}
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )
