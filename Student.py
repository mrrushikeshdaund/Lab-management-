
class Student_info:
    roll_no = None
    name = None
    email = None
    mob_no = None
    branch = None
    year = None
    div = None
    address = None

    def get_info(self):
        self.roll_no = input("enter student roll no:- ")
        self.name = input("enter student name:- ")
        self.email = input("enter student email:- ")
        self.mob_no = input("enter student number:- ")
        self.address = input("enter student address:- ")
        self.branch = input("enter student branch:- ")
        self.year = input("enter student year ")
        self.div = input("enter student div:- ")




def add_student():
    s1 = Student_info()
    s1.get_info()
    file1 = open("student_information.txt","a")
    file1.write(s1.roll_no+","+s1.name+","+ s1.branch+","+s1.year+","+ s1.div+","+ s1.email+","+ s1.mob_no+","+s1.address+"\n")
    file1.close()

def search_student():
    id = str(input("enter student id :- "))
    file1 = open("student_information.txt","r")
    data = file1.readlines()
    file1.close()
    for row in data:
        for atr in row.split(","):
            if atr == id:
                return row

def student_history():
    file1 = open("Book_history.txt","r")
    data = file1.read()
    file1.close()
    print(data)









