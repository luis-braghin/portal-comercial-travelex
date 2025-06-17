import streamlit as st
from streamlit_option_menu import option_menu
import base64

# ========= CONFIGURAÇÕES DE CONTEÚDO ========= #
mensagem_atualizacao = "🔔 Atualização: Estamos prestes a lançar nossa plataforma de CRM!"

eventos = [
    "💥 Super-Quarta Decisão Taxa de Juros (Fed + Copom) – 17 e 18 de Junho",
    "🖙️ Divulgação do BCB Focus (Expectativas do mercado para câmbio e inflação) - 23 de Junho",
    "🧠 Decisão Plataforma CRM para o Banco - 31 de Junho"
]

destaque_comercial = {
    "nome": "Comercial Gabrielle Figueira",
    "motivo": "🚀 Top Receitas da Semana"
}
# ============================================= #

st.set_page_config(page_title="Portal de Planejamento Comercial", layout="wide", page_icon="logo_travelex.png")

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64("logo_travelex.png")

# CSS VISUAL
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }
    .main-container { max-width: 1400px; margin: auto; }
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
    .info-text { font-size: 16px; color: #4a4a4a; }
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

with st.sidebar:
    st.image(f"data:image/png;base64,{logo_base64}", width=180)
    selected = option_menu(
        "Seções",
        [
            "🏠 Início", "📈 Dashboards", "📄 Formulários", "📚 Materiais/Treinamento",
            "🌟 Área de Onboarding/Cadastro", "📁 KYC e Documentos de Abertura",
            "🏢 Área de Crédito", "🔗 Links Úteis"
        ],
        icons=["house", "bar-chart", "file-earmark-text", "book", "person-plus", "folder", "building", "link"],
        menu_icon="cast",
        default_index=0
    )

conteudos = {
    "📁 KYC e Documentos de Abertura": [
        ("PF – KYC", "https://link-kyc-pf"),
        ("PF – Ficha Cadastral", "https://link-ficha-pf"),
        ("PF – Abertura Conta-Corrente Residente", "https://link-conta-residente"),
        ("PF – Abertura Conta-Corrente Não-Residente", "https://link-conta-nao-residente"),
        ("PF – Solicitação Acesso IB", "https://link-acesso-ib-pf"),
        ("PJ – KYC", "https://link-kyc-pj"),
        ("PJ – Ficha Cadastral", "https://link-ficha-pj"),
        ("PJ – Ficha Cadastral Anexo I", "https://link-anexo-i"),
        ("PJ – Ficha Cadastral Anexo II", "https://link-anexo-ii"),
        ("PJ – Abertura de Conta-Corrente", "https://link-conta-pj"),
        ("PJ – Solicitação Acesso IB", "https://link-acesso-ib-pj")
    ],
    "Outros Conteúdos": [
        ("Exemplo 1", "#"),
        ("Exemplo 2", "#")
    ]
}

def mostrar_bloco(titulo, lista):
    if titulo:
        st.markdown(f"<div class='section-title'>{titulo}</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, (nome, link) in enumerate(lista):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
                <a href="{link}" target="_blank" style="text-decoration: none;">
                    <div class="custom-card">{nome}</div>
                </a>
            """, unsafe_allow_html=True)

if selected == "🏠 Início":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    st.markdown(f"""<div class='highlight-box'>
        <div style="display: flex; align-items: center;">
            <img src='data:image/png;base64,{logo_base64}' width='60' style='margin-right: 20px;'>
            <div>
                <h1 style='margin: 0; color: #00205B;'>Portal de Planejamento Comercial</h1>
                <p class='info-text'>Travelex Bank · Tudo o que você precisa em um só lugar.</p>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    st.info(mensagem_atualizacao)

    st.markdown("<div class='section-title'>📆 Próximos Eventos</div>", unsafe_allow_html=True)
    for evento in eventos:
        st.markdown(f"- {evento}")

    st.markdown("<div class='section-title'>🏆 Comercial Destaque da Semana</div>", unsafe_allow_html=True)
    st.markdown(f"""<div class="metric-box">
        🌟 <strong>{destaque_comercial['nome']}</strong><br>
        <span style="font-size: 14px; font-weight: normal">{destaque_comercial['motivo']}</span>
    </div>""", unsafe_allow_html=True)

    for secao, blocos in conteudos.items():
        if secao == "📁 KYC e Documentos de Abertura":
            pf_docs = [(nome, link) for nome, link in blocos if "PF –" in nome]
            pj_docs = [(nome, link) for nome, link in blocos if "PJ –" in nome]

            st.markdown(f"<div class='section-title'>📁 {secao}</div>", unsafe_allow_html=True)
            if pf_docs:
                st.markdown("<div class='section-title'>👤 Documentos Pessoa Física (PF)</div>", unsafe_allow_html=True)
                mostrar_bloco("", pf_docs)
            if pj_docs:
                st.markdown("<div class='section-title'>🏢 Documentos Pessoa Jurídica (PJ)</div>", unsafe_allow_html=True)
                mostrar_bloco("", pj_docs)
        else:
            mostrar_bloco(secao, blocos)

    st.markdown("</div>", unsafe_allow_html=True)

elif selected == "📁 KYC e Documentos de Abertura":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    pf_docs = [(nome, link) for nome, link in conteudos[selected] if "PF –" in nome]
    pj_docs = [(nome, link) for nome, link in conteudos[selected] if "PJ –" in nome]

    st.markdown("<div class='section-title'>👤 Documentos Pessoa Física (PF)</div>", unsafe_allow_html=True)
    mostrar_bloco("", pf_docs)

    st.markdown("<div class='section-title'>🏢 Documentos Pessoa Jurídica (PJ)</div>", unsafe_allow_html=True)
    mostrar_bloco("", pj_docs)
    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    mostrar_bloco(selected, conteudos.get(selected, []))
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<br><hr><div style='text-align:center; font-size:13px; color:#6c757d;'>
Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank<br>
🔐 Acesso: somente uso interno | 📊 Dados de uso sendo monitorados
</div>""", unsafe_allow_html=True)
