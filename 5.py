def is_prime(num):
    for i in range(2, int(num**(1/2))):
        if num % i == 0 :
            return False
    return True

def next_prime(num):
    while True :
        if is_prime(num) :
            return num
        else :
            num += 1

def getPrimes (num) :
    primes = {}
    i = 2

    while (num != 1) :
        if num % i == 0 :
            if i not in primes.keys():
                primes[i] = 1
            else :
                primes[i] += 1
            num = num // i
        else :
            i = next_prime(i+1)

    return primes

if __name__ == "__main__" :
    i = 2
    factors = {}
    while i <= 20 :
        primes = getPrimes(i) # Get prime factorization of the number
        for key in primes.keys() :
            if key not in factors :
                factors[key] = 1
            else :
                if factors[key] < primes[key] :
                    factors[key] = primes[key]
        i += 1
    mult = 1
    for key in factors.keys() :
        mult = mult * (key ** factors[key])

    print(mult)