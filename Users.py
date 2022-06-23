class Users:
 
#-----(add user)--------------------------------------------------------------

    def add_user(self):
        user_id = input("Enter the user id: ")
        user_name = input("Enter the user name: ")
        address = input("Enter the address: ")
        password = input("Enter the password: ")

        if (user_id == "" or user_name == "" or address == "" or password == ""):
            return self.add_user()

        elif (len(user_name) > 20 ):
            print("❗️the user name should be less than 20 character❗️")
            return self.add_user()
        
        else:
            with open(self.users_list , "a") as b:
                b.writelines(
                    f"{user_id},{user_name},{address},{password}\n"
                )
            
            self.users_dict.update(
                {
                    str(int(max(self.users_dict))+1):{
                        "id": user_id,
                        "name": user_name,
                        "address": address,
                        "password": password,
                    }
                }
            )
            print(f"✅✅ {user_name} has been added successfully ✅✅")

#-----(delete book)--------------------------------------------------------------

    def delete_user(self):
        userID = int(input("Enter the user ID to delete it: "))
        try:
            file = open(self.users_list , "r")
            lines = file.readlines()
            del lines[userID - 1]
            modefiedFile = open(self.users_list , "w")
            for line in lines:
                modefiedFile.write(line)
            print("✅✅ The user deleted successfully ✅✅")
        except Exception as e:
            print(f"❌❌The user with ID : {userID} not found❌❌")


#-----(update user)--------------------------------------------------------------

    def update_user(self):
            userID = input("Enter user ID : ")
            if userID in self.users_dict.keys():
                print("What do you want to update in the user?")
                pressKeyListForUpdat = {
                    "1": "Edit id",
                    "2": "Edit name",
                    "3": "Edit password",
                    "4": "Edit address",
                    "q": "quit",
                }
                for key, value in pressKeyListForUpdat.items():
                    print("Press", key, "To", value)
                option_key = input("Press Key : ").lower()
                
                if option_key == "1":
                    print("\nCurrent Action : EDIT ID\n")
                    oldData = input("Enter a old id : ")
                    newData = input("Enter a new id : ")
                    with open(self.users_list, "r") as file:
                        data = file.readlines()[int(userID) - 1]
                        data = data.replace(oldData, newData)
                    with open(self.users_list, "a") as file:
                        file.write(data)
                    file = open(self.users_list, "r")
                    lines = file.readlines()
                    del lines[int(userID) - 1]
                    newFile = open(self.users_list, "w+")
                    for line in lines:
                        newFile.write(line)
                    self.users_dict.update(
                        {
                            str(int(userID)): {
                                "ID": newData,
                                "Name": self.users_dict[userID]["Name"],
                                "Password": self.users_dict[userID]["Password"],
                                "Address": self.users_dict[userID]["Address"]
                            }
                        }
                    )

                elif option_key == "2":
                    print("\nCurrent Action : EDIT NAME\n")
                    oldData = input("Enter a old name : ")
                    newData = input("Enter a new name : ")
                    with open(self.users_list, "r") as file:
                        data = file.readlines()[int(userID) - 1]
                        data = data.replace(oldData, newData)
                    with open(self.users_list, "a") as file:
                        file.write(data)
                    file = open(self.users_list, "r")
                    lines = file.readlines()
                    del lines[int(userID) - 1]
                    newFile = open(self.users_list, "w+")
                    for line in lines:
                        newFile.write(line)
                    self.users_dict.update(
                        {
                            str(int(userID)): {
                                "ID": self.users_dict[userID]["ID"],
                                "Name": newData,
                                "Password": self.users_dict[userID]["Password"],
                                "Address": self.users_dict[userID]["Address"]
                            }
                        }
                    )
                

                elif option_key == "3":
                    print("\nCurrent Action : EDIT NAME\n")
                    oldData = input("Enter a old password : ")
                    newData = input("Enter a new password : ")
                    with open(self.users_list, "r") as file:
                        data = file.readlines()[int(userID) - 1]
                        data = data.replace(oldData, newData)
                    with open(self.users_list, "a") as file:
                        file.write(data)
                    file = open(self.users_list, "r")
                    lines = file.readlines()
                    del lines[int(userID) - 1]
                    newFile = open(self.users_list, "w+")
                    for line in lines:
                        newFile.write(line)
                    self.users_dict.update(
                        {
                            str(int(userID)): {
                                "ID": self.users_dict[userID]["ID"],
                                "Name": self.users_dict[userID]["Name"],
                                "Password": newData,
                                "Address": self.users_dict[userID]["Address"]
                            }
                        }
                    )


                elif option_key == "4":
                    print("\nCurrent Action : EDIT NAME\n")
                    oldData = input("Enter a old address : ")
                    newData = input("Enter a new address : ")
                    with open(self.users_list, "r") as file:
                        data = file.readlines()[int(userID) - 1]
                        data = data.replace(oldData, newData)
                    with open(self.users_list, "a") as file:
                        file.write(data)
                    file = open(self.users_list, "r")
                    lines = file.readlines()
                    del lines[int(userID) - 1]
                    newFile = open(self.users_list, "w+")
                    for line in lines:
                        newFile.write(line)
                    self.users_dict.update(
                        {
                            str(int(userID)): {
                                "ID": self.users_dict[userID]["ID"],
                                "Name": self.users_dict[userID]["Name"],
                                "Password": self.users_dict[userID]["Password"],
                                "Address": newData
                            }
                        }
                    )

                elif option_key == "q":
                    exit()    
                print("✅✅ User has been updated successfully ✅✅\n")
            else:
                print("❌User ID is not found❌")

 
 
#-----(show users)--------------------------------------------------------------

    def show_users(self):
        print(
            "=============================================== 👤 List of Users 👤 ==============================================="
        )
        print(
            "{0:^1}{1:>12s}{2:>17s}{3:>17s}".format(
                "User ID", "Name", "Pssword", "Address"
            )
        )
        print(
            "===================================================================================================================="
        )
        for keys, value in self.users_dict.items():
            print(
                "{0:^1}{1:>18s}{2:>15s}{3:>18s}".format(
                    keys,
                    value.get("Name"),
                    value.get("Password"),
                    value.get("Address"),
                    value.get("ID"),
                )
            )
        print(
            "===================================================================================================================="
        )