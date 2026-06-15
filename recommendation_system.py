"""
CONTENT-BASED RECOMMENDATION SYSTEM

This system recommends:
1. Movies
2. Books
3. Products
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = [
    ["Inception", "science fiction action thriller dream"],
    ["Interstellar", "science fiction space adventure future"],
    ["The Matrix", "science fiction action virtual reality"],
    ["John Wick", "action crime thriller revenge"],
    ["The Dark Knight", "action superhero crime batman"],
    ["Titanic", "romance drama emotional love"],
    ["Doctor Strange", "superhero fantasy magic action"],
    ["Top Gun Maverick", "action aviation military adventure"],
    ["Avatar", "science fiction fantasy adventure"],
    ["Avengers Endgame", "superhero action marvel adventure"]
]

books = [
    ["Harry Potter", "fantasy magic wizard adventure"],
    ["The Hobbit", "fantasy dragon adventure"],
    ["Lord of the Rings", "fantasy epic adventure war"],
    ["Atomic Habits", "productivity habits self improvement"],
    ["Deep Work", "focus productivity career"],
    ["Rich Dad Poor Dad", "finance money business"],
    ["Think and Grow Rich", "motivation success wealth"],
    ["Dune", "science fiction space politics"],
    ["1984", "dystopian future politics"],
    ["The Alchemist", "dream inspiration adventure"]
]
products = [
    ["Gaming Laptop", "electronics gaming performance"],
    ["Mechanical Keyboard", "gaming typing electronics"],
    ["Wireless Mouse", "electronics computer accessory"],
    ["Smartphone", "electronics camera internet mobile"],
    ["Bluetooth Speaker", "music wireless electronics"],
    ["Running Shoes", "fitness running sports"],
    ["Fitness Band", "fitness health tracking"],
    ["Protein Powder", "fitness gym nutrition"],
    ["Coffee Maker", "kitchen coffee appliance"],
    ["Air Fryer", "healthy cooking kitchen appliance"]
]

class ContentRecommender:

    def __init__(self, data):

        self.df = pd.DataFrame(
            data,
            columns=["Title", "Features"]
        )

        self.vectorizer = TfidfVectorizer()

        self.tfidf_matrix = self.vectorizer.fit_transform(
            self.df["Features"]
        )



    def show_items(self):

        print("\nAvailable Items:\n")

        for item in self.df["Title"]:
            print(item)


    def recommend(self, user_interest, top_n=5):

        user_vector = self.vectorizer.transform(
            [user_interest]
        )

        similarity_scores = cosine_similarity(
            user_vector,
            self.tfidf_matrix
        )

        scores = similarity_scores.flatten()

        sorted_indexes = scores.argsort()[::-1]

        print("\nRecommended Items:\n")

        count = 0

        for index in sorted_indexes:

            if scores[index] > 0:

                print(
                    f"{count + 1}. "
                    f"{self.df.iloc[index]['Title']} "
                    f"(Score: {scores[index]:.2f})"
                )

                count += 1

                if count == top_n:
                    break

        if count == 0:
            print("No matching recommendations found.")



    def search(self, keyword):

        keyword = keyword.lower()

        results = []

        for _, row in self.df.iterrows():

            if keyword in row["Features"].lower():

                results.append(row["Title"])

        print("\nSearch Results:\n")

        if results:

            for item in results:
                print(item)

        else:
            print("No results found.")
    # DISPLAY DETAILS
    def details(self):

        print("\nItems and Features:\n")

        for _, row in self.df.iterrows():

            print(f"Title    : {row['Title']}")
            print(f"Features : {row['Features']}")
            print("-" * 40)

# CREATE OBJECTS

movie_system = ContentRecommender(movies)

book_system = ContentRecommender(books)

product_system = ContentRecommender(products)

# MOVIE MENU


def movie_menu():

    while True:

        print("\n")
        print("=" * 40)
        print("MOVIE RECOMMENDATION")
        print("=" * 40)

        print("1. Show Movies")
        print("2. Recommend Movies")
        print("3. Search Movies")
        print("4. Movie Details")
        print("5. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            movie_system.show_items()

        elif choice == "2":

            interest = input(
                "\nEnter interests: "
            )

            movie_system.recommend(interest)

        elif choice == "3":

            keyword = input(
                "\nEnter keyword: "
            )

            movie_system.search(keyword)

        elif choice == "4":

            movie_system.details()

        elif choice == "5":

            break

        else:

            print("Invalid Choice")

# BOOK MENU
def book_menu():

    while True:

        print("\n")
        print("=" * 40)
        print("BOOK RECOMMENDATION")
        print("=" * 40)

        print("1. Show Books")
        print("2. Recommend Books")
        print("3. Search Books")
        print("4. Book Details")
        print("5. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            book_system.show_items()

        elif choice == "2":

            interest = input(
                "\nEnter interests: "
            )

            book_system.recommend(interest)

        elif choice == "3":

            keyword = input(
                "\nEnter keyword: "
            )

            book_system.search(keyword)

        elif choice == "4":

            book_system.details()

        elif choice == "5":

            break

        else:

            print("Invalid Choice")

# PRODUCT MENU

def product_menu():

    while True:

        print("\n")
        print("=" * 40)
        print("PRODUCT RECOMMENDATION")
        print("=" * 40)

        print("1. Show Products")
        print("2. Recommend Products")
        print("3. Search Products")
        print("4. Product Details")
        print("5. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            product_system.show_items()

        elif choice == "2":

            interest = input(
                "\nEnter interests: "
            )

            product_system.recommend(interest)

        elif choice == "3":

            keyword = input(
                "\nEnter keyword: "
            )

            product_system.search(keyword)

        elif choice == "4":

            product_system.details()

        elif choice == "5":

            break

        else:

            print("Invalid Choice")

# MAIN MENU

def main():

    while True:

        print("\n")
        print("=" * 50)
        print("CONTENT BASED RECOMMENDATION SYSTEM")
        print("=" * 50)

        print("1. Movies")
        print("2. Books")
        print("3. Products")
        print("4. Exit")

        choice = input(
            "\nEnter Choice: "
        )

        if choice == "1":

            movie_menu()

        elif choice == "2":

            book_menu()

        elif choice == "3":

            product_menu()

        elif choice == "4":

            print("\nThank You!")
            break

        else:

            print("\nInvalid Choice")


if __name__ == "__main__":
    main()