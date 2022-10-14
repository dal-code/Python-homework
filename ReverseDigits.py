def ReverseDigits( n ):
    a = []
    for i in range(len(str(n))):
        a.append(n % 10)
        n = n // 10
    a.reverse()
    return  a




if __name__=='__main__':
    n = ReverseDigits( 123 )
    print( n )

