
import streamlit as st
import random

# ===================== PERSONALIZATION =====================
HER_NAME = "Princess"     # ← You can change this if you want
YOUR_NAME = "Me"          # ← Changed as requested
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

# Step 1: Grand Welcome
if st.session_state.step == 1:
    st.markdown(f'<h1 class="princess-title">Happy Birthday, {HER_NAME}!</h1>', unsafe_allow_html=True)
    st.markdown("### My dearest Princess 💖")
    
    if st.button("💕 Begin Your Birthday Journey →", type="primary", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# Step 2: Lovely Message From Me
elif st.session_state.step == 2:
    st.markdown(f'<h1 class="princess-title" style="font-size:4rem;">A Message From Me</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background:rgba(255,255,255,0.9); padding:40px; border-radius:30px; 
                box-shadow:0 20px 50px rgba(0,0,0,0.15); text-align:center; font-size:1.65rem; line-height:2.5rem;">
        My beautiful Princess,<br><br>
        Every day with you feels like a fairytale.<br>
        Your smile is my favorite sight, your laugh is my favorite sound,<br>
        and your love is the greatest gift I've ever received.<br><br>
        Thank you for being you. Thank you for being mine.<br><br>
        I love you more than yesterday, but a little less than tomorrow 💖
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("❤️ Continue →", type="primary", use_container_width=True):
            st.session_state.step = 3
            st.rerun()

# Step 3: Beautiful Pet
elif st.session_state.step == 3:
    st.markdown("### 🐱 Your Royal Birthday Companion")
    
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown('<div style="font-size:260px; text-align:center;">🐱</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f"#### Princess Sparkle says Hi, {HER_NAME}!")
        if st.button("💖 Cuddle Her", use_container_width=True):
            st.success(random.choice([
                "🐱 *Purrrrrr* She loves you so much!",
                "💕 She gives you endless head boops!",
                "😻 Happy Birthday from your royal cat!"
            ]))
            st.balloons()

    if st.button("🎂 Next → Cake Time!", type="primary", use_container_width=True):
        st.session_state.step = 4
        st.rerun()

# Step 4: Interactive Cake
elif st.session_state.step == 4:
    st.markdown("### 🎂 Make a Wish, My Princess!")
    st.markdown("**Tap the cake to blow out the candles** ✨")

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        cake_emoji = "🎂" if st.session_state.candles_lit else "✨🎂"
        if st.button(cake_emoji, key="cake", use_container_width=True):
            if st.session_state.candles_lit:
                st.session_state.candles_lit = False
                st.balloons()
                st.snow()
                st.success(f"🎉 Wish Granted, {HER_NAME}! I love you endlessly ✨")
            st.rerun()

    if not st.session_state.candles_lit:
        st.markdown(f"""
        <h2 style="text-align:center; color:#831843; font-family:'Dancing Script', cursive; font-size:2.6rem;">
            Happy Birthday My Princess ❤️<br>
            I love you so much
        </h2>
        """, unsafe_allow_html=True)

    if st.button("🔄 Light Candles Again"):
        st.session_state.candles_lit = True
        st.rerun()

    if st.button("🎉 Final Celebration!", type="primary", use_container_width=True):
        st.balloons()
        st.snow()

# Progress
progress = st.progress(st.session_state.step / 4)
st.caption(f"Step {st.session_state.step} of 4 • Made with ❤️ by {YOUR_NAME}")

st.markdown("---")
st.markdown("<p style='text-align:center; color:#831843;'>Made specially for the most beautiful Princess in the world</p>", unsafe_allow_html=True)
