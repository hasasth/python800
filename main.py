import math

def volume(r):
    return 4/3 * math.pi * r ** 3

radius= float(input('enter the value of r:'))
vol=volume(r=radius)
print(f'the volume of sphere is ={vol}')