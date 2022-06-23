from Books import Books
from Users import Users
class LMS(Books , Users):
    def __init__(self, books_list , users_list , library_name):
        self.books_list = books_list
        self.users_list = users_list
        self.library_name = library_name
        bookID = 1
        userID = 1
        self.books_dict = {}
        self.users_dict = {}
        

#----------------------------------------------------------------------------------
# Books dictionary

        with open(books_list) as bl:
            book_info = bl.readlines()

        for line in book_info:
            title, status , author , quantity , rackNo , price = line.strip().split(",")
            self.books_dict.update(
                {
                    str(bookID):{
                        "book title":title,
                        "Lender name":"",
                        "Lend Date":"",
                        "Status":status,
                        "Author":author,
                        "Quentity":quantity,
                        "RackNo":rackNo,
                        "Price":price
                    }
                }
            )
            bookID += 1

#----------------------------------------------------------------------------------
# Users dictionary

        with open(users_list) as ul:
            user_info = ul.readlines()

        for line in user_info:
            userID, name , address , password = line.strip().split(",")
            self.users_dict.update(
                {
                    str(userID):{
                        "ID":userID,
                        "Name":name,
                        "Password":password,
                        "Address":address,
                    }
                }
            )
            userID = int(userID) +1

#----------------------------------------------------------------------------------
