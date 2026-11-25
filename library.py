from student import *


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.students = []


    def addBook(self, book):
        self.books.append(book)


    def addStudent(self, student):
        self.students.append(student)


    def showBooks(self):
        if not self.books:
            print("There are no books.")
            return

        for book in self.books:
            book.showInfo()
            print("----------------------")


    def showStudents(self):
        if not self.students:
            print("There are no students.")
            return
        
        for student in self.students:
            student.showInfo()
            print("----------------------")



    # def searchBook(self, bookID):
    # def searchStudent(self, studentID):
    # def borrowBook(self, studentID, bookID):
    # def returnBook(self, studentID, bookID):

    def searchBooks(self,bookID):

        if not self.books:
            print("No books found.")
            return

        for book in self.books:
            if book.bookID == bookID:
                print("Book found")
                return

        print("No book found with this ID.")

    def searchStudent(self,studentID):

        if not self.student:
            print("There are no student")
            return

        for student in self.students:
            if student.studentID == studentID:
             print("Student found")
             return
        print("No student found with this ID.")

    def borrowBook(self,studentID,bookID):
        for student in self.students:
            if student.studentID == studentID:
                for book in self.books:
                    if book.bookID == bookID:
                         student.borrowBook(book)
                         return
                print("No book found with this ID.")
                return
        print("No student found with this ID.")

    def returnBook(self,studentID,bookID):
        for student in self.students:
            if student.studentID == studentID:
                for book in self.books:
                    if book.bookID == bookID:
                        student.returnBook(book)
                        return
                print("No book found with this ID.")
                return
        print("No student found with this ID.")

                
