def SumOfItems( l ):
    a = 0
    for i in range(0, len(l)):
        if isinstance(l[i], str):
            if '.' in l[i]:
                l[i] = float(l[i])
            else:
                l[i] = int(l[i])
        a = a + l[i]

    return a



if __name__=='__main__':
    r = SumOfItems( [1, '234', '456', 670., '91000']  )
    print( r )
    assert r == 92361.
