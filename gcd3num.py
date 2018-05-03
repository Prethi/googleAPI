def func1(x,y):
    while x>0:

        if x<y:
            x,y = y,x  #Keeping x greater always
        x = x-y

    print 'gcd = ', y
    return y

    #print xx/y
    #print yy/y

def main():
    xx = x=input('enter x ')
    yy = y=input('enter y ')
    yy = z=input('enter z ')

    gcd = func1(x,y)
    final_gcd = func1(gcd, z)

    print 'gcd = ', final_gcd


if __name__ == '__main__':
    main()
