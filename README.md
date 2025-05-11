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
## 🔧 Requirements
Install the required packages using:  pip install -r requirements.txt
---
## ▶️ How to Run
python movie_recommender.py 
---
## 📌 Example Output
=== Movie Recommendation System ===
Enter a movie title: Avatar        

Top recommendations for 'Avatar':

🎬 Alien: Resurrection
   Two hundred years after Lt. Ripley died, a group of scientists clone her, hoping to breed the ultimate weapon. But the new Ripley is full of surprises … as are the new aliens. Ripley must team with a band of smugglers to keep the creatures from reaching Earth.

🎬 The Black Hole
   The explorer craft U.S.S. Palomino is returning to Earth after a fruitless 18-month search for extra-terrestrial life when the crew comes upon a supposedly lost ship, the magnificent U.S.S. Cygnus, hovering near a black hole. The ship is controlled by Dr. Hans Reinhardt and his monstrous robot companion, Maximillian. But the initial wonderment and awe the Palomino crew feel for the ship and its resistance to the power of the black hole turn to horror as they uncover Reinhardt's plans.

🎬 Serenity
   When the renegade crew of Serenity agrees to hide a fugitive on their ship, they find themselves in an action-packed battle between the relentless military might of a totalitarian regime who will destroy anything – or anyone – to get the girl back and the bloodthirsty creatures who roam the uncharted areas of space. But... the greatest danger of all may be on their ship.

🎬 Aliens
   When Ripley's lifepod is found by a salvage crew over 50 years later, she finds that terra-formers are on the very planet they found the alien species. When the company sends a family of colonists out to investigate her story, all contact is lost with the planet and colonists. They enlist Ripley and the colonial marines to return and search for answers.

🎬 Supernova
   Set in the 22nd century, when a battered salvage ship sends out a distress signal, the seasoned crew of the rescue hospital ship Nova-17 responds. What they find is a black hole--that threatens to destroy both ships--and a mysterious survivor whose body quickly mutates into a monstrous and deadly form.
---

## 🧠 How It Works
1. Data Cleaning: Cleans the genre and overview fields in the dataset.
2. Embeddings: Uses a pre-trained transformer model to convert overviews into vectors.
3. Similarity Score: Calculates cosine similarity between embeddings to find the most similar movies.
4. Top Matches: Ranks and displays the top 5 recommendations (excluding the input movie itself).

# 📦 Dataset
We use the TMDB 5000 Movie Dataset:
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
