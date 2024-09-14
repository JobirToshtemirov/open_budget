import hashlib
import threading
from Database.db_settings import Database , execute_query
from Decorator.decorator import log_decorator 
from Utils.email import send_mail,check_email


ADMIN_LOGIN = "password"
ADMIN_PASSWORD = "login"



class Auth:
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
            SELECT * FROM users WHERE passport_info=%s OR email=%s
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
            print("\nYour login and password sended your email address")
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
                passport_info: str = input("Emailingiz ga borgan loginingizni kiriting: ").strip()
                password: str = hashlib.sha256(input("Parolingizni kiriting: ").strip().encode('utf-8')).hexdigest()


                if passport_info == ADMIN_LOGIN and password == hashlib.sha256(
                        ADMIN_PASSWORD.encode('utf-8')).hexdigest():
                    return {'is_login': True, 'role': 'admin'}


                query = '''
                SELECT role FROM users WHERE passport_info=%s AND password=%s
                '''
                params = (passport_info, password,)
                user = execute_query(query, params, fetch='one')

                if user is None:
                    print("Invalid passport info or password.")
                    return {'is_login': False, 'role': 'user'}
               
                update_query = 'UPDATE users SET status=TRUE WHERE passport_info=%s'
                execute_query(update_query, params=(passport_info,))

                return {'is_login': True, 'role': user[0]} 
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

   