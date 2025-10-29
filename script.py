# accio program -- grab me my book recommendations
"""entry point script file to demonstrate code completion"""
from recommendations import BookRecommender


# welcome function
def display_welcome_message():
    """display welcome message to the user"""
    print("""
    ╔══════════════════════════════════════════════╗
    ║             📚 ACCIO BOOKS! 📚              ║
    ║      Your Magical Book Recommendation       ║
    ║                 Program                     ║
    ╚══════════════════════════════════════════════╝
    """)

#display menu function
def display_menu():
    """display menu options to the user"""
    print("\n" + "="*50)
    print("What would you like to do?")
    print("1. 🔍 Search books by genre or title")
    print("2. 🎲 Get random recommendations")
    print("3. 📊 Show popular genres")
    print("4. ❓ Get help")
    print("5. 🚪 Exit")
    print("="*50)

def display_recommendations(recommendations, title="Book Recommendations"):
    """display book recommendations to the user"""
    if not recommendations:
        print("\n❌ No books found matching your criteria.")
        print("   Try a different search term or check out random recommendations!")
        return

    print(f"\n📖 {title} ({len(recommendations)} found):")
    print("-" * 80)

    for idx, book in enumerate(recommendations, start=1):
        print(f"{idx:2d}. {book['Name']}")
        print(f"    Genre: {book['Genre']}")
        print(f"    URL: {book['URL']}")
        print()

def get_search_query():
    """prompt user for search query"""
    return input("\n🔍 Enter genre, book title, or keyword: ").strip()


def main():
    """main program loop"""
    # initialize recommender
    recommender = BookRecommender(file_path='books.csv')

    display_welcome_message()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            # search books
            query = get_search_query()
            if query:
                results = recommender.search_books(query)
                display_recommendations(results, title=f"Search Results for '{query}'")
            else:
                print("⚠️  Please enter a valid search term.")
        elif choice == '2':
            # random recommendations
            count_input = input("How many recommendations would you like? (default 5): ").strip()
            try:
                count = int(count_input) if count_input else 5
                results = recommender.get_random_sample_recommendations(max_recommendations=count)
                display_recommendations(results, title="✨ Random Book Recommendations")

            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '3':
            # popular genres
            print("\n📊 Most Popular Genres:")
            print("-" * 30)
            popular_genres = recommender.get_popular_genres()
            for genre, count in popular_genres:
                print(f"   {genre}: {count} books")

        elif choice == '4':
            # help
             print("""
            🤔 How to use Accio Books:
            
            • Search by genre: Enter genres like 'Sci Fiction', 'Horror', 'Adventure'
            • Search by title: Enter book titles or keywords from titles
            • Get random picks: Discover new books randomly
            • Explore genres: See which genres have the most books
            
            💡 Tip: Try searching for 'fantasy', 'mystery', or your favorite author!
            """)

        elif choice == '5':
            # Exit
            print("\n✨ Thank you for using Accio Books! Happy reading! 📚")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1-5.")

        # ask if user wants to continue
        if choice != '5':
            continue_choice = input("\nContinue searching? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                print("\n✨ Thank you for using Accio Books! Happy reading! 📚")
                break

if __name__ == "__main__":
    main()
