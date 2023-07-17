import operator

sorted_books = sorted(books.items(), key=operator.itemgetter(1))

# Print the title of the first book (shortest)
print(sorted_books[0][0])

# Print the title of the last book (longest)
print(sorted_books[-1][0])