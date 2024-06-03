import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from genres.service import GenreService


def show_genres():
	genre_services = GenreService()
	genres = genre_services.get_genres()

	if genres:

		st.write('Genres List:')

		# Convert genres to DataFrame
		genres_df = pd.json_normalize(genres)

		# Show genres in AgGrid
		AgGrid(
			data=genres_df,
			reload_data=True,
			key='genres_grid',
		)
	else:
		st.warning('No genres found')

	st.title('Add a new genre')
	name = st.text_input('Genre name')
	if st.button('Save'):
		new_genre = genre_services.create_genre(
			name=name,
		)
		if new_genre:
			st.rerun()
		else:
			st.error('Error creating genre')
