# Handling Invalid Sales Data Inputs

def get_valid_number(prompt, number_type=float):
    while True:
        user_input = input(prompt).strip()
        try:
            return number_type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {number_type.__name__}.")


def main():
    print("Retail Sales Data Entry")

    units_sold = get_valid_number(
        "Enter the number of units sold: ", int
    )
    price_per_unit = get_valid_number(
        "Enter the price per unit: "
    )

    total_sales = units_sold * price_per_unit
    print(f"Total sales amount: ${total_sales:.2f}")


if __name__ == "__main__":
    main()
