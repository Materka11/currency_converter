### Overview

This is a simple Currency Converter application built using Python and Tkinter. The application allows users to convert a specified amount from one currency to another using a custom conversion class (`ConvertCurrency`).

## Features

- Graphical User Interface (GUI) using Tkinter.
- User inputs:
  - Base currency (e.g., USD)
  - Target currency (e.g., EUR)
  - Amount to convert
- Displays the converted amount.
- Handles errors gracefully.

## Prerequisites

Before running the application, ensure you have Python 3.x installed on your system.

## Installation & Setup

1. Clone or download the repository.
2. Install required dependencies (if any).
3. Ensure that the convert_currency.py module exists and implements the ConvertCurrency class.

## Running the Application

Run the following command in the terminal or command prompt:

```
python app.py
```

(Replace `app.py` with the actual filename of your script if different.)

## Code Explanation

- The UI is created using Tkinter, including labels, input fields, and a button.
- The ConvertCurrency class is responsible for handling the conversion.
- The convert_currency function reads user inputs and updates the result label.

## Dependencies

- Tkinter (comes pre-installed with Python)
- convert_currency.py (Ensure this module is implemented)

## Example Usage

1. Enter USD in the "From Currency" field.
2. Enter EUR in the "To Currency" field.
3. Enter 100 in the "Amount" field.
4. Click the Convert button.
5. The result will be displayed.
   .

## License

This project is open-source. You may modify and distribute it as needed.
