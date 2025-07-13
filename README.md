# Book Genre Prediction Chatbot

[![Hugging Face Space](https://img.shields.io/badge/HuggingFace-Live_App-yellow?logo=huggingface)](https://huggingface.co/spaces/Deepesh120/deepesh-book-genre-bot)
[![View on GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/Deepesh456/book_genre_predictor_chatbot)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-success?logo=streamlit)](https://huggingface.co/spaces/Deepesh120/deepesh-book-genre-bot)

> A real-time chatbot that predicts a book's genre from its title using an LSTM deep learning model. Built with TensorFlow, deployed using Streamlit, and hosted live on Hugging Face Spaces.

## Live Demo

Try it here:  
**[https://huggingface.co/spaces/Deepesh120/deepesh-book-genre-bot](https://huggingface.co/spaces/Deepesh120/deepesh-book-genre-bot)**

Just type a book title like:

```
The Alchemist  
Harry Potter and the Prisoner of Azkaban  
The Art of Quantum Computing
```

And get instant predictions + confidence scores + Amazon link!

## Features

- Input: Just the book title  
- Model: LSTM-based neural network using Keras + TensorFlow  
- Output: Top genre prediction with confidence score  
- Top 5 genre probabilities  
- Links to Amazon (if matched)  
- Streamlit UI, deployed via Hugging Face Spaces

## How It Works

1. Tokenization of title with trained tokenizer  
2. Genre prediction using a TensorFlow SavedModel  
3. Post-processing: confidence scores, label decoding  
4. Amazon link display if matched in metadata

## Tech Stack
------------------------------------------------------
|  Layer  |            Tools                         |
|---------|------------------------------------------|
| Model   | TensorFlow + Keras (LSTM)                |
| NLP     | Tokenizer, LabelEncoder                  |
| UI      | Streamlit                                |
| Hosting | Hugging Face Spaces                      |
| Dataset | Custom + goodbooks-10k + Amazon metadata |
------------------------------------------------------

##  Project Structure

```
 book-genre-predictor-chatbot
├── app.py
├── requirements.txt
├── books.csv
├── tokenizer_config.json
├── label_map.json
├── genre_model_tf/
├── book_genre_chatbot.ipynb
└── README.md
```

## Sample Output

```
Input: The Art of Quantum Computing

Predicted Genre: Arts, Film & Photography  
Confidence: 0.12  
View on Amazon (if matched in dataset)

Top 5 Genres:
- Arts, Film & Photography: 0.12  
- Business & Economics: 0.11  
- Sciences, Technology & Medicine: 0.10  
- Politics: 0.09  
- Religion: 0.08
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
