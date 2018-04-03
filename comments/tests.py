a = [1,2,3,4]

index = len(a) - 1
if len(a) > 2:
    for i in range(3):
        while index >= 0:
            a[index],a[index-1] = a[index-1],a[index]
            index -= 1
print(a)