# import streamlit as st
# from processing import preprocess
# from processing.display import Main
# import pandas as pd
# import requests

# # Page configuration
# st.set_page_config(
#     page_title="Movie Recommender",
#     layout="wide",  # Changed to 'wide' for a broader layout
#     page_icon="",
# )

# # Custom CSS for styling
# st.markdown(
#     """
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
#     html, body, [class*="css"] {
#         font-family: 'Poppins', sans-serif;
#         background-image: url('https://images.unsplash.com/photo-1685495856559-5d96a0e51acb?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'); /* URL of your background image */
#         background-size: cover; /* Ensure it covers the entire page */
#         background-attachment: fixed; /* Fixed background on scroll */
#         color: #ffffff; /* Light text color for better readability */
#     }
#     .stButton>button {
#         color: #ffffff;
#         border: none;
#         border-radius: 20px;
#         background-color: #6C63FF; /* Stylish purple background for buttons */
#         padding: 0.5rem 1rem;
#         font-weight: 600;
#     }
#     .stButton>button:hover {
#         background-color: #FFC107; /* Gold color on hover */
#     }
#     .main-container {
#         margin: auto;
#         padding: 2rem;
#         border-radius: 20px;
#         background-color: rgba(255, 255, 255, 0.15); /* Slightly transparent white for content background */
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Soft shadow for depth */
#     }
#     .title {
#         text-align: center;
#         font-weight: 700;
#         color: #FFC107; /* Gold color for titles */
#         margin-bottom: 2rem;
#     }
#     .section {
#         margin-top: 2rem;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Initialize session state variables
# if "selected_movie_name" not in st.session_state:
#     st.session_state["selected_movie_name"] = None

# # TMDB API key
# TMDB_API_KEY = "6bc3065293c944b5ad11cb7cd15c076e"

# def fetch_posters(movie_id):
#     """
#     Fetch the poster URL for a given movie ID using TMDB API.
#     """
#     response = requests.get(
#         f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
#     )
#     data = response.json()
#     try:
#         return f"https://image.tmdb.org/t/p/w780/{data['poster_path']}"
#     except KeyError:
#         return "https://via.placeholder.com/150"

# def display_movie_details(selected_movie_name):
#     """
#     Display details for the selected movie.
#     """
#     st.markdown("<div class='section main-container'>", unsafe_allow_html=True)
#     st.title(f"🎥 Details for {selected_movie_name}")

#     try:
#         info = preprocess.get_details(selected_movie_name)
#         if not info:
#             st.warning("Details not available for the selected movie.")
#             return

#         image_col, text_col = st.columns((1, 2))
#         with image_col:
#             st.image(info[0], width=210)  # Poster

#         with text_col:
#             st.subheader(selected_movie_name)
#             st.text(f"Rating: {info[8]} | Runtime: {info[6]}")
#             st.write("Overview:")
#             st.write(info[3])

#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.text("Genres:")
#                 st.write(", ".join(info[2]))
#             with col2:
#                 st.text("Release Date:")
#                 st.write(info[4])
#             with col3:
#                 st.text("Director:")
#                 st.write(", ".join(info[12]))
            

#     except Exception as e:
#         st.error(f"Error fetching movie details: {e}")
#     st.markdown("</div>", unsafe_allow_html=True)

# def recommend_display(new_df, selected_movie_name):
#     """
#     Display movie recommendations for the selected movie.
#     """
#     st.markdown("<div class='section main-container'>", unsafe_allow_html=True)
#     st.subheader(f"Recommended Movies for '{selected_movie_name}'")
#     st.write("---")
#     try:
#         movies, posters = preprocess.recommend(new_df, selected_movie_name, r"Files/similarity_tags_tags.pkl")
#         for i in range(0, len(movies), 4):
#             cols = st.columns(4)
#             for j, col in enumerate(cols):
#                 if i + j < len(movies):
#                     with col:
#                         st.image(posters[i + j], width=210)
#                         if st.button(movies[i + j], key=f"movie_{movies[i + j]}_{i + j}"):
#                             st.session_state["selected_movie_name"] = movies[i + j]
#                             st.experimental_rerun()
#     except Exception as e:
#         st.error(f"Error fetching recommendations: {e}")
#     st.markdown("</div>", unsafe_allow_html=True)

