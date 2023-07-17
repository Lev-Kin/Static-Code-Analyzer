numbers = input()
digits = [int(x) for x in numbers]

averages = [(digits[i] + digits[i+1]) / 2 for i in range(len(digits)-1)]

print(averages)
