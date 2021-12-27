import random
import string


# Dice i sided die roll
def dice_roll():
    print("ROLLING SIX SIDED DIE...  ")
    print(random.randint(1, 6))


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


def print_binary_search_result(search_result):
    if search_result != -1:
        print("Element is present at index", str(search_result))
    else:
        print("Element is not present in array")


# Roll a die
dice_roll()

# Generate a random password
generate_password()

# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)
print_binary_search_result(result)
