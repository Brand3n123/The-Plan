class Trip:
    def __init__(self, location, distance_miles, speed):
        self.location = location
        self.distance_miles = distance_miles
        self.speed = speed
    
    def __repr__(self):
        trip_time = self.distance_miles / self.speed
        return f"The {self.distance_miles} mile trip to {self.location} will take {trip_time} hours at a speed of {self.speed} MPH."
    
    def speed_up(self, increase_speed):
        self.speed += increase_speed
    
    def slow_down(self, decrease_speed):
        self.speed -= decrease_speed

Vacation = Trip("Savannah, GA", 500, 55)
Business_Italy = Trip("Italy", 2000, 300)
Business_Italy.speed_up(100)
Vacation.slow_down(25)
Vacation.speed_up(470)

def check_fastest(*trips):
    fastest_trip = None
    for trip in trips:
        if fastest_trip == None:
            fastest_trip = trip
        elif fastest_trip.speed < trip.speed:
            fastest_trip = trip
    return fastest_trip.location

print(check_fastest(Vacation, Business_Italy))