# Simple College Library Chatbot
# Copilot: Add an "available" field to each book. 
# Mark three books as available and two as borrowed
books = [
    {"title": "Harry Potter and the Philosopher's Stone", "author": "J. K. Rowling", "available": True},
    {"title": "The Hobbit", "author": "J. R. R. Tolkien", "available": True},
    {"title": "The Diary of a Young Girl", "author": "Anne Frank", "available": True},
    {"title": "Charlotte's Web", "author": "E. B. White", "available": False},
    {"title": "The Little Prince", "author": "Antoine de Saint-Exupéry","available": False}
]
# Copilot: Update the chatbot so it tells the user whether
# a book is available, borrowed, or not in the library. 
# Only use information from the books list. 

print("Welcome to the School Library Chatbot!")
print("Ask about a book, or type 'exit' to stop.")

while True:
    question = input("\nYou: ").lower()
    
    if question == "exit":
        print("Chatbot: Goodbye!")
        break
        
    found_book = None
    
    for book in books:
        if book["title"].lower() in question:
            found_book = book
            break
            
    if found_book:
        if found_book["available"]:
            print(
                f"Chatbot: Yes, '{found_book['title']}' is available."
            )
        else:
            print(
                f"Chatbot: '{found_book['title']}' is currently borrowed."
            )
    else:
        print("Chatbot: That book is not available in our library.")