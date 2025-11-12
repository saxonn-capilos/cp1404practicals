"""
CP1404
Prac_07
Intermediate Exercises - More Guitars!
"""

from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Run 'myguitars' program."""
    guitars = read_guitars_csv()

    enter_new_guitar(guitars)

    write_guitars_to_csv(guitars, FILENAME)

    # Display guitars by make year
    display_sorted_guitars(guitars)


def display_sorted_guitars(guitars):
    """Display sorted guitars list based on object attribute in __lt__ method."""
    guitars.sort()
    print("\nGuitars sorted by make year:")
    for guitar in guitars:
        print(guitar)


def enter_new_guitar(guitars):
    """Ask the user for name, make year, and cost of a guitar until blank input."""
    name = input("Enter guitar name: ")
    while name != "":
        make_year = int(input("Make year: "))
        cost = float(input("Price: $"))
        guitar = Guitar(name, make_year, cost)
        guitars.append(guitar)
        name = input("Enter guitar name: ")


def read_guitars_csv():
    """Reads csv file and returns a list of objects."""
    guitars = []
    with open('guitars.csv', 'r', newline='') as in_file:
        # in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
        in_file.close()
    return guitars


def write_guitars_to_csv(guitars, out_file):
    """Write the list of guitar objects to the given csv file."""
    with open(FILENAME, 'w') as out_file:
        for guitar in guitars:
            out_file.write(guitar.to_csv() + '\n')


if __name__ == "__main__":
    main()
