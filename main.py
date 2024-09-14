import threading
from Utils.queries import create_tables
from Auth.auth import Auth
from Admin.admin import User, Season, Tender, Statistics, Application
from User.user import Vote
from Utils.add_info_for_table import add_info_to_table

vote = Vote()
user = User()
season = Season()
tender= Tender()
statistics = Statistics()
application = Application()
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
                user_first_menu()
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
4. Manage application
5. Back to auth menu
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
            application_menu()
            admin_menu()
        elif choice == '5':
            print("Back to auth menu")
            auth_menu()
        else:
            print("Invalid input")
            admin_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()


def user_first_menu():
    print("""\nWelcome to the first  user's menu:
Choose an option:\n
1. Vote for tender
2. Send application
3. My profile
4. Get info about my actions
""")
    try:
        choice = input("Choose an option: ")
        if choice == '1':
            vote.get_active_tenders()
            vote.vote_for_tender()
            user_first_menu()
        elif choice == '2':
            vote.get_active_seasons()
            vote.send_application()
            user_first_menu()
        elif choice == '3':
            user.user_profile()
            user_first_menu()
        elif choice == '4':
            user_menu()
        else:
            print("Invalid input")
            user_first_menu()
    except Exception as e:
        print(f'Error: {e}')
        user_first_menu()
          


def user_menu():
    print("""\nWelcome to user menu:   
1. My tenders
2. My applications
3. My votes
4. Back to auth menu
""")
    try:
        choice = input("Enter your choice: ")
        if choice == '1':
            user.user_tenders()
            user_menu()
        elif choice == '2':
            user.user_applications()
            user_menu()
        elif choice == '3':
            user.user_votes()
            user_menu()
        elif choice == '4':
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
            season.create_season()
            season_menu()
        elif choice == '2':
            season.update_season()
            season_menu()
        elif choice == '3':
            season.delete_season()
            season_menu()
        elif choice == '4':
            season.start_season(season_id=season.start_season)
            season_menu()
        elif choice == '5':
            season.end_season(season_id=season.end_season)
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
    print("""\nWelcome to tender menu:
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
            tender.create_tender()
            tender_menu()
        elif choice == '2':
            tender.update_tender()
            tender_menu()
        elif choice == '3':
            tender.delete_tender()
            tender_menu()
        elif choice == '4':
            tender.start_tender(tender.start_tender())
            tender_menu()
        elif choice == '5':
            tender.end_tender(tender.end_tender())
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
4. Back to admin menu
5. Back to auth menu
""")
    try:
        choice =input("Choose one of the menu: ")
        if choice == '1':
            statistics.show_all_users()
            statistics_menu()
        elif choice == '2':
            statistics.show_all_votes()
            statistics_menu()
        elif choice == '3':
            statistics.show_all_tenders()
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


def application_menu():
    print("""\nWelcome to application menu:
1. Show all applications
2. Accept application
3. Refuse application
4. Back to admin menu
""")
    try:
        choice = input("Choose application: ")
        if choice == '1':
            application.show_all_applications()
            application_menu()
        elif choice == '2':
            application.show_all_applications()
            application.accept_application()
            application_menu()
        elif choice == '3':
            application.show_all_applications()
            application.refuse_application()
            application_menu()
        elif choice == '4':
            admin_menu()
    except Exception as e:
        print(f'Error: {e}')
        application_menu()
        auth.logout()



if __name__ == '__main__':
    threading.Thread(target=auth.logout).start()
    threading.Thread(target=create_tables).start()
    threading.Thread(target=add_info_to_table).start()
    threading.Thread(target=auth_menu).start()