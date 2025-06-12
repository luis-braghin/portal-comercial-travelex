# Notificação
st.markdown("""
<div style="background-color: #e6f0fb; border-radius: 8px; padding: 10px 20px; margin-top: 20px;">
    🔔 Atualização: Adicionamos o novo relatório de Telemetria!
</div>
""", unsafe_allow_html=True)

# Barra de busca
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

# Espaçamento
st.markdown("<div style='margin-top: 25px'></div>", unsafe_allow_html=True)

# Meta do mês (discreta, menor, "X%")
st.markdown("""
<h3 style='color: #002B5B; font-size: 18px;'>📉 Meta do Mês</h3>
<div style="background-color: #E8EEF7; padding: 14px; border-radius: 10px; text-align: center; color: #002B5B; font-size: 16px;">
    🎯 X%<br>
    <span style="font-size: 13px;">Meta atingida até agora</span>
</div>
""", unsafe_allow_html=True)

# Espaçamento
st.markdown("<div style='margin-top: 25px'></div>", unsafe_allow_html=True)

# Próximos eventos
st.markdown("""
<h3 style='color: #002B5B; font-size: 18px;'>🗓️ Próximos Eventos</h3>
<ul style='line-height: 1.7; font-size: 15px;'>
    <li>🔔 Reunião Trimestral - 20 de Junho</li>
    <li>🧠 Workshop Estratégico - 27 de Junho</li>
    <li>📊 Atualização Power BI - 01 de Julho</li>
</ul>
""", unsafe_allow_html=True)
