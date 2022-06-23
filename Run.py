from LMS import LMS

try:
    library = LMS("data/Books.txt" , "data/Users.txt" , "Alazhar")
    print(f"=======================================📗 welcome to {library.library_name} library 📗=======================================")
    print("you are a: ")
    print("1_Admin 💻\n2_User(student) 🙍")
    choice = input("Enter your choice: ")

    if choice == "1":
        admin = "oday"
        password = "12345"

        name = input("Enter you name: ")
        pass1 = input("Enter your password: ")

        if name == admin and password == pass1:
            options = {
                "AB": "Add Book",
                "DB": "Delete Book",
                "UB": "Update Book",
                "SB": "Show Books",
                "SIB": "Show Issued Book",
                "AU": "Add User",
                "DU": "Delete User",
                "UU": "Updite User",
                "SU": "show Users",
                "Q": "Quit",
            }

            print("\nCurrent mode: 💻ADMIN💻\n")
            while True:
                print("-------------------- ADMIN OPTIONS ---------------------")
                for key,value in options.items():
                    print(f"Press {key} to {value}")
                print("--------------------------------------------------------")

                press_key = input("prss key: ").upper()

                if press_key == "AB":
                    print("\nAdd Book➕ :\n")
                    library.add_book()

                elif press_key == "DB":
                    print("\nDelete Book➖ :\n")
                    library.delete_book()

                elif press_key == "UB":
                    print("\nUpdate Book:\n")
                    library.update_book()

                elif press_key == "SB":
                    print("\nShow Books:\n")
                    library.show_books()
                
                elif press_key == "SIB":
                    print("\nShow Issued Books:\n")
                    library.show_issued_books()

                elif press_key == "AU":
                    print("\nAdd Users:\n")
                    library.add_user()

                elif press_key == "DU":
                    print("\nDelete User:\n")
                    library.delete_user()

                elif press_key == "UU":
                    print("\nUpdate User:\n")
                    library.update_user()
                
                elif press_key == "SU":
                    print("\nShow Users:\n")
                    library.show_users()
                
                elif press_key == "Q":
                    exit()
                else:
                    continue
            
        else:
            print("❌ ERORR [Log in faild] ❌")
        
    elif choice == "2":
        options2 = {
            "SB": "Display Books",
            "IB": "Issue Book",
            "RB": "Return Books",
            "Q": "Quit",
        }
        print("\nCurrent mode: 🙍🏼‍♂️ User 🙍🏼‍♂️\n")
        while True:
            for key,value in options2.items():
                print(f"Press {key} to {value}")

            press_key = input("prss key: ").upper()
            if press_key == "SB":
                print("\Show Book:\n")
                library.show_books()
            elif press_key == "IB":
                print("\nIssue Book:\n")
                library.issue_book()
            elif press_key == "RB":
                print("\nReturn Book:\n")
                library.update_book()
            elif press_key == "Q":
               exit()
            else:
                continue
    else:
        print("❗️ This is not a type of users ❗️")
except Exception as e:
     print("❌ Something went wrong. Please check ❌", e)