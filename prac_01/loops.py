# Odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Question a.
for i in range(0,101,10):
    print(i, end=' ')
print()

# Question b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Question c.
number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    print("*", end="")

# Question d.
number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    print("*" * (i+1))
