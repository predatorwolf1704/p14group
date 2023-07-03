from functions import User


def main():
    try:
        text = """WELCOME TO Online Shop
                1)register
                2)login
                3)exit
                
                >>>"""
        choice = input(text)
        if choice == "1":
            role_txt = """Role:
                        1)Client
                        2)Merchant
                        >>>"""
            data = {"fullname": input("Fullname:"),
                    "username": input("Username:"),
                    "password": input("Password:"),
                    "role": input(role_txt),
                    "email": input("email:")
                    }
            obj = User(**data)
            obj.check_data()
            obj.save_data()

        elif choice == "2":
            data = {
                "username": input("Username:"),
                "password": input("Password:")
            }
            obj = User(**data)
            response = obj.login()
            print(response)
        elif choice == "3":
            print("Goodbye !")
            return
    except Exception as e:
        print(e)
        main()

main()
