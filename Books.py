
import datetime

class Books:
    
#-----(add book)--------------------------------------------------------------

    def add_book(self):
        newBook = input("Enter the name of the book: ")
        newAuthor = input("Enter the Author of the book: ")
        Quentity = input("Enter the Quentity: ")
        RackNo = input("Enter the RackNo: ")
        Price = input("Enter the Price: ")

        if (newBook == "" or newAuthor == "" or Quentity == "" or RackNo == "" or Price ==""):
            return self.add_book()

        elif (len(newBook) > 20 or len(newAuthor) >20 or int(Price) <= 0):
            print("Error❌: the book or Author name should be less than 20 char and the Price more than zero")
            return self.add_book()
        
        else:
            with open(self.books_list , "a") as b:
                b.writelines(
                    f"{newBook},Available,{newAuthor},{RackNo},{Quentity},{Price}\n"
                )
            
            self.books_dict.update(
                {
                    str(int(max(self.books_dict))+1):{
                        "book title":newBook,
                        "Lender name":"",
                        "Lend Date":"",
                        "Status":"Available",
                        "Author":newAuthor,
                        "Quentity":Quentity,
                        "RackNo":RackNo,
                        "Price":Price
                    }
                }
            )
            print(f"✅✅ {newBook} has been added successfully ✅✅")
 
#-----(delete book)--------------------------------------------------------------

    def delete_book(self):
        bookID = int(input("Enter the book ID to delete it: "))
        try:
            file = open(self.books_list , "r")
            lines = file.readlines()
            del lines[bookID - 1]
            modefiedFile = open(self.books_list , "w")
            for line in lines:
                modefiedFile.write(line)
            print("✅✅ The book deleted successfully ✅✅")
        except Exception as e:
            print(f"❌❌ The book with ID : {bookID} not found ❌❌")


#-----(show book)--------------------------------------------------------------

    def show_books(self):
        print("=================================================== List of books ===================================================")
        print(
            "{0:^1}{1:>10s}{2:>20s}{3:>20s}{4:>20s}{5:>20s}{6:>20s}".format(
                "ID" , "Title" , "Status" , "Author" , "Quentity" , "RackNo" , "Price"
            )
        )
        print("=====================================================================================================================")

        for key,value in self.books_dict.items():
            print(
                "{0:^1}{1:>12s}{2:>20s}{3:>20s}{4:>16s}{5:>20s}{6:>22s}".format(
                    key , value.get("book title") , value.get("Status") , value.get("Author") , value.get("Quentity") , value.get("RackNo") , value.get("Price")
                )
            )
        print("=====================================================================================================================")

