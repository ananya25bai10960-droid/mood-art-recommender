print("RUNNING FILE: app_ui.py — FINAL CLEAN VERSION")

import streamlit as st
import pandas as pd

# =========================
# LOAD & CLEAN DATASET
# =========================

df = pd.read_csv("datasheet.csv")

# Strip spaces + lowercase text columns
df = df.apply(
    lambda col: col.str.strip().str.lower()
    if col.dtype == "object"
    else col
)

# Drop rows with missing critical values
df = df.dropna(subset=[
    "mood",
    "music_preference",
    "movie_preference",
    "book_preference",
    "recommended_song",
    "recommended_movie",
    "recommended_book",
    "suggested_hobby"
])

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Mood-Based Recommendation App",
    page_icon="🎧",
    layout="centered"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: bold;
    color: #6C63FF;
    text-align: center;
}
.sub-title {
    font-size: 20px;
    color: #444;
    text-align: center;
}
.result-box {
    background-color: #F4F6FF;
    padding: 20px;
    border-radius: 15px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.markdown("<div class='main-title'>🧠 Mood-Based Wellness Recommender</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Music • Books • Movies • Hobbies</div>", unsafe_allow_html=True)
st.write("")

# =========================
# USER INPUTS
# =========================

mood = st.selectbox(
    "💭 How are you feeling today?",
    sorted(df["mood"].astype(str).unique())
)

energy = st.slider(
    "⚡ Energy Level",
    min_value=1,
    max_value=5,
    value=3
)

sleep = st.slider(
    "😴 Sleep Quality",
    min_value=1,
    max_value=5,
    value=3
)

music_pref = st.selectbox(
    "🎵 Preferred Music Type",
    sorted(df["music_preference"].astype(str).unique())
)

movie_pref = st.selectbox(
    "🎬 Preferred Movie Type",
    sorted(df["movie_preference"].astype(str).unique())
)

book_pref = st.selectbox(
    "📚 Preferred Book Type",
    sorted(df["book_preference"].astype(str).unique())
)

# =========================
# RECOMMENDATION LOGIC
# =========================

if st.button("✨ Get My Recommendations"):
    filtered = df[
        (df["mood"] == mood) &
        (df["energy_level"] == energy) &
        (df["sleep_quality"] == sleep) &
        (df["music_preference"] == music_pref) &
        (df["movie_preference"] == movie_pref) &
        (df["book_preference"] == book_pref)
    ]

    if filtered.empty:
        filtered = df[df["mood"] == mood]
        st.info("No exact match found — showing closest suggestions 💙")

    rec = filtered.iloc[0]

    # =========================
    # GENTLE TIP
    # =========================

    st.markdown("### 💡 Gentle Tip for Today")

    if mood == "sad":
        st.write("Be kind to yourself today — even small comforts count.")
    elif mood == "happy":
        st.write("This is a good time to create, share, or explore something new.")
    elif mood == "anxious":
        st.write("Slow activities like reading or music can help ground you.")
    elif mood == "angry":
        st.write("Physical movement or journaling may help release tension.")
    elif mood == "numb":
        st.write("Gentle sensory activities can help you reconnect slowly.")
    elif mood == "energetic":
        st.write("Channel this energy into something expressive or creative.")
    else:
        st.write("Take today at your own pace — balance is still progress.")

    # =========================
    # RESULT DISPLAY
    # =========================

    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.markdown(f"🎵 **Song Recommendation:** {rec['recommended_song']}")
    st.markdown(f"🎬 **Movie Recommendation:** {rec['recommended_movie']}")
    st.markdown(f"📚 **Book Recommendation:** {rec['recommended_book']}")
    st.markdown(f"🎨 **Suggested Hobby:** {rec['suggested_hobby']}")
    st.markdown("</div>", unsafe_allow_html=True)

    # =========================
    # WHY THIS FITS YOU
    # =========================

    st.markdown("### 🧠 Why this suits you")

    if energy <= 2:
        st.write("You’re low on energy today, so the recommendations are calming and low-effort.")
    elif energy <= 4:
        st.write("Your energy is balanced, so these picks aim to comfort and gently engage you.")
    else:
        st.write("You’re feeling energetic, so the suggestions lean more stimulating and expressive.")