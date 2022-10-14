def SumOfNumbersInString( s ):
    a = s.split( )
    b = 0
    for i in range(0, len(a)):
        if a[i].isnumeric():
            a[i] = int(a[i])
            b = b + a[i]

    return b
   


if __name__=='__main__':
    s = '123 abc 45678 defghijk 1'
    t = SumOfNumbersInString( s )
    print( t )
    #assert t == 123+45678+1
    
    
    
