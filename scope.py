#global scope
#local scope
#nonlocal

x = 3

def make_powerful(number):
    global powerfull_number
    powerfull_number = number ** x
    return powerfull_number

make_powerful(5)
print("printing from global scope", powerfull_number)