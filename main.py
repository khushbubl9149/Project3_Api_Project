
import requests


def get_weather():
    city = input("Enter city name: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    url = "https://wttr.in/" + city

    try:
        response = requests.get(
            url,
            params={"format": "3"},
            timeout=10
        )

        response.raise_for_status()
        print("\nWeather Information:")
        print(response.text)

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.HTTPError:
        print("Error: Unable to find weather information.")

    except requests.exceptions.RequestException as e:
        print("Network error:", e)


def currency_converter():
    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        from_currency = input(
            "From currency (e.g. USD): "
        ).strip().upper()

        to_currency = input(
            "To currency (e.g. INR): "
        ).strip().upper()

        if not from_currency or not to_currency:
            print("Currency codes cannot be empty.")
            return

        url = (
            f"https://open.er-api.com/v6/latest/"
            f"{from_currency}"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("result") != "success":
            print("Error: Invalid source currency.")
            return

        rates = data.get("rates", {})

        if to_currency not in rates:
            print("Error: Invalid target currency.")
            return

        converted_amount = amount * rates[to_currency]

        print("\nCurrency Conversion:")
        print(f"{amount:.2f} {from_currency} = "
              f"{converted_amount:.2f} {to_currency}")

    except ValueError:
        print("Error: Please enter a valid number.")

    except requests.exceptions.Timeout:
        print("Error: API request timed out.")

    except requests.exceptions.HTTPError:
        print("Error: HTTP request failed.")

    except requests.exceptions.RequestException as e:
        print("Network error:", e)


def main():
    while True:
        print("\n===== API TOOL =====")
        print("1. Check Weather")
        print("2. Currency Converter")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            get_weather()

        elif choice == "2":
            currency_converter()

        elif choice == "3":
            print("Thank you for using API Tool!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
