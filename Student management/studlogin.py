from random import choice
from tabulate import tabulate

def clear():
    for i in range(25):
        print('\n')

def stulogin(name):
    print("welcome!,",name)
    menu(name)
    
def makerecord():
    Record = []
    Studentrecord = open('studentrecord.txt','r')
    for line in Studentrecord:
        Name,Regno,Dept,DOB,Contact = line.strip().split(',')
        Record.append([Name,Regno,Dept,DOB,Contact])
    Studentrecord.close()
    return Record

def makegrade():
    grade = []
    grades = open('grades.txt','r')
    for line in grades:
        Name,Regno,Grade = line.strip().split(',')
        grade.append([Name,Regno,Grade])
    grades.close()
    return grade
    

def display(Record = makerecord()):
    clear()
    table = tabulate(Record,headers='firstrow',tablefmt = 'fancy_grid')
    print(table)

def search(val,filterno = 0):
    record = makerecord()
    disprecord = []
    disprecord.append(record[0])
    for i in range(1, len(record)):
        student = record[i]
        if student[filterno] == val:
            disprecord.append(student) 
    display(disprecord)
    
def fortunes():
    forfile = open('fortunes.txt','r')
    fortune = forfile.readlines()
    print(choice(fortune))
    
def menu(name):
    isMenuRuning =True
    
    while isMenuRuning:
        
        print('1) View Your fortune')
        print('2) view Student Detail in the record')
        print('3) View Your record')
        print('4) view grade for students')
        print('0) Log out')
        
        option = int(input("Enter your option "))
        if option == 1:
            clear()
            fortunes()
        elif option == 2:
            display()
        elif option == 3:
            search(name)
        elif option == 4:
            display(makegrade())

        elif option == 0:
            isMenuRuning = False
            print("You have Logged out Successfully")
        else:
            clear()
            print("Invalid Option")