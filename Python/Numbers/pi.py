# Finding pi to the nth digit using
# the Nilakantha's Series to calculate its value

def find_pi(n):
    if type(n) != int:
        raise TypeError("The decimal place needs to be a non-negative integer number.")
    if n < 1 or n > 10:
        raise ValueError("The decimal places can only go from 1 to 10.")

    s = 1
    pi = 3
    for i in range(2,(10000)+1,2):
        pi = pi + s * (4 / (i * (i + 1) * (i + 2)))
        s = -s
    return format(pi, ('.%df' % n))
        
        
def main():
    while True:
        try:
            n = int(input("Insert a value: "))
        except ValueError:
            print("ERROR: The decimal place needs to be a non-negative integer number.")
        else:
            if n > 0 and n<=10:
                res = find_pi(n)
                print("The value of Pi to the {n}th digit is {res}".format(n=n, res=res))
                break
            else:
                print("ERROR: The decimal place needs to be between 1 and 10.")

if __name__ == '__main__':
    main()