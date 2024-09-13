import threading
from Database.db_settings import execute_query
from Decorator.decorator import log_decorator


class Season:

    @log_decorator
    def create_season(self):

        """Create a new season in the database"""

        name = input("Enter  season name: ").capitalize().strip()
        try:
            params = (name,)
            if execute_query(params, fetch='one') is not None:
                print("Season in this name  already exists.")
                return False
            query = '''
                    INSERT INTO seasons (name,start_date,end_date)
                    VALUES (%s, NULL, NULL)
                    '''
            params = (name,)
            threading.Thread(target=execute_query(query, params=params)).start()
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


    @log_decorator  
    def start_season(self, season_id):

        """This query starts a season."""

        season_id = input("Enter the season ID: ").strip()

        try:
            
            start_season = '''
            UPDATE seasons
            SET status = TRUE, start_date = CURRENT_TIMESTAMP 
            WHERE id = %s
            '''
            
            execute_query(start_season, (season_id,))

            print(f"Season {season_id} has been started.")
            return True

        except Exception as e:
            print(f"An error occurred while starting the season: {str(e)}")
            return False


    @log_decorator
    def end_season(self, season_id):
        
        """" this query ending season """

        season_id = input("Enter the season ID: ").strip()
        try:
            end_season = '''
            UPDATE seasons
            SET status = FALSE, end_date = CURRENT_TIMESTAMP
            WHERE id = %s
            '''
            execute_query (end_season, season_id,)
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
            season_id = input("Season_id: ").strip()
            
            season_query = '''
            SELECT * FROM seasons WHERE id = %s
            '''
            
            season = execute_query(season_query, (season_id,), fetch='one')
            
            if season is not None:
                name = input("Enter tender name: ").capitalize().strip()
                description = input("Enter tender description: ").strip()
                
                create_tender_query = '''
                INSERT INTO tenders (name, description,start_date, end_date, season_id)
                VALUES (%s, %s, NULL, NULL, %s)
                '''
                
                execute_query(create_tender_query, (name, description, season_id))
                print("Tender created successfully!")
                return True
            else:
                print("Season not found.")
                return False

        except Exception as e:
            print(f"An error occurred while creating the tender: {str(e)}")
            return False


    def update_tender(self):
        
        """Update a tender in the database"""

        try:
            tender_id = input("Enter the tender ID: ").strip()
            season_id = input("Enter the season ID: ").strip()
            
            season_query = '''
            SELECT * FROM seasons WHERE id = %s
            '''
            
            season = execute_query(season_query, (season_id,), fetch='one')
            
            if season is not None:
                name = input("Enter new tender name: ").capitalize().strip()
                description = input("Enter new tender description: ").strip()
                
                update_tender_query = '''
                UPDATE tenders
                SET name = %s, description = %s, season_id = %s
                WHERE id = %s
                '''
                
                execute_query(update_tender_query, (name, description, season_id, tender_id))
                print("Tender updated successfully!")
                return True
            else:
                print("Season not found.")
                return False
        except Exception as e:
            print(f"An error occurred while updating tender: {str(e)}")
            return False

    @log_decorator
    def delete_tender(self):
        
        """Delete a tender from the database"""

        try:
            tender_id = input("Enter the tender ID: ").strip()
            
            delete_tender_query = '''
            DELETE FROM tenders WHERE id = %s
            '''

            execute_query(delete_tender_query, (tender_id,))
            print("Tender deleted successfully!")
            return True
        except Exception as e:
            print(f"An error occurred while deleting tender: {str(e)}")
            return False


    @log_decorator
    def start_tender(self):
        """This query starts a tender."""
    
        try:
            season_id = input("Enter the season ID: ").strip()
            tender_id = input("Enter the tender ID: ").strip()

            season_query = 'SELECT season_id FROM tenders WHERE season_id = %s'
            tender_query = 'SELECT id FROM tenders WHERE id = %s'
            
            season = execute_query(season_query, (season_id,), fetch='one')
            tender = execute_query(tender_query, (tender_id,), fetch='one')
            
            if season and tender:
                params = (tender_id, season_id)
                start_tender_query = '''
                    UPDATE tenders
                    SET status = TRUE, start_date = CURRENT_TIMESTAMP
                    WHERE id = %s AND season_id = %s
                '''
                
                threading.Thread(target=execute_query, args=(start_tender_query, params)).start()
                print(f"Tender {tender_id} has been started.")
                return True
            else:
                print("Season or Tender not found.")
                return False
        except Exception as e:
            print(f"An error occurred while starting the tender: {str(e)}")
            return False

    @log_decorator
    def end_tender(self):
        """This query ends a tender."""
    
        try:
            season_id = input("Enter the season ID: ").strip()
            tender_id = input("Enter the tender ID: ").strip()

            season_query = 'SELECT season_id FROM tenders WHERE season_id = %s'
            tender_query = 'SELECT id FROM tenders WHERE id = %s'
            
            season = execute_query(season_query, (season_id,), fetch='one')
            tender = execute_query(tender_query, (tender_id,), fetch='one')
            
            if season and tender:
                params = (tender_id,)
                end_tender_query = '''
                    UPDATE tenders
                    SET status = FALSE, end_date = CURRENT_TIMESTAMP
                    WHERE id = %s
                '''
                
                threading.Thread(target=execute_query, args=(end_tender_query, params)).start()
                print(f"Tender {tender_id} has been ended.")
                return True
            else:
                print("Season or Tender not found.")
                return False
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
            print("User not found")
        except Exception as e:
            print(f"An error occurred while retrieving users: {str(e)}")
            return False
    threading.Thread(target=show_all_users,)

    def show_all_votes(votes):
        try:
            query = '''
                SELECT COUNT(*) AS total_votes, user_id
                FROM votes
                GROUP BY user_id
            '''
            votes = execute_query(query, fetch='all')
            threading.Thread(execute_query, args=(query,votes)).start()
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
        
    def show_all_tenders(tenders):

        """Show all tenders in the database"""

        try:
            query = '''
                SELECT id, name, description, status
                FROM tenders
            '''
            tenders = execute_query(query, fetch='all')
            threading.Thread(target=execute_query, args=(query,tenders)).start()
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

    def show_all_applications(self):
        try:
            query = '''
                SELECT id, name, description, status, season_id, user_id
                FROM applications
            '''
            applications= execute_query(query, fetch='all')
            threading.Thread(target=execute_query, args=(applications)).start()
            if applications:
                print("\nAll Applications:")
                for application in applications:
                    id, name, description, status ,season_id, user_id = application
                    print(f"ID: {id}")
                    print(f"Name: {name}") 
                    print(f"Description: {description}")
                    print(f"Status: {'True' if status else 'False'}")
                    print(f"Season ID: {season_id}")
                    print(f"User ID: {user_id}")
                return True
            return False
        except Exception as e:
            print(f"An error occurred while retrieving applications: {str(e)}")
            return False


    def accept_application():
        try:
            application_id = input("Enter the application ID: ").strip()
            accept_application = '''
                UPDATE applications
                SET status = TRUE
                WHERE id = %s
            '''
            threading.Thread(target=execute_query(accept_application, params=(application_id,))).start()
            print(f"Application {application_id} has been accepted.")
            return True
        except Exception as e:
            print(f"An error occurred while accepting application: {str(e)}")
            return False
        
    def refuse_application():
        try:
            application_id = input("Enter the application ID: ").strip()
            refuse_application = '''
                UPDATE applications
                SET status = FALSE
                WHERE id = %s
            '''
            threading.Thread(target=execute_query(refuse_application, params=(application_id,))).start()
            print(f"Application {application_id} has been refused.")
            return True
        except Exception as e:
            print(f"An error occurred while refusing application: {str(e)}")
            return False
        

