from library import *
from student import *
from book import *

library = Library("City Library")

library.addBook(Book(1,"Clean Code","Robert Martin",464 ))
library.addBook(Book(2,"Python Crash Course","Eric Matthes",560))
library.addBook(Book(3,"Atomic Habits","James Clear",320))

library.addStudent(Student(1,"Taleh"))
library.addStudent(Student(2,"Ramiz"))
library.addStudent(Student(3,"Ramal"))

while True:
    print("""
    1.Show books
    2.Show students
    3.Search book
    4.Search student
    5.Borrow book
    6.Return book

    0.Exit
""")

    choice = input("Choice:")

    if choice == "1":
        library.showBooks()
    elif choice == "2":
        library.showStudents()
    elif choice == "3":
        bookID = int(input("Enter ID:"))
        library.searchBooks(bookID)
    elif choice == "4":
        studentID = int(input("Student ID:"))
    elif choice == "5":
        studentID = int(input("Student ID:"))
        bookID = int(input("Book ID:"))
        library.borrowBook(studentID,bookID)
    elif choice == "6":
        studentID = int(input("Enter ID:"))
        bookID = int(input("Book ID:"))
        library.returnBook(studentID,bookID)

    elif choice == "0":
        print("Goodbye")
        break
    else:
        print("Invalid choice.")    

