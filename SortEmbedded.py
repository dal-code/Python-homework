def CompareItems( item ):
    c = []
    index = []
    for i in range(0, len(item)):
        if isinstance(item[i], list):
            item[i].sort()
            c.append(item[i][0])
            index.append(i)
        else:
            c.append(item[i])
    c.sort()
    return item, c, index



def SortEmbedded( l ):
    l, a, index= CompareItems( l )
    r = []
    for i in range(0, len(l)):
        if isinstance(l[i], list):
            if l[i][0] == a[index[0]]:
                r.append(l[i])
        else:
            r.append(l[i])
    for i in range(0, len(l)):
        if isinstance(l[i], list):
            if l[i][0] == a[index[1]]:
                r.append(l[i])

    return r



if __name__=='__main__':
    r = SortEmbedded( [1, [13, 12], [6,5,7,8,9]] )
    print( r )
    # assert r == [1, [5,6,7,8,9], [12, 13]]

