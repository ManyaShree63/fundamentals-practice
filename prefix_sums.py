def build_prefix(nums):
    prefix = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x
    return prefix

def range_sum(prefix, i, j):
    return prefix[j + 1] - prefix[i]

nums = [2, 4, 1, 3]
prefix = build_prefix(nums)
print(prefix)
print(range_sum(prefix, 1, 2))