# def main():
#     """
#     Main function to run the app.
#     """
#     with Main() as bot:
#         bot.main_()
#         new_df, movies, _ = bot.getter()

#         st.markdown("<h1 class='title'> Movies4u</h1>", unsafe_allow_html=True)
#         st.markdown("<div class='main-container'>", unsafe_allow_html=True)

#         # Search box for movie input
#         search_query = st.text_input("Enter the movie name:")

#         # Search button
#         search_button = st.button("Search")

#         if search_button:
#             if search_query:
#                 movie_found = new_df[new_df["title"].str.contains(search_query, case=False, na=False)]
#                 if not movie_found.empty:
#                     st.session_state["selected_movie_name"] = movie_found["title"].iloc[0]
#                     st.experimental_rerun()
#                 else:
#                     st.error("Movie not found. Please try another name.")
#             else:
#                 st.warning("Please enter a movie name before clicking 'Search'.")

#         if st.session_state["selected_movie_name"]:
#             display_movie_details(st.session_state["selected_movie_name"])
#             recommend_display(new_df, st.session_state["selected_movie_name"])


    

# if __name__ == "__main__":
#     main()

































# import streamlit as st
# from processing import preprocess
# from processing.display import Main
# import pandas as pd
# import requests

# # Page configuration
# st.set_page_config(
#     page_title="Movie Recommender",
#     layout="wide",
#     page_icon="",
# )

# # Custom CSS for styling
# st.markdown(
#     """
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
#     html, body, [class*="css"] {
#         font-family: 'Poppins', sans-serif;
#         background-size: cover;
#         background-attachment: fixed;
#         color: #ffffff;
#     }
#     .stButton>button {
#         color: #ffffff;
#         border: none;
#         border-radius: 20px;
#         background-color: #6C63FF;
#         padding: 0.5rem 1rem;
#         font-weight: 600;
#     }
#     .stButton>button:hover {
#         background-color: #FFC107;
#     }
#     .main-container {
#         margin: auto;
#         padding: 2rem;
#         border-radius: 20px;
#         background-color: rgba(255, 255, 255, 0.15);
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#     }
#     .title {
#         text-align: center;
#         font-weight: 700;
#         color: #FFC107;
#         margin-bottom: 2rem;
#     }
#     .section {
#         margin-top: 2rem;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Initialize session state variables
# if "selected_movie_name" not in st.session_state:
#     st.session_state["selected_movie_name"] = None

# if "default_movies" not in st.session_state:
#     st.session_state["default_movies"] = None

# # TMDB API key
# TMDB_API_KEY = "6bc3065293c944b5ad11cb7cd15c076e"

# def fetch_posters(movie_id):
#     """
#     Fetch the poster URL for a given movie ID using TMDB API.
#     """
#     response = requests.get(
#         f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
#     )
#     data = response.json()
#     try:
#         return f"https://image.tmdb.org/t/p/w780/{data['poster_path']}"
#     except KeyError:
#         return "https://via.placeholder.com/150"

# def display_movie_details(selected_movie_name):
#     """
#     Display details for the selected movie.
#     """
#     st.title(f" Details for {selected_movie_name}")

#     try:
#         info = preprocess.get_details(selected_movie_name)
#         if not info:
#             st.warning("Details not available for the selected movie.")
#             return

#         image_col, text_col = st.columns((1, 2))
#         with image_col:
#             st.image(info[0], width=210)

#         with text_col:
#             st.subheader(selected_movie_name)
#             st.text(f"Rating: {info[8]} | Runtime: {info[6]}")
#             st.write("Overview:")
#             st.write(info[3])

#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.text("Genres:")
#                 st.write(", ".join(info[2]))
#             with col2:
#                 st.text("Release Date:")
#                 st.write(info[4])
#             with col3:
#                 st.text("Director:")
#                 st.write(", ".join(info[12]))
#     except Exception as e:
#         st.error(f"Error fetching movie details: {e}")

