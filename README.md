# Library Chatbot

A simple interactive chatbot for a school library that helps users check book availability.

## Features

- **Book Search**: Ask about any book in the library
- **Availability Status**: Check if a book is available or currently borrowed
- **User-Friendly Interface**: Simple conversational interface for easy interaction
- **Exit Command**: Type 'exit' to stop the chatbot

## Books in Library

The chatbot currently manages the following books:

| Title | Author | Status |
|-------|--------|--------|
| Harry Potter and the Philosopher's Stone | J. K. Rowling | Available |
| The Hobbit | J. R. R. Tolkien | Available |
| The Diary of a Young Girl | Anne Frank | Available |
| Charlotte's Web | E. B. White | Borrowed |
| The Little Prince | Antoine de Saint-Exupéry | Borrowed |

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the files
2. No additional dependencies required - uses only Python standard library

## Usage

1. Run the chatbot:
   ```bash
   python library_chatbot.py
   ```

2. You'll see the welcome message:
   ```
   Welcome to the School Library Chatbot!
   Ask about a book, or type 'exit' to stop.
   ```

3. Ask about any book:
   ```
   You: Is Harry Potter available?
   Chatbot: Yes, 'Harry Potter and the Philosopher's Stone' is available.
   ```

4. Type 'exit' to quit:
   ```
   You: exit
   Chatbot: Goodbye!
   ```

## How It Works

- The chatbot maintains a list of books with their availability status
- When you ask about a book, it searches for matching titles in the database
- It responds with the current availability status
- If the book is not found, it informs you the book is not in the library

## Example Interactions

```
You: Do you have The Hobbit?
Chatbot: Yes, 'The Hobbit' is available.

You: Can I borrow Charlotte's Web?
Chatbot: 'Charlotte's Web' is currently borrowed.

You: Do you have Lord of the Rings?
Chatbot: That book is not available in our library.
```

## Future Enhancements

- Add book borrowing and return functionality
- Store book data in a database
- Add user account management
- Implement natural language processing for better understanding
- Add book recommendations
- Track borrowing history

## License

This project is open source and available for educational purposes.

## Author

Created as a learning project for library management chatbots.
