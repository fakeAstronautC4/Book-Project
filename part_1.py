# Let's assign variables to represent a book you enjoy.

# Step 2 - Strings
# Let's start with Python strings. Replace the "None" with the name of a book, and below the name of the author of your book.

book_name = '1984'
author = 'George Orwell'
# book_name = "Dune"
# author = "Frank Herbert"


# Step 3 - Concatenation and f-strings
# Use concatenation and f-strings to make a sentence about your author and book name.

sentence1 = book_name + ' was written by ' + author + '.'
# sentence1 = book_name + " is written by " + author + "."
sentence2 = f"{book_name} has been increasing its popularity in the last few years. A true masterpiece by {author}"
# sentence2 = f"Author, {author}, wrote the book {book_name}."


# Step 4 - Integers
# Now let's practice Integers. Replace the "None" below with the publication date of your book.
publication_year = 1949
# publication_year = 1965


# Step 5 - Floats
# Now estimate what the retail value of your book would be at a store and replace the "None" below with a float value of the price. (Doesn't have to be accurate.)
book_price = 29.99
# book_price = 17.99


# Step 6 - Booleans
# Now we will practice with booleans. Replace the "is_awesome" variable with a boolean. True if your book is awesome, False if your book is not awesome.
is_awesome = True
# is_awesome = True


# Step 7 - print and type functions
# Follow the instructions, and below this line, code all of the suggested print statements and the type statements.
# Code below
print(book_name, 'by ' + author)
print(sentence1, f'\n{sentence2}')
print(f"Published in {publication_year} \nCurrent price: {book_price}\nIs it good? {is_awesome}")

print('================== Types ===============')
print(type(book_price))

