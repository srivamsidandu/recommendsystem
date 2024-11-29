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
# ... existing code ...

# Custom CSS for styling and disabling image expand
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #2C3E50;  /* Default text color - dark blue-grey */
    }
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1614850523459-c2f4c699c52e');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255, 255, 255, 0.75);
        z-index: -1;
    }
    /* Title styling */
    .title {
        text-align: center;
        font-weight: 700;
        color: #1A237E;  /* Deep blue for main title */
        margin-bottom: 2rem;
    }
    /* Movie title and details styling */
    .stMarkdown h1 {  /* For movie titles */
        color: #303F9F;  /* Indigo for movie titles */
        font-weight: 600;
    }
    .stMarkdown h3, .stMarkdown h4 {  /* For section headings */
        color: #3949AB;  /* Lighter indigo for subheadings */
    }
    /* Subheader styling (for movie names) */
    .css-10trblm {  /* Streamlit's subheader class */
        color: #303F9F !important;
        font-weight: 600 !important;
    }
    /* Button styling */
    .stButton>button {
        color: #ffffff;
        border: none;
        border-radius: 20px;
        background-color: #303F9F;  /* Changed to match theme */
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #1A237E;  /* Darker shade for hover */
    }
    /* ... rest of your existing CSS ... */
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
    <style>
    .st-emotion-cache-18ni7ap {
        background-image: url('https://images.unsplash.com/photo-1614850523459-c2f4c699c52e');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        position: relative;
    }

    /* Add an overlay to ensure text remains readable */
    .st-emotion-cache-18ni7ap::before {
        content: "";
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
    }

    /* Ensure content stays above the overlay */
    .st-emotion-cache-18ni7ap > * {
        position: relative;
        z-index: 2;
        color: #7FFFD4 !important;
    }

    /* Additional text color specifications */
    .st-emotion-cache-18ni7ap p,
    .st-emotion-cache-18ni7ap h1,
    .st-emotion-cache-18ni7ap h2,
    .st-emotion-cache-18ni7ap h3,
    .st-emotion-cache-18ni7ap h4,
    .st-emotion-cache-18ni7ap span,
    .st-emotion-cache-18ni7ap div,
    .st-emotion-cache-18ni7ap label,
    .st-emotion-cache-18ni7ap button,
    .st-emotion-cache-17c4ue {
        color: #7FFFD4 !important;
    }
    </style>
