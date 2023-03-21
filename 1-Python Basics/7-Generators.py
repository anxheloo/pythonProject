#Generators are used to create certain type of lists -> we use the yield function to create

def function():
    counter = 0
    while counter < 5:
        yield counter
        counter +=1


def even_numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

for x in function():
    print(x)

print(list(function()))
print(list(even_numbers(25)))
