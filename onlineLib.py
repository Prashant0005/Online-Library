# <<><><><><>Online Library<><><><><><><>
print("Welcome to the MOM Library\n")
class Library:
    def __init__(self,Dictb):
        self.Dict_of_books=Dictb
        self.lendb={}

    def disb(self):
        for key , value in self.Dict_of_books.items():
            print(f"{key} - {value}")

    def lend(self,user,book):
        if book not in self.lendb.keys():
            self.lendb.update({book:user})
            self.Dict_of_books.update({book:"Unavailable"})
            print(f"{book} is lended to {user}. You can collect the book")
        else:
            print(f" {book} is already assigned to someone")

    def add(self,book):
        self.Dict_of_books.update({book:"Available"})
        print("Book has been updated to the Library")

    def ret_book(self,book):
        self.lendb.pop(book)
        self.Dict_of_books.update({book:"Available"})
        print("Book has been returned & updated to the Library")

if __name__ == '__main__':
    pras={"Mahabharat":"Available","Harry Potter":"Available","Python":"Available","Chronicles Of Narnia":"Available","Batman":"Available","Superman":"Available"}
    pras=Library(pras)
    lname="MOM"
    while True:
        print("Welcome to the",lname,"library")
        print("Choose")
        print("1. Display the books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        user_in=int(input())

        if user_in==1:
            pras.disb()
        elif user_in==2:
            book_n=input("Which book you want")
            banda=input("Enter the user name")
            pras.lend(banda,book_n)
        elif user_in==3:
            book_n=input("Enter the book name you want to add")
            pras.add(book_n)
        elif user_in==4:
            book_n=input("Enter the book name you want to return")
            pras.ret_book(book_n)
        else:
            print("Enter a valid option")
            continue

        while (True):
            print("Enter q for quit and c for continue")
            user_ch = input()
            if user_ch=="q":
                exit()
            elif user_ch=="C":
                continue
            else:
                print("Invalid Input! Try Again ")
                continue









































