
my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def bookie(strng):
    for (key, value) in strng.items():
        print (key, value)
    # print('Title: ' + strng['title'])
    # print('Author: ' + strng['author'])
    # print('Published: ' + str(strng['year']))
    # print('Rating: ' + str(strng['rating']))
    # print('Length: ' + str(strng['pages']))
bookie(my_book)

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.
 
# Code below

def titl(dictionar):
    print(dictionar['title'])
def auth(dictiona):
    print(dictiona['author'])
def year(diction):
    print(diction['year'])

# auth(my_book)
# titl(my_book)
# year(my_book)


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

#re-assigning value
def change_author(book, string):
    print(book['author'])
    book['author'] = f'{string}'
    print(book['author'])

change_author(my_book, 'Arthur Pendragon')

#adding new info
def add_key(book, string, sold_c):
    print(book)
    book[string] = sold_c
    print(book)

add_key(my_book, 'sold copies', 4000000)

#removing info
def remove_key(book, string):
    print(book)
    del book[string]
    print(book)

remove_key(my_book, 'sold copies')

