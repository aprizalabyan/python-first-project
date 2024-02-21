from myModule.book import Book

class Library:
  def __init__(self):
    self.books = []

  def display_books(self):
    if not self.books:
      print("No books in the library.")
    else:
      for index, book in enumerate(self.books, start=1):
        print(f"{index}. Title: {book.title}, Year: {book.year}")

  def add_book(self, title, year):
    book = Book(title, year)
    self.books.append(book)
    print("Book added successfully.")

  def update_book(self, index, title, year):
    if 0 <= index < len(self.books):
      self.books[index].title = title
      self.books[index].year = year
      print("Book updated successfully.")
    else:
      print("Invalid index.")

  def delete_book(self, index):
    if 0 <= index < len(self.books):
      del self.books[index]
      print("Book deleted successfully.")
    else:
      print("Invalid index.")