""", unsafe_allow_html=True)
# ... existing code ...

st.markdown(
    """
    <style>
    /* Movie details specific styling */
    .stTextInput>div>div>input {
        color: black !important;
    }
    .element-container{
        color: #7FFFD4 !important;
    }
    
    /* Style for movie overview and other text content */
    .row-widget.stText {
        color: #7FFFD4 !important;
    }
    
    /* Rating and runtime text */
    .stMarkdown text {
        color: #7FFFD4 !important;
    }
    
    /* Overview text */
    .stMarkdown p {
        color: #7FFFD4 !important;
    }
    
    /* Search input text color */
    .stTextInput input {
        color: #7FFFD4 !important;
    }

    /* Update all text colors */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, 
    .stMarkdown p, .stMarkdown div {
        color: #7FFFD4 !important;
    }
    
    /* Subheader text color */
    .css-10trblm {
        color: #7FFFD4 !important;
    }
    
    /* Regular text color */
    .css-1629p8f {
        color: #7FFFD4 !important;
    }
    
    /* Text elements and labels */
    .css-1x8cf1d {
        color: #7FFFD4 !important;
    }
    
    /* Additional text elements */
    .css-183lzff {
        color: #7FFFD4 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ... rest of your existing code ...

# ... rest of your existing code ...

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



st.markdown("""
    <style>
    /* Metric label styling (the title above the value) */
    .css-1wivap2 {  /* Streamlit's metric label class */
        color: #7FFFD4 !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
    }
    
    /* Metric value styling (the actual number) */
    .css-1w25zad {  /* Streamlit's metric value class */
        color: #7FFFD4 !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }
    
    /* Delta value styling (if you're showing changes) */
    .css-1ay4j1f {  /* Streamlit's metric delta class */
        color: #7FFFD4 !important;
    }
    </style>
""", unsafe_allow_html=True)


def display_movie_details(selected_movie_name):
    """
    Display details for the selected movie.
    """

    st.markdown("""
        <style>
        /* Hide anchor links next to headers */
        .css-1wivap2 a, 
        h1 a, 
        h2 a, 
        h3 a, 
        .css-10trblm a,
        .css-zt5igj a,
        [data-testid="stMarkdownContainer"] a {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title(f" {selected_movie_name} ")

    try:
        info = preprocess.get_details(selected_movie_name)
        if not info:
            st.warning("Details not available for the selected movie.")
            return

        # Main layout with poster and basic info
        image_col, text_col = st.columns((1, 2))
        with image_col:
            st.markdown(
                f"<img class='no-hover' src='{info[0]}' style='width: 370px; border-radius: 10px;'>",
                unsafe_allow_html=True,
            )

        with text_col:
            st.subheader(selected_movie_name)
            
            # Rating and Runtime row
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Rating", f"{info[8]}/10")
            with col2:
                st.metric("Runtime", f"{info[6]} min")
            with col3:
                st.metric("Release Year", info[4][:4])  # Assuming date format YYYY-MM-DD

            # Overview
            st.write("📝 Overview:")
            st.write(info[3])

            # Movie Details in columns
            col1, col2 = st.columns(2)
            with col1:
                st.write("🎭 Genres:")
                st.write(", ".join(info[2]))
                
                st.write("📅 Release Date:")
                st.write(info[4])
                
                st.write("💰 Budget:")
                budget = info[9] if info[9] else "N/A"  # Assuming budget is at index 9
                st.write(f"${budget:,}" if budget != "N/A" else "N/A")
                


            with col2:
                st.write("🎬 Director:")
                st.write(", ".join(info[12]))
                
                st.write("💵 Revenue:")
                revenue = info[10] if info[10] else "N/A"  # Assuming revenue is at index 10
                st.write(f"${revenue:,}" if revenue != "N/A" else "N/A")
                
                st.write("Language:")
                production_companies = info[13] if len(info) > 13 else ["N/A"]  # Assuming companies at index 13
                st.write(", ".join(production_companies))
                

        # Cast section
        st.write("👥 Top Cast:")
        cast_cols = st.columns(5)
        cast_names = info[11][:5] if info[11] else []  # Get top 5 cast members
        cast_images = info[15][:5] if len(info) > 15 and info[15] else []  # Assuming cast images at index 15
        cast_roles = info[16][:5] if len(info) > 16 and info[16] else []  # Assuming cast roles at index 16
        
        for i, col in enumerate(cast_cols):
            if i < len(cast_names):
                with col:
                    if cast_images and i < len(cast_images):
                        st.image(cast_images[i], width=100)
                    st.write(cast_names[i])
                    if cast_roles and i < len(cast_roles):
                        st.write(f"as {cast_roles[i]}")

        # Additional details section

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
    # Style adjustments for the header
    st.markdown("""
        <style>
        /* Remove default top padding from main container */
        .block-container {
            padding-top: 1rem !important;
        }
        
        /* Style for home button container */
        div[data-testid="column"]:first-child {
            padding-top: 15px;
        }
        
        /* Remove anchor links from headers */
        .title a {
            display: none !important;
        }
        
        /* Center the title and adjust its position */
        .title {
            margin-top: -15px !important;
            padding-bottom: 1rem;
        }

        /* Reduce top margin of the entire app */
        .main > div {
            padding-top: 1rem !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Create columns with better proportions for alignment
    home_col, spacer1, title_col, spacer2 = st.columns([0.7, 0.3, 4, 1])

    # Add the Home button
    with home_col:
        if st.button("Home"):
            st.session_state["selected_movie_name"] = None
            st.experimental_rerun()

    # Add the title
    with title_col:
        st.markdown("<h1 class='title'>MOVIES FOR YOU</h1>", unsafe_allow_html=True)

    # Rest of your main function code...

    with Main() as bot:
        bot.main_()
        new_df, movies, _ = bot.getter()


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

if __name__== "__main__":
    main()
