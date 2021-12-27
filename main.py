import random
import string
import logging
import pyowm
from pyowm import OWM
import requests, json

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S')
logging.info("Logging activity for DiceRoll...")


# Dice i sided die roll
def dice_roll(die_num, die_num_side):
    count = 0
    print("ROLLING SIX SIDED DICE...  ")
    while count < int(die_num):
        print(random.randint(1, int(die_num_side)))
        count = count + 1


# Generate a random password
def generate_password():
    randompassword = ''.join(
        [random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(12)])
    print("The generated random password is: " + randompassword)


# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


# Checks if the element is in the array, and if so, prints the index
def print_binary_search_result(search_result):
    if search_result != -1:
        print("Element is present at index", str(search_result))
    else:
        print("Element is not present in array")


def get_weather():
    api_key = "e73cc6d6927a19e138e5d9f3349ebca9"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter city name : ")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature (in kelvin unit) = " +
              str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in percentage) = " +
              str(current_humidity) +
              "\n description = " +
              str(weather_description))

    else:
        print(" City Not Found ")


# Roll a die
logging.info("See how many side is the die")
num_die_side = input("How many sided die? ")
logging.info("See how many die is going to be rolled")
num_dice = input("How many die you want to roll? ")
dice_roll(num_dice, num_die_side)

# Generate a random password
generate_password()

# Test array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)
print_binary_search_result(result)

get_weather()