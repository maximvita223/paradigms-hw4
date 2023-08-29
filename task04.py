import math

def prime_numbers():
    count = 3
    while True:
        isprime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        if isprime:
            yield count
        count += 1

eazy = prime_numbers()

for _ in range(10):
    print(next(eazy))
