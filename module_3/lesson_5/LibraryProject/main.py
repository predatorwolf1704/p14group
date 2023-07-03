# 1) database
# 2) model
# 3) UI
# 4) method
from tabulate import tabulate

from module_3.lesson_5.LibraryProject.model import User, Category


class Basic:
    def __init__(self, session):
        self.session_user = session

    def settings(self):
        menu = """
        1) change info
        2) delete account
        3) <- back
        """
        key = int(input(menu))
        match key:
            case 1:
                menu_col = """
                    1) name
                    2) username
                    3) password
                    4) <- back
                        >>>"""
                key = int(input(menu_col))
                if key != 4:
                    new_val = input("New value: ")
                match key:
                    case 1:
                        self.session_user.change_info("name", new_val)
                    case 2:
                        self.session_user.change_info("username", new_val)
                    case 3:
                        self.session_user.change_info("password", new_val)
                    case 4:
                        self.settings()
                self.settings()

            case 2:
                if self.session_user.role == "ADMIN":
                    AdminUI(self.session_user).admin_menu()
                else:
                    UserUI(self.session_user).user_menu()


class UserUI(Basic):
    def __init__(self, session):
        super().__init__(session)

    def user_menu(self):
        pass


class AdminUI(Basic):
    def __init__(self, session):
        super().__init__(session)

    def add_admin(self):
        pass

    def admin_menu(self):
        menu = """
        1) Category
        2) Book
        3) add admin
        4) settings
        5) logout
            >>>"""
        key = int(input(menu))
        match key:
            case 1:
                self.category_crud()
            case 2:
                pass
            case 3:
                self.add_admin()
            case 4:
                self.settings()
            case 5:
                return

    def category_crud(self):
        crud_menu = """
            1) add category
            2) delete category
            3) update category
            4) show category
            5) <- back
                >>>"""
        key = int(input(crud_menu))
        match key:
            case 1:
                name = input("New category name: ")
                response = Category(name=name).add()
                if not response:
                    print("Already exist !")
                else:
                    print("Success add !")
                self.category_crud()

            case 2:
                datas = Category().show()
                print(tabulate(datas, tablefmt="simple_grid"))
                Id_key = int(input("Id : "))
                Category(id=Id_key).delete()
                print("Successfully delete !")
                self.category_crud()
            case 3:
                datas = Category().show()
                print(tabulate(datas, tablefmt="simple_grid"))
                d = {
                    "id": int(input("Id : ")),
                    "name": input("New Name: ")
                }
                Category(**d).update()
                print("Success update")
                self.category_crud()


            case 4:
                datas = Category().show()
                print(tabulate(datas, tablefmt="simple_grid"))
                self.category_crud()
            case 5:
                self.admin_menu()


def register():
    d = {
        "name": input("Name:"),
        "username": input("Username:"),
        "password": input("Password:"),
    }
    user = User(**d)
    if user.check_username():
        print("Your username already exists!")
        return
    user.save_user()
    print("Registration successful !")


def login():
    d = {
        "username": input("Username:"),
        "password": input("Password:"),
    }

    obj = User(**d)
    session_user = obj.login_check()
    if not session_user:
        print("Wrong username or password !")
        return
    print(f"Welcome {session_user.name}")
    if session_user.role == "ADMIN":
        AdminUI(session_user).admin_menu()
    else:
        UserUI(session_user).user_menu()


def UI():
    while True:
        text = """
        1) Register
        2) Login
        3) exit
            >>>"""
        key = int(input(text))
        match key:
            case 1:
                register()
            case 2:
                login()
            case 3:
                break


UI()
