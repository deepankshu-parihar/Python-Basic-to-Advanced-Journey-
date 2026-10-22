students={}
while True:
    print("1.Enter data into Database")
    print("2.View all data in database")
    print("3.Search data in Database")
    print("4.Update data in Database")
    print("5.Delete data in Database")
    print("6.Exit Database.")

    choice=int(input("Enter your choice:"))

    if(choice==1):
        rollno=int(input("Enter Rollno:"))
        if rollno in students:
            print("Student already exist.")
        else:
            name=input("Enter name of the student:")
            clss=input("Enter class of the student:")
            marks=int(input("Enter marks of the student:"))

            students[rollno]={
            "Name":name,
            "Class":clss,
            "Marks":marks
            }

            print("Student Data added sucessfully..")

    elif(choice==2):
        if not students:
            print("Database Empty!")
        else:
            for rollno,data in students.items():
                print("\nRollno:",rollno)
            for key,value in data.items():
                print(key,":",value)

    elif(choice==3):
        rollno==input("Enter rollno. to search:")
        if rollno in students:
            print("Student found!")
            print("Rollno:",rollno)
            for key,value in students[rollno].items():
                print(key,":",value)
        else:
            print("Student not found!")


    elif(choice==4):
        rollno=("Enter rollno to update:")
        if rollno in students:
            print("1.Update Name")
            print("1.Update Class")
            print("1.Update Marks")

        option=int(input("Choose the option given!:"))
        if(choice==1):
            students[rollno]["Name"]=input("Enter new Name:")
        elif(choice==2):
            students[rollno]["Class"]=input("Enter new Class:")
        elif(choice==3):
            students[rollno]["Rollno"]=input("Enter new Rollno:")
        else:
            print("Invalid OPtion!")

            print("Student data Updated")

    elif(choice==5):
        rollno=int(input("Enter rollno to delte:"))
        if rollno in students:
            del students[rollno]
            print("Student deleted sucessfully!")
        else:
            print("Student does not found")

    elif(choice==6):
        print("Exiting database,Goodybye.....")
        break

    else:
        print("Invalid choice!Try again among the given choices......")

