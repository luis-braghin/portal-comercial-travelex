# Portal Comercial Travelex

Portal interno do **Travelex Bank** que centraliza recursos, links, formulários e documentos para a equipe comercial. Construído com Python e Streamlit.

## Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.8+ |
| Framework web | Streamlit |
| Navegação | streamlit-option-menu |
| Animações | streamlit-lottie |
| Tema | Customizado via `.streamlit/config.toml` |

## Como instalar

```bash
git clone <URL_DO_REPOSITORIO>
cd portal-comercial-travelex
pip install -r requirements.txt
```

## Como rodar

```bash
streamlit run main.py
```

O portal abre automaticamente em `http://localhost:8501`.

## Funcionalidades principais

- **Busca global** — pesquisa rápida entre todos os recursos disponíveis na tela inicial
- **CRM (Ploomes)** — acesso direto ao CRM e tutoriais em vídeo
- **Dashboards Power BI** — Market Share, Telemetria, Raio X, Resultados vs Meta, DI/DUE, PLD a vencer, entre outros
- **Formulários** — Dossiê de Planejamento, Migração de Carteira, CAM57, Desconto/Isenção de Tarifa, Feedback Comercial, Gatilhos, Indicação (Corretora); formulários com link de acompanhamento embutido
- **Materiais/Treinamento** — Lâmina de Produtos e fluxos operacionais
- **Onboarding/Cadastro** — Matriz de cadastro, painéis de acompanhamento (Banco e Corretora), links de onboarding e aprovações JIRA
- **KYC e Documentos de Abertura** — documentos separados por Pessoa Física (PF) e Pessoa Jurídica (PJ): KYC, Fichas Cadastrais, Abertura de Conta-Corrente, Acesso IB
- **Área de Crédito** — Proposta de Crédito, Formulário ESG, Dashboard de Crédito
- **Marketing** — Huntag
- **Sistemas do Banco** — Change, SOCC, MATERA, Qulture Rocks, Click Sign
- **Links Úteis** — Radar COMEX, Comprovante PJ, Países Restritos, Minutário Jurídico
- **Destaque Comercial** — exibe o colaborador em destaque da semana na tela inicial
- **Próximos Eventos** — calendário de eventos macro (FOMC, Copom, IPCA, etc.) visível na home

## Estrutura de pastas

```
portal-comercial-travelex/
├── main.py                 # Aplicação principal Streamlit
├── requirements.txt        # Dependências Python
├── logo_travelex.png       # Logo do Travelex Bank
├── README.md
├── CLAUDE.md               # Instruções do projeto para o Claude Code
├── .devcontainer/
│   └── devcontainer.json   # Configuração de dev container (GitHub Codespaces)
└── .streamlit/
    └── config.toml         # Tema e configurações do Streamlit
```

## Variáveis de ambiente

Nenhuma variável de ambiente é necessária. Todos os links e conteúdos estão definidos diretamente em `main.py`.

## Status

**Produção** — Portal em uso pela equipe comercial do Travelex Bank.
