# Calculating the term number n of tha Fibonacci Sequence

def fibonacci_sequence(n):
    if type(n) != int:
        raise TypeError("The sequence term needs to be a non-negative integer number.")
    if n < 0:
        raise ValueError("The sequence term needs to be non-negative.")
    if n < 2:
        return n
    else:
        return fibonacci_sequence(n-1)+fibonacci_sequence(n-2)

def main():
    while True:
        try:
            n = int(input("Insert the sequence term number: "))
        except ValueError:
            print("ERROR: The sequence term needs to be a non-negative integer number.")
        else:
            if n >= 0 and n<= 30:
                res = fibonacci_sequence(n)
                print("The term number {n} of the fibonacci sequence is {res}.".format(n=n, res=res))
                break
            elif n > 30 :
                goOn = input("WARNING: Choosing a term number above 30 may take a long time to calulate, do you want to proceed ? [Y/N]: ")
                if goOn.lower() == "y":
                    res = fibonacci_sequence(n)
                    print("The term number {n} of the fibonacci sequence is {res}.".format(n=n, res=res))
                    break
            else:
                print("ERROR: The sequence term needs to be a non-negative integer number.")

if __name__ == '__main__':
    main()