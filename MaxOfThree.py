def MaxOfThree( x, y, z ):
    if x > y:
        a = x
    else:
        a = y
    if a > z:
        return a
    else:
        return z

if __name__ == '__main__':
    m = MaxOfThree( 1, 5, 3 )
    print( m )
    assert m == 5 
