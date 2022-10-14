def StringToNumber(s):
    if '.' in s:
        return float(s)
    else:
        return int(s)





if __name__=='__main__':
    x = StringToNumber( '12345.123' )
    print( x )
