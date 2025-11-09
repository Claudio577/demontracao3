import streamlit as st
from PIL import Image, ImageChops

# ============================================================
# ⚙️ CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="SmartLog Blockchain — Simulador de Consenso e Fraude",
    layout="wide",
    page_icon="💻"
)

# ============================================================
# 🎨 ESTILO LIMPO E PROFISSIONAL
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
st.markdown("<h1 style='text-align:center; color:#2D8CFF;'>SmartLog Blockchain</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#FF6F61;'>Simulador de Consenso e Detecção de Fraude — Proof of Authority (PoA)</h4>", unsafe_allow_html=True)

st.markdown("""
### Sobre o Desenvolvedor
Sou **estudante e desenvolvedor na área de Inteligência Artificial aplicada (Machine Learning)**,  
atualmente atuando em **projetos de IA Educacional, FinTech e Blockchain Inteligente**.

No **curso em Machine Learning**, desenvolvo **protótipos funcionais** que conectam modelos de IA e sistemas reais,  
utilizando tecnologias como **Streamlit, Firebase, TensorFlow, Web3 e Scikit-Learn**.

O **SmartLog Blockchain** é um **aplicativo educacional e técnico** que demonstra como a **IA e a Blockchain**  
podem ser aplicadas em **sistemas logísticos e auditorias descentralizadas**, simulando **fraudes, consenso e recuperação de dados**.
""")


# ============================================================
# 🚀 SOBRE O PROJETO
# ============================================================
st.markdown("<h2 style='color:#2D8CFF;'>O que é o SmartLog Blockchain</h2>", unsafe_allow_html=True)
st.markdown("""
O **SmartLog Blockchain** é um **simulador visual e interativo** do mecanismo de consenso **Proof-of-Authority (PoA)**,  
utilizado em **redes privadas e logísticas**.

Ele permite que estudantes e profissionais **visualizem e compreendam** o funcionamento interno de uma rede blockchain,  
onde **nós validadores** registram, auditam e sincronizam eventos logísticos, como entregas e rastreamentos.

Com ele, é possível:
- Criar uma **blockchain de entregas** em tempo real;  
- Simular o **consenso entre nós validadores**;  
- Realizar **testes de fraude e recuperação automática de blocos**;  
- Conectar-se a sistemas **Web3 e Firestore** para armazenamento em nuvem.
""")


# ============================================================
# 🖼️ ETAPAS DO PROJETO
# ============================================================
st.markdown("<h2 style='color:#4B7BE5;'>Etapas Visuais do Projeto</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# 1️⃣ Interface principal
img_demo = crop_white_borders("smartlog_demo.png")
with col1:
    if img_demo:
        st.image(img_demo, caption="Interface Principal — Simulação do Consenso PoA", use_column_width=True)
        st.markdown("<p style='color:#444;'>Tela principal mostrando a criação de nós, geração de hashes e execução do consenso distribuído entre validadores.</p>", unsafe_allow_html=True)

# 2️⃣ Auditoria
img_audit = crop_white_borders("smartlog_auditoria.png")
with col2:
    if img_audit:
        st.image(img_audit, caption="Auditoria de Hashes — Antes e Depois", use_column_width=True)
        st.markdown("<p style='color:#444;'>Processo de auditoria automática comparando os hashes dos nós antes e depois do consenso.</p>", unsafe_allow_html=True)


col3, col4 = st.columns(2)

# 3️⃣ Simulação de Fraude
img_fraud = crop_white_borders("smartlog_fraude.png")
with col3:
    if img_fraud:
        st.image(img_fraud, caption="Simulação de Ataque e Recuperação de Nós", use_column_width=True)
        st.markdown("<p style='color:#444;'>Demonstra o cenário de corrupção de dados e a recuperação automática por consenso majoritário.</p>", unsafe_allow_html=True)

# 4️⃣ Firestore
img_fire = crop_white_borders("smartlog_firestore_auditoria.png")
with col4:
    if img_fire:
        st.image(img_fire, caption="Sincronização e Auditoria no Firestore", use_column_width=True)
        st.markdown("<p style='color:#444;'>Painel que salva, carrega e audita blocos da blockchain diretamente no Firebase Firestore.</p>", unsafe_allow_html=True)

# 5️⃣ Web3
img_web3 = crop_white_borders("smartlog_web3_register.png")
if img_web3:
    st.image(img_web3, caption="Registro de Blocos no Contrato SmartLogLedger (Web3)", use_column_width=False)
    st.markdown("""
    <p style='color:#444;'>
    Nesta etapa, o hash validado é enviado ao contrato inteligente <b>SmartLogLedger.sol</b> no Remix Ethereum,  
    registrando o evento <b>BlockRegistered</b> e garantindo rastreabilidade on-chain.
    </p>
    """, unsafe_allow_html=True)


# ============================================================
# 💡 OBJETIVOS
# ============================================================
st.markdown("<h2 style='color:#06D6A0;'>Objetivos e Impacto</h2>", unsafe_allow_html=True)
st.markdown("""
O **SmartLog Blockchain** tem como objetivo **educar e demonstrar** os fundamentos de **blockchain aplicada**  
à **logística inteligente, auditoria de dados e segurança de transações**.

Ele serve como ferramenta de:
- **Aprendizado interativo** para estudantes e profissionais;  
- **Treinamento técnico** em consenso distribuído;  
- **Demonstração prática** para empresas sobre transparência digital.  

Ao integrar IA, blockchain e interfaces gráficas, o projeto mostra como a tecnologia pode  
**detectar fraudes, corrigir inconsistências e garantir confiabilidade** em processos reais.
""")


# ============================================================
# 🧰 TECNOLOGIAS
# ============================================================
st.markdown("<h2 style='color:#F4A261;'>Tecnologias Utilizadas</h2>", unsafe_allow_html=True)
st.markdown("""
- **Python** · Streamlit · Pandas · Hashlib · Requests  
- **Blockchain Simulada (PoA)** com nós independentes  
- **Firebase Firestore** — armazenamento em nuvem  
- **Web3 / Remix Ethereum** — integração educacional  
- **Machine Learning aplicado à auditoria e consenso**
""")


# ============================================================
# 📞 CONTATO
# ============================================================
st.markdown("""
<h3 style='text-align:center; color:#2D8CFF;'>Contato</h3>
<p style='text-align:center;'>
    <b>E-mail:</b> <a href='mailto:claudio.y@hotmail.com'>claudio.y@hotmail.com</a><br>
    <b>WhatsApp:</b> <a href='https://wa.me/5511986364794' target='_blank'>(11) 98636-4794</a>
</p>
""", unsafe_allow_html=True)

st.caption("© 2025 SmartLog Blockchain — Desenvolvido por Claudio Hideki Yoshida | Simulador de Consenso e Fraude (PoA)")
