''' Testing. '''
def main():
    ''' Main function. '''
    num_one = int(input())
    num_two = int(input())
    num_three = int(input())
    total_sum = int(input())
    list_comp = [[i, j, k] for i in range(num_one + 1) for j in range(num_two + 1)
                 for k in range(num_three + 1) if i + j + k != total_sum]
    print(list_comp)

    number_list = [x ** 2 for x in range(10) if x % 2 == 0]
    print(number_list)

if __name__ == "__main__":
    main()
