#Make a list of dinner guests you would like to invite. . Print a message to invite each of them, Modify the list as needed if people cant come or new guests get invited.

guests = ["Johann Sebastian Bach", "President Nixon", "Chevy Chase"]
dinnerGuest = guests.pop(1)
print(f"Excuse me, {dinnerGuest}, would you like to come over for dinner?")
del guests[1]
guests.append("C.S. Lewis")
print(guests)
print(f"Can we invite {guests[0]} instead?")
guests.append("Wayne Gretzky")
print(guests)

print(guests)

print(guests)
guests.sort()
print(guests)

guests.sort(reverse=True)

guests.reverse()
print(guests)