# def recommend_display(new_df, selected_movie_name):
#     """
#     Display movie recommendations for the selected movie.
#     """
#     st.markdown("<div class='section main-container'>", unsafe_allow_html=True)
#     st.subheader(f"Recommended Movies for '{selected_movie_name}'")
#     st.write("---")
#     try:
#         movies, posters = preprocess.recommend(new_df, selected_movie_name, r"Files/similarity_tags_tags.pkl")
#         for i in range(0, len(movies), 4):
#             cols = st.columns(4)
#             for j, col in enumerate(cols):
#                 if i + j < len(movies):
#                     with col:
#                         st.image(posters[i + j], width=250)
#                         if st.button(movies[i + j], key=f"movie_{movies[i + j]}_{i + j}"):
#                             st.session_state["selected_movie_name"] = movies[i + j]
#                             st.experimental_rerun()
#     except Exception as e:
#         st.error(f"Error fetching recommendations: {e}")
#     st.markdown("</div>", unsafe_allow_html=True)

# def display_home_page(new_df):
#     """
#     Display a list of default movies on the home page.
#     """
#     if st.session_state["default_movies"] is None:
#         st.session_state["default_movies"] = new_df.sample(100)  # Generate once and store in session state

#     default_movies = st.session_state["default_movies"]

#     for i in range(0, len(default_movies), 5):  # Display in rows of 5
#         cols = st.columns(4)
#         for j, col in enumerate(cols):
#             if i + j < len(default_movies):
#                 movie_title = default_movies.iloc[i + j]["title"]
#                 movie_id = default_movies.iloc[i + j]["movie_id"]
#                 with col:
#                     st.image(fetch_posters(movie_id), width=250)
#                     if st.button(movie_title, key=f"movie_{movie_title}_{i+j}"):
#                         st.session_state["selected_movie_name"] = movie_title
#                         st.experimental_rerun()

# def main():
#     """
#     Main function to run the app.
#     """
#     with Main() as bot:
#         bot.main_()
#         new_df, movies, _ = bot.getter()

#         st.markdown("<h1 class='title'> Welcome to Movies4u </h1>", unsafe_allow_html=True)

#         # Center the search bar and button
#         #st.markdown("<div class='section main-container'>", unsafe_allow_html=True)

#         # Add vertical spacing for centering
#         st.write("\n" * 6)

#         # Create columns to align search bar and button
#         search_col1, search_col2 = st.columns([3, 1])

#         with search_col1:
#             search_query = st.text_input("Enter the movie name:", label_visibility="collapsed")

#         with search_col2:
#             search_button = st.button("Search", use_container_width=True)

#         # Process the search query
#         if search_button:
#             if search_query:
#                 movie_found = new_df[new_df["title"].str.contains(search_query, case=False, na=False)]
#                 if not movie_found.empty:
#                     st.session_state["selected_movie_name"] = movie_found["title"].iloc[0]
#                     st.experimental_rerun()
#                 else:
#                     st.error("Movie not found. Please try another name.")
#             else:
#                 st.warning("Please enter a movie name before clicking 'Search'.")

#         if st.session_state["selected_movie_name"]:
#             display_movie_details(st.session_state["selected_movie_name"])
#             recommend_display(new_df, st.session_state["selected_movie_name"])
#         else:
#             display_home_page(new_df)

# if __name__ == "__main__":
#     main()









# import streamlit as st
# from processing import preprocess
# from processing.display import Main
# import pandas as pd
# import requests

# # Page configuration
# st.set_page_config(
#     page_title="Movie Recommender",
#     layout="wide",
#     page_icon="",
# )

