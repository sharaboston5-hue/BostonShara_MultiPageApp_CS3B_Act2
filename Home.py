import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

theme = st.sidebar.toggle("🌙 Dark Mode")

# ---------- THEME ----------
if theme:
    bg = "linear-gradient(135deg, #0f172a, #020617)"
    text = "#e2e8f0"
    subtext = "#94a3b8"
    accent = "#38bdf8"
    card = "rgba(255,255,255,0.05)"
else:
    bg = "linear-gradient(135deg, #f8fafc, #e2e8f0)"
    text = "#0f172a"
    subtext = "#475569"
    accent = "#2563eb"
    card = "rgba(255,255,255,0.7)"

# ---------- GLOBAL STYLE ----------
st.markdown(f"""
<style>
.stApp {{
    background: {bg};
    color: {text};
    font-family: 'Segoe UI', sans-serif;
}}

/* TITLE */
.title {{
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 10px;
}}

/* SUBTITLE */
.subtitle {{
    font-size: 18px;
    color: {subtext};
    margin-bottom: 25px;
}}

/* CARD */
.card {{
    background: {card};
    padding: 35px;
    border-radius: 20px;
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.1);
    transition: 0.3s ease;
}}

/* HOVER EFFECT */
.card:hover {{
    transform: translateY(-6px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
}}

/* BADGE */
.badge {{
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    background: {accent};
    color: white;
    font-size: 12px;
    margin-bottom: 15px;
}}

/* BUTTON */
.btn {{
    display: inline-block;
    padding: 10px 18px;
    background: {accent};
    color: white;
    border-radius: 10px;
    text-decoration: none;
    font-size: 14px;
    margin-top: 10px;
    margin-right: 8px;
    transition: 0.3s;
}}

.btn:hover {{
    opacity: 0.8;
}}

/* STATS */
.stats {{
    display: flex;
    gap: 20px;
    margin-top: 20px;
}}

.stat-box {{
    flex: 1;
    padding: 15px;
    border-radius: 12px;
    background: rgba(255,255,255,0.05);
    text-align: center;
}}

.stat-number {{
    font-size: 22px;
    font-weight: bold;
    color: {accent};
}}

.stat-label {{
    font-size: 12px;
    color: {subtext};
}}

</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown(f"""
<div class="card">
<div class="badge">Aspiring Developer</div>

<div class="title">
    Hi, I'm <span style="color:{accent};">Shara Boston</span>
</div>

<p style="line-height:1.7;">
I am a Computer Science student passionate about turning ideas into real, 
working applications. I enjoy building interactive and user-friendly projects 
using <b>Python</b> and <b>Streamlit</b>, while continuously exploring design 
and user experience.
</p>

<p style="line-height:1.7;">
Through hands-on projects, I challenge myself to grow both creatively and 
technically. Each project helps me improve my problem-solving skills and deepen 
my understanding of development.
</p>

<p style="line-height:1.7;">
My goal is to become a skilled developer and create meaningful digital solutions 
that make a real impact.
</p>

<div class="stats">
<div class="stat-box">
    <div class="stat-number">5+</div>
    <div class="stat-label">Projects</div>
</div>

<div class="stat-box">
    <div class="stat-number">3+</div>
    <div class="stat-label">Technologies</div>
</div>

<div class="stat-box">
    <div class="stat-number">100%</div>
    <div class="stat-label">Learning Mode</div>
</div>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.image("06dec741-eeaf-4520-84ff-e9d90d123cb4.jpg", use_container_width=True)

