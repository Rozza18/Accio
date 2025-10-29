"""this file includes books data loaded from a csv file and functions to get book recommendations"""
import csv
from collections import defaultdict
import random


# start BookRecommender class
class BookRecommender:
    """book recommendation system with multiple recommendation strategies"""
    # initialize BookRecommender class method
    def __init__(self, file_path):
        self.books = self.load_books_data(file_path=file_path)
        self.genre_index = self.build_genre_index()
        self.title_index = self.build_title_index()


    # load books data from csv file method
    def load_books_data(self, file_path):
        """load books data from a csv file into a list of dictionaries"""
        books_data = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for line in reader:
                    books_data.append(line)
            print(f"loaded {len(books_data)} books from database.")
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")

        return books_data

    # build genre index method to make fast searching by genre o(1)
    def build_genre_index(self):
        """build an index of books based on genre for quick lookup"""
        genre_index = defaultdict(list)
        for book in self.books:
            genre_index[book['Genre'].lower()].append(book)
        return genre_index

    # build title index method to make fast searching by title keywords
    def build_title_index(self):
        """build an index of books based on title for quick lookup"""
        title_index = defaultdict(list)
        for book in self.books:
            title_words = book['Name'].lower().split()
            for word in title_words:
                if len(word) > 3:  # ignore very short words
                    if word not in title_index:
                        title_index[word] = []
                    title_index[word].append(book)
        return title_index

    # get recommendations method by genre
    def get_recommendations_by_genre(self, genre):
        """get book recommendations based on genre"""
        genre = genre.lower()
        return self.genre_index.get(genre, [])

    # get recommendations method by keyword in title
    def get_recommendations_by_title_keyword(self, keyword):
        """get book recommendations based on keyword in title"""
        keyword = keyword.lower()
        recommendations = []

        # check for exact match with genre first
        if keyword in self.genre_index:
            recommendations.extend(self.genre_index[keyword])

        # then check for title keyword match
        if keyword in self.title_index:
            recommendations.extend(self.title_index[keyword])

        #check for not exact matching titles - partial matches
        for book in self.books:
            if keyword in book['Name'].lower():
                if book not in recommendations:
                    recommendations.append(book)

        return recommendations

    # random sample recommendations method
    def get_random_sample_recommendations(self, max_recommendations=5):
        """get a random sample of book recommendations"""
        if max_recommendations > len(self.books):
            max_recommendations = len(self.books)
        return random.sample(self.books, max_recommendations)

    # get popular genres books
    def get_popular_genres(self, top_n=5):
        """get books from most popular genres"""
        genres_count = defaultdict(int)
        for book in self.books:
            genres_count[book['Genre'].lower()] += 1
        sorted_genres = sorted(genres_count.items(),
                               key=lambda x: x[1], reverse=True)[:top_n] #to get top n genres
        return sorted_genres

    # wrapping function to search books based on user query
    def search_books(self, query):
        """search books based on user query"""
        query = query.lower()
        results = []

        #search by genre
        for genre, book in self.genre_index.items():
            if query in genre:
                results.extend(book)

        #search by title keywords
        for book in self.books:
            if query in book['Name'].lower():
                if book not in results:
                    results.append(book)
        return results
