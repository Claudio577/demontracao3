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
# 🎨 ESTILO PROFISSIONAL E CENTRALIZADO
# ============================================================
st.markdown("""
<style>
body {
    background-color: #f8f9fb;
    color: #222;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3, h4 {
    font-weight: 600;
    text-align: center;
}
p {
    text-align: justify;
}
a {
    color: #2D8CFF !important;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
img {
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    margin-top: 1rem;
    margin-bottom: 1.5rem;
}
hr {
    border: 1px solid #eee;
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# 🧩 FUNÇÃO AUXILIAR — CORTAR BORDAS BRANCAS
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
# 👨‍💻 SOBRE O DESENVOLVEDOR
# ============================================================
st.markdown("""
### Sobre o Projeto  
O **SmartLog Blockchain** é uma ferramenta educacional e técnica desenvolvida para demonstrar, de forma clara e visual,  
como tecnologias modernas como **Blockchain, auditoria automática, análise distribuída e Web3** podem ser aplicadas em:

- Logística inteligente  
- Cadeias de suprimentos automatizadas  
- Rastreabilidade avançada  
- Sistemas críticos da **Indústria 4.0**  
- Auditoria de integridade de dados  
- Processos descentralizados  

O projeto foi criado com foco em inovação tecnológica aplicada, conectando **conceitos teóricos** com **sistemas reais**,  
podendo ser utilizado para ensino, demonstração, consultoria técnica ou prova de conceito.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🚀 SOBRE O SMARTLOG BLOCKCHAIN
# ============================================================
st.markdown("<h2 style='color:#2D8CFF;'>O que é o SmartLog Blockchain</h2>", unsafe_allow_html=True)
st.markdown("""
O **SmartLog Blockchain** simula uma rede baseada no mecanismo de consenso **Proof-of-Authority (PoA)**,  
usado em redes permissionadas e ambientes industriais que exigem **alta confiabilidade e auditoria rápida**.

Ele permite visualizar:

- O comportamento dos **nós validadores**  
- A criação de blocos logísticos em tempo real  
- A checagem de integridade via **hashes e auditorias automáticas**  
- Ataques simulados e processos de **recuperação de inconsistências**  
- A interação com **Firestore** e **redes Web3**, refletindo pipelines de dados reais da Indústria 4.0  

O objetivo é demonstrar como Blockchain pode trazer **transparência, segurança e rastreabilidade**  
para sistemas logísticos e industriais.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🖼️ ETAPAS DO PROJETO
# ============================================================
st.markdown("<h2 style='color:#4B7BE5;'>Etapas Visuais do Projeto</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

img_demo = crop_white_borders("smartlog_demo.png")
img_audit = crop_white_borders("smartlog_auditoria.png")
img_fraud = crop_white_borders("smartlog_fraude.png")
img_fire = crop_white_borders("smartlog_firestore_auditoria.png")
img_web3 = crop_white_borders("smartlog_web3_register.png")

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
    st.image(img_web3, caption="Registro de Blocos em Rede Web3 — Integração para Indústria 4.0", use_column_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 💡 OBJETIVOS E IMPACTO
# ============================================================
st.markdown("<h2 style='color:#06D6A0;'>Objetivos e Impacto</h2>", unsafe_allow_html=True)
st.markdown("""
O projeto demonstra como **Blockchain e sistemas distribuídos** podem:

- Aumentar a confiança em processos logísticos  
- Melhorar rastreabilidade ponta a ponta  
- Automatizar auditorias de integridade  
- Integrar múltiplas fontes de dados  
- Prevenir fraudes e anomalias  
- Servir como base tecnológica para **Indústria 4.0**, IoT e automação avançada  

O SmartLog é uma ferramenta prática para capacitação, pesquisa e desenvolvimento de soluções reais.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🧰 TECNOLOGIAS UTILIZADAS
# ============================================================
st.markdown("<h2 style='color:#F4A261;'>Tecnologias Utilizadas</h2>", unsafe_allow_html=True)
st.markdown("""
- **Python** · Streamlit · Pandas · Hashlib · Requests  
- **Blockchain (PoA)** — Simulação de rede permissionada  
- **Firebase Firestore** — Sincronização e auditoria distribuída  
- **Web3 / Remix Ethereum** — Registro descentralizado  
- **Automação e Integridade de Dados para Indústria 4.0**
""")

st.markdown("<hr>", unsafe_allow_html=True)

