# 📚 Accio Books - Book Recommendation System

A magical Python-based book recommendation system that helps you discover your next favorite read! Built with efficient data structures and algorithms for fast, intelligent book suggestions.

## ✨ Features

- **🔍 Smart Search**: Search by genre, title keywords, or partial matches
- **🎲 Random Discovery**: Get random book recommendations
- **📊 Genre Analytics**: See popular genres and book counts
- **⚡ Fast Performance**: Optimized with hash tables and indexing
- **📱 User-Friendly**: Interactive terminal interface with emojis

## 🚀 Quick Start

### Prerequisites
- Python 3.10
- `books.csv` data file

### Installation
1. Clone or download the project files
2. Ensure `books.csv` is in the same directory
3. Run the program:

```bash
python script.py

Usage Examples
Search for "sci fiction" to see science fiction books

Enter "dune" to find books with that title

Use "random" to get surprise recommendations

Type "help" for guidance


🏗️ Project Structure

accio-books/
├── script.py              # Main program interface
├── recommendations.py     # Core recommendation engine
├── books.csv             # Book database (1000+ entries)
└── README.md            # This file


🧠 Technical Highlights
Data Structures Used
Hash Tables: defaultdict for O(1) genre lookups

Indexing: Dual indexes for genres and titles

Counters: Track genre popularity efficiently


Algorithms Implemented
Search Algorithms: Multi-strategy search (genre + title)

Sorting: Genre popularity ranking

Random Sampling: Fair book selection

Key Functions
BookRecommender.search_books() - Comprehensive search

build_genre_index() - Fast genre-based lookup

get_popular_genres() - Genre analytics

get_random_sample_recommendations() - Discovery engine

📊 Dataset
The system uses a comprehensive dataset with:

1000+ books across multiple genres

Sci Fiction, Horror, Adventure, Historical Fiction, and more

Complete metadata including Goodreads URLs

🎯 Use Cases
Readers: Discover new books based on preferences

Book Clubs: Find discussion-worthy titles

Libraries: Assist patrons with recommendations

Students: Learn about data structures in practice

🔧 Customization
Adding New Books
Edit books.csv with format:

Genre,Name,URL
New Genre,Book Title,https://example.com

Extending Functionality
The modular design makes it easy to add:

Author-based recommendations

Rating-based sorting

Personal reading history

Export capabilities

📈 Performance
Search Speed: O(1) for indexed genres, O(n) for comprehensive search

Memory Usage: Efficient indexing minimizes redundancy

Scalability: Handles 1000+ books with instant response


🤝 Contributing
Feel free to fork and enhance:

Add new recommendation algorithms

Improve the user interface

Expand the book database

Add unit tests

📝 License
Open source - feel free to use for learning and projects!


🎓 Learning Outcomes
This project demonstrates:

Practical use of data structures

Algorithm optimization techniques

CSV data processing

User interface design

Software architecture patterns