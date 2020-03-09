class StringToNumberHelper:
  def __init__(self, string):
    self.string = string.strip()

  def perform(self, options={}):
    try:
      number = float(self.string)
    except:
      return False

    if "positive" in options and options["positive"]:
      if number <= 0:
        return False

    if "integer" in options and options["integer"]:
      if int(number) != number:
        return False
      else:
        number = int(number)

    return number
