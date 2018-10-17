''' Testing. '''
import numpy

def main():
    ''' Main function. '''
    poly = [float(x) for x in input().split()]
    x = float(input())
    print(poly)
    print(x)
    print(numpy.polyval(poly, x))

if __name__ == "__main__":
    main()
