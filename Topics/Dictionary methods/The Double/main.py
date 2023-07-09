double_alphabet = {}

for i in range(97, 123):  # Unicode range for lowercase letters 'a' to 'z'
    letter = chr(i)  # Convert Unicode number to character
    double_alphabet[letter] = letter * 2
