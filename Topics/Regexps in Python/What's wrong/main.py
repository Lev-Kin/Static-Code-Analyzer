import re

w1 = input()
w2 = input()

# The correct method name is match(), not mach()
if re.match(w1, w2):
    # len(w) should be changed to len(w1) to calculate the length of the first word
    print(len(w1) * 2)
else:
    print('no matching')