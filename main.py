import streamlit as st
import base64

st.set_page_config(page_title="Portal Comercial Travelex", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_path = "logo_travelex.png"
logo_base64 = get_base64_of_bin_file(logo_path)

st.markdown(f"""
<style>
    html {{
        scroll-behavior: smooth;
    }}
    .sidebar-links a {{
        color: white;
        display: block;
        padding: 8px 0;
        text-decoration: none;
    }}
    .sidebar-links a:hover {{
        text-decoration: underline;
    }}
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
    .search-button-container {{
        margin-top: 26px;
    }}
    .footer {{
        margin-top: 40px;
        font-size: 12px;
        color: #6c757d;
        text-align: center;
    }}
</style>
""", unsafe_allow_html=True)

# Sidebar
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

# Cabeçalho e Notificação
st.markdown(f"""
<div id="inicio" style='background-color: #ffffff; padding: 30px 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.05); display: flex; align-items: center;'>
    <img src='data:image/png;base64,{logo_base64}' width='60' style='margin-right: 20px;'>
    <div>
        <h1 style='margin-bottom: 0px; color: #002B5B;'>Central de Planejamento Comercial</h1>
        <p style='margin-top: 5px; color: #6c757d;'>Travelex Bank · Tudo o que você precisa em um só lugar.</p>
    </div>
</div>
<div style='margin-top: 20px; background-color: #e3f2fd; padding: 10px; border-radius: 8px;'>
    🔔 Atualização: Adicionamos o novo relatório de Telemetria!
</div>
""", unsafe_allow_html=True)

# Meta do Mês
st.markdown("""
<h3>📉 Meta do Mês</h3>
<div style='background-color: #001f5b; color: white; padding: 30px; border-radius: 12px; text-align: center;'>
    <div style='font-size: 32px;'>🎯 75%</div>
    <div style='margin-top: 10px;'>Meta atingida até agora</div>
</div>
""", unsafe_allow_html=True)

# Próximos Eventos
st.markdown("""
<h3>📅 Próximos Eventos</h3>
<ul>
    <li>🔔 Reunião Trimestral - 20 de Junho</li>
    <li>🧠 Workshop Estratégico - 27 de Junho</li>
    <li>📊 Atualização Power BI - 01 de Julho</li>
</ul>
""", unsafe_allow_html=True)

# Rodapé
st.markdown("""
<div class="footer">
    Desenvolvido pela área de Planejamento Comercial (Gestão Felipe Von Pressentin) – Travelex Bank<br>
    🔒 Acesso: somente uso interno | 📋 Dados de uso sendo monitorados | 📈 Total de acessos: <b>23</b>
</div>
""", unsafe_allow_html=True)

# (Restante das seções como Dashboards, Formulários, Materiais, etc, deve seguir o mesmo padrão anterior com o fix aplicado nas seções.)
