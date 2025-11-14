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
O **SmartLog Blockchain** é uma ferramenta educacional e técnica desenvolvida para demonstrar, de forma visual,  
como tecnologias modernas como **Blockchain, auditoria automática, Web3 e análise distribuída** podem ser aplicadas a:

- Logística inteligente  
- Cadeias de suprimentos complexas  
- Rastreabilidade ponta a ponta  
- Automação e integração de dados  
- Processos descentralizados  
- Sistemas avançados da **Indústria 4.0**  

O objetivo é conectar **conceitos teóricos** com **implementações reais**, permitindo que estudantes, profissionais  
e empresas compreendam como essas tecnologias podem melhorar segurança, transparência e eficiência operacional.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🚀 SOBRE O SMARTLOG BLOCKCHAIN
# ============================================================
st.markdown("<h2 style='color:#2D8CFF;'>O que é o SmartLog Blockchain</h2>", unsafe_allow_html=True)
st.markdown("""
O **SmartLog Blockchain** simula uma rede permissionada baseada no consenso **Proof-of-Authority (PoA)**,  
usado em ambientes industriais e corporativos que exigem **alta confiabilidade, rastreabilidade e auditoria rápida**.

A solução permite que o usuário visualize:

- A validação de blocos por **nós validadores**  
- A formação de cadeias logísticas auditáveis  
- A checagem de integridade por **hashes criptográficos**  
- A simulação de ataques e recuperação de dados  
- Integração com **Firestore** para auditoria distribuída  
- Registro de blocos em **Web3** e contratos inteligentes  

O simulador mostra na prática como Blockchain reforça a confiança em sistemas críticos da Indústria 4.0.
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
img_web3_explain = crop_white_borders("smartlog_fire.png")  # NOVA IMAGEM


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
        caption="Registro de Blocos em Rede Web3 — Integração Blockchain para Indústria 4.0",
        use_column_width=True
    )


# ============================================================
# NOVA IMAGEM: EXPLICAÇÃO DA ARQUITETURA WEB3
# ============================================================
if img_web3_explain:
    st.image(
        img_web3_explain,
        caption=(
            "Arquitetura Web3 — Funcionamento da Comunicação Descentralizada: "
            "Esta visualização explica como carteiras digitais, transações assinadas "
            "criptograficamente e contratos inteligentes interagem para registrar eventos "
            "logísticos com segurança. "
            "Esse modelo serve como base para soluções de rastreabilidade, IoT industrial, "
            "automação e cadeias de suprimentos inteligentes dentro do ecossistema da Indústria 4.0."
        ),
        use_column_width=True
    )

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 💡 OBJETIVOS E IMPACTO
# ============================================================
st.markdown("<h2 style='color:#06D6A0;'>Objetivos e Impacto</h2>", unsafe_allow_html=True)
st.markdown("""
O **SmartLog Blockchain** demonstra como tecnologias modernas podem fortalecer processos logísticos e industriais,  
garantindo **segurança, transparência, rastreabilidade e automação inteligente**.

A solução permite:
- Auditoria contínua de integridade  
- Detecção de fraudes e anomalias  
- Integração entre sistemas heterogêneos  
- Rastreabilidade ponta a ponta  
- Governança digital baseada em dados  
- Aplicações diretas para **Indústria 4.0**, IoT e automação industrial  

É uma ferramenta ideal para ensino, pesquisa, inovação e desenvolvimento de soluções reais.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🧰 TECNOLOGIAS UTILIZADAS
# ============================================================
st.markdown("<h2 style='color:#F4A261;'>Tecnologias Utilizadas</h2>", unsafe_allow_html=True)
st.markdown("""
- **Python** · Streamlit · Pandas · Hashlib · Requests  
- **Blockchain (PoA)** — Rede permissionada simulada  
- **Firebase Firestore** — Auditoria e sincronização distribuída  
- **Web3 / Contratos Inteligentes** — Registro descentralizado  
- **Governança e Automação para Indústria 4.0**
""")

st.markdown("<hr>", unsafe_allow_html=True)

