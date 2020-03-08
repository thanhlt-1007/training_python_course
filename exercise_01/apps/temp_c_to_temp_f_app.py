from helpers.string_to_number_helper import StringToNumberHelper

class TempCToTempFApp:
  def __init__(self):
    self.__get_input_string()

  def perform(self):
    self.__convert_temp_c()

    while not self.temp_C:
      print("You entered an invalid a numbers as temperature in Celsius")
      self.__get_input_string()
      self.__convert_temp_c()

    self.temp_F = 32 + self.temp_C * 1.8
    print("___RESULT___")
    print(self.__result_string())

  # private methods
  def __get_input_string(self):
    self.input_string = input("Enter a numbers as temperature in Celsius: ")

  def __convert_temp_c(self):
    self.temp_C = StringToNumberHelper(self.input_string).perform()

  def __result_string(self):
    return "{temp_C} in Celsius is {temp_F} in Fahrenheit".format(**self.__result_format())

  def __result_format(self):
    return {"temp_C": self.temp_C, "temp_F": self.temp_F}
