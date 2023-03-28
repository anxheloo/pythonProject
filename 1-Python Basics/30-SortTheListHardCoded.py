
a = [1,2,4,-5,7,9,3,2]

for i in range(len(a)):
    for j in range(i + 1, len(a)):

        if a[i] > a[j]:
           a[i], a[j] = a[j], a[i]

print(a)