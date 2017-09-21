kilobyte = 1024
megabyte = 1048576
terabyte = 1099511627776
terabyte2m = 1000000

print(f"Press 1 to convert from kilobytes to bytes")
print(f"Press 2 to convert from megabytes to bytes")
print(f"Press 3 to convert from terabytes to bytes")
print(f"Press 4 to convert from terabytes to megabytes")

def conversion1():
    num = int(input()) * kilobyte
    print(f"{num} bytes")

def conversion2():
    num = int(input()) * megabyte
    print(f"{num} bytes")

def conversion3():
    num = int(input()) * terabyte
    print(f"{num} bytes")

def conversion4():
    num = int(input()) * terabyte2m
    print(f"{num} megabytes")

x = int(input())
if x == 1:
    print("Type number for conversion")
    conversion1()
elif x == 2:
    print("Type number for conversion")
    conversion2()
elif x == 3:
    print("Type number for conversion")
    conversion3()
elif x == 4:
    print("Type number for conversion")
    conversion4()
