import copy


def detect_copy():
    obj = [[1, 2]]
    copy_obj = copying_machine(obj)

    if id(obj[0]) == id(copy_obj[0]):
        return "shallow copy"
    else:
        return "deep copy"
