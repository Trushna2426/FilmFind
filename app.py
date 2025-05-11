from flask import Flask, render_template, request, jsonify
import pandas as pd
from movie_recommender import recommend_movies  

# Initialize Flask app
app = Flask(__name__)

# Load the dataset_
df = pd.read_csv("tmdb_5000_movies.csv")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    movie_title = request.form.get('movie_title')
    
    if movie_title:
        recommendations = recommend_movies(movie_title, top_n=5)
        
        if recommendations is not None and not recommendations.empty:
            return render_template('recommendations.html', recommendations=recommendations.to_dict(orient="records"))
        else:
            return render_template('recommendations.html', recommendations=[], error=f"  '{movie_title}' not found.")
    return render_template('recommendations.html', recommendations=[], error="Please enter a movie title.")

if __name__ == '__main__':
    app.run(debug=True)
