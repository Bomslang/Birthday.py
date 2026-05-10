import streamlit as st
import random

# ===================== PERSONALIZATION =====================
HER_NAME = "Princess"          # ← You can still change this
YOUR_NAME = "Me"         # ← Change to your name
# ========================================================

st.set_page_config(page_title=f"Happy Birthday {HER_NAME}!", page_icon="👑", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:wght@700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4, #f8c1d9);
        overflow: hidden;
    }
    .princess-title {
        font-family: 'Dancing Script', cursive;
        font-size: 5.2rem;
        color: #db2777;
        text-align: center;
        text-shadow: 0 6px 20px rgba(219, 39, 119, 0.4);
        animation: glow 2.5s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 6px 20px rgba(219, 39, 119, 0.4); }
        to { text-shadow: 0 12px 35px rgba(236, 72, 153, 0.7); }
    }

    .heart {
        position: absolute;
        font-size: 28px;
        opacity: 0.75;
        animation: floatHeart 14s linear infinite;
        z-index: -1;
    }
    @keyframes floatHeart {
        0% { transform: translateY(100vh) rotate(0deg); }
        100% { transform: translateY(-120vh) rotate(360deg); }
    }

    .cake {
        font-size: 240px;
        cursor: pointer;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .cake:hover {
        transform: scale(1.28) rotate(15deg);
    }
</style>
""", unsafe_allow_html=True)

# Floating Hearts Background
def add_floating_hearts():
    hearts_html = '<div style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:-1; overflow:hidden;">'
    for i in range(20):
        left = random.randint(5, 95)
        delay = random.uniform(0, 15)
        size = random.randint(22, 48)
        hearts_html += f'''
        <div class="heart" style="left:{left}%; animation-delay:{delay}s; font-size:{size}px;">
            {'❤️' if i % 3 != 0 else '💖'}
        </div>'''
    hearts_html += "</div>"
    st.markdown(hearts_html, unsafe_allow_html=True)

add_floating_hearts()

# Background Music
st.markdown("""
<audio autoplay loop>
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

# Session State
if 'step' not in st.session_state: st.session_state.step = 1
if 'candles_lit' not in st.session_state: st.session_state.candles_lit = True

st.title(f"🎉 Happy Birthday, {HER_NAME}! 👑")

# ===================== STEP 1: Grand Welcome =====================
if st.session_state.step == 1:
    st.markdown(f'<h1 class="princess-title">Happy Birthday, {HER_NAME}!</h1>', unsafe_allow_html=True)
    st.markdown("### My dearest Princess 💖")
    
    if st.button("💕 Begin
