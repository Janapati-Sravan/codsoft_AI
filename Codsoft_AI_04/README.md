Content-Based Recommendation System

A Python-based Content-Based Recommendation System that suggests movies, books, or products to users based on their stated interests. It uses TF-IDF vectorization and cosine similarity to match user input against item descriptions.

📌 Features


Three Independent Recommendation Categories: Movies, Books & Products
Content-Based Filtering using TF-IDF + Cosine Similarity
Personalized Recommendations based on free-text user interests
Keyword Search across item features
Item Listing (view all available titles)
Detailed View (titles with their associated feature tags)
Top-N Recommendations with similarity scores
Interactive Menu-Driven Command Line Interface


🛠️ Technologies Used


Python 3
pandas
scikit-learn (TfidfVectorizer, cosine_similarity)


📂 Project Structure

recommendation_system/
│
├── recommendation_system.py   # Main source code
├── README.md                  # Project documentation

▶️ How to Run


Make sure Python 3 is installed.
Install the required dependencies:


bashpip install pandas scikit-learn


Clone or download this repository.
Open a terminal in the project folder and run:


bashpython recommendation_system.py


Follow the on-screen menu to explore movies, books, or products!


💬 How to Use


From the main menu, choose a category: Movies, Books, or Products.
Within each category menu, you can:

Show Items — list all available titles in that category
Recommend Items — enter your interests as free text (e.g. space adventure) to get the top matching titles, ranked by similarity score
Search Items — enter a keyword to find titles whose features contain it
Item Details — view every title along with its underlying feature tags
Back — return to the main menu



Choose Exit from the main menu to quit the program.


💬 Example Session

==================================================
CONTENT BASED RECOMMENDATION SYSTEM
==================================================
1. Movies
2. Books
3. Products
4. Exit

Enter Choice: 1

========================================
MOVIE RECOMMENDATION
========================================
1. Show Movies
2. Recommend Movies
3. Search Movies
4. Movie Details
5. Back

Enter Choice: 2

Enter interests: space adventure science fiction

Recommended Items:

1. Interstellar (Score: 0.62)
2. Avatar (Score: 0.45)
3. The Matrix (Score: 0.31)

⚙️ How It Works


Each category (movies, books, products) is a small built-in dataset of [Title, Features] pairs, where Features is a short string of descriptive keywords/tags.
The ContentRecommender class wraps a dataset in a pandas DataFrame and fits a TfidfVectorizer on the Features column, producing a TF-IDF matrix representing each item.
recommend(user_interest, top_n) transforms the user's input text into the same TF-IDF space, computes cosine similarity against every item, and prints the top matches with a score above zero.
search(keyword) performs a simple case-insensitive substring search over each item's Features text.
show_items() and details() provide simple listing/inspection utilities.
Three separate ContentRecommender instances are created — one each for movies, books, and products — and three corresponding menu functions (movie_menu, book_menu, product_menu) drive the interactive CLI, all coordinated by main().