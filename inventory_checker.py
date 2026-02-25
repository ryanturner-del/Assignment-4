# Inventory Quantity Checker with Error Handling

def get_valid_int(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    print("Inventory Checker")

    inventory = get_valid_int("Enter the current inventory quantity: ")

    while True:
        threshold = get_valid_int("Enter the threshold quantity: ")

        try:
            percent_of_threshold = (inventory / threshold) * 100
        except ZeroDivisionError:
            print("Threshold cannot be zero. Please enter a valid threshold.")
            continue

        print(f"Inventory is {percent_of_threshold:.2f}% of the threshold.")

        if inventory < threshold:
            print("Inventory is below the threshold. Consider restocking.")
        else:
            print("Inventory is sufficient.")

        break  # valid threshold entered


if __name__ == "__main__":
    main()
