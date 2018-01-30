def is_prime(num):
    for i in range(2, int(num**(1/2))):
        if num % i == 0 :
            return False
    return True


if __name__ == "__main__" :
    num = 600851475143
    i = 2

    while i < num**(1/2) :
        if (num % i == 0) :
            if(is_prime(i)) :
                high = i
            elif (is_prime(num // i)) :
                print(num // i)
                break
        i += 1

    print(high)