class User:

    @log_decorator
    def user_profile(self):

        """Show user's profile information"""

        try:
            query = '''
                SELECT id, first_name, last_name,  phone_number, email, address, role, status
                FROM users
                WHERE status = True
            '''
            user_data =(execute_query(query, fetch='one'))
            threading.Thread(target=execute_query, args=(user_data)).start()

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
        
    
    @log_decorator
    def user_tenders(self):

        """Show user's tenders"""

        try:
            user_id = input("Enter your ID: ").strip()
            query = '''
                SELECT id, name, description, status,season_id,
                FROM tenders
                WHERE user_id= %s
            '''
            params = (user_id,)
            tenders= execute_query(query, params=params, fetch='all')
            if tenders:
                print("\nYour Tenders:")
                for tender in tenders:
                    id, name, description,season_id, status= tender
                    print(f"ID: {id}")
                    print(f"Name: {name}")
                    print(f"Description: {description}")
                    print(f"Season ID: {season_id}")
                    print(f"Status: {'True' if status else 'False'}")
                return True
            print("No Tenders")
        except Exception as e:
            print(f"Error retrieving tenders: {e}")
            return False
        
    
    @log_decorator
    def user_applications(self):

        """Show user's applications"""
        try:
            user_id = input("Enter your ID: ").strip()
            query = '''
                SELECT id, name, description, status, season_id
                FROM applications
                WHERE user_id= %s
            '''
            params = (user_id,)
            applications =execute_query(query, params=params, fetch='all')
            if applications:
                print("\nYour Applications:")
                for application in applications:
                    id, name, description, status,  season_id = application
                    print(f"ID: {id}")
                    print(f"Name: {name}")
                    print(f"Description: {description}")
                    print(f"Status: {'True' if status else 'False'}")
                    print(f"Season ID: {season_id}")
                return True
            print("No Applications")
        except Exception as e:
            print(f"Error retrieving applications: {e}")
            return False
    threading.Thread(target = user_applications).start()
            
        
    @log_decorator
    def user_votes(self):
        try:
            user_id = input("Enter your ID: ").strip()
            query = '''
                SELECT COUNT(*) AS total_votes
                FROM votes
                WHERE user_id= %s
            '''
            params = (user_id,)
            votes = execute_query(query, params=params, fetch='one')
            threading.Thread(target = execute_query, args= votes,).start()
            if votes:
                total_votes = votes['total_votes']
                print(f"\nTotal Votes: {total_votes}")
                return True
            return False
        except Exception as e:
            print(f"Error retrieving votes: {e}")
            return False
        
