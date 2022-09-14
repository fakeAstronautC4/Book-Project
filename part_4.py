### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
from turtle import title


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
    

    book_dictionary = {
        'title': title,
        'author': author,
        'year': year,
        'rating': rating,
        'pages': pages
    }
    fav_books.append(book_dictionary)
    return(book_dictionary)
# new_book()
    


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# CODED ON PREV STEP

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

fav_books = [
    {
    'title':'The return of the King',
    'author': 'J.R.R. Tolkien',
    'year': 1955,
    'ratings': 4.92,
    'pages': 416
    },
    {
    'title': '1984',
    'author': 'George Orwell',
    'year': 1949,
    'ratings': 4.99,
    'pages': 328
    },
    {
    'title': 'The Secret',
    'author': 'Rhonda Byrne',
    'year': 2006,
    'ratings': 4.55,
    'pages': 198
    }, 
    {
    'title': 'Dune',
    'author': 'Frank Herbert',
    'year': 1965,
    'ratings': 4.98,
    'pages': 412
    },
    {
    'title': 'Harry Potter',
    'author': 'J.K. Rowling',
    'year': 1997,
    'ratings': 4.79,
    'pages': 223
    }
]
        
# Code here
def bookie(strng):
    for item in strng:
        print(f"Title: {item['title']}")
        # for (key, value) in item.items():
        #     print (key, value)
bookie(fav_books)


def main_menu():
    choice = 0
    while choice == 0:
        choice = input('What would you like to do?\nAdd a new book -- 1\nShow all books -- 2\nClose the program -- 3\n: ')
        if (choice == '1'):
            new_book()
            choice = 0
        elif (choice == '2'):
            bookie(fav_books)
            choice = 0
        elif (choice == '3'):
            break
        else:
            continue
# main_menu()


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
# CODED ON PREV STEP