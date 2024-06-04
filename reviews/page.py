import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from movies.service import MovieService
from reviews.service import ReviewService


def show_rate():
	review_service = ReviewService()
	reviews = review_service.get_reviews()

	if reviews:
		st.write('Rate List:')

		reviews_df = pd.json_normalize(reviews)

		AgGrid(
			data=reviews_df,
			reload_data=True,
			key='genres_grid',
			fit_columns_on_grid_load=True,
		)
	else:
		st.warning('No review found')

	st.title('Add a new review')

	movie_service = MovieService()
	movies = movie_service.get_movies()

	movie_titles = {movie['title']: movie['id'] for movie in movies}
	selected_movie_title = st.selectbox(
		label='Movie',
		options=list(movie_titles.keys()),
	)

	stars = st.number_input(
		min_value=0,
		max_value=5,
		label='Stars',
		step=1,
	)

	comment = st.text_area('Comment')

	if st.button('Save'):
		new_review = review_service.create_reviews(
			movie=movie_titles[selected_movie_title],
			stars=stars,
			comment=comment,
		)
		if new_review:
			st.rerun()
		else:
			st.error('Error creating review')
