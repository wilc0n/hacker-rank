''' Testing. '''
def main():
    ''' Main function '''
    students_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        row = [name, score]
        students_scores.append(row)
    students_scores.sort(key=lambda x: float(x[1]))
    lowest_score = students_scores[0][1]
    num = 0
    while students_scores[num][1] == lowest_score:
        num += 1
    second_low_score = students_scores[num][1]
    results = [item[0] for item in students_scores if item[1] == second_low_score]
    results.sort()
    for name in results:
        print(name)

if __name__ == "__main__":
    main()
