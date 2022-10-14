def LeftRotate( l, k ):
    for i in range(0, abs(k)):
        if k > 0:
            l.insert(0, l.pop())
        elif k < 0:
            l.insert(len(l), l.pop(0))
    return l







if __name__=='__main__':
    l = [ 1, 2, 3, 4, 5]
    r = LeftRotate( l, 1 )
    print( r )
    assert r == [5, 1, 2, 3, 4]
