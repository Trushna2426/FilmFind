# 🎬 FilmFind – Movie Recommendation System

FilmFind is a **content-based movie recommendation system** built using NLP techniques and transformer-based embeddings. It helps users discover similar movies based on the description of a movie they already like.
---

## 📚 Project Overview

This project uses the **TMDB 5000 Movie Dataset** to recommend movies based on semantic similarity between movie overviews. By using **Sentence Transformers**, it understands the meaning behind the descriptions and finds the most relevant matches — even if the keywords don’t exactly match.
---

## 🚀 Key Features
-  Recommends top 5 similar movies for any given title
-  Uses **BERT-based sentence embeddings** (`all-MiniLM-L6-v2`)
-  Caches embeddings to improve performance
-  Command-line interface (CLI) for user interaction
---
## 🧠 Model Used
- all-MiniLM-L6-v2 from sentence-transformers

## 🛠️ Tech Stack
1. Frontend: HTML, CSS
2. Backend: Flask (Python)
3. NLP: sentence-transformers
4. Libraries: pandas, numpy, scikit-learn
5. Dataset: TMDB 5000 Movie Dataset (CSV)
---
## 📁 Folder Structure
    
FilmFind/
├── static/
│ └── index.css 
├── templates/
│ ├── index.html 
│ └── recommendations.html 
├── movie_recommender.py  : Main Code
├── app.py                : Flask app and routes
├── movie_embeddings.npy  : Cached model output
├── tmdb_5000_movies.csv  : Dataset 
├── requirements.txt      : Python dependencies
└── README.md    
---
## ⚙️ Installation
1. 🔧 Requirements
Install the required packages using:  pip install -r requirements.txt

2. ▶️ Run the app
python app.py

3. 🛜 Access in Browser
http://127.0.0.1:5000
---

## 📌 Example Output
1. Homepage : This is the homepage where users can enter the name of a movie to get recommendations.
![Input Page](input_form.png.png)

2.Recommendations : This screen displays recommended movies as flash-style cards once a user submits their input.
![Recommendations Page](recommendations.png.png)
---

## 🧠 How It Works
1. Data Cleaning: Cleans the genre and overview fields in the dataset.
2. Embeddings: Uses a pre-trained transformer model to convert overviews into vectors.
3. Similarity Score: Calculates cosine similarity between embeddings to find the most similar movies.
4. Top Matches: Ranks and displays the top 5 recommendations (excluding the input movie itself).

---
## 🚀 What’s Coming Next
- 🎯 Add fuzzy search or autocomplete.
- 📊 Improve recommendation accuracy with more features (genre, cast).
- 🌐 Deploy the system to Render or Hugging Face Spaces.
- 📱 Make the layout fully responsive for mobile.
- 🧠 Replace static CSV with a real-time API like TMDB.

---

# 📦 Dataset
We use the TMDB 5000 Movie Dataset:  
You can download it directly from [Kaggle](https://www.kaggle.com/datasets/shruti79/tmdb-5000-movie-dataset).

Available at Kaggle

# 📚 Libraries Used
pandas
numpy
sentence-transformers
scikit-learn

# 🔐 License
This project is open-source and free to use under the MIT License.

👤 Author
Made by Trushna – learning & building through the MS AI NSI Internship – April 2025.
