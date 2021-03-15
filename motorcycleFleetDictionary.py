# learning to use Python range and dictionaries to make a fleet of imaginary motorcycles

motorcycle = []
for motorcycleFleet in range(10):
    newMoto = {'Make': 'Triumph', 'Model': 'Bonneville'}
    motorcycle.append(newMoto)
print(f"there are {len(motorcycle)}")