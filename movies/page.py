from datetime import datetime

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService


def show_movies():
	movie_service = MovieService()
	movies = movie_service.get_movies()

	if movies:
		st.write('Movie List:')

		movies_df = pd.json_normalize(movies)

		# Remove columns that are not needed
		movies_df = movies_df.drop(columns=['actors', 'genre.id'])

		AgGrid(
			data=movies_df,
			reload_data=True,
			key='movies_grid',

		)
	else:
		st.warning('No movies found')

	st.title('Add a new movie')

	title = st.text_input('Movie name')

	release_date = st.date_input(
		label='Release Date',
		value=datetime.today(),
		min_value=datetime(1600, 1, 1).date(),
		max_value=datetime.today(),
		format='DD-MM-YYYY',
	)

	genre_service = GenreService()
	genres = genre_service.get_genres()

	# Create a dictionary with genre names as keys and genre ids as values
	genre_names = {genre['name']: genre['id'] for genre in genres}

	# Create a list with genre names
	selected_genre_name = st.selectbox(
		label='Genre',
		options=list(genre_names.keys()),
	)

	actors_service = ActorService()
	actors = actors_service.get_actors()

	# Create a dictionary with genre names as keys and genre ids as values
	actor_names = {actor['name']: actor['id'] for actor in actors}

	# Create a list with genre names
	selected_actors_names = st.multiselect(
		label='Actors',
		options=list(actor_names.keys()),
	)

	# Create a list with genre ids
	selected_actors_ids = [actor_names[name] for name in selected_actors_names]

	resume = st.text_area('Resume')

	if st.button('Save'):
		new_movie = movie_service.create_movie(
			title=title,
			release_date=release_date,
			genre=genre_names[selected_genre_name],
			actors=selected_actors_ids,
			resume=resume,
		)
		if new_movie:
			st.rerun()
		else:
			st.error('Error creating movie')
