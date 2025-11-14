import streamlit as st
from PIL import Image, ImageChops

# ============================================================
# ⚙️ CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="SmartLog Blockchain — Auditoria, Consenso e Indústria 4.0",
    layout="wide",
    page_icon="💻"
)

# ============================================================
# 🎨 ESTILO PROFISSIONAL — TÍTULOS CENTRALIZADOS + TEXTO À ESQUERDA (SEM HR)
# ============================================================
st.markdown("""
<style>
/* Fundo e Fonte */
body {
    background-color: #f8f9fb;
    color: #222;
    font-family: 'Poppins', sans-serif;
}

/* TITULOS CENTRALIZADOS */
h1, h2, h3, h4 {
    font-weight: 600;
    text-align: center !important;
    margin-bottom: 0.5rem; /* Ajuste para compensar a remoção do HR */
}

/* PARÁGRAFOS E LISTAS À ESQUERDA */
p, li, ul {
    text-align: left !important;
    margin-left: auto;
    margin-right: auto;
    max-width: 900px; /* EVITA TEXTO MUITO LARGO, FICA PREMIUM */
    margin-bottom: 1.25rem; /* Espaçamento padrão */
}

/* Links */
a {
    color: #2D8CFF !important;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}

/* Imagens */
img {
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    margin-top: 1.5rem;
    margin-bottom: 2rem;
}

/* Separador (HR) - Removido */
/* hr {
    border: 1px solid #eee;
    margin: 2.5rem 0;
} */
</style>
""", unsafe_allow_html=True)


# ============================================================
# 🧩 FUNÇÃO — CORTAR BORDAS BRANCAS
# ============================================================
def crop_white_borders(img_path, base_width=650):
    try:
        img = Image.open(img_path)
        # Tenta pegar a cor do pixel (0,0) para usar como fundo
        bg = Image.new(img.mode, img.size, img.getpixel((0, 0))) 
        diff = ImageChops.difference(img, bg)
        bbox = diff.getbbox()
        if bbox:
            img = img.crop(bbox)
        w_percent = base_width / float(img.size[0])
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((base_width, h_size), Image.Resampling.LANCZOS)
        return img
    except:
        return None


# ============================================================
# 🧠 CABEÇALHO PRINCIPAL
# ============================================================
st.markdown("<h1 style='color:#2D8CFF;'>SmartLog Blockchain</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color:#FF6F61;'>Simulador de Consenso, Auditoria e Blockchain para Indústria 4.0</h4>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True) # Espaçamento maior após o cabeçalho


# ============================================================
# 👨‍💻 SOBRE O PROJETO
# ============================================================
st.markdown("<h2>Sobre o Projeto</h2>", unsafe_allow_html=True)

st.markdown("""
O **SmartLog Blockchain** é uma ferramenta educacional e técnica desenvolvida para demonstrar, de forma visual, 
como tecnologias modernas como **Blockchain, auditoria automática, Web3 e sistemas distribuídos** podem ser aplicadas em:

- Logística inteligente
- Cadeias de suprimentos complexas
- Rastreabilidade ponta a ponta
- Automação e integração de dados
- Processos descentralizados
- Aplicações reais da **Indústria 4.0**
""")

st.markdown("<br><br>", unsafe_allow_html=True) # Espaçamento de seção


# ============================================================
# 🚀 SOBRE O SMARTLOG BLOCKCHAIN
# ============================================================
st.markdown("<h2 style='color:#2D8CFF;'>O que é o SmartLog Blockchain</h2>", unsafe_allow_html=True)

st.markdown("""
O simulador representa uma rede permissionada baseada no consenso **Proof-of-Authority (PoA)**, 
utilizado em ambientes industriais e logísticos que exigem **alta confiabilidade, segurança e auditoria automática**.

Ele permite visualizar:

- Validação de blocos por nós autorizados
- Hashes de integridade
- Simulações de ataques e recuperação automática
- Auditoria distribuída com Firestore
- Registro descentralizado usando **Web3** e contratos inteligentes
""")

st.markdown("<br><br>", unsafe_allow_html=True) # Espaçamento de seção


# ============================================================
# 🖼️ ETAPAS VISUAIS DO PROJETO
# ============================================================
st.markdown("<h2 style='color:#4B7BE5;'>Etapas Visuais do Projeto</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# É essencial que os arquivos de imagem ('smartlog_demo.png', etc.) estejam no diretório correto.
img_demo = crop_white_borders("smartlog_demo.png")
img_audit = crop_white_borders("smartlog_auditoria.png")
img_fraud = crop_white_borders("smartlog_fraude.png")
img_fire = crop_white_borders("smartlog_firestore_auditoria.png")
img_web3 = crop_white_borders("smartlog_web3_register.png")
img_web3_explain = crop_white_borders("smartlog_fire.png")

with col1:
    if img_demo:
        st.image(img_demo, caption="Consenso PoA — Formação e Validação de Blocos")

    if img_fraud:
        st.image(
            img_fraud,
            caption="Simulação de Ataques — Detecção e recuperação automática de inconsistências."
        )

with col2:
    if img_audit:
        st.image(img_audit, caption="Auditoria de Hashes — Antes e Depois")

    if img_fire:
        st.image(img_fire, caption="Sincronização com Firestore — Auditoria distribuída")

if img_web3:
    st.image(
        img_web3,
        caption="Registro de Blocos em Web3 — Integração Blockchain para Indústria 4.0",
        use_column_width=True
    )

if img_web3_explain:
    st.image(
        img_web3_explain,
        caption="Arquitetura Web3 — Como contratos inteligentes registram eventos com segurança.",
        use_column_width=True
    )

st.markdown("<br><br>", unsafe_allow_html=True) # Espaçamento de seção


# ============================================================
# 💡 OBJETIVOS E IMPACTO
# ============================================================
st.markdown("<h2 style='color:#06D6A0;'>Objetivos e Impacto</h2>", unsafe_allow_html=True)

st.markdown("""
O SmartLog Blockchain demonstra, na prática, como tecnologias emergentes fortalecem:

- Auditoria contínua
- Rastreabilidade confiável
- Detecção de fraudes
- Governança digital
- Automação na **Indústria 4.0**

É ideal para ensino, pesquisa, inovação e experimentação.
""")

st.markdown("<br><br>", unsafe_allow_html=True) # Espaçamento de seção


# ============================================================
# 🧰 TECNOLOGIAS
# ============================================================
st.markdown("<h2 style='color:#F4A261;'>Tecnologias Utilizadas</h2>", unsafe_allow_html=True)

st.markdown("""
- Python — Streamlit — Pandas — Hashlib
- Blockchain (PoA) — Auditoria distribuída
- Firebase Firestore
- Web3 · Contratos Inteligentes
- Soluções para Indústria 4.0
""")

st.markdown("<br><br><br>", unsafe_allow_html=True) # Espaço final para melhor acabamento
""")

st.markdown("<hr>", unsafe_allow_html=True)