# # Custom CSS for styling and disabling image expand
# st.markdown(
#     """
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
#     html, body, [class*="css"] {
#         font-family: 'Poppins', sans-serif;
#         background-size: cover;
#         background-attachment: fixed;
#         color: #ffffff;
#     }
#     .stButton>button {
#         color: #ffffff;
#         border: none;
#         border-radius: 20px;
#         background-color: #6C63FF;
#         padding: 0.5rem 1rem;
#         font-weight: 600;
#     }
#     .stButton>button:hover {
#         background-color: #FFC107;
#     }
#     .main-container {
#         margin: auto;
#         padding: 2rem;
#         border-radius: 20px;
#         background-color: rgba(255, 255, 255, 0.15);
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#     }
#     .title {
#         text-align: center;
#         font-weight: 700;
#         color: #FFC107;
#         margin-bottom: 2rem;
#     }
#     .section {
#         margin-top: 2rem;
#     }
#     .no-hover:hover {
#         pointer-events: none;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Initialize session state variables
# if "selected_movie_name" not in st.session_state:
#     st.session_state["selected_movie_name"] = None

# if "default_movies" not in st.session_state:
#     st.session_state["default_movies"] = None

# # TMDB API key
# TMDB_API_KEY = "6bc3065293c944b5ad11cb7cd15c076e"

# def fetch_posters(movie_id):
#     """
#     Fetch the poster URL for a given movie ID using TMDB API.
#     """
#     response = requests.get(
#         f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
#     )
#     data = response.json()
#     try:
#         return f"https://image.tmdb.org/t/p/w780/{data['poster_path']}"
#     except KeyError:
#         return "https://via.placeholder.com/150"

# def display_movie_details(selected_movie_name):
#     """
#     Display details for the selected movie.
#     """
#     st.title(f" {selected_movie_name}  details")

#     try:
#         info = preprocess.get_details(selected_movie_name)
#         if not info:
#             st.warning("Details not available for the selected movie.")
#             return

#         image_col, text_col = st.columns((1, 2))
#         with image_col:
#             st.markdown(
#                 f"<img class='no-hover' src='{info[0]}' style='width: 210px; border-radius: 10px;'>",
#                 unsafe_allow_html=True,
#             )

#         with text_col:
#             st.subheader(selected_movie_name)
#             st.text(f"Rating: {info[8]} | Runtime: {info[6]}")
#             st.write("Overview:")
#             st.write(info[3])

#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.text("Genres:")
#                 st.write(", ".join(info[2]))
#             with col2:
#                 st.text("Release Date:")
#                 st.write(info[4])
#             with col3:
#                 st.text("Director:")
#                 st.write(", ".join(info[12]))
#     except Exception as e:
#         st.error(f"Error fetching movie details: {e}")

# def recommend_display(new_df, selected_movie_name):
#     """
#     Display movie recommendations for the selected movie.
#     """
#     st.markdown("<div class='section main-container'>", unsafe_allow_html=True)
#     st.subheader(f"Similar Movies like '{selected_movie_name}'")
#     st.write("---")
#     try:
#         movies, posters = preprocess.recommend(new_df, selected_movie_name, r"Files/similarity_tags_tags.pkl")
#         for i in range(0, len(movies), 4):
#             cols = st.columns(4)
#             for j, col in enumerate(cols):
#                 if i + j < len(movies):
#                     with col:
#                         st.markdown(
#                             f"<img class='no-hover' src='{posters[i+j]}' style='width: 250px; border-radius: 10px;'>",
#                             unsafe_allow_html=True,
#                         )
#                         if st.button(movies[i + j], key=f"movie_{movies[i + j]}_{i + j}"):
#                             st.session_state["selected_movie_name"] = movies[i + j]
#                             st.experimental_rerun()
#     except Exception as e:
#         st.error(f"Error fetching recommendations: {e}")
#     st.markdown("</div>", unsafe_allow_html=True)

# def display_home_page(new_df):
#     """
#     Display a list of default movies on the home page.
#     """
#     if st.session_state["default_movies"] is None:
#         st.session_state["default_movies"] = new_df.sample(100)  # Generate once and store in session state

#     default_movies = st.session_state["default_movies"]

