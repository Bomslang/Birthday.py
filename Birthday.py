        import streamlit as st
import random
import time

# ===================== PERSONALIZATION =====================
HER_NAME = "YourGirlfriendName"   # ← Change to her real name
YOUR_NAME = "YourName"            # ← Your name
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
        text-shadow: 0 6px 20px rgba(219, 39, 119, 0.3);
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 6px 20px rgba(219, 39, 119, 0.3); }
        to { text-shadow: 0 10px 30px rgba(236, 72, 153, 0.6); }
    }

    /* Floating Hearts Background */
    .heart {
        position: absolute;
        font-size: 30px;
        opacity: 0.7;
        animation: floatHeart 12s linear infinite;
        z-index: -1;
    }
    @keyframes floatHeart {
        0% { transform: translateY(100vh) rotate(0deg); }
        100% { transform: translateY(-100vh) rotate(360deg); }
    }

    .cake {
        font-size: 240px;
        cursor: pointer;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        filter: drop-shadow(0 15px 25px rgba(0,0,0,0.2));
    }
    .cake:hover {
        transform: scale(1.25) rotate(15deg);
    }

    .sparkle {
        animation: sparkle 1.5s infinite;
    }
    @keyframes sparkle {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.4; }
    }
</style>
""", unsafe_allow_html=True)

# Animated Floating Hearts Background
def add_floating_hearts():
    hearts_html = """
    <div style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:-1; overflow:hidden;">
    """
    for i in range(18):
        left = random.randint(5, 95)
        delay = random.uniform(0, 12)
        size = random.randint(20, 45)
        hearts_html += f'''
        <div class="heart" style="left:{left}%; animation-delay:{delay}s; font-size:{size}px;">
            {'❤️' if i % 2 == 0 else '💖'}
        </div>
        '''
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
if 'wishes' not in st.session_state: st.session_state.wishes = 0

st.title(f"🎉 Happy Birthday, {HER_NAME}! 👑")

if st.session_state.step == 1:
    st.markdown(f'<h1 class="princess-title">Happy Birthday, {HER_NAME}!</h1>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.85); padding:40px; border-radius:30px; 
                box-shadow:0 20px 50px rgba(0,0,0,0.15); text-align:center; font-size:1.7rem; line-height:2.4rem;">
        My dearest {HER_NAME},<br><br>
        You are the most beautiful soul I know.<br>
        Your smile lights up my entire universe.<br><br>
        I love you more than all the stars combined 💖
    </div>
    """, unsafe_allow_html=True)

    if st.button("💕 Open Your Magical Gifts →", type="primary", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.markdown("### 🐱 Meet Princess Sparkle!")
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown('<div style="font-size:280px; text-align:center; animation: sparkle 2s infinite;">🐱</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f"#### Hi {HER_NAME}!")
        if st.button("💖 Cuddle Princess Sparkle", use_container_width=True):
            st.success(random.choice([
                f"🐱 *Purrrrrr* {HER_NAME} she loves you!",
                "💕 Big head boops and cuddles incoming!",
                "😻 She says you're the best human ever!"
            ]))
            st.balloons()

    if st.button("🎂 Next → Cake Time!", type="primary", use_container_width=True):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.markdown("### 🎂 Make a Wish, My Princess!")
    st.markdown("**Tap the cake to blow out the candles** ✨")

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        cake = "🎂" if st.session_state.candles_lit else "✨🎂"
        if st.button(cake, key="cake_btn", use_container_width=True):
            if st.session_state.candles_lit:
                st.session_state.candles_lit = False
                st.session_state.wishes += 1
                st.balloons()
                st.snow()
                st.success(f"🎉 Wish Granted, {HER_NAME}! May all your dreams come true! ✨")
            st.rerun()

    if not st.session_state.candles_lit:
        st.markdown(f"""
        <h2 style="text-align:center; color:#831843; font-family:'Dancing Script', cursive; font-size:2.8rem;">
            I love you endlessly, {HER_NAME} ❤️
        </h2>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("🔄 Light Candles Again"):
            st.session_state.candles_lit = True
            st.rerun()

    if st.button("🎉 Final Grand Celebration!", type="primary", use_container_width=True):
        st.balloons()
        st.snow()

# Progress
st.progress(st.session_state.step / 3.0)
st.caption(f"Made with ❤️ by {YOUR_NAME}")

st.markdown("---")
st.markdown("<p style='text-align:center; color:#831843;'>Made specially for the most amazing girl in the world</p>", unsafe_allow_html=True)
