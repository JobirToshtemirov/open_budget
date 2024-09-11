import hashlib
import threading
from datetime import datetime
from Database.db_settings import Database , execute_query
from Decorator.decorator import log_decorator 
from Utils.email import send_mail,check_email


ADMIN_LOGIN = "password"
ADMIN_PASSWORD = "login"


class Auth:
    def __init__(self):
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").__str__()
        self.__database = Database()

    @log_decorator
    def register(self):
        """
        Register a new user in the system.
        Checks for existing users with the same phone number or email.
        """
        first_name = input("Ismingizni kiriting: ").capitalize().strip()
        last_name = input("Familiyangizni kiriting: ").capitalize().strip()
        phone_number = input("Telefon raqamingizni kiriting: ").strip()
        email = input("Email kiriting: ").strip()
        password = input("Shahsiy parol o'rnating: ").strip()
        passport_info = input("Passport malumotlaringizni kiriting masalan AC 7770777: ").strip()
        address = input("Yashash manzilingiz (Viloyat)-ni kiriting: ").strip()
        hash_pass = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()
        role = 'user'
        try:
            check_email(email)
            subjects = "You logged in Open budget platform"
            message = f"Your login in Open budget platform: {passport_info}\nYour password in Open budget platform: {password}\n"
            threading.Thread(target=send_mail(email, subjects, message)).start()

            query = '''
            SELECT * FROM users WHERE passport=%s OR email=%s
            '''
            params = (passport_info, email)
            if execute_query(query, params, fetch='one') is not None:
                print("Passport or email already exists.")
                return False
            query = '''
            INSERT INTO users (first_name, last_name, phone_number, email, password, passport_info, address, role)
            VALUES (%s,%s, %s, %s, %s, %s, %s, %s)
            '''
            params = (first_name, last_name, phone_number, email, hash_pass, passport_info, address, role)
            execute_query(query, params=params)
            print("Registration successfully")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while registering: {str(e)}")
            return False

    @log_decorator
    def login(self):
        """
        Authenticate a user by checking their email and password.
        Updates the user's login status to True upon successful login.
        """
        try:
            phone_number: str = input("Phone number: ").strip()
            password: str = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()

            if phone_number == ADMIN_LOGIN and password == hashlib.sha256(
                    ADMIN_PASSWORD.encode('utf-8')).hexdigest():
                return {'is_login': True, 'role': '_admin'}

            query = '''
            SELECT role FROM users WHERE phone_number=%s AND password=%s
            '''
            params = (phone_number, password)
            user = execute_query(query, params, fetch='one')

            if user is None:
                print("Invalid phone_number or password.")
                return {'is_login': False}

            # Correctly update the status for a successful login
            update_query = 'UPDATE users SET status=TRUE WHERE phone_number=%s'
            execute_query(update_query, params=(phone_number,))

            return {'is_login': True, 'role': user['role']}
        except ValueError:
            print("Invalid input. Please try again.")
            return None
        except IndexError:
            print("Email or password is incorrect.")
            return None
        except Exception as e:
            print(f"An error occurred while logging in: {str(e)}")
            return None

    @log_decorator
    def logout(self):
        """
                Set the login status of all users to False (i.e., log out all users).
        """
        query = 'UPDATE users SET status=FALSE;'
        execute_query(query)
        return True