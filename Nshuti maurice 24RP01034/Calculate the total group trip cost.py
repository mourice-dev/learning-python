# Question 4: Calculate the total group trip cost.

price_per_person = 250
group_size = 15
group_discount = 100
total_discount = (group_size // 5) * group_discount
group_trip_cost = (price_per_person * group_size) - total_discount
print(group_trip_cost)