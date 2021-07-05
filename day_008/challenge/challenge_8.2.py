# Prime number checker
# Check with the highest prime number to test the speed of both methods - Eg: 100001777
# List of prime numbers website - http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php

import time


def prime_checker(num):
    if num > 1:
        for n in range(2, num):
            if num % n == 0:
                return print("It's not a prime number")
        else:
            return print("It is a prime number")


method_1 = int(input("Check the number : "))
t0 = time.time()
prime_checker(method_1)
t1 = time.time()
t = t1 - t0
print(f"Time taken : {t}")

print("\n")

# Efficient method
print("Efficient Method")


def prime(num):
    if num <= 1:
        print("1 is neither prime nor composite number")
    elif ((num + 7) / 6) == type(int) or ((num - 7) / 6) == type(int):
        print("hello")
        print("It is a prime number")
    else:
        print("It's not a prime number")


method_2 = int(input("Check the number : "))
t0 = time.time()
prime(method_2)
t1 = time.time()
t = t1 - t0
print(f"Time taken : {t}")
