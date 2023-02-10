## CIS3301-CODE-7-Temperature-Conversion-with-Functions

In this coding assignment, you are asked to create a little program that executes temperature conversions from Fahrenheit to Celsius and Kelvin. Additionally, your program should give the user a suggestion of clothing depending on the temperature in Celsius that the program receives.

You are going to code this program in four different functions. The functions are:

* `get_temperature_in_celsius`:
  + The function receives the temperature in **Fahrenheit**
  + The function **must** return the temperature in **Celsius**.
* `get_temperature_in_kelvin_from_c`:
  + The function receives the temperature in **Celsius**.
  + The function **must** return the temperature in **Kelvin**.
* `get_temperature_in_kelvin_from_f`:
  + The function receives the temperature in **Fahrenheit**.
  + The function **must** return the temperature in **Kelvin**.
* `get_clothing_recommendation`:
  + The function receives the temperature in **Celsius**.
  + The function must return a random item from the following lists:
    - Temperature below or equal to 10C - Return a **random** item from **cold_weather_clothing**
    - 10C < Temperature <= 15C  - Return a **random** item from **cool_weather_clothing**
    - 15C < Temperature <= 25C  - Return a **random** item from **warm_weather_clothing**
    - 26C < Temperature <= 35C  - Return a **random** item from **hot_weather_clothing**

## User Prompts

In this program, you can code/create any user prompts. However, all the outputs to the user must be inside the following if statement:

`if __name__ == "__main__":`

Make sure you code your assignment in the file "code_7.py". Also, do not forget to implement your code inside the respective functions.
