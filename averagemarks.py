if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    student_Average=0.0
    for i_ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        sum=0.0
        for i in scores:
            sum+=i
        student_Average=sum/3.0 
    query_name = input()
    marks=student_marks[query_name]
    for i in marks:
        student_Average+=i
    print(student_Average/3)