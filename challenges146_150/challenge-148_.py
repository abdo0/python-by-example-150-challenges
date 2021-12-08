import csv

def get_data():
    file=list(csv.reader(open("passwords.csv")))
    tmp=[]
    for x in file:
        tmp.append(x)
    return tmp

def create_userID(tmp):
    name_again=True
    while name_again==True:
        userID=input("Enter a new user ID: ")
        userID.lower()
        inlist=False
        row=0
        for y in tmp:
            if userID in tmp[row][0]:
                print(userID, "has already been allocated")
                inlist=True
            row=row+1
        if inlist==False:
            name_again=False
    return userID

def create_password():
    sclist=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?"]
    nclist=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    tryagain=True
    while tryagain==True:
        score=0
        uc=False
        lc=False
        sc=False
        nc=False
        password=input("Enter Password: ")
        password2=input("Enter password again: ")
        length=len(password)
        if length>=8:
            score=score+1
        for x in password:
            if x.islower():
                lc=True
            if x.isupper():
                uc=True
            if x in sclist:
                sc=True
            if x in nclist:
                ns=True

        if sc==True:
            score=score+1
        if lc==True:
            score=score+1
        if uc==True:
            score=score+1
        if nc==True:
            score=score+1

        if score==1 or score==2:
            print("This is a weak password. Try again.")

        if score==3 or score==4:
            print("This password could be improved. ")
            again=input("Do you want to try for a stronger password? (y/n) ")
            again.lower()
            if again=="n":
                tryagain=False

        if password != password2:
            print("Password do not match. File not saved")
            main()
        else:
            return password

def find_userID(tmp):
    ask_name_again=True 
    userID=""
    while ask_name_again == True:
        searchID=input("Enter the user ID you are looking for ")
        searchID.lower()
        inlist=False
        row=0
        for y in tmp:
            if searchID in tmp[row][0]:
                inlist=True
            row=row+1
        if inlist==True:
            userID=searchID
            ask_name_again=False
        else:
            print(searchID, "is NOT in the list")
    return userID

def change_password(userID,tmp):
    if userID!="":
        password=create_password()
        ID=userID.index(userID)
        tmp(ID)[1]=password
        file=open("passwords.csv", "w")
        x=0
        for row in tmp:
            newrecord=tmp[x][0] + "," +tmp[x][1] + "\n"
            file.write(newrecord)
            x=x+1
        file.close()

def display_all_userID():
    tmp=get_data()
    x=0
    for row in tmp:
        print(tmp[x][0])
        x=x+1

def main():
    tmp=get_data()
    go_again=True
    while go_again==True:
        print()
        print("1) Create a new User ID")
        print("2) Change a password")
        print("3) Display all User IDs")
        print("4) Quit")
        print()

        selection=int(input("Enter Selection: "))
        if selection==1:
            userID=create_userID(tmp)
            password=create_password()
            file=open("Passwords.csv","a")
            newrecord=userID+","+password+"\n"
            file.write(str(newrecord))
            file.close()
        elif selection==2:
            userID=find_userID(tmp)
            change_password(userID,tmp)
        elif selection==3:
            display_all_userID()
        elif selection==4:
            go_again=False
        else:
            print("Incorrect selection")

main()