def linear_search(a, target):
    for idx, i in enumerate(a):
        if i == target:
            return idx
    return False


a = [1, 2, 3, 4, 5, 6, 7]
target = 6

print(linear_search(a, target))
