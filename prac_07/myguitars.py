"""
CP1404
Prac_07
Intermediate Exercises - More Guitars!
"""
from operator import itemgetter

from guitar import Guitar

def main():
    """Read file of guitars, save as objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    for guitar in guitars:
        print(guitar)

    guitars.sort()
    print("These are the oldest guitars:")
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()