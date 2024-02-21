from myModule.img_downloader import image_downloader

def show_menu(library):
  print("\n------- MENU --------")
  print("1. Show books")
  print("2. Add book")
  print("3. Update book")
  print("4. Delete book")
  print("99. Exit")
  handle_select(library)

def handle_select(library):
  select = int(input("Select menu : "))
  if select == 1:
    print("\nList of books")
    library.display_books()
  elif select == 2:
    print("\nAdd new book")
    title = input("Title: ")
    year = input("Year: ")
    library.add_book(title, year)
  elif select == 3:
    print("\nUpdate a book")
    index = int(input("Index of book: "))
    title = input("Title: ")
    year = input("Year: ")
    library.update_book(index - 1, title, year)
  elif select == 4:
    print("\nDelete a book")
    index = int(input("Index of book: "))
    library.delete_book(index - 1)
  elif select == 5:
    print("\nHey!! Welcome to the Image downloader...")
    link = input("Please enter the url from where you want to download the image..")
    image_downloader(link)
  elif select == 99:
    print("\nExit the program...")
    exit()
  else:
    print("Invalid menu.")
  