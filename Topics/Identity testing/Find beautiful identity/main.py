def object_with_beautiful_identity():
    for i in range(10_000):
        if id(i) % 1000 == 888:
            return i


# Call the function to find the object
# result = object_with_beautiful_identity()
# print(result)
