''' Testing. '''
def main():
    ''' Main function. '''
    num_students = int(input())
    student_marks = {}
    for _ in range(num_students):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum_marks = 0
    for mark in student_marks[query_name]:
        sum_marks += mark
    num_marks = len(student_marks[query_name])
    avg_marks = sum_marks / num_marks
    print("%.2f" % avg_marks)

if __name__ == "__main__":
    main()
