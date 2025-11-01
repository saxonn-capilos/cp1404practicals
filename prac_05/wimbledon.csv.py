"""
Wimbledon
Estimate: 60 minutes
Actual: 40 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    champions_data = read_wimbledon_data(FILENAME)
    champion_to_wins = count_champion_wins(champions_data)
    print("Wimbledon champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")

    champion_countries = count_champion_countries(champions_data)
    sorted_countries = sorted(champion_countries)
    countries_string = ', '.join(sorted_countries)
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:")
    print(countries_string)


def read_wimbledon_data(filename):
    """Read the data from wimbledon.csv and return as list of lists"""
    champions_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            year = parts[0].strip()
            country = parts[1].strip()
            name = parts[2].strip()
            champions_data.append([year, country, name])
        champions_data.pop(0)
    return champions_data


def count_champion_wins(champions_data):
    """Return a dictionary of how many times each champion has won"""
    champion_to_wins = {}
    for record in champions_data:
        name = record[2]
        if name in champion_to_wins:
            champion_to_wins[name] += 1
        else:
            champion_to_wins[name] = 1
    return champion_to_wins


def count_champion_countries(champions_data):
    """Get every different champion country from the date"""
    countries = set()
    for record in champions_data:
        country = record[1]
        countries.add(country)
    return countries


main()