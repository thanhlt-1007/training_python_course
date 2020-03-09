from helpers.string_to_number_helper import StringToNumberHelper

class BookShopApp:
  def __init__(self):
    self.__get_books()
    self.__get_book()

  def perform(self):
    print ("___RESULT___")
    if self.__books_include_book():
      print("{quantity} items available".format(quantity = self.books[self.book]))
    else:
      print("Out of stock")

  # private methods
  def __get_books(self):
    self.books = {}
    entering = True

    while entering:
      self.__enter_a_book()

      input_string = input("Continue enter another book(y/n): ")
      entering = input_string.strip().lower() == "y"

  def __enter_a_book(self):
    input_string = input("Enter a book with title and quantity (ex: math, 1): ")

    title, quantity = input_string.split(",")
    title = title.strip().lower()
    quantity = StringToNumberHelper(quantity).perform({"integer": True, "positive": True})

    if quantity:
      print("valid number")
      self.books[title] = quantity

      print("Saved {title} with {quantity} book(s)".format(title = title, quantity = quantity))
    else:
      print("Invalid quantity for {title}".format(title = title))

  def __get_book(self):
    input_string = input("Enter a book with title (ex: math): ")
    self.book = input_string.strip().lower()

  def __books_include_book(self):
    return self.book in self.books
