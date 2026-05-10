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
        0% { transform: translateY(100vh) rotate(0deg);
