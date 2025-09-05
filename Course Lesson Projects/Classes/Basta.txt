brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
arepas_menu_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}


class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_hour = start_time
    self.end_hour = end_time
    if start_time < 12:
      self.start_time = f"{start_time}am"
    else:
      self.start_time = f"{start_time - 12}pm"
    if end_time < 12:
      self.end_time = f"{end_time}am"
    else:
      self.end_time = f"{end_time - 12}pm"

  def __repr__(self):
    return (f"{self.name} menu available from {self.start_time} to {self.end_time}")
  
  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
    return total

brunch = Menu("brunch", brunch_items, 11, 16)
early_bird = Menu("early bird", early_bird_items, 7, 11)
dinner = Menu("dinner", dinner_items, 17, 21)
kids = Menu("kids", kids_items, 7, 21)
arepas = Menu("arepas", arepas_menu_items, 10, 20)

all_menus = [brunch, early_bird, dinner, kids]

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return f"The address of the restaurant is {self.address}."
  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if menu.start_hour <= time <= menu.end_hour:
        available.append(menu)
    return available

flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)
arepas_place = Franchise("189 Fitzgerald Avenue", all_menus)

franchises = [flagship_store, new_installment]

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  
  def __repr__(self):
    return f"The business_name is {self.name} and contains franchises at the following locations: {self.franchises}."

basta_business = Business("Basta Fazoolin' with my Heart", franchises)
arepas_business = Business("Take a' Arepa", arepas_place)

print(arepas_business)