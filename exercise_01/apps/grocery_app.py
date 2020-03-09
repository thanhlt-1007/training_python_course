from helpers.string_to_list_helper import StringToListHelper

class GroceryApp:
  def __init__(self):
    self.__get_list_goods()
    self.__get_goods()

  def perform(self):
    print ("___RESULT___")
    if self.__list_goods_include_goods():
      print("Available")
    else:
      print("Out of stock")

  # private methods
  def __get_list_goods(self):
    input_string = input("Enter a list of goods (ex: laptop, mouse): ")
    self.list_goods = StringToListHelper(input_string).to_lower_list()

  def __get_goods(self):
    input_string = input("Enter goods: ")
    self.goods = input_string.strip().lower()

  def __list_goods_include_goods(self):
    try:
      self.list_goods.index(self.goods)
      return True
    except:
      return False
