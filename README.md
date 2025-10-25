Multi Converter

  Multi Converter is a simple Python-based console application that allows users to perform different types of unit conversions — including Length, Currency, and Temperature conversions — all from a single program.

Features

  Length Converter
  Convert between meters and feet with ease.

  Meters → Feet
  
  Feet → Meters
  
  Currency Converter
  Convert between Indian Rupees (INR) and US Dollars (USD).
  
  INR → USD
  
  USD → INR
  (Note: The conversion rate is set as 1 USD = 88 INR for demonstration purposes.)
  
  Temperature Converter
  Convert between Celsius and Fahrenheit.
  
  Celsius → Fahrenheit
  
  Fahrenheit → Celsius

User-Friendly Menu System
The program runs in a loop and allows you to select different converters or exit anytime.

🧠 How It Works

  Run the Python file.
  
  The program displays a main menu with four options:
  
  1 → Length Converter
  
  2 → Currency Converter
  
  3 → Temperature Converter
  
  4 → Exit

Choose a conversion type and follow the prompts to input your values.

The program will calculate and display the result.

You can continue converting or exit the program anytime.

Code Structure

  multi_converter() → Main menu function
  
  Length_converter() → Handles length conversions
  
  Currency_Converter() → Handles currency conversions
  
  Temperature_Converter() → Handles temperature conversions
  
  Each converter function:
  
  Takes user input
  
  Performs calculation using a simple formula
  
  Displays the converted value
