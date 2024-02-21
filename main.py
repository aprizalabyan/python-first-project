from myModule.menu import show_menu
from myModule.library import Library

def main():
  library = Library()
  while True:
    show_menu(library)

if __name__ == "__main__":
  main()