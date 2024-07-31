
search_space = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

n = len(search_space)
low = 0
high = n - 1

while low <= high:
    mid = (low+high)/2

    if target == search_space[mid]:
        print(target)
