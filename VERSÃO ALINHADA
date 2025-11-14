import streamlit as st
from PIL import Image, ImageChops

# ============================================================
# ⚙️ CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="SmartLog Blockchain — Inovação IA-Labs",
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
st.markdown("<h1 style='color:#2D8CFF;'>SmartLog Blockchain — IA-Labs</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color:#FF6F61;'>Simulador de Consenso, Auditoria e Governança de Dados</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 👨‍💻 SOBRE O IA-LABS / DESENVOLVEDOR
# ============================================================
st.markdown("""
### Sobre o IA-Labs  
O **IA-Labs** é um laboratório nacional de **política pública orientada por dados**, parceiro estratégico de governos e organizações que buscam **inovação social, transformação digital e impacto real**.

Nossa atuação abrange:
- Educação  
- Saúde  
- Indústria 4.0  
- Segurança Nacional  
- Defesa Tecnológica  
- Gestão Pública  

Combinamos **Inteligência Artificial**, engenharia de dados e metodologias ágeis para criar soluções que geram **transparência, eficiência e governança** em grande escala.

O **SmartLog Blockchain** faz parte de um conjunto de ferramentas e protótipos que ilustram como tecnologias emergentes podem apoiar decisões públicas e aprimorar auditorias e sistemas críticos.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🚀 SOBRE O PROJETO — VERSÃO IA-LABS
# ============================================================
st.markdown("<h2 style='color:#2D8CFF;'>O que é o SmartLog Blockchain</h2>", unsafe_allow_html=True)
st.markdown("""
O **SmartLog Blockchain** é um **simulador visual e técnico** que demonstra como **Blockchain, IA e análise distribuída**  
podem ser aplicadas a políticas públicas, logística, auditoria e governança digital.

Ele reflete os valores do **IA-Labs**, proporcionando:
- **Visão unificada de dados**, mesmo quando originados de sistemas diferentes;  
- **Análises rápidas**, graças à arquitetura paralela e validadores independentes;  
- **Integração total**, conectando blocos, redes Web3 e bancos em nuvem;  
- **Detecção e correção automática de inconsistências**, reforçando a confiança do processo.

Assim como nas soluções reais desenvolvidas pelo IA-Labs, o foco está em **transparência, integridade e impacto prático**.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🖼️ ETAPAS DO PROJETO — VERSÃO IA-LABS
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
        st.image(img_demo, caption="Simulação do Consenso PoA — Integridade e Governança")
    if img_fraud:
        st.image(img_fraud, caption="Detecção de Inconsistências e Recuperação — Transparência Total")

with col2:
    if img_audit:
        st.image(img_audit, caption="Auditoria de Hashes — Validação Antes/Depois")
    if img_fire:
        st.image(img_fire, caption="Sincronização em Nuvem — Integração com Firestore")

if img_web3:
    st.image(img_web3, caption="Registro Descentralizado no Contrato SmartLogLedger (Web3)", use_column_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 💡 OBJETIVOS E IMPACTO — VERSÃO IA-LABS
# ============================================================
st.markdown("<h2 style='color:#06D6A0;'>Objetivos e Impacto</h2>", unsafe_allow_html=True)
st.markdown("""
O **SmartLog Blockchain** demonstra como tecnologias emergentes podem fortalecer sistemas de interesse público,  
garantindo **transparência, auditoria, rastreabilidade e segurança**.

A solução apoia:
- Políticas públicas baseadas em dados;  
- Auditoria e prestação de contas;  
- Detecção precoce de fraudes;  
- Integração entre órgãos e serviços;  
- Automação e governança digital.

É um exemplo de como o IA-Labs promove **inovação com impacto social**, sempre com foco em **dados confiáveis e decisões inteligentes**.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# 🧰 TECNOLOGIAS UTILIZADAS
# ============================================================
st.markdown("<h2 style='color:#F4A261;'>Tecnologias Utilizadas</h2>", unsafe_allow_html=True)
st.markdown("""
- **Python** · Streamlit · Pandas · Hashlib · Requests  
- **Blockchain (PoA)** — arquitetura distribuída  
- **Firebase Firestore** — armazenamento e auditoria  
- **Web3 / Remix Ethereum** — registro descentralizado  
- **Técnicas de IA e Governança de Dados**
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

st.caption("© 2025 SmartLog Blockchain — Desenvolvido em alinhamento aos valores do IA-Labs")
