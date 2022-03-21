import streamlit as st
import pandas as pd
import pickle
import requests

movies = pd.read_csv('movies.csv')
titles = movies['title'].values
cos_sim = pickle.load(open('cos_sim.pkl','rb'))

def poster(movie_id):
	response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=95dca92046a60652d899a8816ca278b1&language=en-US'.format(movie_id))
	data = response.json()
	return 'https://image.tmdb.org/t/p/original' + data['poster_path']



def top_5_movies(movie_title):
	index = movies[movies['title'] == movie_title].index[0]
	rec_movies = sorted(list(enumerate(cos_sim[index])),reverse= True,key = lambda x: x[1])[1:6]
	rec_movies_list = [];posters = []
	for i in rec_movies:
		movie_id = movies['movie_id'][i[0]]
		rec_movies_list.append(movies['title'][i[0]])
		posters.append(poster(movie_id))
	return rec_movies_list,posters

st.title('Movie Recommender System')

movie_name = st.selectbox('Choose your movie',titles)

if st.button('Recommend'):
	recs,posters = top_5_movies(movie_name)
	col1, col2, col3, col4, col5 = st.columns(5)
	with col1:
		st.text(recs[0])
		st.image(posters[0])
	with col2:
		st.text(recs[1])
		st.image(posters[1])
	with col3:
		st.text(recs[2])
		st.image(posters[2])
	with col4:
		st.text(recs[3])
		st.image(posters[3])
	with col5:
		st.text(recs[4])
		st.image(posters[4])