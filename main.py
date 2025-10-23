import streamlit as st
from streamlit_option_menu import option_menu
import base64

# ========= CONFIGURAÇÕES DE CONTEÚDO ========= #
mensagem_atualizacao = "🔔 Atualização: Lançamento nova ferramenta: Dossiê de Planejamento!!!"

eventos = [
    "🇧🇷 Brasil – Bloomberg New Economy / B20 (SP) – 22–23/out",
    "🇺🇸 EUA – CPI de setembro – início de outubro",
    "🇺🇸 EUA – Reunião do FOMC – 28–29/out",
    "🇧🇷 Brasil – Reunião do Copom: decisão da Selic – 5–6/nov"
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
    .acompanhamento-card {
        border-left: 6px solid #4CAF50;
        background: #ffffff;
        padding: 18px 22px;
        border-radius: 12px;
        margin: 12px 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.06);
        transition: transform 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
        text-align: center;
    }
    .acompanhamento-card:hover {
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

with st.sidebar:
    st.image(f"data:image/png;base64,{logo_base64}", width=180)
    selected = option_menu(
        "Seções",
        [
            "🏠 Início",
            "🧬 CRM",
            "📊 Dashboards",
            "📄 Formulários",
            "📚 Materiais/Treinamento",
            "🆕 Área de Onboarding/Cadastro",
            "📁 KYC e Documentos de Abertura",
            "🏢 Área de Crédito",
            "📣 Marketing",
            "🏦 Sistemas do Banco",
            "🔗 Links Úteis"
        ],
        icons=["house", "person-lines-fill", "bar-chart", "file-earmark-text", "book", "person-plus", "folder", "building", "megaphone", "link"],
        menu_icon="cast",
        default_index=0
    )

conteudos = {
    "🧬 CRM": [
        ("🧩 Site da Ploomes (CRM)", "https://app10.ploomes.com/"),
        ("📖 Tutorial Ploomes pt.1 (CRM)", "https://confidence1-my.sharepoint.com/:v:/g/personal/distribuircomercial_travelexbank_com_br/EdC51t32k4FOkGEzVfZ7h5UBeHseoRXjrFvJPaA-hOoFrQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=nDa7cf"),
        ("📖 Tutorial Ploomes pt.2 (CRM)", "https://teams.microsoft.com/l/meetingrecap?driveId=b%21cnl7pCy16E-ESaIuAkbW6G0qFRFxOoRIjNPs12eQszXpmNvYwnzJQ6andzTodky5&driveItemId=01DUVS5QPBUYHJTXGDTVDLECM7BCMUG33Q&sitePath=https%3A%2F%2Fconfidence1-my.sharepoint.com%2F%3Av%3A%2Fg%2Fpersonal%2Fgsmiranda_travelexbank_com_br%2FEeGmDpncw51GsgmfCJlDb3ABrCnZ71752tcKI_Td16Oa1g&fileUrl=https%3A%2F%2Fconfidence1-my.sharepoint.com%2Fpersonal%2Fgsmiranda_travelexbank_com_br%2FDocuments%2FPessoais%2FGrava%25C3%25A7%25C3%25B5es%2F%25F0%259F%259A%2580%2520Lan%25C3%25A7amento%2520do%2520Funil%2520na%2520Ploomes%2520%25C2%25B7%25200608-20250806_160548-Grava%25C3%25A7%25C3%25A3o%2520de%2520Reuni%25C3%25A3o.mp4%3Fweb%3D1&iCalUid=040000008200E00074C5B7101A82E008000000001CB058C10E03DC01000000000000000010000000EC9AA0A67D56A449B0B455F266F1F979&threadId=19%3Ameeting_MmNkZDk0MWItN2E2OC00ZDBjLWJmMjMtOGQwNzU4NWFiNDVk%40thread.v2&organizerId=fe065a87-0012-4e33-acce-6a18a0ba0ab8&tenantId=daed6ffc-b8c9-4777-8ae3-69487d0eef56&callId=d8920d60-e661-4a09-a07e-7a2a6ba1ef7b&threadType=Meeting&meetingType=Scheduled&subType=RecapSharingLink_RecapCore")
    ],
    "📊 Dashboards": [
        ("🧠 Dashboard Unificado (Versão Beta)", "https://app.powerbi.com/links/g0711Nttbb?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&pbi_source=linkShare&bookmarkGuid=35fe9c2f-d75d-40f9-8610-9e5075d7f7c7"),
        ("📌 Gestão Comercial – Market Share", "https://app.powerbi.com/links/VrFjeMY32s"),
        ("📡 Telemetria 🆕", "https://app.powerbi.com/links/DN8VawnQyN"),
        ("🔍 Raio X", "https://app.powerbi.com/links/r_cCxY0hQF"),
        ("📈 Resultados vs Meta", "https://app.powerbi.com/links/5tOpR8JJh4"),
        ("🗂️ Estrutura Comercial", "https://app.powerbi.com/links/8-lwAHL3Bb?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&pbi_source=linkShare"),
        ("📊 DI/DUE", "https://app.powerbi.com/groups/me/reports/8b08b858-8067-4adb-a1a9-a511c981b816/2e5df3a16e8323e9651f?experience=power-bi"),
        ("📊 PLD a vencer", "https://app.powerbi.com/groups/me/reports/e8fdd4f8-5c18-481f-9919-7bfe53373b50/4f457ae5e54901bee4b0")
    ],

    "📄 Formulários": [
    ("⭐ Dossiê de Planejamento", "https://luis-braghin.github.io/dossie_planejamento/", "https://confidence1-my.sharepoint.com/:v:/g/personal/distribuircomercial_travelexbank_com_br/EZ4zCr-4ZotMsqTvM2hO3-IBFaD_4-XRg7WGc7NHdhD8Bw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=QLnj5f"),
    ("📄 Migração de Carteira", "https://forms.office.com/r/W1y1KXzJ5q", "https://confidence1.sharepoint.com/:l:/s/Comercial-Crdito-Jurdico/FNtfu99LrY5AoVj4dU2-XNkBEKe8db21Ws7qDWOdF3ANmw?e=aacYpV"),
    ("📄 Solicitação de CAM57", "https://forms.office.com/r/KZhZEFYVSW", "https://confidence1.sharepoint.com/:l:/s/Comercial-Crdito-Jurdico/FMyX4ZlrIDFMjjE4vDf-S2IBucyUJaW94Uh_aZQN8hHmxg?e=sA3nK8"),
    ("📄 Desconto/Isenção de Tarifa", "https://forms.office.com/r/UMUg6gUg4E", "https://confidence1.sharepoint.com/:l:/s/Comercial-Crdito-Jurdico/FBDTTxephIFFgD_jqSvyqh4BrgyIDOmFXHK_sCsKq39gKA?e=LSYLWE"),
    ("📄 Feedback Comercial", "https://forms.office.com/r/7Ct99i1s77", None)
],

    "📚 Materiais/Treinamento": [
        ("📌 Lâmina de Produtos", "https://linktr.ee/travelexbank23"),
        ("📌 Fluxo de isenção de Tarifas", "https://confidence1-my.sharepoint.com/:v:/g/personal/distribuircomercial_travelexbank_com_br/Eem8EpSae-9AlGYavH26a-MBjMPO4vdJ13062YaSFCCS7w?e=tbg0te&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D")
    ],
    "🆕 Área de Onboarding/Cadastro": [
        ("📋 Matriz de Cadastro - GCAD-NOR47-A1", "https://confidence1.sharepoint.com/:x:/r/Compliance/normativas/_layouts/15/doc2.aspx?sourcedoc=%7B10092125-7128-49CC-9D1A-D0EBF63C41E5%7D&file=GCAD-NOR47-A1%20-%20Matriz%20de%20Cadastro.xlsx"),
        ("📥 Painel Onboarding B2B - Cadastro", "https://confidence1.sharepoint.com/sites/PainelOnboarding/_layouts/15/AccessDenied.aspx?Source=https%3A%2F%2Fconfidence1%2Esharepoint%2Ecom%2Fsites%2FPainelOnboarding%2FLists%2FCadastro%2FAllItems%2Easpx"),
        ("🏦 Link para Onboarding - Banco", "https://forms.office.com/Pages/ResponsePage.aspx?id=_G_t2sm4d0eK42lIfQ7vVlYe_Zie5XdOjKJ73Ib1fSRUQUcyMVgxWFVYVUxSWE1NNEVZNEYyRlJBMi4u"),
        ("💼Link para Onboarding - Corretora", "https://forms.office.com/Pages/ResponsePage.aspx?id=_G_t2sm4d0eK42lIfQ7vVlYe_Zie5XdOjKJ73Ib1fSRUNkpQTTVGVE9JWktDV1dTV0gzSlg3Uk5SQS4u"),
        ("🏦 Painel de Acompanhamento de Onboarding - Banco", "https://confidence1.sharepoint.com/sites/PainelOnboarding/Lists/Cadastro/AllItems.aspx"),
        ("💼 Painel de Acompanhamento de Onboarding - Corretora", "https://confidence1.sharepoint.com/sites/PainelOnboarding/Lists/Corretora/AllItems.aspx?viewpath=%2Fsites%2FPainelOnboarding%2FLists%2FCorretora%2FAllItems.aspx"),
        ("📂 Cadastro de Clientes – Status & Pendências", "https://confidence1.sharepoint.com/:l:/r/sites/CadastroB2B/_layouts/15/DashboardRedirectPage.aspx?id=%2Fsites%2FCadastroB2B%2FDocumentos%20Compartilhados%2FGeneral%2FLista%20de%20status%20de%20abertura&web=1")
    ],
    "📁 KYC e Documentos de Abertura": [
        ("📄 PF – Modelo de Declaração de Recursos", "https://confidence1.sharepoint.com/Compliance/normativas/DocumentosNormativas/GCAD-NOR47-F51%20-%20Declara%C3%A7%C3%A3o%20de%20Recursos.docx"),
        ("📄 PF – Declaração Conta Recursos Próprios", "https://confidence1.sharepoint.com/Compliance/normativas/DocumentosNormativas/GCAD-NOR47-F14%20-%20Declara%C3%A7%C3%A3o%20Conta%20Recursos%20Pr%C3%B3prios.docx"),
        ("📄 PJ – Modelo de Atestado de Capacidade Financeira", "https://confidence1.sharepoint.com/Compliance/normativas/DocumentosNormativas/GCAD-NOR47-F59%20-%20Atestado%20de%20Capacidade%20Financeira.docx"),
        ("📄 PJ – Modelo de Declaração de Desembolso de Recursos Próprios", "https://confidence1.sharepoint.com/Compliance/normativas/DocumentosNormativas/GCAD-NOR47-F10%20-%20Desembolso%20de%20Recursos%20Pr%C3%B3prios.docx"),
        ("📄 PJ – Modelo de Declaração de Recursos PJ", "https://confidence1.sharepoint.com/Compliance/normativas/DocumentosNormativas/GCAD-NOR47-F52%20-%20Declara%C3%A7%C3%A3o%20de%20Recursos%20PJ.docx"),
        ("📄 PJ – Matriz de Atribuição e Alçada", "https://confidence1.sharepoint.com/Compliance/normativas/DocumentosNormativas/GCAD-NOR47-F11%20-%20Matriz%20de%20Atribui%C3%A7%C3%A3o%20e%20Al%C3%A7ada.xlsx"),
        ("📄 PJ – Declaração de Natureza de Transação", "https://confidence1.sharepoint.com/Compliance/normativas/DocumentosNormativas/GCAD-NOR47-F53%20-%20Declara%C3%A7%C3%A3o%20de%20Natureza%20de%20Transa%C3%A7%C3%A3o.docx")
    ],
    "🏢 Área de Crédito": [
        ("💰 Lista de Aprovação de Produtos", "https://confidence1.sharepoint.com/:x:/s/Comercial-Crdito-Jurdico/EaCLs-DqSSxNlH-20r_62zYB3YLAbZLRrLnSbEgAJSFJIw?e=VHJyW9"),
        ("📌 Alçada das ORFs e Comitês", "https://confidence1.sharepoint.com/:x:/s/Comercial-Crdito-Jurdico/EeSZv6cKbDpGk5OqApq0_a0BmDH0YCzqm1OEVG_2bxCdgg?e=5P9bbE"),
        ("📊 Estrutura de Comitê", "https://confidence1.sharepoint.com/:f:/r/sites/Comercial-Crdito-Jurdico/Documentos%20Compartilhados/Estrutura%20de%20Comit%C3%AA?csf=1&web=1&e=fADDdn"),
        ("📝 Template de Parecer de Crédito PJ", "https://confidence1.sharepoint.com/sites/Comercial-Crdito-Jurdico/Documentos%20Compartilhados/An%C3%A1lise%20de%20Cr%C3%A9dito/Parecer%20Cr%C3%A9dito%20-%20V52%20-%20APROVADO%20(20-09-2024).xlsx"),
        ("📝 Template de Parecer de Crédito PF", "https://confidence1.sharepoint.com/sites/Comercial-Crdito-Jurdico/Documentos%20Compartilhados/An%C3%A1lise%20de%20Cr%C3%A9dito/Parecer%20Cr%C3%A9dito%20PF%20-%20Vers%C3%A3o%2003%20(17-08-2023).xlsx")
    ],
    "📣 Marketing": [
        ("🏢 Apresentações Institucionais", "https://confidence1.sharepoint.com/:f:/r/sites/MarcaComunicacao/Documentos%20Compartilhados/General/Apresenta%C3%A7%C3%B5es%20Institucionais%20-%20Modelo%20Atual?csf=1&web=1&e=vgr5UO"),
        ("🎨 Materiais de Marketing", "https://confidence1.sharepoint.com/:f:/r/sites/MarcaComunicacao/Documentos%20Compartilhados/General/Materiais%20de%20Marketing?csf=1&web=1&e=2Xg9g6")
    ],
    "🏦 Sistemas do Banco": [
        ("💳 TAC", "https://www.sisgef.net.br/sisfundacao.php?cd_org=3&cd_cliente=3&cd_banco=366&ds_banco=TRAVELEX%20BANCO%20DE%20CAMBIO"),
        ("🖥️ GEF", "https://www.sisgef.net.br/menuadmin.php")
    ],
    "🔗 Links Úteis": [
        ("⚠️ BFF – Formulário Abuso de Mercado", "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4d0eK42lIfQ7vVlYe_Zie5XdOjKJ73Ib1fSRUNEVWMkRYRVIySzFBQlY3VjkyMjdYUVZQRC4u"),
        ("📞 Ramal Corporativo", "https://outlook.office365.com/owa/calendar/RamalCorporativo@travelexbank.onmicrosoft.com/bookings/"),
        ("📞 Gestão de Pagamentos", "https://outlook.office365.com/owa/calendar/GestodePagamentos@travelexbank.onmicrosoft.com/bookings/"),
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

def mostrar_formularios_com_tracking(titulo, lista):
    """Exibe formulários com link de acompanhamento ao lado"""
    if titulo:
        st.markdown(f"<div class='section-title'>{titulo}</div>", unsafe_allow_html=True)
    
    for nome, link_form, link_list in lista:
        if link_list:  # Se tem link de acompanhamento
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"""
                    <a href="{link_form}" target="_blank" style="text-decoration: none;">
                        <div class="custom-card">{nome}</div>
                    </a>
                """, unsafe_allow_html=True)
            with col2:
                # Define o texto do botão baseado no nome do formulário
                texto_botao = "🎥 Video-Aula" if "Dossiê de Planejamento" in nome else "📊 Acompanhar"
                st.markdown(f"""
                    <a href="{link_list}" target="_blank" style="text-decoration: none;">
                        <div class="acompanhamento-card">{texto_botao}</div>
                    </a>
                """, unsafe_allow_html=True)
        else:  # Se não tem link de acompanhamento, exibe só o formulário normal
            st.markdown(f"""
                <a href="{link_form}" target="_blank" style="text-decoration: none;">
                    <div class="custom-card">{nome}</div>
                </a>
            """, unsafe_allow_html=True)

def buscar_conteudos(termo):
    resultados = {}
    termo = termo.lower()
    for secao, itens in conteudos.items():
        if secao == "📄 Formulários":
            filtrados = [(nome, link, link_list) for nome, link, link_list in itens if termo in nome.lower()]
        else:
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
                if secao == "📄 Formulários":
                    mostrar_formularios_com_tracking("", itens)
                else:
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
        st.markdown("<div class='section-title'>🏆 Comercial Destaque (Semana Geral) </div>", unsafe_allow_html=True)
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
            elif secao == "📄 Formulários":
                mostrar_formularios_com_tracking(secao, conteudos[secao])
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
        if secao_nome == "📄 Formulários":
            mostrar_formularios_com_tracking(secao_nome, conteudos[secao_nome])
        else:
            mostrar_bloco(secao_nome, conteudos[secao_nome])
    else:
        st.warning("Nenhum conteúdo encontrado para esta seção.")

st.markdown("</div>", unsafe_allow_html=True)
