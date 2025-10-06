"""
CP1404 prac_04
Walkthrough Example: Calculating a List of Cumulative Totals
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes, number_of_months)


def print_income_report(incomes, number_of_months):
    """Print income report."""
    report = format_income_report(incomes, number_of_months)
    print(report)


def format_income_report(incomes, number_of_months):
    """Format income data into a report string."""
    totals = calculate_running_total(incomes[:number_of_months])

    lines = ["\nIncome Report", "-------------"]
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total = totals[month - 1]
        lines.append("Month {:2} - Income: ${:10.2f} \t Total: ${:10.2f}".format(month, income, total))

    return "\n".join(lines)


def calculate_running_total(incomes):
    """Calculate running total for income."""
    total = 0
    totals = []
    for income in incomes:
        total += income
        totals.append(total)
    return totals


main()