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
# 🎨 ESTILO PROFISSIONAL (Títulos centralizados + texto à esquerda)
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
    text-align: left;
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
st.markdown("<h4 style='color:#FF6F61;'>Simulador de Consenso e Detecção de Fraude — Proof of Authority (PoA)</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 👨‍💻 SOBRE O DESENVOLVEDOR
# ============================================================
st.markdown("""
### Sobre o Desenvolvedor
Sou **estudante e desenvolvedor na área de Inteligência Artificial aplicada (Machine Learning)**,  
atuando em **projetos de IA Educacional, FinTech e Blockchain Inteligente**.

Durante o curso de **Machine Learning**, desenvolvo **protótipos funcionais** que conectam IA e sistemas reais,  
utilizando **Streamlit, Firebase, TensorFlow, Web3 e Scikit-Learn**.

O **SmartLog Blockchain** é um **aplicativo educacional e técnico** que demonstra como a **IA e a Blockchain**  
podem ser aplicadas em **sistemas logísticos e auditorias descentralizadas**, simulando **fraudes, consenso e recuperação de dados**.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🚀 SOBRE O PROJETO
# ============================================================
st.markdown("<h2 style='color:#2D8CFF;'>O que é o SmartLog Blockchain</h2>", unsafe_allow_html=True)
st.markdown("""
O **SmartLog Blockchain** é um **simulador visual e interativo** do mecanismo de consenso **Proof-of-Authority (PoA)**,  
utilizado em **redes privadas e logísticas**.

Ele permite que estudantes e profissionais **visualizem e compreendam** o funcionamento de uma rede blockchain,  
onde **nós validadores** registram, auditam e sincronizam eventos logísticos.

Com ele, é possível:
- Criar uma **blockchain de entregas** em tempo real;  
- Simular o **consenso entre nós validadores**;  
- Executar **testes de fraude e recuperação automática de blocos**;  
- Integrar com **Web3 e Firestore** para armazenamento em nuvem e auditoria.
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
img_web3_explain = crop_white_borders("smartlog_fire.png")   # NOVA IMAGEM AQUI!

with col1:
    if img_demo:
        st.image(img_demo, caption="Interface Principal — Simulação do Consenso PoA")
    if img_fraud:
        st.image(img_fraud, caption="Simulação de Ataque e Recuperação de Nós")

with col2:
    if img_audit:
        st.image(img_audit, caption="Auditoria de Hashes — Antes e Depois")
    if img_fire:
        st.image(img_fire, caption="Sincronização e Auditoria no Firestore")

if img_web3:
    st.image(img_web3, caption="Registro de Blocos no Contrato SmartLogLedger (Web3)", use_column_width=True)

# ============================================================
# 🆕 IMAGEM EXTRA — EXPLICAÇÃO SOBRE WEB3
# ============================================================
if img_web3_explain:
    st.image(
        img_web3_explain,
        caption=(
            "Arquitetura Web3 — Explicação visual de como contratos inteligentes, "
            "carteiras digitais e transações assinadas registram eventos com segurança. "
            "Esse fluxo demonstra os elementos essenciais da Web3 usados para auditoria, "
            "rastreabilidade e integração com sistemas blockchain."
        ),
        use_column_width=True
    )

st.markdown("<hr>", unsafe_allow_html=True)

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

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🧰 TECNOLOGIAS
# ============================================================
st.markdown("<h2 style='color:#F4A261;'>Tecnologias Utilizadas</h2>", unsafe_allow_html=True)
st.markdown("""
- **Python** · Streamlit · Pandas · Hashlib · Requests  
- **Blockchain Simulada (PoA)**  
- **Firebase Firestore** — armazenamento e auditoria  
- **Web3 / Remix Ethereum** — integração educacional  
- **Machine Learning aplicado à auditoria**
""")

st.markdown("<hr>", unsafe_allow_html=True)

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
