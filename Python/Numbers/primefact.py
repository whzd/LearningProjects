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
   if type(n) != int:
      raise TypeError("The sequence term needs to be a non-negative integer number.")
   if n <= 0:
      raise ValueError("The sequence term needs to be non-negative.")
   p = 2
   vec = []
   while n >= p*p:
      if n % p == 0:
         vec.append(p)
         n = n / p
      else:
         p = p + 1
   vec.append(int(n))
   return vec
  

def main():
   while True:
      try:
         n = int(input("Insert the number: "))
      except ValueError:
         print("ERROR: The sequence term needs to be a non-negative integer number.")
      else:
         if n > 0 :
            vec = prime_factors(n)
            print("The Prime Factors of the number {n} are: {fact}".format(n=n, fact=' * '.join(map(str,vec)), end=''))
            break
         else:
            print("ERROR: The sequence term needs to be a non-negative integer number.")

if __name__ == '__main__':
    main()