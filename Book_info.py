import Student

class Book:
    id = None
    Name = None
    author = None
    publication = None
    count = None

    def getinfo(self):
        self.id = input("Enter Book Id :- ")
        self.Name = input("Enter Book name :- ")
        self.author = input("Enter Book Author :- ")
        self.publication = input("Enter Book Publication :- ")


def add_book():
    b1 = Book()
    b1.getinfo()
    file1 = open("book_information.txt","a")
    file1.write(b1.id+","+b1.Name+","+b1.author+","+b1.publication+","+"\n")
    file1.close()
    print("Book is Add..")

def retrun_book():
    b2 = Book()
    s1 = Student.Student_info()
    b2.id = input("enter retrun book id :- ")
    b2.name = input("enter retrun book name :- ")
    s1.roll_no = input("enter student roll no :- ")
    s1.name = input("enter student name :- ")
    file2 = open("Book_History.txt","a")
    file2.write(b2.id+","+b2.Name+","+s1.roll_no+","+s1.name+"\n")
    file2.close()

def issue_book():
    std = Student.search_student()
    book = search_book()
    date = input("enter date in format (DD:MM:YYYY)")
    file2 = open("Book_History.txt", "a")
    file2.write(std+","+book+","+ date +"\n")
    file2.close()
    print("book issue....")


def search_book():
    id = str(input("enter book id :- "))
    file1 = open("book_information.txt","r")
    data = file1.readlines()
    file1.close()
    for row in data:
        for av in row.split(","):
            if av == id:
                return row


def book_history():
    file1 = open("book_history.txt","r")
    data = file1.read()
    file1.close()
    print(data)







