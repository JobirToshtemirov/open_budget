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
            result_login = auth.login()
            if not result_login['is_login']:
                auth_menu()
            elif result_login['role'] == 'admin':
                admin_menu()
                auth_menu()
            elif result_login['role'] == 'user':
                user_menu()
                auth_menu()
        elif user_input == 3:
            print("\nGood bye!")
            auth.logout()         
        else:
            print("Invalid input")
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


def admin_menu():
    print("""\nWelcome to admin menu:
1. Manage season
2. Manage tender
3. All statistics
4. Back to auth menu
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
        elif choice == '4':
            print("Back to auth menu")
            auth_menu()
        else:
            print("Invalid input")
            admin_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()

def user_menu():
    print("""\nWelcome to user menu:   
1. My profile
2. My tenders
3. My applications
4. My votes
5. Back to auth menu
""")
    try:
        choice = input("Enter your choice: ")
        if choice == '1':
            user_profile()
            user_menu()
        elif choice == '2':
            user_tenders()
            user_menu()
        elif choice == '3':
            user_applications()
            user_menu()
        elif choice == '4':
            user_votes()
            user_menu()
        elif choice == '5':
            print("Back to auth menu")
            auth_menu()
        else:
            print("Invalid input")
            user_menu()
    except Exception as e:
        print(f'Error: {e}')
        user_menu()

def season_menu():
    print("""\nWelcome to season menu:
1. Create season
2. Update season
3. Delete season
4. Start season
5. End season
6. Back to admin menu
""")
    try:
        choice =input("Choose one of the menu: ")
        if choice == '1':
            create_season()
            season_menu()
        elif choice == '2':
            update_season()
            season_menu()
        elif choice == '3':
            delete_season()
            season_menu()
        elif choice == '4':
            start_season()
            season_menu()
        elif choice == '5':
            end_season()
            season_menu()
        elif choice == '6':
            admin_menu()
        else:
            print("Invalid input")
            season_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()



def tender_menu():
    print("""\nWelcome to season menu:
1. Create tender
2. Update tender
3. Delete tender
4. Start tender
5. End tender
6. Back to admin menu
""")
    try:
        choice =input("Choose one of the menu: ")
        if choice == '1':
            create_tender()
            season_menu()
        elif choice == '2':
            update_tender()
            season_menu()
        elif choice == '3':
            delete_tender()
            season_menu()
        elif choice == '4':
            start_tender()
            season_menu()
        elif choice == '5':
            end_tender()
            tender_menu()
        elif choice == '6':
            admin_menu()
        else:
            print("Invalid input")
            tender_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()

def statistics_menu():

    print("""\nWelcome to statistics menu:
1. Show all users
2. Show all votes 
3. Show all tenders
4. Bach to admin menu
5. Back to auth menu
""")
    try:
        choice =input("Choose one of the menu: ")
        if choice == '1':
            season_menu()
            statistics_menu()
        elif choice == '2':
            manage_tender_menu()
            statistics_menu()
        elif choice == '3':
            staticmethod_menu()
            statistics_menu()
        elif choice == '4':
            admin_menu()
        elif choice == '5':
            auth_menu()
        else:
            print("Invalid input")
            statistics_menu()
    except Exception as e:
        print(f'Error: {e}')
        statistics_menu()

if __name__ == '__main__':
    threading.Thread(target=auth_menu()).start()
    threading.Thread(target=create_tables()).start()