from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"

class GenreRequest(BaseModel):
    genre: str

class BooksRequest(BaseModel):
    genre: str
    top_100_books: List[str]

class Top10BooksRequest(BaseModel):
    top_10_books: List[str]

def fetch_books_from_google_books(genre: str, max_results: int = 100):
    response = requests.get(GOOGLE_BOOKS_API_URL, params={
        "q": genre,
        "maxResults": max_results,
        "printType": "books"
    })
    response.raise_for_status()
    books = response.json().get("items", [])
    return [book["volumeInfo"]["title"] for book in books]

@app.post("/top-100-books")
def get_top_100_books(request: GenreRequest):
    try:
        books = fetch_books_from_google_books(request.genre)
        return books
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/top-10-books")
def get_top_10_books(request: BooksRequest):
    top_10_books = request.top_100_books[:10]
    return top_10_books

@app.post("/select-book")
def select_book(request: Top10BooksRequest):
    selected_book = request.top_10_books[0] if request.top_10_books else "No books available"
    return {"selected_book": selected_book}

@app.get("/conclude")
def conclude():
    return {"message": "Thank you for using the LLM Book Finder!"}
