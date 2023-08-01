import copy


def solve(obj):
    try:
        copied_obj = copy.deepcopy(obj)
        return copied_obj is not obj
    except Exception:
        return False
