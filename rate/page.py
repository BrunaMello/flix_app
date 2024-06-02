import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

file_path = 'rate/rate.csv'
rate = pd.read_csv(file_path)


def show_rate():
	st.write('Rate List:')

	AgGrid(
		data=rate,
		reload_data=True,
		key='genres_grid',
		fit_columns_on_grid_load=True,
	)
