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
    "nome": "Comercial _______",
    "motivo": "Em desenvolvimento"
}
# ============================================= #

st.set_page_config(page_title="Portal de Planejamento Comercial", layout="wide", page_icon="logo_travelex.png")

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64("logo_travelex.png")

# CSS MODERNO VISUAL
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
        ["🏠 Início", "📊 Dashboards", "📄 Formulários", "📚 Materiais", "🏢 Crédito", "🔗 Links Úteis"],
        icons=["house", "bar-chart", "file-earmark-text", "book", "building", "link"],
        menu_icon="cast",
        default_index=0
    )

conteudos = {
    "📊 Dashboards Comerciais": [
        ("📌 Gestão Comercial – Market Share", "https://app.powerbi.com/links/VrFjeMY32s"),
        ("📡 Telemetria 🆕", "https://app.powerbi.com/links/DN8VawnQyN"),
        ("🔍 Raio X", "https://app.powerbi.com/links/r_cCxY0hQF"),
        ("📈 Resultados vs Meta", "https://app.powerbi.com/links/5tOpR8JJh4"),
        ("📊 DI/DUE", "https://app.powerbi.com/groups/me/reports/8b08b858-8067-4adb-a1a9-a511c981b816/2e5df3a16e8323e9651f?experience=power-bi"),
        ("📊 PLD a vencer", "https://app.powerbi.com/groups/me/reports/e8fdd4f8-5c18-481f-9919-7bfe53373b50/4f457ae5e54901bee4b0?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&experience=power-bi")
    ],
    "📄 Formulários": [
        ("📄 Migração de Carteira", "https://forms.office.com/pages/responsepage.aspx?id=1"),
        ("📄 Extração de CAM57", "https://forms.office.com/pages/responsepage.aspx?id=2")
    ],
    "📚 Materiais": [
        ("📁 Treinamentos e Manuais", "https://example.com/materials")
    ],
    "🏢 Área de Crédito": [
        ("🧾 Proposta de Crédito", "https://forms.office.com/pages/responsepage.aspx?id=creditform"),
        ("🌱 Formulário ESG", "https://forms.office.com/pages/responsepage.aspx?id=esgform"),
        ("📊 Dashboard Crédito", "https://app.powerbi.com/links/newcreditdash")
    ],
    "🔗 Links Úteis": [
        ("🌐 Radar (Habilitação COMEX)", "https://servicos.receita.fazenda.gov.br/servicos/radar/consultasituacaocpfcnpj.asp"),
        ("📄 Comprovante PJ", "https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp"),
        ("📄 Países Restritos e Monitorados", "https://confidence1.sharepoint.com/Compliance/normativas/DocumentosNormativas/GGIR-MPP89-A1%20-%20Pa%C3%ADses%20Restritos%20e%20Monitorados.pdf?isSPOFile=1&OR=Teams-HL&CT=1706105239041&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMzExMzAyNjIwMiIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D"),
        ("📌 Lâmina de Produtos", "https://linktr.ee/travelexbank23")
    ]
}

def mostrar_bloco(titulo, lista):
    st.markdown(f"<div class='section-title'>{titulo}</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, (nome, link) in enumerate(lista):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
                <a href="{link}" target="_blank" style="text-decoration: none;">
                    <div class="custom-card">{nome}</div>
                </a>
            """, unsafe_allow_html=True)

def buscar_conteudos(termo):
    resultados = {}
    termo = termo.lower()
    for secao, itens in conteudos.items():
        filtrados = [(nome, link) for nome, link in itens if termo in nome.lower()]
        if filtrados:
            resultados[secao] = filtrados
    return resultados

if selected == "🏠 Início":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    # CAMPO DE BUSCA FUNCIONAL
    termo = st.text_input(
        "🔎 Buscar relatórios, formulários ou materiais...",
        placeholder="Ex: CAM57, ESG, Market Share",
        key="busca_ativa"
    )

    st.markdown(f"""
    <div class='highlight-box'>
        <div style="display: flex; align-items: center;">
            <img src='data:image/png;base64,{logo_base64}' width='60' style='margin-right: 20px;'>
            <div>
                <h1 style='margin: 0; color: #00205B;'>Portal de Planejamento Comercial</h1>
                <p class='info-text'>Travelex Bank · Tudo o que você precisa em um só lugar.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.info(mensagem_atualizacao)

    st.markdown("<div class='section-title'>🏆 Comercial Destaque da Semana</div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="metric-box">
            🌟 <strong>{destaque_comercial['nome']}</strong><br>
            <span style="font-size: 14px; font-weight: normal">{destaque_comercial['motivo']}</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>🗓️ Próximos Eventos</div>", unsafe_allow_html=True)
    for evento in eventos:
        st.markdown(f"- {evento}")

    if termo:
        resultados = buscar_conteudos(termo)
        st.markdown(f"<div class='section-title'>🔎 Resultados para: <em>{termo}</em></div>", unsafe_allow_html=True)
        if resultados:
            for secao, itens in resultados.items():
                for nome, link in itens:
                    st.markdown(f"""
                        <a href="{link}" target="_blank" style="text-decoration: none;">
                            <div class="custom-card">{nome} <small style='color:#888;font-size:13px;display:block'>{secao}</small></div>
                        </a>
                    """, unsafe_allow_html=True)
        else:
            st.warning("Nenhum resultado encontrado para a busca.")

    else:
            st.warning("Nenhum resultado encontrado para a busca.")

    else:
        # Só mostra o restante se não estiver buscando
        st.markdown("<div class='section-title'>🏆 Comercial Destaque da Semana</div>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class="metric-box">
                🌟 <strong>{destaque_comercial['nome']}</strong><br>
                <span style="font-size: 14px; font-weight: normal">{destaque_comercial['motivo']}</span>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='section-title'>🗓️ Próximos Eventos</div>", unsafe_allow_html=True)
        for evento in eventos:
            st.markdown(f"- {evento}")

        for secao, blocos in conteudos.items():
            mostrar_bloco(secao, blocos)

    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    secao_nome = next((k for k in conteudos.keys() if any(p in k for p in selected.split())), None)
    if secao_nome:
        mostrar_bloco(secao_nome, conteudos[secao_nome])
    else:
        st.warning("Nenhum conteúdo encontrado para esta seção.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""<br><hr><div style='text-align:center; font-size:13px; color:#6c757d;'>
    Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank<br>
    🔐 Acesso: somente uso interno | 📊 Dados de uso sendo monitorados
</div>""", unsafe_allow_html=True)
