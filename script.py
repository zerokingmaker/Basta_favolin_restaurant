import datetime
from datetime import datetime
from datetime import timedelta

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = datetime.strptime(start_time, "%H:%M")
    self.end_time = datetime.strptime(end_time, "%H:%M")

  def __repr__(self):
    return "{name} menu available from {start} to {end}".format(name=self.name, start=self.start_time.strftime("%I:%M %p"), end=self.end_time.strftime("%I:%M %p"))

  def calculate_bill(self, purchased_items):
    sum = 0
    for item in purchased_items:
      if item in self.items :
        sum+= self.items[item]
    return sum    


brunch = Menu("Brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, "11:00", "16:00")

early_bird = Menu("Early-bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, "15:00", "18:00")

dinner = Menu("Dinner", {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, "17:00", "23:00")

kids = Menu("Kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, "11:00", "21:00")

print(brunch)
print(kids)
brunch_bill = brunch.calculate_bill(["pancakes", "home fries", "coffee"])

print(brunch_bill)

early_bird_bill = early_bird.calculate_bill({"salumeria plate", "mushroom ravioli (vegan)"})

print(early_bird_bill)

class Franchise:
 def __init__(self, address, menus):
    self.address = address
    self.menus = menus
 def __repr__(self, address):
   return self.address 

 def available_menus(self, time):
   list_of_menu = []
   time_converted = datetime.strptime(time, "%H:%M")
   for menu in self.menus :
     if time_converted >= menu.start_time and time_converted <= menu.end_time :
       list_of_menu.append(menu)

   for menu in list_of_menu:
     print(menu)


flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

flagship_store.available_menus("20:10")
flagship_store.available_menus("17:00")

class Business:
 def __init__(self, name, franchises):
   self.name = name
   self.franchises = franchises

basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = Menu("Take a’ Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, "10:00", "20:00")

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

arepa_business = Business("Take a' Arepa", arepas_place)
