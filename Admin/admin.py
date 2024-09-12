import threading
from Database.db_settings import execute_query
from Decorator.decorator import log_decorator
from Utils.email import check_email

class Season:

    @log_decorator
    def create_season(self):

        """Create a new season in the database"""

        name = input("Enter  season name: ").capitalize().strip()
        try:
            params = (name,)
            if execute_query(query, params, fetch='one') is not None:
                print("Season in this name  already exists.")
                return False
            query = '''
                    INSERT INTO seasons (name)
                    VALUES (%s)
                    '''
            params = (name,)
            execute_query(query, params=params)
            print("Season created successfully successfully")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while adding season: {str(e)}")
            return False
        

    @log_decorator
    def update_season(self):

        """update the season in the database"""

        season_id = input("Enter the season ID: ").strip()
        new_name = input("Enter new name: ").capitalize().strip()

        query = '''UPDATE seasons SET name = %s WHERE id = %s'''
        params = (new_name, season_id)
        threading.Thread(target=execute_query(query, params)).start()
        print("Season updated successfully!")
        return None

    
    @log_decorator
    def delete_season(self):

        """delete a season from the database"""

        season_id = input("Enter the season ID: ").strip()

        query = "DELETE FROM seasons WHERE id = %s"
        params = (season_id,)
        threading.Thread(target=execute_query(query, params)).start()
        print("Season deleted successfully!")
        return None


    def start_season(self,season_id):

        """" this query starting season """

        try:
            season_id = input("Enter the season ID: ").strip()
            start_season = '''
            UPDATE seasons
            SET status = TRUE
            WHERE id = %s
            '''
            threading.Thread(target=execute_query(start_season, params=(season_id,)))

            print(f"Season {season_id} has been started.")
            return True
        except Exception as e:
            print(f"An error occurred while starting the season: {str(e)}")
            return False

    def end_season(self, season_id):
        
        """" this query ending season """

        try:
            season_id = input("Enter the season ID: ").strip()
            end_season = '''
            UPDATE seasons
            SET status = FALSE
            WHERE id = %s
            '''
            threading.Thread(target=execute_query(end_season, params=(season_id,)))
            print(f"Season {season_id} has been ended.")
            return True
        except Exception as e:
            print(f"An error occurred while ending the season: {str(e)}")
            return False



class Tender:
    @log_decorator
    def create_tender(self):

        """Create a new tender in the database"""

        try:    
            name = input("Enter tender name: ").capitalize().strip()
            description = input("Enter tender description: ").strip()
            threading.Thread(target=execute_query, args=(name,description,)).start()
            print("Tender created successfully!")
            return None
        except Exception as e:
            print(f"An error occurred while creating tender: {str(e)}")
            return False
    

    def update_tender(self):
        
        """Update a tender in the database"""

        try: 
            tender_id = input("Enter the tender ID: ").strip()
            name = input("Enter new name: ").capitalize().strip()
            description = input("Enter new description: ").strip()
            threading.Thread(target=execute_query(name, description, tender_id,)).start()
            print("Tender updated successfully!")
            return None
        except Exception as e:
            print(f"An error occurred while updating tender: {str(e)}")
            return False


    @log_decorator
    def delete_tender(self):
        
        """Delete a tender from the database"""

        try:
            tender_id = input("Enter the tender ID: ").strip()
            query = '''DELETE  FROM tender WHERE id %s '''
            params =(tender_id)
            threading.Thread(target=execute_query(query,params,)).start()
            print("Tender deleted successfully!")
            return None
        except Exception as e:
            print(f"An error occurred while deleting tender: {str(e)}")
            return False
        
    def start_tender(self):
        
        """" this query starting tender """
        
        try:
            tender_id = input("Enter the tender ID: ").strip()
            start_tender = '''
            UPDATE tender
            SET status = TRUE
            WHERE id = %s
            '''
            threading.Thread(target=execute_query(start_tender, params=(tender_id,))).start()
            print(f"Tender {tender_id} has been started.")
            return True
        except Exception as e:
            print(f"An error occurred while starting the tender: {str(e)}")
            return False
        
    def end_tender(self):
        
        """" this query ending tender """
        
        try:
            tender_id = input("Enter the tender ID: ").strip()
            end_tender = '''
            UPDATE tender
            SET status = FALSE
            WHERE id = %s
            '''
            threading.Thread(target=execute_query(end_tender, params=(tender_id,))).start()
            print(f"Tender {tender_id} has been ended.")
            return True
        except Exception as e:
            print(f"An error occurred while ending the tender: {str(e)}")
            return False
        
class Statistics:

    @log_decorator
    def show_all_users(self):
        try:
            query = '''
                SELECT id, first_name, last_name, phone_number, email
                FROM users
            '''
            users = execute_query(query, fetch='all')
            if users:
                print("\nAll Users:")
                for user in users:
                    id, first_name, last_name, phone_number, email = user
                    print(f"id: {id}")
                    print(f"Name: {first_name}")
                    print(f"Last Name: {last_name}")
                    print(f"Phone_number:{phone_number} ")
                    print(f"Email: {email}")
                return True
            return False
        except Exception as e:
            print(f"An error occurred while retrieving users: {str(e)}")
            return False

    def show_all_votes():
        try:
            query = '''
                SELECT COUNT(*) AS total_votes, user_id
                FROM votes
                GROUP BY user_id
            '''
            votes = execute_query(query, fetch='all')
            if votes:
                print("\nTotal Votes:")
                for vote in votes:
                    total_votes, user_id = vote
                    print(f"User ID: {user_id}")
                    print(f"Total Votes: {total_votes}")
                return True
            return False
        except Exception as e:
            print(f"An error occurred while retrieving votes: {str(e)}")
            return False
        
    def show_all_tenders():

        """Show all tenders in the database"""

        try:
            query = '''
                SELECT id, name, description, status
                FROM tender
            '''
            tenders = execute_query(query, fetch='all')
            if tenders:
                print("\nAll Tenders:")
                for tender in tenders:
                    id, name, description, status = tender
                    print(f"ID: {id}")
                    print(f"Name: {name}")
                    print(f"Description: {description}")
                    print(f"Status: {'True' if status else 'False'}")
                return True
            return False
        except Exception as e:
            print(f"An error occurred while retrieving tenders: {str(e)}")
            return False
            

class Application:

    pass


class User:

    @log_decorator
    def user_profile(self):
        try:
            query = '''
                SELECT id, first_name, last_name,  phone_number, email, address, role, status
                FROM users
                WHERE status = True
            '''
            user_data = execute_query(query, fetch='one')

            if user_data:
                id,first_name, last_name,  phone_number, email, address, role, status = user_data
                print("\nYour Profile:")
                print(f"id:{id}")
                print(f"Name: {first_name}")
                print(f"Last Name: {last_name}")
                print(f"Phone Number: {phone_number}")
                print(f"Email: {email}")
                print(f"Address: {address}")
                print(f"Role: {role.capitalize()}")
                print(f"Status: {'True' if status else 'False'}")
                return True
            else:
                print("Profile not found.")
                return False

        except Exception as e:
            print(f"Error retrieving profile: {e}")
            return False