#-----(update book)--------------------------------------------------------------

    def update_book(self):
            bookID = input("Enter Books key : ")
            if bookID in self.books_dict.keys():
                print("What do you want to update in the book? ")
                pressKeyListForUpdat = {
                    "1": "Edit name",
                    "2": "Edit Author",
                    "3": "Edit Quentity",
                    "4": "Edit RackNo",
                    "5": "Edit Price",
                    "6": "Exit",
                }
                for key, value in pressKeyListForUpdat.items():
                    print("Press", key, "To", value)
                option_key = input("Press Key : ").lower()
                
                if option_key == "1":
                    print("\nCurrent Action : EDIT NAME\n")
                    oldData = input("Enter a old name : ")
                    newData = input("Enter a new name : ")
                    with open(self.books_list, "r") as file:
                        data = file.readlines()[int(bookID) - 1]
                        data = data.replace(oldData, newData)
                    with open(self.books_list, "a") as file:
                        file.write(data)
                    file = open(self.books_list, "r")
                    lines = file.readlines()
                    del lines[int(bookID) - 1]
                    newFile = open(self.books_list, "w+")
                    for line in lines:
                        newFile.write(line)
                    self.books_dict.update(
                        {
                            str(int(bookID)): {
                                "book title": newData,
                                "Lender name": self.books_dict[bookID]["Lender name"],
                                "Lend Date": self.books_dict[bookID]["Lend Date"],
                                "Status": self.books_dict[bookID]["Status"],
                                "Author": self.books_dict[bookID]["Author"],
                                "Price": self.books_dict[bookID]["Price"],
                                "Quentity": self.books_dict[bookID]["Quentity"],
                                "RackNo": self.books_dict[bookID]["RackNo"],
                            }
                        }
                    )

                elif option_key == "2":
                    print("\nCurrent Action : EDIT Author\n")
                    oldData = input("Enter a old Author : ")
                    newData = input("Enter a new Author : ")
                    with open(self.books_list, "r") as file:
                        data = file.readlines()[int(bookID) - 1]
                        data = data.replace(oldData, newData)
                    with open(self.books_list, "a") as file:
                        file.write(data)
                    file = open(self.books_list, "r")
                    lines = file.readlines()
                    del lines[int(bookID) - 1]
                    newFile = open(self.books_list, "w+")
                    for line in lines:
                        newFile.write(line)
                    self.books_dict.update(
                        {
                            str(int(bookID)): {
                                "book title": self.books_dict[bookID]["book title"],
                                "Lender name": self.books_dict[bookID]["Lender name"],
                                "Lend Date": self.books_dict[bookID]["Lend Date"],
                                "Status": self.books_dict[bookID]["Status"],
                                "Author": newData,
                                "Price": self.books_dict[bookID]["Price"],
                                "Quentity": self.books_dict[bookID]["Quentity"],
                                "RackNo": self.books_dict[bookID]["RackNo"],
                            }
                        }
                    )
                
                elif option_key == "3":
                    print("\nCurrent Action : EDIT Quentity\n")
                    oldData = input("Enter a old Quentity : ")
                    newData = input("Enter a new Quentity : ")
                    with open(self.books_list, "r") as file:
                        data = file.readlines()[int(bookID) - 1]
                        data = data.replace(oldData, newData)
                    with open(self.books_list, "a") as file:
                        file.write(data)
                    file = open(self.books_list, "r")
                    lines = file.readlines()
                    del lines[int(bookID) - 1]
                    newFile = open(self.books_list, "w+")
                    for line in lines:
                        newFile.write(line)
                    self.books_dict.update(
                        {
                            str(int(bookID)): {
                                "book title": self.books_dict[bookID]["book title"],
                                "Lender name": self.books_dict[bookID]["Lender name"],
                                "Lend Date": self.books_dict[bookID]["Lend Date"],
                                "Status": self.books_dict[bookID]["Status"],
                                "Author": self.books_dict[bookID]["Author"],
                                "Price": self.books_dict[bookID]["Price"],
                                "Quentity": newData,
                                "RackNo": self.books_dict[bookID]["RackNo"],
                            }
                        }
                    )
                elif option_key == "4":
                    print("\nCurrent Action : EDIT RackNo\n")
                    oldData = input("Enter a old RackNo : ")
                    newData = input("Enter a new RackNo : ")
                    with open(self.books_list, "r") as file:
                        data = file.readlines()[int(bookID) - 1]
                        data = data.replace(oldData, newData)
                    with open(self.books_list, "a") as file:
                        file.write(data)
                    file = open(self.books_list, "r")
                    lines = file.readlines()
                    del lines[int(bookID) - 1]
                    newFile = open(self.books_list, "w+")
                    for line in lines:
                        newFile.write(line)
                    self.books_dict.update(
                        {
                            str(int(bookID)): {
                                "book title": self.books_dict[bookID]["book title"],
                                "Lender name": self.books_dict[bookID]["Lender name"],
                                "Lend Date": self.books_dict[bookID]["Lend Date"],
                                "Status": self.books_dict[bookID]["Status"],
                                "Author": self.books_dict[bookID]["Author"],
                                "Price": self.books_dict[bookID]["Price"],
                                "Quentity": self.books_dict[bookID]["Quentity"],
                                "RackNo": newData,
                            }
                        }
                    )
                
                elif option_key == "5":
                    print("\nCurrent Action : EDIT Price\n")
                    oldData = input("Enter a old Price : ")
                    newData = input("Enter a new Price : ")
                    with open(self.books_list, "r") as file:
                        data = file.readlines()[int(bookID) - 1]
                        data = data.replace(oldData, newData)
                    with open(self.books_list, "a") as file:
                        file.write(data)
                    file = open(self.books_list, "r")
                    lines = file.readlines()
                    del lines[int(bookID) - 1]
                    newFile = open(self.books_list, "w+")
                    for line in lines:
                        newFile.write(line)
                    self.books_dict.update(
                        {
                            str(int(bookID)): {
                                "book title": self.books_dict[bookID]["book title"],
                                "Lender name": self.books_dict[bookID]["Lender name"],
                                "Lend Date": self.books_dict[bookID]["Lend Date"],
                                "Status": self.books_dict[bookID]["Status"],
                                "Author": self.books_dict[bookID]["Author"],
                                "Price": newData,
                                "Quentity": self.books_dict[bookID]["Quentity"],
                                "RackNo": self.books_dict[bookID]["RackNo"],
                                # "lenderID": self.books_dict[bookID]["lenderID"],
                                # "lenderAddress": self.books_dict[bookID]["lenderAddress"],
                            }
                        }
                    )

                elif option_key == "6":
                    exit()

                print("✅✅ The book has been updated successfully ✅✅\n")
            else:
                print("❌The book ID is not found❌")
                return self.update_book()




