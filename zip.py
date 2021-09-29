def compare():
    a = [1,2,3]
    return (i<=j for i,j in zip(a, a[1:]))

print(compare())

