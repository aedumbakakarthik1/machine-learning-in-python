# Map Fuction in python

def even_or_odd(num):
    if num% 2 == 0:
        return "the {} is even ".format(num)
    else:
        return "the {} is odd ".format(num)
a=even_or_odd(24)
print(a)

# now we use the function

lst=[1,2,3,4,5,6,7,8,9]
print(list(map(even_or_odd,lst)))