def mean(*args):
    nums = [float(i) for i in args]
    return sum(nums) / len(nums)

print(mean(9.0, '6', 9.0, '0'))