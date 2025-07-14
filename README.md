# Deepesh's Book Genre Predictor Chatbot

[![Hugging Face Space](https://img.shields.io/badge/HuggingFace-Live_App-yellow?logo=huggingface)](https://huggingface.co/spaces/Deepesh120/deepesh-book-genre-bot)
[![View on GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/Deepesh456/book_genre_predictor_chatbot)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-success?logo=streamlit)](https://huggingface.co/spaces/Deepesh120/deepesh-book-genre-bot)

> A cozy, AI-powered chatbot that predicts the **genre of any book title** using an LSTM-based deep learning model. Also gives you **Top-rated Book Suggestions** by genre with Amazon links!

## Live Demo

Try it here:  
**[https://huggingface.co/spaces/Deepesh120/deepesh-book-genre-bot](https://huggingface.co/spaces/Deepesh120/deepesh-book-genre-bot)**


## Features

```

- Predict book genres using an LSTM model  
- Visualize top 5 genre probabilities  
- Get 5 book recommendations per genre (with “Show More”)  
- Instant Amazon links for each book  
- Dual functionality: Genre prediction **or** Top 10 books by genre  
- Cozy bookstore UI with background image and styled input

```

## How It Works

```

- User inputs book title or genre
- Title is tokenized using trained Keras tokenizer
- Model predicts genre via a TensorFlow SavedModel
- Top 5 class probabilities are sorted and visualized
- Metadata is matched for Amazon link & book suggestions

```

## Tech Stack
-------------------------------------------------------
|  Layer   |            Tools                         |
|----------|------------------------------------------|
| Model    | TensorFlow + Keras (LSTM)                |
| NLP      | Tokenizer, LabelEncoder                  |
| Frontend | Streamlit                                |
| Hosting  | Hugging Face Spaces                      |
| Dataset  | Amazon metadata                          |
-------------------------------------------------------

##  Project Structure

```
 book-genre-predictor-chatbot
├── streamlit_app.py
├── requirements.txt
├── books.csv
├── tokenizer_config.json
├── label_map.json
├── genre_model_tf/
├── book_genre_chatbot.ipynb
└── README.md
```

## Sample Output

### Option 1: Check Genre of a Book

```
Input: The Art of Quantum Computing

📖 Predicted Genre: Arts, Film & Photography  
🎯 Confidence: 0.12  
🔗 Search on Amazon

📊 Top 5 Genre Probabilities
Arts, Film & Photography: 0.12  
Business & Economics: 0.11  
Sciences, Technology & Medicine: 0.10  
Politics: 0.09  
Religion: 0.08

📚 You may also like:
🔹 The Power of Art — ⭐ 4.6  
🔹 The Photographer's Eye — ⭐ 4.5  
🔹 Drawing on the Right Side of the Brain — ⭐ 4.4

```

### 📘 Option 2: Get Top Books by Genre

```
Input Genre: Romance

🎯Top Books in Romance:
🔹 Me Before You — ⭐ 4.7  
🔹 The Notebook — ⭐ 4.6  
🔹 It Ends With Us — ⭐ 4.5  
🔹 The Fault in Our Stars — ⭐ 4.5  
🔹 Pride and Prejudice — ⭐ 4.4  
(more when you click "Show More")

```

## Run Locally

```
git clone https://github.com/Deepesh456/book-genre-predictor-chatbot.git  
cd book-genre-predictor-chatbot  
python -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
streamlit run app.py
```

## Author

**Deepeshkumar K**   
📧 deepeshkumark120@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/deepeshkumark)  
🔗 [GitHub](https://github.com/Deepesh456)

## Show Support

If you liked this project, feel free to ⭐ star the repo and share the Hugging Face link!
