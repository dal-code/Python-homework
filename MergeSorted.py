def MergeSorted( l1, l2 ):
    l1.extend(l2)
    list.sort(l1)
    return l1
    





if __name__=='__main__':
    l1 = [ 1, 22, 333, 4444, 55555]
     
    l2 = [ 3, 44, 111, 222, 666]

    l = MergeSorted( l1, l2 )
    print( l )
