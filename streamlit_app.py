import json
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit.components.v1 as components

# Set the background image
background_image = "movie.png"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url({background_image});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Set the theme to light
st.beta_set_theme("light")

# Add a heading
st.title("Movie Recommender created by Parth Kulkarni")

# Load the movie dataset
with open('movie.json', 'r') as f:
    movie_dict = json.load(f)
movies = pd.DataFrame(movie_dict)

# Create the count vectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Calculate the cosine similarity
similar = cosine_similarity(vectors)

# Define the function to recommend movies
def recommend_content(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dist = similar[movie_index]
    movie_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]
    movie_name = []
    for i in movie_list:
        movie_name.append(movies.iloc[i[0]].title)
    return movie_name

# Add the form to input a movie title
with st.form(key='movie_form'):
    movie_input = st.text_input('Enter a movie title')
    submit_button = st.form_submit_button(label='Recommend')

# If the form is submitted, recommend movies
if submit_button:
    recommended_movies = recommend_content(movie_input)
    st.write('Recommended movies:')
    st.write(json.dumps(recommended_movies))