import math

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

def prime_factors(n):

 if(is_prime(n)):
    print(n),
 else:
    for i in range(2, int(math.sqrt(n))):
        if(n%i == 0):
              prime_factors(i)
              prime_factors(n//i)

def main():
    prime_factors(28)

if __name__ == '__main__':
    main()