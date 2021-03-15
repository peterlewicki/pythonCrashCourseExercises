#pizza example to learn about lists inside dictionaries
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'pepperoni', 'onion'],
}

#summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings: ")
for topping in pizza['toppings']:
    print(f'\t{topping}')