# Age Verification

def get_customer_age():
    while True:
        raw = input("Please enter your age: ").strip()
        try:
            age = int(raw)
            if age <= 0:
                print("Age must be positive. Please try again.")
                continue
            return age
        except ValueError:
            print("Invalid input. Please enter a valid age.")


def main():
    print("Welcome to the age verification system.")

    # Simulate NameError by commenting this out first
    # eligible_age = 18

    try:
        age = get_customer_age()

        if age >= eligible_age:
            print("Customer is eligible for age-restricted promotions.")
        else:
            print("Customer is NOT eligible for age-restricted promotions.")

    except NameError:
        print("NameError occurred: eligible_age is not defined.")
        print("Fix: Uncomment 'eligible_age = 18'.")


if __name__ == "__main__":
    main()