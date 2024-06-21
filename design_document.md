## Introduction
LLM Book Finder is designed to provide users with top book recommendations across various genres. It uses FastAPI for building a RESTful API and integrates with the Google Books API for fetching book data.

## Technologies Used
- **FastAPI**: Chosen for its ease of use in building APIs with Python.
- **Google Books API**: Provides a rich source of book information for recommendations.

## Endpoints
- `/top-100-books`: Fetches the top 100 books for a specified genre.
- `/top-10-books`: Filters the top 10 books from a list of 100 books.
- `/select-book`: Selects one book from the top 10 list.
- `/conclude`: Concludes the interaction with a thank-you message.

## Future Improvements
- Enhanced recommendation algorithms.
- Integration with additional book data sources.
- User authentication for personalized recommendations.
