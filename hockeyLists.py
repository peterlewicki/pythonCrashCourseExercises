#Creating a list of Canadian NHL teams to practice working with lists and if statements in Python

teams = ["senators", "leafs", "canadiens", "jets", "oilers", "flames", "canucks"]
for team in teams:
    if team == "leafs":
     print(team.title())


print(teams)

newTeam = "bruins"
if newTeam not in teams:
    print(f"The {newTeam.title()} are not a Canadian team. ")

print(teams)
for team in teams:
    if team == "leafs":
        print(f"The {team} are my favorite Canadian team")
    else:
        print("That's a no from me, dog.")

print("\n")

print(teams)
listTeams = ["canadiens", "riffraff", "canucks"]
for listTeam in listTeams:
    if listTeam in teams:
        print(f"Yes, {listTeam} is the name of a hockey team")
    else:
        print(f"No,{listTeam} is not a real hockey team")