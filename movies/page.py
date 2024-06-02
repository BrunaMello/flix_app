import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

file_path = 'movies/movies.csv'
movies = pd.read_csv(file_path)


def show_movies():
	st.write('Movie List:')

	AgGrid(
		data=movies,
		reload_data=True,
		key='genres_grid',
	)

	st.title('Add a new movie')
	name = st.text_input('Movie name')
	if st.button('Save'):
		st.success(f'Genre "{name}" saved successfully')
