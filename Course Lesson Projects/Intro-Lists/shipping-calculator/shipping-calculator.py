#input weight of package
weight = 1.5

#assign cost variables by shipping method
ground_cost = 0
ground_prem_cost = 125
drone_cost = 0

#Ground Shipping
if (weight <= 2):
  ground_cost = (20 + (weight * 1.5))
elif (weight > 2 and weight <= 6):
  ground_cost = (20 + (weight * 3))
elif (weight > 6 and weight <= 10):
  ground_cost = (20 + (weight * 4))
elif (weight > 10):
  ground_cost = (20 + (weight * 4.75)) 

print("Ground Shipping: $", ground_cost)

#Premium Ground Shipping

print("Ground Shipping Premium: $", ground_prem_cost)


#Drone Shipping
if (weight <= 2):
  drone_cost = weight * 4.50
elif (weight > 2 and weight <= 6):
  drone_cost = weight * 9.00
elif (weight > 6 and weight <= 10):
  drone_cost = weight * 12.00
elif (weight > 10):
  drone_cost = weight * 14.25

print("Drone Shipping: $", drone_cost)