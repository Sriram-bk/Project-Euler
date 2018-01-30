def isPal(x) :
    rev_x = int((str(x))[::-1])
    if x == rev_x :
        return True
    else :
        return False

if __name__ == "__main__" :
    largest_pal = 0
    i = 999
    while i >= 100 :
        j = 999
        while j >= i :
            if i*j <= largest_pal :
                break
            if isPal(i*j) :
                largest_pal = i*j
            j -= 1
        i -= 1
    print(largest_pal)