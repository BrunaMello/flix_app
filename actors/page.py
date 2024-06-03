from datetime import datetime

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from actors.service import ActorService


def show_actors():
	actors_service = ActorService()
	actors = actors_service.get_actors()

	if actors:
		st.write('Actors List:')

		actors_df = pd.json_normalize(actors)

		AgGrid(
			data=actors_df,
			reload_data=True,
			key='actors_grid',
		)
	else:
		st.warning('No actors found')

	st.title('Add a new actor')

	name = st.text_input('Actor name')
	birthday = st.date_input(
		label='Birthday',
		value=datetime.today(),
		min_value=datetime(1600, 1, 1),
		max_value=datetime.today(),
		format='DD-MM-YYYY',
	)
	nationality_dropdown = ['BRAZIL', 'USA']
	nationality = st.selectbox(
		label='Nationality',
		options=nationality_dropdown,
	)

	if st.button('Save'):
		new_actor = actors_service.create_actor(
			name=name,
			birthday=birthday,
			nationality=nationality,
		)
		if new_actor:
			st.rerun()
		else:
			st.error('Error creating actor')
