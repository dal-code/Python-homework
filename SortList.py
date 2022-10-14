def SortList( lst, order ):
    if order == 'asc':
        c = sorted(lst)
    if order == 'desc':
        c = sorted(lst, reverse = True)
    if order == 'none':
        c = lst
    return c
   


if __name__=='__main__':
    lst = [ 1, 3, 2, 5, 4]
    l = SortList( lst, 'asc' )
    print( l )
    l = SortList( lst, 'desc' )
    print( l )
    l = SortList( lst, 'none' )
    print( l )
    
        
