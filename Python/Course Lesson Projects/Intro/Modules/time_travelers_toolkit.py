from datetime import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
from custom_module import generate_time_travel_message as message


now = dt.now()
target_year = abs(randint(2000, 2500))
possible_destinations = ["Paris", "Venus", "Princeton", "Los Angelas", "Italy", "Florida", "London", "Canada", "Mexico", "The Sun"]
destination = choice(possible_destinations)

base_cost = Decimal("150000")
multiplier_0_100 = Decimal("1.5")
multiplier_100_500 = Decimal("2.5")
multiplier_500_plus = Decimal("5")
calculated_cost = 0

def apply_multiplier(base_cost):
  if abs(now.year - target_year) <= 100:
    calculated_cost = base_cost * multiplier_0_100
  elif 100 < abs(now.year - target_year) <= 500:
    calculated_cost = base_cost * multiplier_100_500
  elif 500 <= abs(now.year - target_year):
    calculated_cost = base_cost * multiplier_500_plus
  return calculated_cost

print(message(target_year, destination, apply_multiplier(base_cost)))