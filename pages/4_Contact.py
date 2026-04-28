import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

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

.header {{
    text-align:center;
    padding:30px;
    margin-bottom:30px;
    background:{glass};
    border-radius:20px;
    backdrop-filter: blur(18px);
    border:1px solid rgba(255,255,255,0.15);
}}

.contact-box {{
    background:{glass};
    padding:25px;
    border-radius:18px;
    backdrop-filter: blur(18px);
    border:1px solid rgba(255,255,255,0.15);
    margin-bottom:20px;
    transition:0.3s;
}}

.contact-box:hover {{
    transform: translateY(-5px);
}}

.label {{
    font-size:14px;
    opacity:0.7;
}}

.value {{
    font-size:18px;
    font-weight:600;
    color:{accent};
}}

input, textarea {{
    border-radius:10px !important;
}}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown(f"""
<div class="header">
    <h1 style="color:{accent};">Contact Me</h1>
    <p>Feel free to reach out for collaboration or opportunities</p>
</div>
""", unsafe_allow_html=True)

# ---------- CONTACT INFO ----------
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="contact-box">
        <div class="label">📧 Email</div>
        <div class="value">sharaboston5@gmail.com</div>
    </div>

    <div class="contact-box">
        <div class="label">📱 Phone</div>
        <div class="value">09102204577</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="contact-box">
        <div class="label">🌐 Facebook</div>
        <div class="value">https://www.facebook.com/share/18GD6pMWaZ/</div>
    </div>

    <div class="contact-box">
        <div class="label">💼 GitHub</div>
        <div class="value">https://github.com/sharaboston5-hue</div>
    </div>
    """, unsafe_allow_html=True)

# ---------- CONTACT FORM ----------
st.markdown(f"""
<div class="contact-box">
    <h3 style="color:{accent};">Send a Message</h3>
</div>
""", unsafe_allow_html=True)

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    submit = st.form_submit_button("Send Message")

    if submit:
        st.success("✅ Message sent successfully!")