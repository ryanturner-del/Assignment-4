# salary_adjustment.py
# Exercise 5: Employee Salary Adjustment Simulator

def get_valid_float(prompt):
    """Keep prompting until the user enters a valid float."""
    while True:
        text = input(prompt).strip()
        try:
            return float(text)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("Salary Adjustment Simulator")

    current_salary = get_valid_float("Enter the employee's current salary: ")
    adjustment_percent = get_valid_float("Enter the adjustment percentage (0 to 100): ")

    if adjustment_percent < 0:
        print("Adjustment percentage cannot be negative.")
        return

    if adjustment_percent > 100:
        print("Adjustment percentage cannot be greater than 100.")
        return

    new_salary = current_salary * (1 + adjustment_percent / 100)
    print(f"New salary: ${new_salary:.2f}")


if __name__ == "__main__":
    main()