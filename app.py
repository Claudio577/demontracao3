import streamlit as st
from PIL import Image, ImageChops

# ============================================================
# ⚙️ CONFIGURAÇÃO GERAL DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="SmartLog Blockchain — Simulador de Consenso e Fraude",
    layout="wide",
    page_icon="🧠"
)

# ============================================================
# 🎨 ESTILO VISUAL — CORES E TIPOGRAFIA
# ============================================================
st.markdown("""
<style>
body {
    background-color: #f8f9fb;
    color: #222;
    font-family: 'Poppins', sans-serif;
}
header, [data-testid="stHeader"] {
    display: none;
}
h1, h2, h3, h4 {
    font-weight: 600;
}
.main-card {
    background: white;
    padding: 2.2rem 2.8rem;
    border-radius: 16px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.06);
    margin-top: 1.8rem;
}
a {
    color: #2D8CFF !important;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# 🧩 FUNÇÃO AUXILIAR — REMOVER BORDAS BRANCAS DE IMAGENS
# ============================================================
def crop_white_borders(img_path):
    try:
        img = Image.open(img_path)
        bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
        diff = ImageChops.difference(img, bg)
        bbox = diff.getbbox()
        if bbox:
            img = img.crop(bbox)
        return img
    except:
        return None

# ============================================================
# 🏗️ CABEÇALHO E APRESENTAÇÃO PESSOAL
# ============================================================
st.markdown("<h1 style='text-align:center; color:#2D8CFF;'>SmartLog Blockchain</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#FF5B6A;'>Simulador de Consenso e Detecção de Fraude — Proof of Authority (PoA)</h4>", unsafe_allow_html=True)

st.markdown("""
### 👨‍💻 Sobre o Desenvolvedor
Sou **estudante e desenvolvedor na área de Inteligência Artificial aplicada (Machine Learning)**,  
atualmente atuando em **projetos de IA Educacional, FinTech e Blockchain Inteligente**.

Com base no **curso em Machine Learning**, desenvolvo **protótipos funcionais** que conectam modelos de IA e sistemas reais,  
utilizando tecnologias como **Streamlit, Firebase, TensorFlow, Web3 e Scikit-Learn**.

O **SmartLog Blockchain** é um **aplicativo educacional e técnico** que demonstra como a **IA e a Blockchain**  
podem ser aplicadas em **sistemas logísticos e auditorias descentralizadas**, simulando **fraudes, consenso e recuperação de dados**.
""")

# ============================================================
# 🧠 DESCRIÇÃO DO PROJETO
# ============================================================
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("## 🚀 O que é o SmartLog Blockchain?")
st.markdown("""
O **SmartLog Blockchain** é um **simulador visual e interativo** do mecanismo de consenso **Proof-of-Authority (PoA)**,  
utilizado em **redes privadas e logísticas**.

Ele permite que estudantes e profissionais **visualizem e compreendam** o funcionamento interno de uma rede blockchain,  
onde **nós validadores** registram, auditam e sincronizam eventos logísticos, como entregas, transportes e rastreios.

Com ele, é possível:
- Criar uma **blockchain de entregas** em tempo real;  
- Simular o **consenso entre nós validadores**;  
- Realizar **testes de fraude e recuperação automática de blocos**;  
- Conectar-se a sistemas **Web3 e Firestore** para armazenamento em nuvem.
""")
st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# 🖼️ GALERIA DE IMAGENS — ETAPAS DO PROJETO
# ============================================================

st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("## 🧭 Etapas Visuais do Projeto — Galeria Interativa")

col1, col2 = st.columns(2)

# 1️⃣ Demonstração geral
img_demo = crop_white_borders("smartlog_demo.png")
with col1:
    if img_demo:
        st.image(img_demo, caption="Interface Principal — Simulação do Consenso PoA", use_column_width=True)
        st.markdown("Tela principal do simulador, mostrando a criação de nós, geração de hashes e execução do consenso distribuído entre validadores.")
    else:
        st.warning("Imagem `smartlog_demo.png` não encontrada.")

# 2️⃣ Auditoria
img_audit = crop_white_borders("smartlog_auditoria.png")
with col2:
    if img_audit:
        st.image(img_audit, caption="Auditoria de Hashes — Antes e Depois", use_column_width=True)
        st.markdown("Mostra o processo de auditoria automática, comparando os hashes dos nós antes e depois do consenso.")
    else:
        st.warning("Imagem `smartlog_auditoria.png` não encontrada.")

st.divider()

col3, col4 = st.columns(2)

# 3️⃣ Simulação de fraude
img_fraud = crop_white_borders("smartlog_fraude.png")
with col3:
    if img_fraud:
        st.image(img_fraud, caption="Simulação de Ataque e Recuperação de Nós", use_column_width=True)
        st.markdown("Demonstra a simulação de corrupção de dados e o processo de recuperação automática via consenso majoritário.")
    else:
        st.warning("Imagem `smartlog_fraude.png` não encontrada.")

# 4️⃣ Firestore + Auditoria
img_fire = crop_white_borders("smartlog_firestore_auditoria.png")
with col4:
    if img_fire:
        st.image(img_fire, caption="Sincronização e Auditoria no Firestore", use_column_width=True)
        st.markdown("Interface que permite salvar, carregar e auditar blocos da blockchain diretamente na nuvem usando o Firebase Firestore.")
    else:
        st.warning("Imagem `smartlog_firestore_auditoria.png` não encontrada.")

st.divider()

# 5️⃣ Registro Web3
img_web3 = crop_white_borders("smartlog_web3_register.png")
if img_web3:
    st.image(img_web3, caption="Registro de Blocos no Contrato SmartLogLedger (Web3)", use_column_width=True)
    st.markdown("""
    Nesta etapa, o hash do bloco confirmado no simulador é **enviado ao contrato inteligente SmartLogLedger.sol**
    no **Remix Ethereum**, registrando o evento `BlockRegistered` e garantindo **imparcialidade e rastreabilidade on-chain**.
    """)
else:
    st.warning("Imagem `smartlog_web3_register.png` não encontrada.")

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# 💡 OBJETIVOS E IMPACTO
# ============================================================
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("## 💡 Objetivos e Impacto do Projeto")
st.markdown("""
O **SmartLog Blockchain** tem como objetivo **educar, demonstrar e explorar** os fundamentos de **blockchain aplicada**  
à **logística inteligente, auditoria de dados e segurança de transações**.

Ele serve como ferramenta de:
- **Aprendizado interativo** para estudantes de tecnologia e engenharia;  
- **Treinamento técnico** em blockchain privada e consenso distribuído;  
- **Demonstração prática** para instituições e empresas sobre transparência digital.  

Ao integrar IA, blockchain e interfaces gráficas, o projeto mostra como a tecnologia pode  
**detectar fraudes, corrigir inconsistências e garantir confiabilidade** em processos reais.
""")
st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# 🧰 TECNOLOGIAS UTILIZADAS
# ============================================================
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("## 🧰 Tecnologias Utilizadas")
st.markdown("""
- **Python** · Streamlit · Pandas · Hashlib · Requests  
- **Blockchain Simulada (PoA)** com nós independentes  
- **Firebase Firestore** — armazenamento em nuvem  
- **Web3 / Remix Ethereum** — integração educacional  
- **Machine Learning aplicado à auditoria e consenso**
""")
st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# 📞 CONTATO E RODAPÉ
# ============================================================
st.markdown("""
<h3 style='text-align:center; color:#2D8CFF;'>📩 Contato</h3>
<p style='text-align:center;'>
    <b>E-mail:</b> <a href='mailto:claudio.y@hotmail.com'>claudio.y@hotmail.com</a><br>
    <b>WhatsApp:</b> <a href='https://wa.me/5511986364794' target='_blank'>(11) 98636-4794</a>
</p>
""", unsafe_allow_html=True)

st.caption("© 2025 SmartLog Blockchain — Simulador de Consenso e Fraude | Desenvolvido por Claudio Hideki Yoshida 💡")
