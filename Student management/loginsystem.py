def login():
    
    loginFile = open('user_pass.txt','r')
    trylimit = 2
    for i in range(trylimit):
        
        username = input("Enter the Username: ") #getting username/password
        password = input("Enter the Password: ")

        for line in loginFile:
            role,name,code = line.strip().split(',')
            #print(role,name,code)   #debug
            if username == name and password == code:
                print([username,role])
                return [username,role]
        else:
            clear()
            print("Wrong Userename/Password, Try again!")
    else:
        print("Number of tries exceded, The program is closed")
                        
def clear():
    for i in range(25):
        print('\n')
    
