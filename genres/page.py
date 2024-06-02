import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

genres = [
	{'id': 1, 'name': 'Action'},
	{'id': 2, 'name': 'Adventure'},
	{'id': 3, 'name': 'Comedy'},
	{'id': 4, 'name': 'Drama'},
	{'id': 5, 'name': 'Horror'},
	{'id': 6, 'name': 'Mystery'},
	{'id': 7, 'name': 'Sci-Fi'},
	{'id': 8, 'name': 'Thriller'},
]


def show_genres():
	st.write('Genres List:')

	AgGrid(
		data=pd.DataFrame(genres),
		reload_data=True,
		key='genres_grid',
	)

	st.title('Add a new genre')
	name = st.text_input('Genre name')
	if st.button('Save'):
		st.success(f'Genre "{name}" saved successfully')
