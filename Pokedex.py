class Pokedex:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  
  def speak(self):
      print(self.name + ', ' + self.name + '!')
  
  def display_details(self):
      print('Entry Number: ' + str(self.entry))
      print('Name: ' + self.name)
      print('Type: ' + self.types)
      print('Description: ' + self.description)
      print('Pikachu has already been caught!')

Pokemon = Pokedex(25, 'Pikachu', 'Electrico', 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', True)

Pokemon.speak()
Pokemon.display_details()

  