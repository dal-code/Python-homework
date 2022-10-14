def FlattenList( l ):
    a = []
    x = len(l)
    for i in range(0, x):

        if type(l[i]) == list:
            for item in l[i]:
                a.append(item)
        else:
            a.append(l[i])
    return a



if __name__=='__main__':
    r = FlattenList( [1, [2], [3,4,5], [6,7], 8] )
    assert r == [1, 2, 3, 4, 5, 6, 7, 8]

