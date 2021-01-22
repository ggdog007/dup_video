import numpy as np

a = np.random.randint(10, 80, 20).tolist()
# a= [39, 20, 56, 30, 53, 62, 46, 61, 40, 70, 37, 39, 66, 51, 74, 71, 39, 20, 14, 39]
print("a=",a)
print("\n")

c = []
start = 1

while a:
    b = []
    d = []
    base = a[0]

    for item in a:
        if abs(base - item)<10:
            b.append(item)
        else:
            d.append(item)
    a = d

    if len(b)>1:
        c.append(b)
        print("a=",a)
        print("c=",c)
        print("\n")
