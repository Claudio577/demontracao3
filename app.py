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
# 🎨 ESTILO — Títulos centralizados + parágrafos à esquerda
# ============================================================
st.markdown("""
<style>
body {
    background-color: #f8f9fb;
    color: #222;
    font-family: 'Poppins', sans-serif;
}

/* Títulos (mas usaremos inline também para garantir o alinhamento) */
h1, h2, h3, h4 {
    font-weight: 600;
}

/* Parágrafos padrão à esquerda */
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

/* Linha */
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
# 🧠 CABEÇALHO PRINCIPAL (centralizado corretamente)
# ============================================================
st.markdown("<h1 style='color:#2D8CFF; text-align:center;'>SmartLog Blockchain</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color:#FF6F61; text-align:center;'>Simulador de Consenso e Detecção de Fraude — Proof of Authority (PoA)</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)


# ============================================================
# 👨‍💻 SOBRE O DESENVOLVEDOR
# ============================================================
st.markdown("<h2 style='text-align:center;'>Sobre o Desenvolvedor</h2>", unsafe_allow_html=True)
st.markdown("""
Sou **estudante e desenvolvedor na área de Inteligência Artificial aplicada (Machine Learning)**,  
atuando em **projetos de IA Educacional, FinTech e Blockchain Inteligente**.

Durante o curso de **Machine Learning**, desenvolvo **protótipos funcionais** que conectam IA e sistemas reais,  
utilizando **Streamlit, Firebase, TensorFlow, Web3 e Scikit-Learn**.

O **SmartLog Blockchain** é um aplicativo educacional e técnico que demonstra como IA e Blockchain  
podem ser aplicadas em **sistemas logísticos e auditorias descentralizadas**, simulando fraudes, consenso e recuperação de dados.
""")

st.markdown("<hr>", unsafe_allow_html=True)


# ============================================================
# 🚀 SOBRE O PROJETO
# ============================================================
st.markdown("<h2 style='color:#2D8CFF; text-align:center;'>O que é o SmartLog Blockchain</h2>", unsafe_allow_html=True)
st.markdown("""
O **SmartLog Blockchain** é um simulador **visual e interativo** do consenso **Proof-of-Authority (PoA)**,
um modelo utilizado em redes privadas que exige validadores confiáveis.

Com o simulador é possível:

- Criar uma blockchain de entregas em tempo real;  
- Simular o consenso entre nós validadores;  
- Executar testes de **fraude e recuperação automática**;  
- Integrar com **Web3** para registro descentralizado;  
- Conectar com **Firestore** para auditoria e rastreabilidade em nuvem.

Uma ferramenta ideal para aprender e demonstrar como blockchain reforça **segurança, rastreamento e auditoria digital**.
""")

st.markdown("<hr>", unsafe_allow_html=True)


# ============================================================
# 🖼️ ETAPAS DO PROJETO (TODAS AS IMAGENS)
# ============================================================
st.markdown("<h2 style='color:#4B7BE5; text-align:center;'>Etapas Visuais do Projeto</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Carregar imagens
img_demo = crop_white_borders("smartlog_demo.png")
img_audit = crop_white_borders("smartlog_auditoria.png")
img_fraud = crop_white_borders("smartlog_fraude.png")
img_fire = crop_white_borders("smartlog_firestore_auditoria.png")
img_web3 = crop_white_borders("smartlog_web3_register.png")
img_web3_explain = crop_white_borders("smartlog_fire.png")


with col1:
    if img_demo:
        st.image(img_demo, caption="Interface Principal — Simulação do Consenso PoA")

    if img_fraud:
        st.image(
            img_fraud,
            caption=(
                "Simulação de Fraude — Um bloco adulterado quebra a integridade da cadeia. "
                "A blockchain detecta automaticamente inconsistências e identifica o ponto exato do ataque."
            )
        )


with col2:
    if img_audit:
        st.image(img_audit, caption="Auditoria de Hashes — Verificação Antes e Depois")

    if img_fire:
        st.image(img_fire, caption="Sincronização e Auditoria no Firestore")


if img_web3:
    st.image(
        img_web3,
        caption="Registro de Blocos no Contrato SmartLogLedger (Web3)",
        use_column_width=True
    )

# Explicação extra Web3
if img_web3_explain:
    st.image(
        img_web3_explain,
        caption=(
            "Arquitetura Web3 — Explica como carteiras digitais, transações assinadas e contratos inteligentes "
            "trabalham juntos para registrar eventos de forma descentralizada e segura."
        ),
        use_column_width=True
    )

st.markdown("<hr>", unsafe_allow_html=True)


# ============================================================
# 💡 OBJETIVOS
# ============================================================
st.markdown("<h2 style='color:#06D6A0; text-align:center;'>Objetivos e Impacto</h2>", unsafe_allow_html=True)
st.markdown("""
O **SmartLog Blockchain** demonstra como blockchain pode ser usada em:

- Logística inteligente  
- Auditoria automatizada  
- Rastreabilidade confiável  
- Deteção de fraudes e inconsistências  
- Transparência e governança digital  

Ao integrar IA, blockchain e cloud, o projeto mostra como tecnologias modernas  
podem proteger dados e aumentar a confiabilidade de sistemas reais.
""")

st.markdown("<hr>", unsafe_allow_html=True)


# ============================================================
# 🧰 TECNOLOGIAS
# ============================================================
st.markdown("<h2 style='color:#F4A261; text-align:center;'>Tecnologias Utilizadas</h2>", unsafe_allow_html=True)
st.markdown("""
- **Python** · Streamlit · Pandas · Hashlib · Requests  
- **Blockchain Simulada (PoA)**  
- **Firebase Firestore** — Auditoria em nuvem  
- **Web3 / Remix Ethereum** — Registro descentralizado  
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
