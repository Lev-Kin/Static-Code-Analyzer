def check_name(name):
    first_letter = name[0]
    second_letter = name[1]

    if 'B' <= first_letter <= 'N' and second_letter in r'aeiouAEIOU':
        print("Suitable!")


# Test with the sample input
name = input()
check_name(name)
