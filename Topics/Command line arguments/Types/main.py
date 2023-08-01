args = sys.argv

args = sys.argv[1:]  # Get the command-line arguments, excluding the script name
numbers = [int(arg) for arg in args]  # Convert the arguments to integers
result = sum(numbers)  # Calculate the sum of the numbers

print(result)