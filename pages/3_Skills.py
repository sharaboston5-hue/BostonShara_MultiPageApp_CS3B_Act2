import streamlit as st

st.set_page_config(page_title="Skills", layout="wide")

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

.card {{
    background:{glass};
    padding:22px;
    border-radius:18px;
    backdrop-filter: blur(18px);
    border:1px solid rgba(255,255,255,0.15);
    transition:0.3s;
}}

.card:hover {{
    transform: translateY(-6px);
}}

.category {{
    font-size:18px;
    font-weight:600;
    color:{accent};
    margin-bottom:10px;
}}

.item {{
    margin:5px 0;
    font-size:14px;
    opacity:0.9;
}}

.badge {{
    display:inline-block;
    padding:4px 10px;
    border-radius:999px;
    font-size:11px;
    background:{accent};
    color:white;
    margin-bottom:10px;
}}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER (NEW CONTEXT) ----------
st.markdown(f"""
<div class="title">My Skills</div>
""", unsafe_allow_html=True)

# ---------- GRID ----------
col1, col2, col3 = st.columns(3)

# ---------- COLUMN 1 ----------
with col1:
    st.markdown(f"""
<div class="card">
<div class="badge">Core</div>
<div class="category">Programming</div>

<div class="item">Python (Main Language)</div>
<div class="item">Basic JavaScript</div>
<div class="item">Problem Solving</div>
</div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
<div class="card" style="margin-top:15px;">
<div class="badge">Structure</div>
<div class="category">Web Basics</div>

<div class="item">HTML</div>
<div class="item">CSS</div>
<div class="item">Responsive Layout Thinking</div>
</div>
    """, unsafe_allow_html=True)

# ---------- COLUMN 2 ----------
with col2:
    st.markdown(f"""
<div class="card">
<div class="badge">Framework</div>
<div class="category">Development Tools</div>

<div class="item">Streamlit</div>
<div class="item">Git & GitHub</div>
<div class="item">Basic UI Structuring</div>
</div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
<div class="card" style="margin-top:15px;">
<div class="badge">Design</div>
<div class="category">UI/UX Interest</div>

<div class="item">Glassmorphism UI</div>
<div class="item">Clean Layout Design</div>
<div class="item">User Experience Thinking</div>
</div>
    """, unsafe_allow_html=True)

# ---------- COLUMN 3 ----------
with col3:
    st.markdown(f"""
<div class="card">
<div class="badge">Soft Skills</div>
<div class="category">Personal Growth</div>

<div class="item">Creativity</div>
<div class="item">Consistency in Learning</div>
<div class="item">Critical Thinking</div>
</div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
<div class="card" style="margin-top:15px;">
<div class="badge">Goal</div>
<div class="category">Career Focus</div>

<div class="item">Become Full-Stack Developer</div>
<div class="item">Build Real-World Applications</div>
<div class="item">Improve UI/UX Skills</div>
</div>
    """, unsafe_allow_html=True)