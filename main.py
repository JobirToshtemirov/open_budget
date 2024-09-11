import threading
from utils.queries import create_tables
def auth_menu():
    print('''
1. Register
2. Login
3. Logout
    ''')
    try:
        user_input: int = int(input("Choose menu: "))
        if user_input == 1:
            print("\nHello world")
            auth_menu()
        elif user_input == 2:
            print("\nHello world")
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
        create_tables()

if __name__ == '__main__':
    threading.Thread(target=auth_menu()).start
    threading.Thread(target=create_tables()).start()
