# Financial calc

def main():
    print("Profit Margin Ratio Calculator")

    while True:
        try:
            profit = float(input("Enter profit amount: ").strip())
            revenue = float(input("Enter revenue amount: ").strip())

            ratio = profit / revenue   # may cause ZeroDivisionError

        except ValueError:
            pass  # silent reprompting for invalid numbers

        except ZeroDivisionError:
            pass  # silent reprompting if revenue = 0

        else:
            print(f"Profit Margin Ratio: {ratio * 100:.2f}%")
            break   # exit loop once valid input is entered


if __name__ == "__main__":
    main()
        