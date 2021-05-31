import quizfile
import pyfile
import submission
import tkinter as tk
import tkinter.filedialog as fd

index = 0
print("Submission")
sub1 = submission.Submission()
print("학생의 이름을 입력하시오: ")
name = input()
sub1.student_name(name)
print("학생 ID를 입력하시오: ")
snum = input()
sub1.student_ID(snum)
sub1.anum = "%04d" %index
index = index + 1

while True:  
    print("[1: 알고리즘 과제 제출] [2: 퀴즈 과제 제출] [3: 제출 결과 확인] [0: 프로그램 종료]")
    work = int(input())
    if work == 1:
        title = pyfile.py_sel()
        sub1.title(title)
        print("Name: " + sub1.s_name, "ID: " + sub1.snum, "Submission ID: "+ sub1.anum, "Title: " + sub1.s_title)
    elif work == 2:
        filename = quizfile.txt_qize(5)
        sub1.file_name(filename)
        print("Name: " + sub1.s_name, "ID: " + sub1.snum, "Submission ID: "+ sub1.anum, "Title: " + sub1.filename)
    elif work == 3:
        print("제출 결과 확인")
    elif work == 0:
        print("End")
        break
