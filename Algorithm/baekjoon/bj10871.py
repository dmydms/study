a, b = [int(n) for n in input().split(' ')]

nums = [n for n in input().split(' ') if int(n) < b]
print(' '.join(nums))    