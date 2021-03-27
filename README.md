# Relationship between two numbers
def relationship(a, b):
    if a >b:
        print(1)
    if a <b:
        print(-1)    
    if a == b:
        print(0)

a = int(input('Write a number: '))
b = int(input('Write a number: '))
relationship(a, b)
