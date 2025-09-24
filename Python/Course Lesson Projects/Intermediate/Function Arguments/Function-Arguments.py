class Trip:
    def __init__(self, distance_km, passenger_count, base_fare):
        self.distance_km = distance_km
        self.passenger_count = passenger_count
        self.base_fare = base_fare

    def cost(self, extra_passenger_fee = 10): 
        if self.passenger_count > 1:
            cost = (self.base_fare * self.distance_km) + (extra_passenger_fee * (self.passenger_count - 1))
        elif self.passenger_count == 1:
            cost = self.base_fare * self.distance_km
        return cost

class Driver:
    def __init__(self, name, speed, salary):
        self.name = name
        self.speed = speed
        self.salary = salary

    def __repr__(self):
        return f"{self.name}"

bob_driver = Driver("Bob", 45, 20)
mark_driver = Driver("Mark", 50, 15)
trip_test = Trip(13, 1, 15)

def assign_drivers(trip, *drivers):
    cheapest_driver is None
    price_of_cheapest_driver is None
    for driver in drivers:
        price_of_driver = (trip.distance_km / driver.speed) * driver.salary 
        if cheapest_driver == None:
            cheapest_driver = driver
            price_of_cheapest_driver = price_of_driver
        elif price_of_driver < price_of_cheapest_driver:
            cheapest_driver = driver
            price_of_cheapest_driver = price_of_driver
    return cheapest_driver, price_of_cheapest_driver

print(assign_drivers(trip_test, bob_driver, mark_driver))




def calculate_earnings(*drivers, **trips):
    best_driver = None
    driver_earnings = {}
    for trip in trips:
        driver, cost = assign_drivers(trip, *drivers)
        if driver not in driver_earnings:
            driver_earnings[driver] = cost
        else:
            driver_earnings[driver] += cost