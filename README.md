# Recommendation-System

 Test My Application:
 
 streamlitt deployment:
https://howittzer99-movie--recommendation-streamlit-app-embhj7.streamlit.app/
 
This machine learning project is a Flask Web Application that uses collaborative item-to-item filtering to recommend suitable movies based on user’s rating of a previously watched movie.

![image](https://repository-images.githubusercontent.com/275336521/20d38e00-6634-11eb-9d1f-6a5232d0f84f)

## About  
This Content Based Filtering Movie Recommender is built on a [flask app](https://flask.palletsprojects.com/en/2.0.x/) using Python programming language and JavaScript programming language. Two snippets of code were created using the concept of CB. The first one is in Python programming language using the package “scikit-learn” and the second snippet of code is in JavaScript programming language which uses no packages and operates based on logic. Here, feature extraction methods and distance metrics are utilised to generate recommendations. 

Dataset: TMDB 5000

### Distance metric
The distance metric used in this recommender is Cosine Similarity. Cosine Similarity computes the similarity of items by measuring the cosine of the angle between two vectors projected in a multidimensional vector space. With Cosine Similarity, non-binary vector values are taken into consideration during calculation as the values directly influence the position of the vector. Cosine Similarity focuses on the contents of the items and disregards the size of the items. Hence, Cosine Similarity is suitable for text documents with different word counts. 

![image](https://user-images.githubusercontent.com/65379600/129465404-790cbc28-ee78-4c2f-85c8-e40f82ac72d6.png)   ![image](https://user-images.githubusercontent.com/65379600/129466224-5b165535-f7be-4378-a8bb-0438d4e60574.png)

### Python Code
The python code in app.py will generate a list of movie recommendations provided that the user entered a valid movie name. When the entered movie name matches with a movie name in the dataset, recommendations will be generated according to the soup column (all details concatenated into one string) of each movie. In this set of code, the TF-IDF Vectorizer and Cosine Similarity function is imported from the “scikit-learn” package.

### Javascript Code
The javascript code in notfound.html is executed when the user entered an invalid movie name. This set of code will return movie titles that are similar to the input that the user has entered, if applicable. The entered data will be checked against all existing movie names to find the most similar movie names. Since this snippet of code doesn't use any packages, a dictionary was created to store the terms for vectorising purposes and several functions were also created to compute the TF-IDF and Cosine Similarity values.

 
 run locally using dockers:
 ```
 docker pull parthkulkarni/recsys:app
 docker pull parthkulkarni/recsys:frontend
 ```
 ```
 docker run -d --name rec_project_app parthkulkarni/recsys:app
 docker run -d --name rec_project_frontend -p 80:80 parthkulkarni/recsys:frontend
 ```
 Visit https://localhost in your web browser to confirm that the application is running correctly.

## Setup locally without dockers

download this repository

activate environment and install requirements (windows):
```
python -m venv venv
.\venv\scripts\activate
python -m pip install -r requirements.txt 
```

run flask app locally:
```
set FLASK_APP=my_app.py
set FLASK_ENV=development
flask run
```