#     for i in range(0, len(default_movies), 5):  # Display in rows of 5
#         cols = st.columns(4)
#         for j, col in enumerate(cols):
#             if i + j < len(default_movies):
#                 movie_title = default_movies.iloc[i + j]["title"]
#                 movie_id = default_movies.iloc[i + j]["movie_id"]
#                 with col:
#                     st.markdown(
#                         f"<img class='no-hover' src='{fetch_posters(movie_id)}' style='width: 250px; border-radius: 10px;'>",
#                         unsafe_allow_html=True,
#                     )
#                     if st.button(movie_title, key=f"movie_{movie_title}_{i+j}"):
#                         st.session_state["selected_movie_name"] = movie_title
#                         st.experimental_rerun()

# def main():
#     """
#     Main function to run the app.
#     """
#     with Main() as bot:
#         bot.main_()
#         new_df, movies, _ = bot.getter()

#         st.markdown("<h1 class='title'> Welcome to Movies4u </h1>", unsafe_allow_html=True)

#         # Add vertical spacing for centering
#         st.write("\n" * 1)
#         str = "      "
#         # Create columns to align search bar and button
#         search_col3,search_col1, search_col2,search_col3 = st.columns([1,2.5, 0.5,1])

#         with search_col3 :
#                 str= "      "

#         with search_col1:
#             search_query = st.text_input("Enter the movie name:", label_visibility="collapsed")

#         with search_col2:
#             search_button = st.button("Search", use_container_width=True)

#         # Process the search query
#         if search_button:
#             if search_query:
#                 movie_found = new_df[new_df["title"].str.contains(search_query, case=False, na=False)]
#                 if not movie_found.empty:
#                     st.session_state["selected_movie_name"] = movie_found["title"].iloc[0]
#                     st.experimental_rerun()
#                 else:
#                     st.error("Movie not found. Please try another name.")
#             else:
#                 st.warning("Please enter a movie name before clicking 'Search'.")

#         if st.session_state["selected_movie_name"]:
#             display_movie_details(st.session_state["selected_movie_name"])
#             recommend_display(new_df, st.session_state["selected_movie_name"])
#         else:
#             display_home_page(new_df)

# if __name__ == "__main__":
#     main()






import streamlit as st
from processing import preprocess
from processing.display import Main
import pandas as pd
import requests

# Page configuration
st.set_page_config(
    page_title="Movie Recommender",
    layout="wide",
    page_icon="",
)

