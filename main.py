import streamlit as st
from streamlit_option_menu import option_menu
import base64

# ========= CONFIGURAÇÕES DE CONTEÚDO ========= #
mensagem_atualizacao = "🔔 Atualização: Nossa plataforma de CRM está oficialmente no ar. Foi criada uma seção no site chamada CRM com os links correspondentes!"

eventos = [

    "🧠 Lançamento oficial da Ploomes (CRM) - 24 de julho" ,
    "📈 Prévia da Inflação IPCA-15 – 24 de julho",
    "💸 Reunião do FOMC (Fed) – 30–31 de julho"
]

destaque_comercial = {
    "nome": "Gregorio Rheingantz",
    "motivo": "🚀 Top Receitas"
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
            "🏠 Início", "📊 Dashboards", "📄 Formulários", "📚 Materiais/Treinamento",
            "🆕 Área de Onboarding/Cadastro", "📁 KYC e Documentos de Abertura",
            "🏢 Área de Crédito","🏦 Sistemas do Banco", "🔗 Links Úteis"
        ],
        icons=["house", "bar-chart", "file-earmark-text", "book", "person-plus", "folder", "building", "link"],
        menu_icon="cast",
        default_index=0
    )

conteudos = {
    "🧬 CRM": [
        ("🧩 Site da Ploomes", "https://app10.ploomes.com/")
    ],
    "📊 Dashboards": [
        ("🧠 Dashboard Unificado (Versão Beta)", "https://app.powerbi.com/links/g0711Nttbb?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&pbi_source=linkShare&bookmarkGuid=35fe9c2f-d75d-40f9-8610-9e5075d7f7c7"),
        ("📌 Gestão Comercial – Market Share", "https://app.powerbi.com/links/VrFjeMY32s"),
        ("📡 Telemetria 🆕", "https://app.powerbi.com/links/DN8VawnQyN"),
        ("🔍 Raio X", "https://app.powerbi.com/links/r_cCxY0hQF"),
        ("📈 Resultados vs Meta", "https://app.powerbi.com/links/5tOpR8JJh4"),
        ("📊 DI/DUE", "https://app.powerbi.com/groups/me/reports/8b08b858-8067-4adb-a1a9-a511c981b816/2e5df3a16e8323e9651f?experience=power-bi"),
        ("📊 PLD a vencer", "https://app.powerbi.com/groups/me/reports/e8fdd4f8-5c18-481f-9919-7bfe53373b50/4f457ae5e54901bee4b0")
    ],
    "📄 Formulários": [
        ("📄 Migração de Carteira", "https://forms.office.com/r/W1y1KXzJ5q"),
        ("📄 Feedback Comercial", "https://forms.office.com/r/7Ct99i1s77")

    ],
    "📚 Materiais/Treinamento": [
        ("📌 Lâmina de Produtos", "https://linktr.ee/travelexbank23")
    ],
    "🆕 Área de Onboarding/Cadastro": [
        ("📋 Matriz de Cadastro - GCAD-NOR47-A1", "https://confidence1.sharepoint.com/:x:/r/Compliance/normativas/_layouts/15/doc2.aspx?sourcedoc=%7B10092125-7128-49CC-9D1A-D0EBF63C41E5%7D&file=GCAD-NOR47-A1%20-%20Matriz%20de%20Cadastro.xlsx"),
        ("📥 Painel Onboarding B2B - Cadastro", "https://confidence1.sharepoint.com/sites/PainelOnboarding/_layouts/15/AccessDenied.aspx?Source=https%3A%2F%2Fconfidence1%2Esharepoint%2Ecom%2Fsites%2FPainelOnboarding%2FLists%2FCadastro%2FAllItems%2Easpx"),
        ("🏦 Link para Onboarding - Banco", "https://forms.office.com/Pages/ResponsePage.aspx?id=_G_t2sm4d0eK42lIfQ7vVlYe_Zie5XdOjKJ73Ib1fSRUQUcyMVgxWFVYVUxSWE1NNEVZNEYyRlJBMi4u"),
        ("💼Link para Onboarding - Corretora", "https://forms.office.com/Pages/ResponsePage.aspx?id=_G_t2sm4d0eK42lIfQ7vVlYe_Zie5XdOjKJ73Ib1fSRUNkpQTTVGVE9JWktDV1dTV0gzSlg3Uk5SQS4u"),
        ("🏦 Painel de Acompanhamento de Onboarding - Banco", "https://confidence1.sharepoint.com/sites/PainelOnboarding/Lists/Cadastro/AllItems.aspx"),
        ("💼 Painel de Acompanhamento de Onboarding - Corretora", "https://confidence1.sharepoint.com/sites/PainelOnboarding/Lists/Cadastro%20%20Corretora/AllItems.aspx?env=WebViewList&OR=Teams-HL&CT=1675864797062&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMzAxMDEwMDkxMyIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D"),
        ("📘 Normativas Compliance", "https://confidence1.sharepoint.com/Compliance/normativas/Paginas/default.aspx"),
        ("✅ Aprovações JIRA", "https://jiratvx.atlassian.net/servicedesk/customer/user/login?destination=user%2Fapprovals%3Fpage%3D1")
    ],
    "📁 KYC e Documentos de Abertura": [
    # Documentos Pessoa Física (PF)
    ("PF – KYC", "https://confidence1-my.sharepoint.com/:w:/g/personal/lebraghin_travelexbank_com_br/EUa4o6w-MjxCjic2tr3sIooBjhRiYMXldjbfFjaMiW3F_w?e=QMWJPK"),
    ("PF – Ficha Cadastral", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/EcV0bAVC7XZKijziB5RPUoEBYgNy33jPZ6XT8ZsYOHxwpA?e=jo4u3b"),
    ("PF – Abertura Conta-Corrente Residente", "https://confidence1-my.sharepoint.com/:w:/g/personal/lebraghin_travelexbank_com_br/EdmVfh80u7JBvJD4PXFIroEBU9DURBDX5a1eaFvBmDQsPg?e=G6wy6z"),
    ("PF – Abertura Conta-Corrente Não-Residente", "https://confidence1-my.sharepoint.com/:w:/g/personal/lebraghin_travelexbank_com_br/ERHddXZmnmlCoREHjD-H-2ABhASxKpIh9HvUGppa3ttN8Q?e=MEFMa6"),
    ("PF – Solicitação Acesso IB", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/EbXp2JoQqLRPq3mrEiXJVtYBndV5Sm96Jzw7zP_PcSxktw?e=K9s5Uf"),

    # Documentos Pessoa Jurídica (PJ)
    ("PJ – KYC", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/Ef9ganuI9vBBssiO51SJEqIBLWjwgEn1PSurkViQsOjxtQ?e=PNilNx"),
    ("PJ – Ficha Cadastral", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/EZqeDZjyZrdKrfbHFHgm9HsBAs5IctAPv4vK4BNkvc-fLw?e=Mgdt3U"),
    ("PJ – Ficha Cadastral Anexo I", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/EVNcXLzx5GJFmgj_h182CvkBQZEam3C-cqn8W48igTxqSA?e=0lfhyG"),
    ("PJ – Ficha Cadastral Anexo II", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/Eb4elygC4rpJl3U2dei-yEsBYBEErg3J4GpbgX4hWdCHMA?e=wJRI1T"),
    ("PJ – Abertura de Conta-Corrente", "https://confidence1-my.sharepoint.com/:w:/g/personal/lebraghin_travelexbank_com_br/Eb9seXTCcGJBlikpGoTSC8cBXQxIWP7_MVnbTl9fL1DzRQ?e=oNDx4r"),
    ("PJ – Solicitação Acesso IB", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/EUtWaDiB-4JMtN_O2UjytLkBfl04Uo7ihl7ILlVEL0y6KQ?e=cPjgs6")
],

      "🏢 Área de Crédito": [
        ("🧾 Proposta de Crédito", "https://forms.office.com/r/u4WjFNHZaL"),
        ("🌱 Formulário ESG", "https://forms.office.com/Pages/ResponsePage.aspx?id=_G_t2sm4d0eK42lIfQ7vVnOftT6ZTJtKkIs9SprWJzlUNlNLUjI3MTIyTVZURVI1MFpXN0U5MDk3Sy4u"),
        ("📊 Dashboard Crédito", "https://app.powerbi.com/links/L2YIaQlY_D?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&pbi_source=linkShare&bookmarkGuid=df37e966-fe9a-4757-bdf5-7cb92485c20c")
    ],
 
     "🏦 Sistemas do Banco": [
        ("🔄 Change", "http://change.travelexbank.com.br/cambio/DefaultC.aspx"),
        ("🛡️ SOCC ", "http://socc.bancoconfidence.com.br/confidence/expired.html?lastAccess=1750860447419"),
        ("🧮 MATERA", "https://backoffice.mp.prd.travelexbank.com.br:8443/matera/"),
        ("🌟 Qulture Rocks", "https://app.qulture.rocks/users/sign_in"),
        ("✍️ Click Sign", "https://app.clicksign.com/?session_expired=true")
    ],
    "🔗 Links Úteis": [
        ("🌐 Radar (Habilitação COMEX)", "https://servicos.receita.fazenda.gov.br/servicos/radar/consultasituacaocpfcnpj.asp"),
        ("📄 Comprovante PJ", "https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp"),
        ("📄 Países Restritos e Monitorados", "https://confidence1.sharepoint.com/Compliance/normativas/DocumentosNormativas/GGIR-MPP89-A1%20-%20Pa%C3%ADses%20Restritos%20e%20Monitorados.pdf"),
        ("⚖️ Minutário Jurídico", "https://confidence1.sharepoint.com/sites/Connect/SitePages/Minut%C3%A1rio-Jur%C3%ADdico.aspx?CT=1751310750721&OR=OWA-NT-Mail&CID=5d1d7d46-a08e-6727-f9fe-4da31b69ce86&web=1")
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

def buscar_conteudos(termo):
    resultados = {}
    termo = termo.lower()
    for secao, itens in conteudos.items():
        filtrados = [(nome, link) for nome, link in itens if termo in nome.lower()]
        if filtrados:
            resultados[secao] = filtrados
    return resultados

st.markdown("<div class='main-container'>", unsafe_allow_html=True)

if selected == "🏠 Início":
    termo = st.text_input(
        "🔎 Buscar relatórios, formulários ou materiais...",
        placeholder="Ex: CAM57, ESG, Market Share",
        key="busca_ativa"
    )

    if not termo:
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

    if termo:
        st.markdown("<div id='resultados'></div>", unsafe_allow_html=True)
        st.markdown("""
            <script>
                const anchor = document.getElementById("resultados");
                if (anchor) { anchor.scrollIntoView({ behavior: "smooth", block: "start" }); }
            </script>
        """, unsafe_allow_html=True)

        resultados = buscar_conteudos(termo)
        st.markdown(f"<div class='section-title'>🔎 Resultados para: <em>{termo}</em></div>", unsafe_allow_html=True)
        if resultados:
            for secao, itens in resultados.items():
                for nome, link in itens:
                    st.markdown(f"""
                        <a href="{link}" target="_blank" style="text-decoration: none;">
                            <div class="custom-card">{nome}
                                <small style='color:#888;font-size:13px;display:block'>{secao}</small>
                            </div>
                        </a>
                    """, unsafe_allow_html=True)
        else:
            st.warning("Nenhum resultado encontrado para a busca.")
    else:
        st.markdown("<div class='section-title'>🏆 Comercial Destaque da Semana</div>", unsafe_allow_html=True)
        st.markdown(f"""<div class="metric-box">
            🌟 <strong>{destaque_comercial['nome']}</strong><br>
            <span style="font-size: 14px; font-weight: normal">{destaque_comercial['motivo']}</span>
        </div>""", unsafe_allow_html=True)

        st.markdown("<div class='section-title'>🗓️ Próximos Eventos</div>", unsafe_allow_html=True)
        for evento in eventos:
            st.markdown(f"- {evento}")

        for secao in conteudos:
            if secao == "📁 KYC e Documentos de Abertura":
                pf_docs = [(nome, link) for nome, link in conteudos[secao] if "PF –" in nome]
                pj_docs = [(nome, link) for nome, link in conteudos[secao] if "PJ –" in nome]

                st.markdown("<div class='section-title'>📁 KYC e Documentos de Abertura</div>", unsafe_allow_html=True)

                if pf_docs:
                    st.markdown("<div class='section-title subtitulo-kyc'>👤 Documentos Pessoa Física (PF)</div>", unsafe_allow_html=True)
                    mostrar_bloco("", pf_docs)
                if pj_docs:
                    st.markdown("<div class='section-title subtitulo-kyc'>🏢 Documentos Pessoa Jurídica (PJ)</div>", unsafe_allow_html=True)
                    mostrar_bloco("", pj_docs)
            else:
                mostrar_bloco(secao, conteudos[secao])

elif selected == "📁 KYC e Documentos de Abertura":
    pf_docs = [(nome, link) for nome, link in conteudos["📁 KYC e Documentos de Abertura"] if "PF –" in nome]
    pj_docs = [(nome, link) for nome, link in conteudos["📁 KYC e Documentos de Abertura"] if "PJ –" in nome]

    st.markdown("<div class='section-title subtitulo-kyc'>👤 Documentos Pessoa Física (PF)</div>", unsafe_allow_html=True)
    mostrar_bloco("", pf_docs)

    st.markdown("<div class='section-title subtitulo-kyc'>🏢 Documentos Pessoa Jurídica (PJ)</div>", unsafe_allow_html=True)
    mostrar_bloco("", pj_docs)

else:
    secao_nome = next((k for k in conteudos.keys() if k == selected), None)
    if secao_nome:
        mostrar_bloco(secao_nome, conteudos[secao_nome])
    else:
        st.warning("Nenhum conteúdo encontrado para esta seção.")

st.markdown("</div>", unsafe_allow_html=True)

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
    .subtitulo-kyc {
        font-size: 22px !important;
        font-weight: 600;
        color: #00205B;
        margin-top: 10px !important;
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

