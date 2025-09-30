"""
Do-from-scratch Exercise: Files
"""

# 1.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = name.rstrip()
print(f"Hi {name}!")
in_file.close()

