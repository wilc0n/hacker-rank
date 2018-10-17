''' Testing. '''
def main():
    ''' Main function. '''
    num_ints = int(input())
    tuple1 = tuple([int(x) for x in input().split()])
    print(hash(tuple1))

if __name__ == "__main__":
    main()
