objects = [["Train", 22680, 10], 
           ["Car", 1500, 3], 
           ["Boulder", 500, 9.8]]

def get_force(mass, acceleration):
    return mass * acceleration 
def get_energy(mass, c=3*10**8):
    return mass * (c**2)

for object in objects:
        print(f"{object[0]}: Force = {get_force(object[1], object[2])} N, Energy = {get_energy(object[1])}")