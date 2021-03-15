
#various exercises to learn for loops, ranges etc in Python

for value in range(101):
    print(value)

numbers = list(range(1, 5000))
print(numbers)

evens = list(range(2, 20, 2))
print(evens)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#same as the above except even more condensed, something called a list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

bloop = [value+10 for value in range(2,30,2)]
print(bloop)

millions = []
for value in range(1,1000001):
    millions.append(value)
print(sum(millions))