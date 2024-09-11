import threading
from Utils.queries import create_tables
from Auth.auth import Auth

auth=Auth()

def auth_menu():
    print('''
1. Register
2. Login
3. Logout
    ''')
    try:
        user_input: int = int(input("Choose menu: "))
        if user_input == 1:
            auth.register()
            auth_menu()
        elif user_input == 2:
            auth.login()
            auth_menu()
            result_login = 2
            if not result_login['is_login']:
                auth_menu()
                pass
            elif result_login['role'] == 'admin':
                pass
            elif result_login['role'] == 'user':
                pass
        elif user_input == 3:
            print("\nGood bye!")
            pass         
            auth_menu()
        else:
            print("Invalid input")
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


def admin_menu():
    print("""\nWelcome to admin menu:
1.Manage season
2.Manage tender
3.All statistics
4.
""")
    try:
        choice =input("Choose one of the menu: ")
        if choice == '1':
            season_menu()
            admin_menu()
        elif choice == '2':
            tender_menu()
            admin_menu()
        elif choice == '3':
            statistics_menu()
            admin_menu()
        else:
            print("Invalid input")
            admin_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()


def statistics_menu():

    print("""\nWelcome to statistics menu:
1.Show all users
2.Show all votes 
3.Show all tenders
4.
""")
    try:
        choice =input("Choose one of the menu: ")
        if choice == '1':
            season_menu()
            admin_menu()
        elif choice == '2':
            manage_tender_menu()
            admin_menu()
        elif choice == '3':
            staticmethod_menu()
            admin_menu()
        else:
            print("Invalid input")
            admin_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()

"""

if __name__ == '__main__':
    threading.Thread(target=create_tables()).start()
    threading.Thread(target=auth_menu()).start
