import requests

API_LINK = "https://api.frankfurter.app/"

class ConvertCurrency():
    def __init__(self, from_currency_entry, to_currency_entry, amount_entry):
        self.from_currency = from_currency_entry.get().upper()
        self.to_currency = to_currency_entry.get().upper()

        amount_input = amount_entry.get()
        if not amount_input or not amount_input.replace('.', '', 1).isdigit(): 
            raise ValueError("Please enter a valid amount.")
        
        self.amount = float(amount_input)
        
    def getResult(self): 
        try:
            if self.amount <= 0:
                raise ValueError("Amount must be greater than zero.")
        
            response = requests.get(f"{API_LINK}latest?amount={self.amount}&from={self.from_currency}&to={self.to_currency}")
            
            if response.status_code != 200:
                raise Exception("Failed to fetch data from the API.")
            
            data = response.json()
            if self.to_currency not in data['rates']:
                raise Exception(f"Invalid currency: {self.to_currency}")
            
            result = data['rates'][self.to_currency]
            return f"{self.amount} {self.from_currency} = {result} {self.to_currency}"

        except requests.exceptions.RequestException as e:
                return f"Request Error", f"Error occurred: {str(e)}"
        except ValueError as e:
                return f"Invalid Input", f"Invalid input: {str(e)}"
        except Exception as e:
                return f"Error", str(e)

        
        
           


