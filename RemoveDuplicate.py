def RemoveDuplicate( l ):
    a = []
    for i in range(0, len(l)-1):
        if l[i+1] == l[i]:
            a.append(i+1)
    a.reverse()
    for i in range(0, len(a)):
        l.pop(a[i])
    return  l



if __name__=='__main__':
    l = [0, 0, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 2, 2]
    r = RemoveDuplicate( l )
    print( r )
    assert r == [0, 1, 2, 3, 4, 5, 6, 2]

