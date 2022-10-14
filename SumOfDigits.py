def SumOfDigits( n ):
    a = 0
    for i in range(1, len(str(n))+1):
        a = a + (n % 10)
        n = n // 10
    return a



if __name__=='__main__':
    s = SumOfDigits( 12345 )
    print( s )