#-----(issue book)--------------------------------------------------------------

    def issue_book(self):
        def test(name , password , bookID):
            with open(self.users_list) as ul:
                if name and password in ul.read():
                    self.books_dict[bookID]["Lender name"] = name
                    self.books_dict[bookID]["Lend Date"] = currentDate
                    self.books_dict[bookID]["Status"] = "Issued!"
                    print("✅✅ The Book Has Been Issued successfully ✅✅")
                else:
                    print("User Not Fount, userName or password is wrong!")    

        bookID = input("Enter the Book ID: ")
        currentDate = datetime.datetime.now().strftime("%Y-%m-%d")
        if bookID in self.books_dict.keys():
            if self.books_dict[bookID]["Status"] == "Available":
                Name = input("Enter your name: ")
                Password = input("Enter your password: ")
                test(name=Name , password=Password , bookID=bookID)

            elif not self.books_dict[bookID]["Status"] =="Available":
                print(f"❌This book alredy issued to {self.books_dict[bookID]['Lender name']} on {self.books_dict[bookID]['Lend Date']}❌")

        else:
            print("❗️ The book is not found ❗️")
            return self.issue_book()


#-----(return book)--------------------------------------------------------------
    
    def return_book(self):
        bookID = input("Enter the book ID: ")
        if bookID in self.books_dict.keys():
            if self.books_dict[bookID]["Status"] == "Available":
                print("The book is already available in the library ❗️❓")
                self.return_book()

            elif not self.books_dict[bookID]["Status"] == "Available":
                self.books_dict[bookID]["Lender name"] = ""
                self.books_dict[bookID]["Lend Date"] = ""
                self.books_dict[bookID]["Status"] = "Available"
                print("✅✅ The book has been returned successfully ✅✅")
        else:
            print("❗️The book is not found (id wrong)❗️")


#-----(show_issued_books)--------------------------------------------------------------

    def show_issued_books(self):
        print("=================================================== List of books ===================================================")
        print(
            "{0:^1}{1:>10s}{2:>20s}{3:>20s}{4:>20s}{5:>20s}{6:>20s}".format(
                "ID" , "Title" , "Status" , "Author" , "Quentity" , "RackNo" , "Price"
            )
        )
        print("=====================================================================================================================")

        for key,value in self.books_dict.items():
            if not value.get("Status") == "Available":
                print(
                    "{0:^1}{1:>12s}{2:>20s}{3:>20s}{4:>16s}{5:>20s}{6:>22s}".format(
                        key , value.get("book title") , value.get("Status") , value.get("Author") , value.get("Quentity") , value.get("RackNo") , value.get("Price")
                    )
                )

