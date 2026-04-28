import streamlit as st

st.set_page_config(page_title="About Me", layout="wide")

# ---------- THEME ----------
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

# ---------- GLOBAL STYLE ----------
st.markdown(f"""
<style>
.stApp {{
    background: {bg};
    color: {text};
    font-family: 'Segoe UI', sans-serif;
}}

.glass {{
    background: {glass};
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    transition: 0.3s ease;
}}

.glass:hover {{
    transform: translateY(-5px);
    box-shadow: 0 12px 45px rgba(0,0,0,0.25);
}}

.title {{
    font-size: 42px;
    text-align:center;
    color: {accent};
    margin-bottom: 5px;
}}

.subtitle {{
    text-align:center;
    opacity:0.7;
    margin-bottom: 30px;
}}

.badge {{
    display:inline-block;
    padding:6px 12px;
    border-radius:999px;
    background:{accent};
    color:white;
    font-size:12px;
}}

h3 {{
    margin-bottom:10px;
    color:{accent};
}}

p {{
    line-height:1.7;
    opacity:0.9;
}}

.stats {{
    display:flex;
    justify-content:space-between;
    margin-top:15px;
}}

.stat {{
    text-align:center;
}}

.stat h2 {{
    margin:0;
    color:{accent};
}}

.stat p {{
    margin:0;
    font-size:12px;
    opacity:0.7;
}}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown(f"""
<div style="
    text-align:center;
    padding: 30px 20px;
    margin-bottom: 20px;
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
        About Me
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

# ---------- LEFT ----------
with col1:
    st.markdown(f"""
<div class="glass">

<div style="display:flex; gap:15px; align-items:center;">
<div style="
                width:60px;
                height:60px;
                border-radius:50%;
                background:{accent};
                display:flex;
                justify-content:center;
                align-items:center;
                color:white;
                font-size:24px;
            ">
            👩‍💻
</div>

<div>
                <h3 style="margin:0;">Shara Boston</h3>
                <p style="margin:0; opacity:0.7;">Aspiring Developer</p>
</div>
</div>

<hr style="opacity:0.2; margin:15px 0;">

<span class="badge">Overview</span>
<p> I am a Computer Science student who is passionate about building modern and meaningful applications. I enjoy understanding how systems work behind the scenes and using that knowledge to turn ideas into functional software. </p> <p> I am continuously learning new technologies and improving my skills in programming, especially in Python and web development. I like working on projects that challenge me to think critically and solve real-world problems. </p> <p> My goal is to grow as a developer and create applications that are not only functional but also user-friendly and impactful for people who use them. </p>

<span class="badge">Currently Learning</span>
<p> I am currently focusing on improving my skills in frontend development, backend systems, and UI/UX design. I enjoy learning how both the visual and functional parts of an application work together to create a smooth user experience. </p> <p> I am also exploring how to build more responsive and interactive web applications, while strengthening my understanding of how full-stack systems are developed and connected. </p>

</div>
    """, unsafe_allow_html=True)

# ---------- RIGHT ----------
with col2:
    st.markdown(f"""
<div class="glass">

<h3>📊 Stats</h3>

<div class="stats">
<div class="stat">
<h2>5+</h2>
<p>Projects</p>
</div>

<div class="stat">
<h2>3+</h2>
<p>Tools</p>
</div>

<div class="stat">
<h2>1</h2>
<p>Goal</p>
</div>
</div>

<hr style="opacity:0.2; margin:15px 0;">

<h3>🚀 Mission</h3>
<p> My goal is to grow as a developer by continuously learning and improving my technical skills while building meaningful digital solutions. I want to create applications that not only function well but also provide real value to users. </p> <p> I aim to work on projects that solve real-world problems, improve user experience, and make everyday tasks easier through thoughtful design and efficient development. </p>

<div style="
            margin-top:15px;
            padding:10px;
            border-left:3px solid {accent};
            background:rgba(255,255,255,0.05);
            border-radius:10px;
        ">
        💡 Learning never stops — every project is progress.
</div>

</div>
    """, unsafe_allow_html=True)