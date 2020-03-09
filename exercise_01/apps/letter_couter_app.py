class LetterCounterApp:
  def __init__(self):
    self.input_string = input("Enter a string: ")
    self.sub_string = input("Enter a character or a string: ")

  def perform(self):
    self.count = self.input_string.count(self.sub_string)

    print("___RESULT___")
    print(self.__result_string())

  # private methods
  def __result_string(self):
    return "'{sub_string}' occurs {count} time(s) in '{input_string}'".format(**self.__result_format())

  def __result_format(self):
    return {"sub_string": self.sub_string, "count": self.count, "input_string": self.input_string}
