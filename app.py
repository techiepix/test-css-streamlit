import streamlit as st

st.set_page_config(page_title="My Cute Portfolio 🌸", layout="wide")

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🌸 My Cute Portfolio 🌸</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Welcome to my pastel world ✨</p>', unsafe_allow_html=True)

# Profile Picture
st.image("assets/profile.png", width=200)

# Layout 3 Kolom
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h3>📚 About Me</h3><p>Mahasiswa Data Science 💻 suka AI & design.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>🚀 Projects</h3><p>YOLOv5 palm detection 🌴<br>Streamlit dashboards 📊<br>Sims 4 CC 🎨</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h3>📩 Contact</h3><p>Email: <b>me@email.com</b><br>IG: @mycutehandle 🌸</p></div>', unsafe_allow_html=True)

# Button
if st.button("✨ Say Hi ✨"):
    st.balloons()
    st.success("Yay! Thanks for visiting 💖")
