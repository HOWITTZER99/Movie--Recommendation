import json
from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

with open('movie.json', 'r') as f:
    movie_dict = json.load(f)
movies = pd.DataFrame(movie_dict)
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similar = cosine_similarity(vectors)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_content():
    movie = request.json['movie']
    movie_index = movies[movies['title']== movie].index[0]
    dist = similar[movie_index]
    movie_list = sorted(list(enumerate(dist)),reverse=True, key=lambda x:x[1])[1:6]
    movie_name = []
    for i in movie_list:
        movie_name.append(movies.iloc[i[0]].title)
    return jsonify(movie_name)

if __name__ == '__main__':
    app.run(debug=True)