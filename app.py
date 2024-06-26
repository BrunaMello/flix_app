import streamlit as st

from actors.page import show_actors
from genres.page import show_genres
from home.page import show_home
from login.page import show_login
from movies.page import show_movies
from reviews.page import show_review


def main():
	if 'token' not in st.session_state:
		show_login()
	else:
		st.title("Flix App")

		menu_options = st.sidebar.selectbox(
			'Select one option',
			['Home', 'Genre', 'Actors', 'Movies', 'Reviews']
		)

		if menu_options == 'Home':
			show_home()

		if menu_options == 'Genre':
			show_genres()

		if menu_options == 'Actors':
			show_actors()

		if menu_options == 'Movies':
			show_movies()

		if menu_options == 'Reviews':
			show_review()


if __name__ == '__main__':
	main()
