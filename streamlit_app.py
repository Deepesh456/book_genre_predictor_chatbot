import streamlit as st
import keras
import pickle
import json
import numpy as np
from keras.preprocessing.sequence import pad_sequences

# Load model
model = keras.models.load_model("genre_model.h5")

# Load tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Load label map
with open("label_map.json", "r") as f:
    label_map = json.load(f)
label_map = {int(k): v for k, v in label_map.items()}

# App title
st.title("📚 Book Genre Prediction Chatbot")
st.markdown("Enter a **book title** and get a predicted genre using Deep Learning (LSTM model).")

# User input
user_input = st.text_input("Enter a Book Title")

if user_input:
    # Preprocess input
    sequence = tokenizer.texts_to_sequences([user_input])
    padded = pad_sequences(sequence, maxlen=15, padding='post')
    
    # Predict
    prediction = model.predict(padded)[0]
    predicted_class = int(np.argmax(prediction))
    confidence = float(prediction[predicted_class])

    # Show result
    st.success(f"📖 Predicted Genre: **{label_map[predicted_class]}**")
    st.write(f"🎯 Confidence: `{confidence:.2f}`")

    # Optional Amazon link
    amazon_link = f"https://www.amazon.in/s?k={'+'.join(user_input.split())}"
    st.markdown(f"[🔗 Search on Amazon]({amazon_link})")

    # Show only top 5 genre probabilities
    st.subheader("📊 Top 5 Genre Probabilities")
    probs = {label_map[i]: float(pred) for i, pred in enumerate(prediction)}
    top_probs = sorted(probs.items(), key=lambda x: x[1], reverse=True)[:5]

    for genre, prob in top_probs:
        st.write(f"{genre}: {prob:.2f}")
