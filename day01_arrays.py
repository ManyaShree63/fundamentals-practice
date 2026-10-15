# Day 1: Arrays - traversal, max, min, reverse

def find_max(arr):
    best = arr[0]
    for x in arr:
        if x > best:
            best = x
    return best


def find_min(arr):
    best = arr[0]
    for x in arr:
        if x < best:
            best = x
    return best


def reverse(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def maximum_wealth(accounts):
    best = 0
    for customer in accounts:
        total = sum(customer)
        if total > best:
            best = total
    return best


if __name__ == "__main__":
    print(find_max([4, 9, 1, 7]))        # 9
    print(find_min([4, 9, 1, 7]))        # 1
    print(reverse([1, 2, 3, 4, 5]))      # [5, 4, 3, 2, 1]
    print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))  # 6