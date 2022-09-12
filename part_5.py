### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here



def new_book():
    title = input("Title: ")
    author = input("Author: ")
    try:
        year = int(input("Published year: "))
    except:
        year = int(input('Please type an actual number: '))
    try:
        rating = float(input("Rating: "))
    except:
        rating = float(input("Please type a number: "))
    try:
        pages = int(input("Length: "))
    except:
        pages = int(input("Please type a valid number: "))

    f = open("book.txt", "a")
    f.write('{}, {}, {}, {}, {}\n'.format(title, author, year, rating, pages))
#new_book()

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def bookie():
    with open('book.txt', "r") as file:
        items = file.readlines()
        
        for line in items:
            title, author, year, rating, pages = line.split(", ")
            
            book_dictionary = {
                "title": title,
                "author": author,
                "year": year,
                "rating": rating,
                "pages": pages.strip()
            } 
            
            print('======={}======'.format(title))
            for stuff in book_dictionary:
                val = book_dictionary[stuff]
                print(stuff,val) 

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!
def authors_books(stringvar):
    with open('book.txt', "r") as file:
        items = file.readlines()
        for line in items:
            title, author, year, rating, pages = line.split(", ")
            if author == stringvar:
                print(title)
            


def main_menu():
    choice = 0
    while choice == 0:
        choice = input("What would you like to do?\nAdd a new book -- 1\nShow all books -- 2\nLook up an author's books -- 3\nClose the program -- 4\n--> ")
        if (choice == '1'):
            new_book()
            choice = 0
        elif (choice == '2'):
            bookie()
            choice = 0
        elif (choice == '3'):
            auth = input("What author are you looking for? ")
            authors_books(str(auth))
            choice = 0
        elif (choice == '4'):
            break
        else:
            continue



if __name__ == "__main__":
    main_menu()
else:
    #try running import.py to make sure its working... but it is :)
    print('This file has no access to this module')