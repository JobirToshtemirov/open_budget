import smtplib
import threading
from Database.db_settings import execute_query
from Decorator.decorator import log_decorator


class EmailSendMessage:

    @log_decorator
    def send_email_all_users(self):

        subject = input("Enter subject: ")
        message = input("Enter message: ")

        query = """
        SELECT email FROM users
        """

        result = execute_query(query, fetch="all")

        if result:
            for row in result:
                email = row['email']
                threading.Thread(target=send_mail, args=(email, subject, message)).start()

            print("Emails sent successfully.")
            return True
        else:
            print("No users found.")
            return False

@log_decorator
def send_mail(to_user, subject, message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_sender = 'toshtemirovjobir6@gmail.com'
    smtp_password = 'shqc qgxc ufen lxhp'
    email = f"Subject: {subject}\n\n{message}"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, to_user, email)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Failed {e}")

@log_decorator
def check_email(email):
    """
    Check if the email is valid.

    """
    if '@gmail' in email:
        return True
    else:
        return False
