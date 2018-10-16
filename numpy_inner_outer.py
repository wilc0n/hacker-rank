''' Testing. '''
import numpy

def main():
    ''' Main function. '''
    first_array = [int(x) for x in input().split()]
    second_array = [int(x) for x in input().split()]
    print(first_array)
    print(second_array)
    print(numpy.inner(first_array, second_array))
    print(numpy.outer(first_array, second_array))

if __name__ == "__main__":
    main()
