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
logo_path = "logo_travelex.png"  # Certifique-se de que o arquivo está no mesmo diretório
logo_base64 = get_base64_of_bin_file(logo_path)

# Sidebar
with st.sidebar:
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <img src='data:image/png;base64,{logo_base64}' width='150'>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## Seções")
    st.markdown("<a href='#inicio' style='text-decoration: none;'>🏠 Início</a>", unsafe_allow_html=True)
    st.markdown("<a href='#dashboards-comerciais' style='text-decoration: none;'>📊 Dashboards</a>", unsafe_allow_html=True)
    st.markdown("<a href='#formularios' style='text-decoration: none;'>📄 Formulários</a>", unsafe_allow_html=True)
    st.markdown("<a href='#materiais' style='text-decoration: none;'>📚 Materiais</a>", unsafe_allow_html=True)
    st.markdown("<a href='#area-de-credito' style='text-decoration: none;'>🏢 Área de Crédito</a>", unsafe_allow_html=True)

# Cabeçalho com fundo e logo centralizada
st.markdown(
    f"""
    <div id='inicio' style='background-color: #ffffff; padding: 30px 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.05); display: flex; align-items: center;'>
        <img src='data:image/png;base64,{logo_base64}' width='80' style='margin-right: 20px;'>
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
st.markdown("<div id='busca'></div>", unsafe_allow_html=True)
st.markdown("## 🔎 Pesquisar", unsafe_allow_html=True)
col1, col2 = st.columns([9, 1])
with col1:
    query = st.text_input("", placeholder="Buscar dashboards, formulários ou materiais")
with col2:
    st.button("🔍 Buscar")

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

for secao, links in secoes.items():
    st.markdown("""<br><br>""", unsafe_allow_html=True)
    anchor = secao.lower().replace(" ", "-").replace("–", "-").replace("ç", "c").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ã", "a").replace("ê", "e").replace("ô", "o").replace("õ", "o")
    st.markdown(f"<div id='{anchor}'></div>", unsafe_allow_html=True)
    st.markdown(f"### {secao}")
    col1, col2 = st.columns(2)
    metade = len(links) // 2 + len(links) % 2
    with col1:
        for nome, url in links[:metade]:
            st.markdown(
                f"""
                <a href="{url}" target="_blank" style="text-decoration: none;">
                    <div style="border: 1px solid #003366; padding: 12px 20px; border-radius: 10px; margin: 10px 0; background-color: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.05); transition: transform 0.2s;">
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
                    <div style="border: 1px solid #003366; padding: 12px 20px; border-radius: 10px; margin: 10px 0; background-color: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.05); transition: transform 0.2s;">
                        {nome}
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )
