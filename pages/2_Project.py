import streamlit as st

st.set_page_config(page_title="Projects", layout="wide")

theme = st.sidebar.toggle("🌙 Dark Mode")

if theme:
    bg = "linear-gradient(135deg, #0f172a, #020617)"
    text = "#e2e8f0"
    accent = "#38bdf8"
    glass = "rgba(255,255,255,0.06)"
else:
    bg = "linear-gradient(135deg, #e0eafc, #cfdef3)"
    text = "#0f172a"
    accent = "#2563eb"
    glass = "rgba(255,255,255,0.55)"

# ---------- STYLE ----------
st.markdown(f"""
<style>
.stApp {{
    background: {bg};
    color: {text};
    font-family: 'Segoe UI', sans-serif;
}}

.title {{
    text-align:center;
    font-size:44px;
    color:{accent};
}}

.subtitle {{
    text-align:center;
    opacity:0.7;
    margin-bottom:30px;
}}

.timeline {{
    background:{glass};
    padding:25px;
    border-radius:18px;
    backdrop-filter: blur(18px);
    border:1px solid rgba(255,255,255,0.15);
    margin-bottom:20px;
    transition:0.3s;
}}

.timeline:hover {{
    transform: translateY(-5px);
}}

.badge {{
    display:inline-block;
    padding:5px 10px;
    border-radius:999px;
    background:{accent};
    color:white;
    font-size:11px;
    margin-bottom:10px;
}}

h3 {{
    margin-bottom:5px;
}}

p {{
    font-size:14px;
    opacity:0.85;
    line-height:1.6;
}}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown(f"""
<div style="
    text-align:center;
    padding: 30px 20px;
    margin-bottom: 25px;
    background: {glass};
    border-radius: 20px;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
">
    <div style="
        font-size: 44px;
        font-weight: 700;
        color: {accent};
    ">
        My Projects
    </div>
</div>
""", unsafe_allow_html=True)
# ---------- PROJECT 1 ----------
# ---------- PROJECT 1 ----------
st.markdown(f"""
<div class="timeline">
    <h3>🧮 Basic Calculator App</h3>
    <p>
    A simple calculator built using Python that performs basic arithmetic operations 
    such as addition, subtraction, multiplication, and division. This project helped 
    me understand user input handling and core programming logic.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- PROJECT 2 ----------
st.markdown(f"""
<div class="timeline">
    <h3>🌐 Personal Portfolio Website</h3>
    <p>
    I developed my personal portfolio using Streamlit featuring a modern glassmorphism UI,
    dark mode toggle, and responsive layout. This project showcases my skills, projects,
    and growth as an aspiring developer.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- PROJECT 3 ----------
st.markdown(f"""
<div class="timeline">
    <h3>📝 To-Do List App</h3>
    <p>
    A simple task management app that allows users to add, complete, and delete tasks.
    This project improved my understanding of state management and user interaction.
    </p>
</div>
""", unsafe_allow_html=True)
