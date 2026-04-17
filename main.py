import streamlit as st
from streamlit_option_menu import option_menu
import base64

# ========= CONFIGURAÇÕES DE CONTEÚDO ========= #
mensagem_atualizacao = "🔔 Nova funcionalidade: Dossiê de Planejamento!"

eventos = [
    "🇺🇸 EUA – Reunião do FOMC com decisão de juros & projeções econômicas – 17–18/mar",
    "🇪🇺 Zona do Euro – Reunião do BCE e possível atualização de projeções – meados de mar",
    "🇺🇸 EUA – Payrolls / Relatório de Emprego – 6/mar (1ª sexta-feira)",
    "🇧🇷 Brasil – IPCA (inflação oficial) – meados de mar",
    "🇧🇷 Brasil – Reunião do Copom / decisão de Selic – final de mar",
    "🇨🇳 China – PIB Q1, produção industrial e vendas no varejo – final de mar / início de abr",
    "🇺🇸 EUA – Reunião do FOMC (abril) – 28–29/abr",
    "🇪🇺 Zona do Euro – Reunião do BCE – início de abr"
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
        ("📖 Tutorial Ploomes pt.2 (CRM)", "https://confidence1-my.sharepoint.com/:v:/g/personal/gsmiranda_travelexbank_com_br/IQDhpg6Z3MOdRrIJnwiZQ29wAaD24tGEkwJSVf38oHRVC2w?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=36WR4d")
    ],
    "📊 Dashboards": [
        ("💼 Minha Carteira", "https://app.powerbi.com/links/DaDJ0HIo1A?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&pbi_source=linkShare"),
        ("📌 Gestão Comercial – Market Share", "https://app.powerbi.com/links/VrFjeMY32s"),
        ("📡 Telemetria 🆕", "https://app.powerbi.com/links/DN8VawnQyN"),
        ("🔍 Raio X", "https://app.powerbi.com/links/r_cCxY0hQF"),
        ("📈 Resultados vs Meta", "https://app.powerbi.com/links/GoZ7Yy9gO-?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&pbi_source=linkShare"),
        ("🗂️ Estrutura Comercial", "https://app.powerbi.com/links/8-lwAHL3Bb?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&pbi_source=linkShare"),
        ("📊 DI/DUE", "https://app.powerbi.com/groups/me/reports/8b08b858-8067-4adb-a1a9-a511c981b816/2e5df3a16e8323e9651f?experience=power-bi"),
        ("📊 PLD a vencer", "https://app.powerbi.com/groups/me/reports/e8fdd4f8-5c18-481f-9919-7bfe53373b50/4f457ae5e54901bee4b0")
    ],

     "📄 Formulários": [
    ("⭐ Dossiê de Planejamento", "https://luis-braghin.github.io/dossie_planejamento/", "https://confidence1-my.sharepoint.com/:v:/g/personal/distribuircomercial_travelexbank_com_br/EZ4zCr-4ZotMsqTvM2hO3-IBFaD_4-XRg7WGc7NHdhD8Bw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=QLnj5f"),
    ("📄 Migração de Carteira", "https://forms.office.com/r/W1y1KXzJ5q", "https://confidence1.sharepoint.com/:l:/s/Comercial-Crdito-Jurdico/FNtfu99LrY5AoVj4dU2-XNkBEKe8db21Ws7qDWOdF3ANmw?e=aacYpV"),
    ("📄 Solicitação de CAM57", "https://forms.office.com/r/KZhZEFYVSW", "https://confidence1.sharepoint.com/:l:/s/Comercial-Crdito-Jurdico/FMyX4ZlrIDFMjjE4vDf-S2IBucyUJaW94Uh_aZQN8hHmxg?e=sA3nK8"),
    ("📄 Desconto/Isenção de Tarifa", "https://forms.office.com/r/UMUg6gUg4E", "https://confidence1.sharepoint.com/:l:/s/Comercial-Crdito-Jurdico/FBDTTxephIFFgD_jqSvyqh4BrgyIDOmFXHK_sCsKq39gKA?e=LSYLWE"),
    ("📄 Feedback Comercial", "https://forms.office.com/r/7Ct99i1s77", None),
    ("📄 Formulário de Gatilhos", "https://luis-braghin.github.io/Formulario_Nucleo_Inbound/", None),
    ("📄 Formulário de Indicação - Corretora", "https://forms.office.com/Pages/ResponsePage.aspx?id=_G_t2sm4d0eK42lIfQ7vVp_qK3rzZoxDlPoourIxYWJUQUsyVTFFREZMVTdPVDI2VUo2NU82UERPTS4u", None),
    ("📄 Radar de Oportunidades - Travelex Bank", "https://forms.office.com/r/Z456HfN8Jx", None)
],

    "📚 Materiais/Treinamento": [
        ("📌 Lâmina de Produtos", "https://linktr.ee/travelexbank23"),
        ("📌 Fluxo de isenção de Tarifas", "https://confidence1-my.sharepoint.com/:v:/g/personal/distribuircomercial_travelexbank_com_br/Eem8EpSae-9AlGYavH26a-MBjMPO4vdJ13062YaSFCCS7w?e=tbg0te&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D")
    ],
    "🆕 Área de Onboarding/Cadastro": [
        ("📋 Matriz de Cadastro - GCAD-NOR47-A1", "https://confidence1.sharepoint.com/:x:/r/Compliance/normativas/_layouts/15/doc2.aspx?sourcedoc=%7B10092125-7128-49CC-9D1A-D0EBF63C41E5%7D&file=GCAD-NOR47-A1%20-%20Matriz%20de%20Cadastro.xlsx"),
        ("📥 Painel Onboarding B2B - Cadastro", "https://confidence1.sharepoint.com/sites/PainelOnboarding/_layouts/15/AccessDenied.aspx?Source=https%3A%2F%2Fconfidence1%2Esharepoint%2Ecom%2Fsites%2FPainelOnboarding%2FLists%2FCadastro%2FAllItems%2Easpx"),
        ("🏦 Link para Onboarding - Banco", "https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=_G_t2sm4d0eK42lIfQ7vVkdUQvYVpuBOis8bxXoTLq5UQVUyU1hHTkY1UU5HTEdXNVlNWk02UzRYVi4u"),
        ("💼Link para Onboarding - Corretora", "https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=_G_t2sm4d0eK42lIfQ7vVkdUQvYVpuBOis8bxXoTLq5UQ0tIUlBCN1ZaOVcyNDRKQzNOUERMRVBWRy4u"),
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
        ("PJ – Solicitação Acesso IB", "https://confidence1-my.sharepoint.com/:b:/g/personal/lebraghin_travelexbank_com_br/EUtWaDiB-4JMtN_O2UjytLkBfl04Uo7ihl7ILlVEL0y6KQ?e=cPjgs6"),
        ("PJ - Solicitação para Acesso Boletador - Parceiros", "https://forms.office.com/pages/responsepage.aspx?id=_G_t2sm4d0eK42lIfQ7vVm8BpSowefBPqWPH-QF6aCxUNTRDR0NJWUVCSFBBTkc3M0U0NkMyMEVTOS4u&route=shorturl")
    ],
    "🏢 Área de Crédito": [
        ("🧾 Proposta de Crédito", "https://forms.office.com/r/u4WjFNHZaL"),
        ("🌱 Formulário ESG", "https://forms.office.com/Pages/ResponsePage.aspx?id=_G_t2sm4d0eK42lIfQ7vVnOftT6ZTJtKkIs9SprWJzlUNlNLUjI3MTIyTVZURVI1MFpXN0U5MDk3Sy4u"),
        ("📊 Dashboard Crédito", "https://app.powerbi.com/links/L2YIaQlY_D?ctid=daed6ffc-b8c9-4777-8ae3-69487d0eef56&pbi_source=linkShare&bookmarkGuid=df37e966-fe9a-4757-bdf5-7cb92485c20c")
    ],

    "📣 Marketing": [
        ("📌 Huntag", "https://travelexbank.huntag.app/login?returnurl=%2F")
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
                st.markdown(f"""
                    <a href="{link_list}" target="_blank" style="text-decoration: none;">
                        <div class="acompanhamento-card">📊 Acompanhar</div>
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
