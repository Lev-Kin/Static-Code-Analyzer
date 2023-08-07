def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Read the input number
input_number = int(input())

# Calculate the sum of digits and print the result
result = sum_of_digits(input_number)
print(result)