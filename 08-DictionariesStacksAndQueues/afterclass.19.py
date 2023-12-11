import requests

def get_last_ten_euro_rates():
    url = "http://api.nbp.pl/api/exchangerates/rates/A/EUR/last/10/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx status codes)

        # Parse the JSON response
        data = response.json()
        
        # Extract relevant information from the response
        euro_rates = data.get("rates", [])

        return euro_rates

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Get and print the last ten Euro exchange rates
euro_rates = get_last_ten_euro_rates()

if euro_rates:
    print("Last Ten Euro Exchange Rates:")
    for rate in euro_rates:
        print(f"Date: {rate['effectiveDate']}, Rate: {rate['mid']} {rate['code']}")
else:
    print("Unable to retrieve exchange rate data.")
