isbns={}

class User(object):
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.books={}
    def get_email(self):
        return self.email
    def change_email(self, address):
        self.email=address
        print("Your email is now updated.")
    def __repr__(self):
        print("User {}, email: {}, books read: {}".format(self.name,self.email,len(self.books)))
    def __eq__(self, other_user):
        if self.name==other_user.name:
            if self.email==other_user.email:
                self=other_user

    def read_book(self,book,rating=None):
        self.books[book]=rating
    def get_average_rating(self):
        sum=0
        n=0
        for i in self.books.values():
            if i!= None:
                sum+=i
                n+=1
        return sum/n

class Book(object):
    def __init__(self,title,isbn):
        self.title=title
        self.isbn=isbn
        self.ratings=[]
        isbns[title]=isbn
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def set_isbn(self,new_isbn):
        self.isbn=new_isbn
        isbns[self.title]=new_isbn
        print("This book's ISBN has been updated.")
    def add_rating(self,rating):
        if rating<=4 and rating>=0:
            self.ratings.append(rating) 
        else:
            print("Invalid Rating.")
    def __eq__(self, other_book):
        if self.title==other_book.title:
            if self.isbn==other_book.isbn:
                self=other_book
    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_average_rating(self):
        sum=0
        n=0
        for i in self.ratings:
            sum+=i
            n+=1
        return sum/n

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author=author
    def get_author(self):
        return self.author
    def __repr__(self):
        return "{} by {}.".format(self.title,self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject=subject
        self.level=level
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
        return "{}, a {} manual on {}.".format(self.title,self.level,self.subject)

class TomeRater():
    def __init__(self):
        self.users={}
        self.books={}
    def create_book(self,title,isbn):
        for i in isbns:
            if isbns[i] == isbn:
                if i==title:
                    print("This book already exists, please try again.")
                else:
                    print("This ISBN already exists, please try again.")
                return None
        return Book(title,isbn)
    def create_novel(self,title,author,isbn):
        for i in isbns:
            if isbns[i] == isbn:
                if i==title:
                    print("This novel already exists, please try again.")
                else:
                    print("This ISBN already exists, please try again.")
                return None
        return Fiction(title,author,isbn)
    def create_non_fiction(self,title,subject,level,isbn):
        for i in isbns:
            if isbns[i] == isbn:
                if i==title:
                    print("This non-fiction already exists, please try again.")
                else:
                    print("This ISBN already exists, please try again.")
                return None
        return Non_Fiction(title,subject,level,isbn)
    def add_book_to_user(self,book,email,rating=None):
        if email not in self.users.keys():
            return "No user with email {}!".format(email)
        else:
            self.users[email].read_book(book,rating)
            if rating!=None: 
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book]+=1
            else:
                self.books[book]=1
    def add_user(self,name,email,user_books=None):
        if email not in self.users.keys():
            if ".com" not in email and ".edu" not in email and ".org" not in email:
                print("Invalid email address!")
                return None
            if "@" not in email:
                print("Invalid email address!")
                return None
            self.users[email]=User(name,email)
            if user_books!=None:
                for i in user_books:
                    self.add_book_to_user(i,email)
        else:
            print("User with email {} already exists. Please use another email.".format(email))
    def print_catalog(self):
        for i in self.books.keys():
           print(i.title)
    def print_users(self):
        for i in self.users.keys():
            print(i)
    def most_read_book(self):
        max=0
        book=""
        books=[]
        for i in self.books.keys():
            if self.books[i]>max:
                max=self.books[i]
                book=i.title
        books.append(book)
        for i in self.books.keys():
            if self.books[i]==max and i.title not in books:
                books.append(i.title)
        return ",".join(books)
    def highest_rated_book(self):
        max=0
        book=""
        books=[]
        for i in self.books.keys():
            if i.get_average_rating()>max:
                max=i.get_average_rating()
                book=i.title
        books.append(book)
        for i in self.books.keys():
            if i.get_average_rating()==max and i.title not in books:
                books.append(i.title)
        return ",".join(books)
    def most_positive_user(self):
        max=0
        user=""
        users=[]
        for i in self.users.values():
            if i.get_average_rating()>max:
                max=i.get_average_rating()
                user=i.name
        users.append(user)
        for i in self.users.values():
            if i.get_average_rating()==max and i.name not in users:
                users.append(i)
        return ",".join(users)
    def __repr__(self):
        return "This is a place to read and rate books."