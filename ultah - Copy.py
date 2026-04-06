import streamlit as st
import streamlit.components.v1 as components 
import time

# --- PENGATURAN HALAMAN ---
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="centered")

# --- AREA EDIT DATA ---
NAMA_PANGGILAN = "Seseorang" 
UCAPAN_UTAMA = "Selamat Ulang Tahun!" 
PESAN_TAMBAHAN = """
Semoga di usia yang baru ini, kamu makin bahagia, 
rezekinya lancar, dan semua impianmu segera terwujud. 
Doa terbaik pokoknya buat kamu! 🚀✨
"""

# --- EFEK ANIMASI LOVE JATUH ---
st.markdown("""
<style>
@keyframes fall {
    0% { transform: translateY(-10vh) scale(0.8); opacity: 1; }
    100% { transform: translateY(110vh) scale(1.2); opacity: 0; }
}
.love {
    position: fixed;
    font-size: 35px;
    top: 0;
    z-index: 9999;
    user-select: none;
    pointer-events: none;
}
.l1 { left: 10%; animation: fall 4s linear infinite; }
.l2 { left: 30%; animation: fall 3s linear infinite; }
.l3 { left: 50%; animation: fall 5s linear infinite; }
.l4 { left: 70%; animation: fall 4.5s linear infinite; }
.l5 { left: 90%; animation: fall 3.5s linear infinite; }
</style>
<div class="love l1">❤️</div>
<div class="love l2">💖</div>
<div class="love l3">💕</div>
<div class="love l4">💗</div>
<div class="love l5">❤️</div>
""", unsafe_allow_html=True)

# --- KONTEN TAMPILAN ---
st.write(f"# 🎉 HBD {NAMA_PANGGILAN.upper()}! 🎉")
st.write("---")

st.markdown(f"""
<div style="
    background-color: #fce4ec; 
    padding: 20px; 
    border-radius: 15px; 
    border-left: 10px solid #e91e63;
    margin-bottom: 25px;">
    <h2 style="color: #c2185b; margin-top: 0;">{UCAPAN_UTAMA}</h2>
    <p style="font-size: 1.1em; color: #555; line-height: 1.6;">
        {PESAN_TAMBAHAN.strip().replace('\n', '<br>')}
    </p>
</div>
""", unsafe_allow_html=True)

# --- PEMUTAR SPOTIFY ---
st.write("Dengerin lagu ini spesial buat kamu! 🎧")

# KODE SPOTIFY KAMU DIMASUKKAN DI SINI:
kode_spotify = """
<iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/35o9a4iAfLl5jRmqMX9c1D?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>"""
components.html(kode_spotify, height=160)

st.write("---")
st.caption(f"Dikirim dengan 💖 oleh temanmu di {time.strftime('%Y')}")

# Tetap memunculkan balon
st.balloons()