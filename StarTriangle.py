# python function printing a star triangle

def OutputStarTriangle( n ):
    for i in range(1, n+1):
        a = 2 * i - 1
        for j in range(n-i):
            print(" ", end="")
        for k in range(2*i - 1):
            print("*", end="")
        print(' ')

    



if __name__=='__main__':
    OutputStarTriangle( 5 )
