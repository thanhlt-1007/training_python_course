class StringToListHelper:
  def __init__(self, string):
    self.string = string

  def to_list(self):
    list = self.string.split(",")

    for i in range(len(list)):
      list[i] = list[i].strip()

    return list

  def to_lower_list(self):
    list = self.to_list()

    for i in range(len(list)):
      list[i] = list[i].lower()

    return list
