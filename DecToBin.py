def DecToBin( n ):
    a =[]
    while (1):
        x = n % 2
        a.insert(0, str(x))
        n = int(n / 2)
        if n == 0:
            break
    return "".join(a)




if __name__=='__main__':
    s = DecToBin( 32 )
    print( s )
