def MatTranspose( m ):
    a = []
    b = []
    for j in range(0, len(m[0])):
        for i in range(0, len(m)):
            a.insert(i, m[i][j])
        b.insert(j, a)
        a = []
    return b
  



if __name__=='__main__':
    r = MatTranspose( [[1,2,3], [4,5,6]] )
    print( r )
    assert r == [[1,4], [2,5], [3,6]]
