#add_book(library, title, author, isbn) - takes a dictionary (library), a title (string), an author (string), and an ISBN (string) as
# input, and adds a new book to the library as a dictionary with the keys
# 'title', 'author', 'isbn', and 'available'. The 'available' key should have a boolean value, initially set to True. 
#If the ISBN already exists in the library, print an appropriate message.

def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book with ISBN already exixit in the library.")
    else:
        library[isbn] = {'title':title, 'author':author, 'isbn':isbn, 'available': True}
        print("Book added to the library successfully.")

        library = {}
        add_book(library, "The Great Gatsby", "F.Scot Fizgrelad", "9780743273565")
        add_book(library, "To Kill a Mockingbird", "Haper lee", "9780061120084")
        add_book(library, "The Great Gatsby", "F.Scot Fizgrelad", "9780743273565")

        #this will print an error message


        #remove_book(library, isbn) - 
        # takes a dictionary (library) and an ISBN (string) as input, and removes the book with the given ISBN from the library. 
        # If the ISBN does not exist in the library, print an appropriate message.

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print("Book with ISBN", isbn, "removed from the library.")
    else:
        print("Book with ISBN", isbn, "does not exist in the library")

    

#check_out_book(library, isbn) - 
# takes a dictionary (library) and an ISBN (string) as input,
#  and sets the 'available' key of the book with the given ISBN to False. 
# If the ISBN does not exist in the library or the book is not available, print an appropriate message.


def check_out_book(library, isbn):
    if isbn in library:
      if library[isbn]['available']:
         library[isbn]['available']: = False
         print(f"Book With ISBN {isbn} has been checed out.")
      else:
         print(f"Book With ISBN {isbn} does not exist in the library.")
         

library = {

    '9780743273565':{'title':'The Great Gatsby','author': 'F.Scot Fizgrelad',' available': True},
    '9780061120084':{'title':'To Killa Mockingbird',' author':' Harper Lee','available': False },

}
check_out_book(library,'9780743273565')

check_out_book(library,'9780061120084')


#return_book(library, isbn) - takes a dictionary (library) and an ISBN (string) as input, 
# and sets the 'available' key of the book with the given ISBN to True. 
# If the ISBN does not exist in the library, print an appropriate message.


def return_book(library, isbn):
    if isbn in library:
        library[isbn]['available'] = True
    else:
        print ("Book with ISBN {} does not exist in the library."format(isbn))



#display_books(library) - takes a dictionary (library)
#  as input and prints all the books in the library in a formatted way.


def display_books(library:):
print ("Books in the library:")
for book, author in library.items():
    print(f"{book}by {author}")



my_library = {
    "This Great Gatsby":"F Scott Fizgerald",
    "To Kill Mockingbird":"Harper lee"
}
display_books(my_library)
