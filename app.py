import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = requests.get ("https://api.themoviedb.org/3/movie/{}?api_key=88d2ef8d4d840cff4e811b4cc7a019b7&language=en-US".format(movie_id))
    data = url.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list= sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies ,recommended_movie_posters       
st.header('Recommend a movie')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('cosim.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movies,recommended_movie_posters = recommend(selected_movie)
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.text(recommended_movies[0])
        st.image(recommended_movie_posters[0])
    with c2:
        st.text(recommended_movies[1])
        st.image(recommended_movie_posters[1])

    with c3:
        st.text(recommended_movies[2])
        st.image(recommended_movie_posters[2])
    with c4:
        st.text(recommended_movies[3])
        st.image(recommended_movie_posters[3])
    with c5:
        st.text(recommended_movies[4])
        st.image(recommended_movie_posters[4])