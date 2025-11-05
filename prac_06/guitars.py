"""
CP1404/CP5632 Prac_06
Do-From-Scratch Exercise
Estimated time: 60 minutes
Actual time: 52 minutes
"""


from guitar import Guitar


guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:.2f} added. \n")

    name = input("Name: ")

# Test outputs
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("\n ... snip ... \n")
print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")