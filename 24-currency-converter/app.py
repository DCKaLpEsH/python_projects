import requests

currency_codes = {"USD":"United States Dollar", "INR":"Indian Rupee", "AUD":"Australian Dollar", "CAD":"Canadian Dollar", "CHF":"Swiss Franc", "CNY":"Chinese Yuan", "EUR":"Euro", "GBP":"British Pound", "JPY":"Japanese Yen", "NZD":"New Zealand Dollar", "RUB":"Russian Ruble", "SAR":"Saudi Riyal", "SGD":"Singapore Dollar"}

currency_emojis = {
    "USD": "💲",
    "INR": "₹",
    "AUD": "A$",
    "CAD": "C$",
    "CHF": "CHF",
    "CNY": "CN¥",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "NZD": "NZ$",
    "RUB": "₽",
    "SAR": "﷼",
    "SGD": "SGD"
}


def get_exchange_rates():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        rates = data["rates"]
        rates_for_currency_codes = {code: rates[code] for code in currency_codes}
        return rates_for_currency_codes
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def convert_currency(rates):
    print("\nCurrency Conversion Menu\n")

    from_currency = input("Enter the currency code to convert from: ").upper()
    to_currency = input("Enter the currency code to convert to: ").upper()
    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    if from_currency not in rates or to_currency not in rates:
        print("Invalid currency code. Please try again.")
        return

    converted_amount = amount * rates[to_currency] / rates[from_currency]
    print(f"🪙 {currency_emojis[from_currency]}{amount} {from_currency} is equal to {currency_emojis[to_currency]}{converted_amount:.2f} {to_currency} 🪙")


def main():
    print("==== Currency Converter ====")
    print("Convert currencies using the latest exchange rates.")
    print("\nGetting exchange rates...")
    rates = get_exchange_rates()
    if rates is None:
        print("Failed to retrieve exchange rates. Exiting program.")
        return
    print("Exchange rates retrieved successfully.")

    while True:
        print("\nCurrency Conversion Menu")
        print("1. Convert Currency")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            convert_currency(rates)
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

