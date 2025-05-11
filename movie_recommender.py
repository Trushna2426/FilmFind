import pandas as pd
import ast
import os 
import numpy as np
os.environ["USE_TF"] = "0"

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the CSV file (update path if needed)
df = pd.read_csv("tmdb_5000_movies.csv")

# Display the first few rows
print("Sample Data:")
print(df.head())

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display info about data types and nulls
print("\nDataset Info:")
print(df.info())

# Function to extract genre names from the JSON-like string
def extract_genre_names(genre_str):
    try:
        genres = ast.literal_eval(genre_str)
        return [genre['name'] for genre in genres]
    except:
        return []

# Apply the function to the 'genres' column
df['genres_cleaned'] = df['genres'].apply(extract_genre_names)

# Display a few rows to check
print("\nCleaned Genres:")
print(df[['title', 'genres_cleaned']].head())

# Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Fill missing overviews with empty strings
df['overview'] = df['overview'].fillna('')
# Clean the overview text 
def clean_text(text):
    return str(text).lower().strip()

df['cleaned_overview'] = df['overview'].apply(lambda x: str(x).lower().strip())

EMBEDDINGS_PATH = "movie_embeddings.npy"

# If embeddings already exist, load them
if os.path.exists(EMBEDDINGS_PATH):
    print("Loading precomputed embeddings...")
    embeddings = np.load(EMBEDDINGS_PATH)
else:
    print("Generating embeddings (first-time only)...")
    # Generate embeddings from cleaned overviews
    embeddings = model.encode(df['cleaned_overview'].tolist(), show_progress_bar=True)
    np.save(EMBEDDINGS_PATH, embeddings)
    print("Embeddings saved to file.")


# Function to get recommendations
def recommend_movies(movie_title, top_n=5):
    movie_title = movie_title.strip().lower()
    df['title_lower'] = df['title'].str.lower()

    if movie_title not in df['title_lower'].values:
        return pd.DataFrame()

    idx = df[df['title_lower'] == movie_title].index[0]

    similarity_scores = cosine_similarity(
        [embeddings[idx]], embeddings
    )[0]

    similar_indices = similarity_scores.argsort()[::-1][1:top_n + 1]
    return df.iloc[similar_indices][['title', 'overview']]
print("\nRecommended Movies:")
recommendations = recommend_movies("Avatar", top_n=5)
print(recommendations)


def main():
    print("=== Movie Recommendation System ===")
    user_title = input("Enter a movie title: ")

    print(f"\nTop recommendations for '{user_title}':\n")
    recommendations = recommend_movies(user_title, top_n=5)

    if recommendations is not None and not recommendations.empty:
        for idx, row in recommendations.iterrows():
            print(f"🎬 {row['title']}\n   {row['overview']}\n")
    else:
        print("No recommendations found.")

if __name__ == "__main__":
    main()

