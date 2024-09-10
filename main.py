
def auth_menu():
    print('''
1. Register
2. Login
3. Logout
    ''')
    try:
        user_input: int = int(input("Choose menu: "))
        if user_input == 1:
            pass
        elif user_input == 2:
            result_login = 2
            if not result_login['is_login']:
                auth_menu()
                pass
            elif result_login['role'] == 'admin':
                pass
            elif result_login['role'] == 'user':
                pass
        elif user_input == 3:
            print("Good bye!")
            pass         
            auth_menu()
        else:
            print("Invalid input")
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()