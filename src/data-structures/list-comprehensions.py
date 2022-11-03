list = [1, 2, 3, 4]

print("Initial list", list)

doubled = [x * 2 for x in list]

print(doubled, "Doubled List")

greather_than_2 = [x for x in list if x > 2]

print(greather_than_2, "Greather than 2")
