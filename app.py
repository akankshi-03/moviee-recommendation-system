import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Load Dataset
# -----------------------------
movies = pd.read_csv("ml-latest-small/movies.csv")

# Preprocess genres
movies['genres'] = movies['genres'].str.replace('|', ' ', regex=False)

# -----------------------------
# TF-IDF Vectorization
# -----------------------------
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# -----------------------------
# Cosine Similarity
# -----------------------------
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Index mapping
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend_movies(title):
    if title not in indices:
        return None

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    return movies['title'].iloc[movie_indices]

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Movie Recommender", layout="centered")

st.title("🎬 Movie Recommendation System")
st.write("Content-Based Recommendation using TF-IDF & Cosine Similarity")

movie_name = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    recommendations = recommend_movies(movie_name)

    if recommendations is None:
        st.error("❌ Movie not found in dataset")
    else:
        st.success("✅ Recommended Movies:")
        for movie in recommendations:
            st.write("👉", movie)
