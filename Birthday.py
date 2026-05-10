import streamlit as st
import time
import random

st.set_page_config(page_title="Happy Birthday Princess!", page_icon="👑", layout="centered")

# === Change these two lines ===
HER_NAME = "Princess"          # ← Change to her real name or nickname
YOUR_NAME = "🥰"        # ← Put your name here

st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #ff9a9e, #fad0c4, #f8c1d9); }
    .princess-title { 
        font-family: 'Dancing Script', cursive; 
        font-size: 4.8rem; color: #db2777; 
        text-align: center; text-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    .cake { font-size: 220px; cursor: pointer; transition: all 0.4s; }
    .cake:hover { transform: scale(1.18) rotate(12deg); }
</style>
""", unsafe_allow_html=True)

# Background Music
st.markdown(f"""
<audio autoplay loop>
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 1
if 'candles_lit' not in st.session_state: st.session_state.candles_lit = True

st.title(f"🎉 Happy Birthday, {Princess}! 👑")

if st.session_state.step == 1:
    st.markdown(f'<h1 class="princess-title">Happy Birthday, {HER_NAME}!</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background:white; padding:35px; border-radius:30px; box-shadow:0 15px 40px rgba(0,0,0,0.1); text-align:center; font-size:1.65rem; line-height:2.3rem;">
        You are the most beautiful, kind, and magical person in my life.<br><br>
        Your smile lights up my whole world every single day.<br><br>
        I love you more than all the stars in the sky 💖
    </div>
    """, unsafe_allow_html=True)

    if st.button("💕 Open Your Birthday Magic →", type="primary", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.markdown("### 🐱 Princess Sparkle wants to wish you Happy Birthday!")
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown('<div style="font-size:260px; text-align:center;">🐱</div>', unsafe_allow_html=True)
    with col2:
        if st.button("💖 Cuddle Princess Sparkle", use_container_width=True):
            st.success(random.choice([
                f"🐱 *Purrrr* {princess}, she loves you so much!",
                "💕 She gives you the biggest head boop ever!",
                "😻 Happy Birthday from your cat!"
            ]))
            st.balloons()

    if st.button("🎂 Go to Cake Time →", type="primary", use_container_width=True):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.markdown("### 🎂 Make a Wish, My Love!")
    st.markdown("**Click the cake to blow out the candles** ✨")

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        cake_emoji = "🎂" if st.session_state.candles_lit else "✨🎂"
        if st.button(cake_emoji, key="cake", use_container_width=True):
            if st.session_state.candles_lit:
                st.session_state.candles_lit = False
                st.balloons()
                st.snow()
                st.success(f"🎉 Wish Granted, {HER_NAME}! May your year be filled with endless love and happiness! ✨")
            st.rerun()

    if not st.session_state.candles_lit:
        st.markdown(f"""
        <h2 style="text-align:center; color:#831843;">
            I love you so much, {Princess} ❤️<br>
            Happy Birthday, My Princess!
        </h2>
        """, unsafe_allow_html=True)

    if st.button("🔄 Light Candles Again"):
        st.session_state.candles_lit = True
        st.rerun()

    if st.button("🎉 Final Celebration with Love", type="primary", use_container_width=True):
        st.balloons()
        st.snow()

st.progress(st.session_state.step / 3)
st.caption("Made with ❤️ by " + Me)
