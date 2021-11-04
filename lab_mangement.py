import Student
import Book_info

print("====================== Welcome to Lab ============================")
while True:
        print(" 1 : press one to Add Student. ")
        print(" 2 : press two to Issue Book. ")
        print(" 3 : press three to Return Book. ")
        print(" 4 : press four to Check For Not Return Books. ")
        print(" 5 : press five to Add New Book. ")
        print(" 6 : press Six to Search Student Information.")
        print(" 7 : press Seven to Search Book Information.")
        print(" 8 : press eight to Book History.")
        print(" 9 : press nine to Student History.")
        print(" 0 : press zero to Return Book Reminder.")
        print(" # : press # to Exit. ")
        print("\n")
        choice = int(input("Enter Your Choice No :- "))

        if choice ==1:
            Student.add_student()

        elif choice ==2:
            Book_info.issue_book()

        elif choice ==3:
            Book_info.retrun_book()

        elif choice ==4:
            Book_info.retrun_book()

        elif choice == 5:
            Book_info.add_book()

        elif choice == 6:
            data = Student.search_student()
            print("search result :- ")
            for format in data.split(","):
                print(format, end="  ")

        elif choice == 7:
            data = Book_info.search_book()
            print("search result")
            for format in data.split(","):
                print(format,end="   ")

        elif choice == 8:
            Book_info.book_history()

        elif choice == 9:
            Student.student_history()

        elif choice == 0:
            print("book reminder..")

        else:
            print("Invalid Choice ")


