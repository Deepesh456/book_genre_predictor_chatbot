import streamlit as st
import tensorflow as tf
import pickle
import json
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Page config
st.set_page_config(page_title="📚 Book Genre Chatbot", page_icon="📖", layout="centered")

# Bookstore CSS
st.markdown("""
<style>
.stApp {
    background-image: url('https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1500&q=80');
    background-size: cover;
    background-attachment: fixed;
    font-family: 'Georgia', serif;
}
div.block-container {
    background-color: rgba(255, 255, 255, 0.94);
    padding: 3.5rem 3rem 2rem 3rem;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    margin-top: 2rem;
}
h1, h2, h3, h4, label, .stMarkdown, .stTextInput, .stSubheader, .stSuccess, p,
[data-testid="stMarkdownContainer"] h2 {
    color: #212121 !important;
    font-weight: bold !important;
}
input[class*="stTextInput"] {
    background-color: #fff8f0 !important;
    color: #3e2723 !important;
    border-radius: 8px !important;
    border: 1px solid #d7ccc8 !important;
    font-family: 'Georgia', serif;
}
button {
    background-color: #6d4c41 !important;
    color: white !important;
    border-radius: 8px !important;
    font-weight: bold;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Welcome to Deepesh’s BookBot</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Your cozy AI assistant to find genres and books ✨</h4>", unsafe_allow_html=True)
st.markdown("---")

# Loading LSTM Model, Tokenizer, Label Map
model = tf.keras.models.load_model("genre_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("label_map.json", "r") as f:
    label_map = json.load(f)
label_map = {int(k): v for k, v in label_map.items()}

# Loading book dataset
books_df = pd.read_csv("books.csv")

# User Choice
choice = st.radio("📌 What would you like to do?", ["Check genre of a book", "Get top books by genre"])

# Check Genre of a Book
if choice == "Check genre of a book":
    st.markdown("### 📖 Enter a Book Title")
    user_input = st.text_input("")

    if user_input:
        # Preprocess input
        sequence = tokenizer.texts_to_sequences([user_input])
        padded = pad_sequences(sequence, maxlen=15, padding='post')

        # Predict
        prediction = model.predict(padded)[0]
        pred_class = int(np.argmax(prediction))
        confidence = float(prediction[pred_class])

        st.success(f"📖 Predicted Genre: **{label_map[pred_class]}**")
        st.write(f"🎯 Confidence: `{confidence:.2f}`")

        amazon_link = f"https://www.amazon.in/s?k={'+'.join(user_input.split())}"
        st.markdown(f"[🔗 Search on Amazon]({amazon_link})")

        # Bar Graph of Genre Probabilities
        st.subheader("📊 Top 5 Genre Probabilities")
        probs = {label_map[i]: float(p) for i, p in enumerate(prediction)}
        top5 = sorted(probs.items(), key=lambda x: x[1], reverse=True)[:5]

        for genre, prob in top5:
            percentage = int(prob * 100)
            bar = "█" * (percentage // 3)
            st.markdown(f"**{genre}**: `{percentage}%`<br><span style='color:#6d4c41;'>{bar}</span>", unsafe_allow_html=True)

        # Genre-Based Recommendations
        matched_books = books_df[books_df['Main Genre'] == label_map[pred_class]].drop_duplicates("Title")
        if "suggestions" not in st.session_state:
            st.session_state.suggestions = matched_books.sample(5)

        st.subheader("📚 You may also like:")
        for _, row in st.session_state.suggestions.iterrows():
            st.markdown(f"🔹 **[{row['Title']}]({row['URLs']})** — ⭐ {row['Rating']}")

        if st.button("🔁 Show more suggestions"):
            st.session_state.suggestions = matched_books.sample(5)

# Show Top Books by Genre
else:
    genre_input = st.text_input("📚 Enter a Genre (e.g. Romance, Fantasy, History)")

    # Session state for genre-based paging
    if "genre_suggestion_index" not in st.session_state:
        st.session_state.genre_suggestion_index = 0

    if genre_input:
        genre_filter = genre_input.strip().lower()
        matched = books_df[books_df["Main Genre"].str.lower() == genre_filter]
        matched = matched.drop_duplicates("Title").sort_values(by="Rating", ascending=False)

        start = st.session_state.genre_suggestion_index
        end = start + 10
        top_books = matched.iloc[start:end]

        if top_books.empty:
            st.session_state.genre_suggestion_index = 0
            top_books = matched.iloc[0:10]

        st.markdown(f"### 🎯 Top Books in **{genre_input.title()}**")
        for _, row in top_books.iterrows():
            st.markdown(f"🔹 **[{row['Title']}]({row['URLs']})** — ⭐ {row['Rating']}")

        if st.button("🔁 Show More"):
            st.session_state.genre_suggestion_index += 10
