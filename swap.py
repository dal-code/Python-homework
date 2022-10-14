
def Swap( a, b ):
    c = a
    a = b
    b = c
    return a, b




if __name__=='__main__':
    x, y = Swap( 3., 5 )
    print( x, y )
    
