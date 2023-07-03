from addition.parking.model import User


def UI():
    while True:
        text = """
            1) register
            2) login
            3) exit
                >>>"""
        key = int(input(text))
        match key:
            case 1:
                d = {"name": input("name"),
                     "username": input("username"),
                     "password": input("password")
                     }
                obj = User(**d)
                if not obj.check_user():
                    obj.save_user()
                    print("Register success!")
                else:
                    print("Your username already exists !")



            case 2:
                pass
            case 3:
                break


UI()
