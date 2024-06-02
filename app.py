import streamlit as st

from genres.page import show_genres


def main():
	st.title("Flix App")

	menu_options = st.sidebar.selectbox(
		'Select one option',
		['Home', 'Genre', 'Actors', 'Movies', 'Rate']
	)

	if menu_options == 'Home':
		st.write('Welcome to Flix App')

	if menu_options == 'Genre':
		show_genres()

	if menu_options == 'Actors':
		st.write('Actors')

	if menu_options == 'Movies':
		st.write('Movies')

	if menu_options == 'Rate':
		st.write('Rate')


if __name__ == '__main__':
	main()
