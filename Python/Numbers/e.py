# Finding euler's number (e) to the 'n'th digit
# using Newton's Series Expansion to calculate its value

def fatorial(val):
    if val >= 1:
        return val * fatorial(val-1)
    else:
        return 1

def find_e(n):
    if type(n) != int:
        raise TypeError("The decimal place needs to be a non-negative integer number.")
    if n < 1 or n > 14:
        raise ValueError("The decimal places can only go from 1 to 14.")

    euler = 0
    for i in range(n+4):
        euler = euler +(1/fatorial(i))
        
    return format(euler, ('.%df' % n))
    

def main():
    while True:
        try:
            n = int(input("Insert a value: "))
        except ValueError:
            print("ERROR: The decimal place needs to be a non-negative integer number.")
        else:
            if n > 0 and n<=14:
                res = find_e(n)
                print("The value of the euler's number to the {n}th digit is {res}".format(n=n, res=res))
                break
            else:
                print("ERROR: The decimal place needs to be between 1 and 14.")

if __name__ == '__main__':
    main()