import requests
def get_exchange_rates():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching exchange rates:", response.status_code)
        return None
def convert_currency(amount, currency, rates):
    if currency in rates:
        exchange_rate = rates[currency]
        return amount * exchange_rate
    else:
        print("Wrong currency")
        return None
def main():
    rates_data = get_exchange_rates() 
    if rates_data:
        rates = {item['cc']: item['rate'] for item in rates_data if item['cc'] in ['EUR', 'USD', 'PLN']}
        print("Available currencies: EUR, USD, PLN")
        currency = input("Enter the currency code (EUR, USD, PLN): ").upper()
        if currency in rates:
            try:
                amount = float(input(f"Enter the amount in {currency}: "))
                converted_amount = convert_currency(amount, currency, rates)    
                if converted_amount is not None:
                    print(f"{amount} {currency} is equal to {converted_amount:.2f} UAH")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Unsupported currency. Please try again.")
if __name__ == "__main__":
    main()
