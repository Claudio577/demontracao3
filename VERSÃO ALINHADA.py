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
# 🎨 ESTILO PROFISSIONAL ATUALIZADO
# ============================================================
st.markdown("""
<style>
body {
    background-color: #f8f9fb;
    color: #222;
    font-family: 'Poppins', sans-serif;
}

/* Títulos centralizados */
h1, h2, h3, h4 {
    font-weight: 600;
    text-align: center;
}

/* Parágrafos alinhados à esquerda */
p {
    text-align: left;
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
    margin-top: 1rem;
    margin-bottom: 1.5rem;
}

/* Separador */
hr {
    border: 1px solid #eee;
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# 🧩 FUNÇÃO — CORTAR BORDAS BRANCAS
# ============================================================
def crop_white_borders(img_path, base_width=600):
    try:
        img = Image.open(img_path)
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
st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 👨‍💻 SOBRE O PROJETO
# ============================================================
st.markdown("""
### Sobre o Projeto
O **SmartLog Blockchain** é uma ferramenta educacional e técnica desenvolvida para demonstrar, de forma visual,
como tecnologias modernas como **Blockchain, auditoria automática, Web3 e sistemas distribuídos** podem ser aplicadas a:

- Logística inteligente  
- Cadeias de suprimentos complexas  
- Rastreabilidade ponta a ponta  
- Automação e integração de dados  
- Processos descentralizados  
- Aplicações reais da **Indústria 4.0**  

A solução conecta conceitos teóricos com implementações reais, ajudando profissionais e estudantes
a compreender como essas tecnologias melhoram segurança, transparência e eficiência operacional.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🚀 SOBRE O SMARTLOG BLOCKCHAIN
# ============================================================
st.markdown("<h2 style='color:#2D8CFF;'>O que é o SmartLog Blockchain</h2>", unsafe_allow_html=True)
st.markdown("""
O simulador representa uma rede permissionada baseada no consenso **Proof-of-Authority (PoA)**,
comumente utilizado em indústrias, empresas e sistemas que exigem **alta confiabilidade, auditoria e rastreabilidade**.

O sistema permite visualizar:

- Validação de blocos por **nós autorizados**  
- Formação de cadeias logísticas auditáveis  
- Hashes para checagem de integridade  
- Simulação de ataques e recuperação automática  
- Auditoria distribuída com **Firestore**  
- Registro descentralizado via **Web3** e contratos inteligentes  

Esses recursos mostram como Blockchain reforça a confiança e a automação digital na Indústria 4.0.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🖼️ ETAPAS VISUAIS
# ============================================================
st.markdown("<h2 style='color:#4B7BE5;'>Etapas Visuais do Projeto</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

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
        st.image(img_fraud, caption="Simulação de Ataques e Recuperação Automática")

with col2:
    if img_audit:
        st.image(img_audit, caption="Auditoria de Hashes — Checagem de Integridade")
    if img_fire:
        st.image(img_fire, caption="Sincronização com Firestore — Pipeline Distribuído")

if img_web3:
    st.image(
        img_web3,
        caption="Registro de Blocos em Web3 — Integração Blockchain para Indústria 4.0",
        use_column_width=True
    )

if img_web3_explain:
    st.image(
        img_web3_explain,
        caption=(
            "Arquitetura Web3 — Explicação visual de como contratos inteligentes, transações assinadas "
            "e carteiras digitais interagem para registrar eventos logísticos com segurança. "
            "A base tecnológica usada em rastreabilidade, IoT industrial e automação na Indústria 4.0."
        ),
        use_column_width=True
    )

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 💡 OBJETIVOS E IMPACTO
# ============================================================
st.markdown("<h2 style='color:#06D6A0;'>Objetivos e Impacto</h2>", unsafe_allow_html=True)
st.markdown("""
O **SmartLog Blockchain** demonstra, na prática, como tecnologias emergentes fortalecem sistemas industriais e logísticos
ao garantir **segurança, rastreabilidade, transparência e automação inteligente**.

A solução permite:

- Auditoria contínua  
- Prevenção de fraudes  
- Integração entre sistemas diferentes  
- Rastreabilidade ponta a ponta  
- Governança digital baseada em dados  
- Aplicações diretas na **Indústria 4.0**, IoT e automação  

É ideal para ensino, pesquisa, inovação e desenvolvimento de soluções reais.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🧰 TECNOLOGIAS UTILIZADAS
# ============================================================
st.markdown("<h2 style='color:#F4A261;'>Tecnologias Utilizadas</h2>", unsafe_allow_html=True)
st.markdown("""
- **Python** · Streamlit · Pandas · Hashlib · Requests  
- **Blockchain (PoA)** — Rede permissionada simulada  
- **Firebase Firestore** — Auditoria distribuída  
- **Web3 / Contratos Inteligentes** — Registro descentralizado  
- **Soluções para Automação e Indústria 4.0**
""")

st.markdown("<hr>", unsafe_allow_html=True)

