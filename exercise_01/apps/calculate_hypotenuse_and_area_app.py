from math import sqrt

from helpers.string_to_number_helper import StringToNumberHelper

class CalculateHypotenuseAndAreaApp:
  def __init__(self):
    self.first_edge = self.__get_edge("Enter first edge: ")
    self.second_edge = self.__get_edge("Enter second edge: ")

  def perform(self):
    self.__get_area()
    self.__get_hypotenuse()

    print("__RESULT__")
    print(self.__result_string())

  # private methods
  def __get_edge(self, text):
    number = self.__get_input_string_and_convert(text)

    while not number:
      print("You entered an invalid edge")
      number = self.__get_input_string_and_convert(text)

    return number

  def __get_input_string_and_convert(self, text):
    input_str = input(text)
    number = StringToNumberHelper(input_str).perform({"positive": True})
    return number

  def __get_area(self):
    self.area = self.first_edge * self.second_edge / 2

  def __get_hypotenuse(self):
    self.hypotenuse = sqrt(pow(self.first_edge, 2) + pow(self.second_edge, 2))

  def __result_string(self):
    return "Area is {area}, hypotenuse is {hypotenuse}".format(**self.__result_format())

  def __result_format(self):
    return {"area": self.area, "hypotenuse": self.hypotenuse}
