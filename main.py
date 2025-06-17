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
        ("PF – KYC", "https://confidence1-my.sharepoint.com/:w:/g/personal/lebraghin_travelexbank_com_br/EUa4o6w-MjxCjic2tr3sIooBjhRiYMXldjbfFjaMiW3F_w?e=QMWJPK"),
        ("PF – Ficha Cadastral", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/EcV0bAVC7XZKijziB5RPUoEBYgNy33jPZ6XT8ZsYOHxwpA?e=jo4u3b"),
        ("PF – Abertura Conta-Corrente Residente", "https://confidence1-my.sharepoint.com/:w:/r/personal/lebraghin_travelexbank_com_br/Documents/Imagens%20TVX/Abertura_Conta_Corrente_PF.docx?d=w1f7e95d9bb3441b2bc90f83d7148ae81&csf=1&web=1&e=qEmbeU"),
        ("PF – Abertura Conta-Corrente Não-Residente", "https://confidence1-my.sharepoint.com/:w:/g/personal/lebraghin_travelexbank_com_br/ERHddXZmnmlCoREHjD-H-2ABhASxKpIh9HvUGppa3ttN8Q?e=MEFMa6"),
        ("PF – Solicitação Acesso IB", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/EbXp2JoQqLRPq3mrEiXJVtYBndV5Sm96Jzw7zP_PcSxktw?e=K9s5Uf"),
        ("PJ – KYC", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/Ef9ganuI9vBBssiO51SJEqIBLWjwgEn1PSurkViQsOjxtQ?e=PNilNx"),
        ("PJ – Ficha Cadastral", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/EZqeDZjyZrdKrfbHFHgm9HsBAs5IctAPv4vK4BNkvc-fLw?e=Mgdt3U"),
        ("PJ – Ficha Cadastral Anexo I", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/EVNcXLzx5GJFmgj_h182CvkBQZEam3C-cqn8W48igTxqSA?e=0lfhyG"),
        ("PJ – Ficha Cadastral Anexo II", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/Eb4elygC4rpJl3U2dei-yEsBYBEErg3J4GpbgX4hWdCHMA?e=wJRI1T"),
        ("PJ – Abertura de Conta-Corrente", "https://confidence1-my.sharepoint.com/:w:/g/personal/lebraghin_travelexbank_com_br/Eb9seXTCcGJBlikpGoTSC8cBXQxIWP7_MVnbTl9fL1DzRQ?e=oNDx4r"),
        ("PJ – Solicitação Acesso IB", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/EUtWaDiB-4JMtN_O2UjytLkBfl04Uo7ihl7ILlVEL0y6KQ?e=cPjgs6")
    ],
    "Outros Conteúdos": [
        ("Exemplo 1", "#"),
        ("Exemplo 2", "#")
    ]
}
