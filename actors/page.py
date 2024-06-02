import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

file_path = 'actors/actors.csv'
actors = pd.read_csv(file_path)


def show_actors():
	st.write('Actors List:')

	AgGrid(
		data=actors,
		reload_data=True,
		key='genres_grid',
	)

	st.title('Add a new actor')
	name = st.text_input('Actor name')
	if st.button('Save'):
		st.success(f'Actor "{name}" saved successfully')
