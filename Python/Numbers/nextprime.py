def is_prime(n):
     if n <= 1:
        return False
     elif n <= 3:
        return True
     elif (n % 2 == 0) or (n % 3 == 0):
        return False
     i = 5
     while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i = i + 6
     return True


def next_prime(n):
    if type(n) != int:
        raise TypeError("The sequence term needs to be a non-negative integer number.")
    if n <= 0:
        raise ValueError("The sequence term needs to be non-negative.")
    i = n+1
    while True:
        if(is_prime(i)):
            return i
        i = i+1


def main():
    n=1
    val = next_prime(n)
    print("Prime number: %d" % val)
    while True:
      try:
        opcao = int(input("Next Prime?\n[1-Yes|0-Stop] : "))
      except ValueError:
        print("ERROR: Invalide Option!")
        print("----------------------")
        print("Prime number: %d" % val)
      else:
        if opcao == 0 :
            break
        elif opcao == 1:
            n = val
            val = next_prime(n)
            print("----------------------")
            print("Prime number: %d" % val)
        else:
            print("ERROR: Invalide Option!")
            print("----------------------")
            print("Prime number: %d" % val)

if __name__ == '__main__':
    main()