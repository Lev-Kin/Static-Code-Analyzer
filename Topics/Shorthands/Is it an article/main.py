import re

def is_article(word):
    return bool(re.match(r'\bthe\b', word))

word = input()
print(is_article(word))