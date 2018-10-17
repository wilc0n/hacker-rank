''' Testing. '''
def main():
    ''' Main function. '''
    list1 = []
    num_commands = int(input())
    commands = []
    for _ in range(num_commands):
        commands.append(input().split())
    for command in commands:
        if command[0] == 'insert':
            list1.insert(int(command[1]), int(command[2]))
        if command[0] == 'print':
            print(list1)
        if command[0] == 'remove':
            list1.remove(int(command[1]))
        if command[0] == 'append':
            list1.append(int(command[1]))
        if command[0] == 'sort':
            list1.sort()
        if command[0] == 'pop':
            list1.pop(len(list1) - 1)
        if command[0] == 'reverse':
            list1.reverse()

if __name__ == "__main__":
    main()
