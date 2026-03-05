## 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using **TF-IDF vectorization** and **cosine similarity** on movie genres, deployed as a **web application using Streamlit**. Users can enter a movie name and get **top 10 similar movies** recommended.

---

## 🔹 Features

- Content-based recommendation using **movie genres**
- Preprocessing with **TF-IDF vectorization**
- Similarity calculation using **cosine similarity**
- **Error handling** for movies not present in the dataset
- **Interactive web app** with Streamlit
- Easy deployment for end-users via **Streamlit Cloud**

---

## 🔹 Dataset

- Dataset used: [MovieLens Latest Small](https://grouplens.org/datasets/movielens/latest/)  
- File used: `movies.csv`
- Columns:
  - `movieId`: Unique movie identifier
  - `title`: Movie title
  - `genres`: Genres of the movie (used for content-based recommendations)

---
## 🔹 Project Structure

movie-recommendation-system/
│
├── app.py # Streamlit application + recommendation logic
├── requirements.txt # Python dependencies
└── ml-latest-small/
└── movies.csv # Dataset


---

## 🔹 Installation

1. Clone the repo:
```bash
git clone https://github.com/username/movie-recommendation-system.git

2.Navigate to project folder:

cd movie-recommendation-system

3.Install dependencies:

pip install -r requirements.txt


## 🔹 Project Structure

