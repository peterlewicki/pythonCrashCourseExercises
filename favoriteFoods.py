#short script to learn about working with Python dictionaries

favoriteFood = {
    'peter': 'pizza',
    'bryony': 'indian',
    'charles': 'poutine',
    'eli': 'pizza',
}


for name, food in favoriteFood.items():
    print(name, food)

for name in set(favoriteFood.keys()):
    print(name.title())