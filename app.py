import streamlit as st
import tensorflow as tf
import pickle
import json
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json

# Load model
books_df = pd.read_csv("books.csv")
model = tf.saved_model.load("genre_model_tf")
infer = model.signatures["serving_default"]

# Load tokenizer
with open("tokenizer_config.json", "r") as f:
    tokenizer_json = f.read()
tokenizer = tokenizer_from_json(tokenizer_json)

# Load label map
with open("label_map.json", "r") as f:
    label_map = json.load(f)
label_map = {int(k): v for k, v in label_map.items()}

# App UI
st.set_page_config(page_title="📚 Book Genre Predictor", layout="centered")
st.title("📚 Book Genre Prediction Chatbot")
st.markdown("Enter a **book title** and get a predicted genre using Deep Learning (LSTM model).")

# Input
user_input = st.text_input("Enter Book Title")

if user_input:
    seq = tokenizer.texts_to_sequences([user_input])
    padded = pad_sequences(seq, maxlen=15, padding='post')

    result = infer(tf.constant(padded, dtype=tf.float32))
    prediction = list(result.values())[0].numpy()[0]

    pred_class = int(np.argmax(prediction))
    confidence = float(prediction[pred_class])
    
    st.success(f"📖 Predicted Genre: **{label_map[pred_class]}**")
    st.write(f"🎯 Confidence: `{confidence:.2f}`")

    matched = books_df[books_df['Title'].str.strip().str.lower() == user_input.strip().lower()]
    if not matched.empty:
        book_url = matched.iloc[0].get("URLs", "")
        if isinstance(book_url, str) and book_url.strip().startswith("http"):
            st.markdown(f"🔗 [View on Amazon]({book_url.strip()})")
        else:
            st.info("ℹ️ No valid Amazon link found for this book.")


    st.subheader("📊 Top 5 Genre Probabilities")
    probs = {label_map[i]: float(prob) for i, prob in enumerate(prediction)}
    top_probs = sorted(probs.items(), key=lambda x: x[1], reverse=True)[:5]
    for genre, prob in top_probs:
        st.write(f"{genre}: {prob:.2f}")
