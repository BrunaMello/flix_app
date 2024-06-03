import requests
import streamlit as st

from login.service import logout


class GenreRepository:

	def __init__(self):
		self.__base_url = 'http://brunamello.pythonanywhere.com/api/v1/'
		self.__genres_url = f'{self.__base_url}genre/'

		# Set headers with token
		self.__headers = {
			'Authorization': f'Barer {st.session_state.token}'
		}

	def get_genres(self):
		response = requests.get(
			self.__genres_url,
			headers=self.__headers,
		)
		if response.status_code == 200:
			return response.json()
		if response.status_code == 401:
			logout()
			return None
		raise Exception(f'Error getting genres. Status Code: {response.status_code}')

	def create_genre(self, genre):
		response = requests.post(
			self.__genres_url,
			headers=self.__headers,
			data=genre,
		)
		if response.status_code == 201:
			return response.json()
		if response.status_code == 401:
			logout()
			return None
		raise Exception(f'Error getting genres. Status Code: {response.status_code}')
