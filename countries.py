#straightforward python code to help learn how to create and work with lists etc

countries = ["Canada", "Mexico", "United States", "Cuba"]
for country in countries:
    print(country)

countries.append("Haiti")
print(countries)

for country in countries:
    print(country)

for country in countries:
    print(f"{country} is a North American country.")
    print(f"GO, {country.upper()}, GO!\n")
    print("One step closer to to a well paid job. Pat yourself on the back.")