import tkinter as tk
from convert_currency import ConvertCurrency

window = tk.Tk()
window.title("Currency Converter")


from_currency_label = tk.Label(window, text="From Currency (e.g. USD):")
from_currency_label.grid(row=0, column=0)
from_currency_entry = tk.Entry(window)
from_currency_entry.grid(row=0, column=1)

to_currency_label = tk.Label(window, text="To Currency (e.g. EUR):")
to_currency_label.grid(row=1, column=0)
to_currency_entry = tk.Entry(window)
to_currency_entry.grid(row=1, column=1)

amount_label = tk.Label(window, text="Amount:")
amount_label.grid(row=2, column=0)
amount_entry = tk.Entry(window)
amount_entry.grid(row=2, column=1)



def convert_currency():
    try:
        converter = ConvertCurrency(from_currency_entry, to_currency_entry, amount_entry)
        result = converter.getResult()
        result_label.config(text=result)
    except ValueError as e:
        result_label.config(text=f"Error: {str(e)}") 


convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2)


result_label = tk.Label(window, text="Result will appear here")
result_label.grid(row=4, column=0, columnspan=2)


window.mainloop()
