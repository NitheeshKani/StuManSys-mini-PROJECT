from tabulate import tabulate

def teaclogin(name):
    print("welcome!,",name)
    menu()
    
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

def search(filterno):
    val = input("Enter a value ")
    record = makerecord()
    disprecord = []
    disprecord.append(record[0])
    for i in range(1, len(record)):
        student = record[i]
        if student[filterno] == val:
            disprecord.append(student) 
    display(disprecord) 

def addStudentDetail():
    studentrecord = open('studentrecord.txt','a')
    grades = open('grades.txt','a')
    Name = input("Enter the name:")
    Regno = input("Enter the Regno:")
    Dept = input("Enter the Dept:")
    DOB = input("Enter the DOB:")
    Contact = input("Enter the Contact:")
    val = (f'\n{Name},{Regno},{Dept},{DOB},{Contact}')
    value = (f'\n{Name},{Regno},no data')
    studentrecord.write(val)
    grades.write(value)
    grades.close()
    studentrecord.close()

def searchfilter():
    clear()
    print('1) Search by Name')
    print('2) Search by Regno')
    print('3) Search by Dept')
    print('4) back')
    
    option = int(input("Enter your option "))
    if option == 1:
        search(0)
    elif option == 2:
        search(1)
    elif option == 3:
        search(2)
    elif option == 4:
        clear()
        return
    else:
        clear()
        print("Invalid Option")

def grading():
    
    grades = makegrade()
    modgrade =[]
    ['Name','Regno','Grade']
    for i in range(1, len(grades)):
        student = grades[i]
        if student[2] == 'no data':
            student[2] = input(f"Enter a grade for {student[0]} , {student[1]} ")
            modgrade.append(student)
        else:
            modgrade.append(student)
            
    gradesfile = open('grades.txt','w')
    gradesfile.writelines(','.join(['Name','Regno','Grade']))
    
    gradesfile = open('grades.txt','a')
    for items in modgrade:
        gradesfile.write('\n')
        gradesfile.writelines(','.join(items))
    gradesfile.close()

    
    display(makegrade())
            
       

def menu():
    isMenuRuning =True
    
    while isMenuRuning:
        
        print('1) Add Student Detail in the record')
        print('2) view Student Detail in the record')
        print('3) Search Student Detail in the record')
        print('4) Enter grade for students')
        print('0) Log out')
        
        option = int(input("Enter your option "))
        if option == 1:
            addStudentDetail()
            clear()
        elif option == 2:
            display()
        elif option == 3:
            searchfilter()
        elif option == 4:
            grading()
        elif option == 5:
            display()
        
        elif option == 0:
            isMenuRuning = False
            print("You have Logged out Successfully")
        else:
            clear()
            print("Invalid Option")
        
def clear():
    for i in range(25):
        print('\n')               

