#Think of a few places you'd like to visit.  Put them in a list, make sure theyre not in alphabetical order.
#use some of the concepts learned in this chapter (such as sorted(), reverse(), etc to modify the list

cities = ["Paris", "Rome", "New Orleans", "Los Angeles"]
visit = f"The city I'd most like to visit is {cities[1]}"
print(visit)

cities[0] = "Warsaw"
print(cities)

cities.append("Paris")
cities.append("London")
print(cities)

cities.insert(0, "Brantford")
print(cities)

del cities[0]
print(cities)

print(cities)
american = cities.pop(2)
print(f"{american} is the North American city I most want to visit.")

alreadyBeen = "Paris"
cities.remove(alreadyBeen)
print(f"I've already been to {alreadyBeen}.")

print(len(cities))

print(sorted(cities))