# Custom CSS for styling and disabling image expand
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-size: cover;
        background-attachment: fixed;
        color: #ffffff;
    }
    .stButton>button {
        color: #ffffff;
        border: none;
        border-radius: 20px;
        background-color: #6C63FF;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #FFC107;
    }
    .main-container {
        margin: auto;
        padding: 2rem;
        border-radius: 20px;
        background-color: rgba(255, 255, 255, 0.15);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .title {
        text-align: center;
        font-weight: 700;
        color: #FFC107;
        margin-bottom: 2rem;
    }
    .section {
        margin-top: 2rem;
    }
    .no-hover:hover {
        pointer-events: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state variables
if "selected_movie_name" not in st.session_state:
    st.session_state["selected_movie_name"] = None

if "default_movies" not in st.session_state:
    st.session_state["default_movies"] = None

# TMDB API key
TMDB_API_KEY = "cacb9b2809c0d5862ef7b4a688a83db6"

def fetch_posters(movie_id):
    """
    Fetch the poster URL for a given movie ID using TMDB API.
    """
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    )
    data = response.json()
    try:
        return f"https://image.tmdb.org/t/p/w780/{data['poster_path']}"
    except KeyError:
        return "https://via.placeholder.com/150"

def display_movie_details(selected_movie_name):
    """
    Display details for the selected movie.
    """
    st.title(f" {selected_movie_name}  details")

    try:
        info = preprocess.get_details(selected_movie_name)
        if not info:
            st.warning("Details not available for the selected movie.")
            return

        image_col, text_col = st.columns((1, 2))
        with image_col:
            st.markdown(
                f"<img class='no-hover' src='{info[0]}' style='width: 210px; border-radius: 10px;'>",
                unsafe_allow_html=True,
            )

        with text_col:
            st.subheader(selected_movie_name)
            st.text(f"Rating: {info[8]} | Runtime: {info[6]}")
            st.write("Overview:")
            st.write(info[3])

            col1, col2, col3 = st.columns(3)
            with col1:
                st.text("Genres:")
                st.write(", ".join(info[2]))
            with col2:
                st.text("Release Date:")
                st.write(info[4])
            with col3:
                st.text("Director:")
                st.write(", ".join(info[12]))
    except Exception as e:
        st.error(f"Error fetching movie details: {e}")

def recommend_display(new_df, selected_movie_name):
    """
    Display movie recommendations for the selected movie.
    """
    st.markdown("<div class='section main-container'>", unsafe_allow_html=True)
    st.subheader(f"Similar Movies like '{selected_movie_name}'")
    st.write("---")
    try:
        movies, posters = preprocess.recommend(new_df, selected_movie_name, r"Files/similarity_tags_tags.pkl")
        for i in range(0, len(movies), 4):
            cols = st.columns(4)
            for j, col in enumerate(cols):
                if i + j < len(movies):
                    with col:
                        st.markdown(
                            f"<img class='no-hover' src='{posters[i+j]}' style='width: 250px; border-radius: 10px;'>",
                            unsafe_allow_html=True,
                        )
                        if st.button(movies[i + j], key=f"movie_{movies[i + j]}_{i + j}"):
                            st.session_state["selected_movie_name"] = movies[i + j]
                            st.experimental_rerun()
    except Exception as e:
        st.error(f"Error fetching recommendations: {e}")
    st.markdown("</div>", unsafe_allow_html=True)

def display_home_page(new_df):
    """
    Display a list of default movies on the home page.
    """
    if st.session_state["default_movies"] is None:
        st.session_state["default_movies"] = new_df.sample(40)  # Generate once and store in session state

    default_movies = st.session_state["default_movies"]

    for i in range(0, len(default_movies), 5):  # Display in rows of 5
        cols = st.columns(4)
        for j, col in enumerate(cols):
            if i + j < len(default_movies):
                movie_title = default_movies.iloc[i + j]["title"]
                movie_id = default_movies.iloc[i + j]["movie_id"]
                with col:
                    st.markdown(
                        f"<img class='no-hover' src='{fetch_posters(movie_id)}' style='width: 250px; border-radius: 10px;'>",
                        unsafe_allow_html=True,
                    )
                    if st.button(movie_title, key=f"movie_{movie_title}_{i+j}"):
                        st.session_state["selected_movie_name"] = movie_title
                        st.experimental_rerun()

def main():
    """
    Main function to run the app.
    """
    # Add a Home button at the top left
    home_col, title_col = st.columns([0.1, 0.9])
    with home_col:
        if st.button("Home"):
            st.session_state["selected_movie_name"] = None
            st.experimental_rerun()

    with Main() as bot:
        bot.main_()
        new_df, movies, _ = bot.getter()

        st.markdown("<h1 class='title'> Welcome to Movies4u </h1>", unsafe_allow_html=True)

        # Add vertical spacing for centering
        st.write("\n" * 1)

        # Create columns to align search bar and button
        search_col3, search_col1, search_col2, search_col3 = st.columns([1, 2.5, 0.5, 1])

        with search_col1:
            search_query = st.text_input("Enter the movie name:", label_visibility="collapsed")

        with search_col2:
            search_button = st.button("Search", use_container_width=True)

        # Process the search query
        if search_button:
            if search_query:
                movie_found = new_df[new_df["title"].str.contains(search_query, case=False, na=False)]
                if not movie_found.empty:
                    st.session_state["selected_movie_name"] = movie_found["title"].iloc[0]
                    st.experimental_rerun()
                else:
                    st.error("Movie not found. Please try another name.")
            else:
                st.warning("Please enter a movie name before clicking 'Search'.")

        if st.session_state["selected_movie_name"]:
            display_movie_details(st.session_state["selected_movie_name"])
            recommend_display(new_df, st.session_state["selected_movie_name"])
        else:
            display_home_page(new_df)

if __name__ == "__main__":
    main()
