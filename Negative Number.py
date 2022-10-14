def negative(x):
    return x % 2 == 1
a = [2, 5, 6, 9, 7, 3]
result = filter(negative,a)
print('original list :', a)
print('filtered list :', list(result))