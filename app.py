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
# ⚙️ FUNCIONALIDADES E SIMULAÇÃO
# ============================================================
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("## ⚙️ Funcionalidades Principais")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - Criação de **nós blockchain** simulados (Node_A, Node_B, Node_C)  
    - Geração de **hashes criptográficos SHA-256**  
    - Simulação de **consenso PoA (Proof-of-Authority)**  
    - Votação entre nós e validação de blocos  
    - **Auditoria automática de integridade**  
    - Armazenamento opcional em **Firebase Firestore**  
    """)

with col2:
    st.markdown("""
    - **Simulação de ataque** (corrupção de dados e hashes)  
    - Detecção e recuperação de nós corrompidos  
    - Integração opcional com **Web3 (Remix / Ethereum)**  
    - Painel interativo de logs e auditoria  
    - Exportação de blocos e eventos logísticos  
    """)

st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# 🖥️ IMAGEM OU DIAGRAMA
# ============================================================
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("## 🖥️ Visualização e Interface Didática")

img_blockchain = crop_white_borders("smartlog_demo.png")
if img_blockchain:
    st.image(img_blockchain, caption="Interface do SmartLog Blockchain — Consenso PoA em ação", use_column_width=True)
else:
    st.info("Você pode adicionar uma imagem chamada `smartlog_demo.png` para ilustrar a interface do simulador.")

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
