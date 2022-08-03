import random
import collections
class Books:
    def __init__(self, title, author, year, publisher, availableCopies, publicationDate):
        self.ID = random.randint(0,999)
        self.title = title
        self.author = author
        self.year =  year
        self.publisher = publisher
        self.availableCopies = availableCopies
        self.publicationDate = publicationDate
    def getID(self):
        return self.ID
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getYear(self):
        return self.year
    def getPublisher(self):
        return self.publisher
    def getAvailableCopies(self):
        return self.availableCopies
    def getPubblicationDate(self):
        return self.publicationDate
    def setTitle(self, title):
        self.title = title
    def setAuthor(self, author):
        self.author = author
    def setYear(self, year):
        self.year =  year
    def setPublisher(self, publisher):
        self.publisher = publisher
    def setAvailableCopies(self, availableCopies):
        self.availableCopies = availableCopies
    def setPublicationDate(self, publicationDate):
        self.publicationDate = publicationDate
    
class BookList:
    def __init__(self):
        self.books = []
    def addBook(self, book):
        if isinstance(book, Books):
            self.books.append(book)
        else:
            raise Exception("Provided object is not an instance of books")
    def searchBook(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    def removeBook(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break
    def numOfBooks(self):
        return len(self.books)
class Users:
    def __init__(self, username, firstname, surname, houseNumber, street, postcode, email, dob):
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.houseNumber = houseNumber
        self.street = street
        self.postcode = postcode
        self.email = email
        self.dob = dob
    def getUsername(self):
        return self.username
    def getFirstname(self):
        return self.firstname
    def getSurname(self):
        return self.surname
    def getHouseNumber(self):
        return self.houseNumber
    def getStreet(self):
        return self.street
    def getPostcode(self):
        return self.postcode
    def getEmail(self):
        return self.email
    def getDOB(self):
        return self.dob
    def setUsername(self, username):
        self.username = username
    def setFirstname(self, firstname):
        self.firstname = firstname
    def setSurname(self, surname):
        self.surname = surname
    def setHouseNumber(self, houseNumber):
        self.houseNumber = houseNumber
    def setStreet(self, street):
        self.street = street
    def setPostcode(self, postcode):
        self.postcode = postcode
    def setEmail(self, email):
        self.email = email
    def setDOB(self, dob):
        self.dob = dob
class UserList:
    def __init__(self):
        self.users = []
    def addUser(self, user):
        if isinstance(user, Users):
            self.users.append(user)
        else:
            raise Exception("Provided object is not an instance of users")
    def searchUser(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
    def removeUser(self, firstname):
        for user in self.users:
            if user.firstname == firstname:
                self.users.remove(user)
                break
    def numOfUsers(self):
        return len(self.users)
class Loans:
    def __init__(self):
        self.loans = collections.defaultdict(list)
    def borrowBook(self, username, book):
        if book.getAvailableCopies() > 0:
            book.setAvailableCopies(book.getAvailableCopies() - 1)
            self.loans[username].append(book)
        else:
            raise Exception("Book not available")
    def returnBook(self, username, title):
        for book in self.loans[username]:
            if book.title == title:
                book.setAvailableCopies(book.getAvailableCopies() + 1)
                self.loans[username].remove(book)
                return book
        return None
    def returnAllBooks(self, username):
        numOfBooks = len(self.loans[username])
        for book in self.loans[username]:
            book.setAvailableCopies(book.getAvailableCopies() + 1)
            self.loans[username].remove(book)
        return numOfBooks
    def printOverDueBooks(self, userList):
        print("Overdue Books:")
        print("Username\tFirstName\tTitle")
        for key in self.loans:
            user = userList.searchUser(key)
            for book in self.loans[key]:
                print(user.getUsername()+"\t\t"+user.getFirstname()+"\t\t"+book.getTitle())

bookList = BookList()
userList = UserList()
loans = Loans()
menu_options = {
    1: 'Add a Book',
    2: 'Add a User',
    3: 'Remove a Book',
    4: 'Remove a User',
    5: 'Borrow a Book',
    6: 'Return a Book',
    7: 'Print all overdue Books',
    0: 'Exit'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    year = int(input("Enter Book Year: "))
    publisher = input("Enter Book Pubblisher: ")
    availableCopies = int(input("Enter number of available copies of Book: "))
    publicationDate = input("Enter Book Publication Date: ")
    b =  Books(title, author, year, publisher, availableCopies, publicationDate)
    bookList.addBook(b)


def option2():
    username = input("Enter Username: ")
    firstname = input("Enter Firstname: ")
    surname = input("Enter Surname: ")
    houseNumber = input("Enter House Number: ")
    street = input("Enter Street: ")
    postcode = input("Enter Postcode: ")
    email = input("Enter Email: ")
    dob = input("Enter Date of Birth: ")
    u = Users(username, firstname, surname, houseNumber, street, postcode, email, dob)
    userList.addUser(u)

def option3():
    title = input("Enter Book Title: ")
    bookList.removeBook(title)

def option4():
    firstname = input("Enter Firstname: ")
    userList.removeUser(firstname)

def option5():
    username = input("Enter Username: ")
    title = input("Enter Book Title: ")
    b = bookList.searchBook(title)
    loans.borrowBook(username, b)

def option6():
    username = input("Enter Username: ")
    title = input("Enter Book Title: ")
    loans.returnBook(username, title)

def option7():
    loans.printOverDueBooks(userList)

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 7:
            option7()
        elif option == 0:
            print('Thank you')
            exit()
        else:
            print('Invalid option. Please enter a number between 0 and 7.')