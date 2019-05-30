#christopher parks
#search

def searchEntry(book):
    search = str(input("enter a name that you desire information on: "))
    search = search.lower()
    search = search.capitalize()
    if search in  book:
        print(search,"is in book")
        print(book[search])
    else:
        print("It is not in book")

