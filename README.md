Here's a README for the "flix_app" project:

---

# Flix App

Flix App is a web application for exploring and reviewing movies, built using Streamlit. The app allows users to browse
through movies, view detailed information, read reviews, and add their own reviews. It also features a login system for
user authentication.

## Features

- **Home Page**: Displays a list of movies with options to filter by genre or search by title.
- **Movie Details**: Shows detailed information about the selected movie, including cast, genre, and reviews.
- **User Reviews**: Allows users to read and write reviews for movies.
- **Login/Logout**: User authentication to manage reviews and personalize the experience.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/BrunaMello/flix_app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd flix_app
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    streamlit run app.py
    ```

## Usage

- Visit the home page to browse movies.
- Click on a movie to see more details and reviews.
- Log in to write your own reviews.

## Project Structure

- `app.py`: Main file to run the Streamlit app.
- `actors/`: Contains actor-related functionalities.
- `api/`: Handles API requests.
- `genres/`: Manages movie genres.
- `home/`: Home page components.
- `login/`: User authentication components.
- `movies/`: Movie-related functionalities.
- `reviews/`: Handles user reviews.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

---
