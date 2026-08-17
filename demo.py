def check_even_odd(number):
    """Function to check if a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
test_value = 17
result = check_even_odd(test_value)
print(f"The number {test_value} is {result}.")
