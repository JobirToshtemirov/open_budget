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
    def start_season(self):

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
    def end_season(season_id):
        
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

    @log_decorator
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
                print(f"\nTender {tender_id} has been started.")
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
            
            season = execute_query(season_query , (season_id,), fetch='one')
            tender = execute_query(tender_query , (tender_id,), fetch='one')
            
            if season and tender:
                params = (tender_id,)
                end_tender_query = '''
                    UPDATE tenders
                    SET status = FALSE, end_date = CURRENT_TIMESTAMP
                    WHERE id = %s
                '''
                
                threading.Thread(target=execute_query, args=(end_tender_query, params)).start()
                print(f"\nTender {tender_id} has been ended.")
                return True
            else:
                print("Season or Tender not found.")
                return False
        except Exception as e:
            print(f"An error occurred while ending the tender: {str(e)}")
            return False

        
class Statistics:

    @log_decorator
    def show_all_users(user):
        try:
            query = '''
                SELECT id, first_name, last_name, phone_number, email, status
                FROM users
            '''
            users = execute_query(query = query, fetch='all')
            if users:
                print("\n\t\t\tAll Users:\n")
                for user in users:
                    id, first_name, last_name, phone_number, email, status = user
                    print(f"\t\t\tid: {id}")
                    print(f"\t\t\tName: {first_name}")
                    print(f"\t\t\tLast Name: {last_name}")
                    print(f"\t\t\tPhone_number:{phone_number} ")
                    print(f"\t\t\tEmail: {email}")
                    print(f"\t\t\tStatus: {status}\n")
                return True
            print("User not found")
        except Exception as e:
            print(f"An error occurred while retrieving users: {str(e)}")
            return False
    threading.Thread(target=show_all_users,)


    @log_decorator
    def show_all_seasons(seasons):
        try:
            query = '''
                SELECT id, name, start_date, end_date
                FROM seasons
            '''
            seasons = execute_query(query=query, fetch='all')
            threading.Thread(target=execute_query, args=(query, seasons)).start()
            if seasons:
                print("\n\t\t\tAll Seasons:\n")
                for season in seasons:
                    id, name, start_date, end_date = season
                    print(f"\t\t\tID: {id}")
                    print(f"\t\t\tName: {name}")
                    print(f"\t\t\tStart Date: {start_date}")
                    print(f"\t\t\tEnd Date: {end_date}\n")
                return True
            return False
        except Exception as e:
            print(f"An error occurred while retrieving seasons: {str(e)}")


    def show_all_votes(votes):
        try:
            query = '''
                SELECT COUNT(*) AS total_votes, user_id
                FROM votes
                GROUP BY user_id
            '''
            votes = execute_query(query = query, fetch='all')
            threading.Thread(target = execute_query, args=(query, votes)).start()
            if votes:
                print("\n\t\t\tTotal Votes:\n")
                for vote in votes:
                    total_votes, user_id = vote
                    print(f"\t\t\tUser ID: {user_id}")
                    print(f"\t\t\tTotal Votes: {total_votes}\n")
                return True
            return False
        except Exception as e:
            print(f"An error occurred while retrieving votes: {str(e)}")
            return False
        

    @log_decorator  
    def show_all_tenders(tenders):

        """Show all tenders in the database"""

        try:
            query = '''
                SELECT id, name, description,start_date, end_date, status
                FROM tenders
            '''
            tenders = execute_query(query=query, fetch='all')
            threading.Thread(target=execute_query, args=(query,tenders)).start()
            if tenders:
                print("\n\t\t\tAll Tenders:\n")
                for tender in tenders:
                    id, name, description, start_date, end_date, status = tender
                    print(f"\t\t\tID: {id}")
                    print(f"\t\t\tName: {name}")
                    print(f"\t\t\tDescription: {description}")
                    print(f"\t\t\tStart Date: {start_date}")
                    print(f"\t\t\tEnd Date: {end_date}")
                    print(f"\t\t\tStatus: {'True' if status else 'False'}\n")
                return True
            return False
        except Exception as e:
            print(f"An error occurred while retrieving tenders: {str(e)}")
            return False
        

    @log_decorator    
    def show_active_season(self):
        try:
            query = '''
                SELECT id, name, start_date, end_date
                FROM seasons
                WHERE status = TRUE
            '''
            season = execute_query(query=query, fetch='one')
            threading.Thread(target=execute_query, args=(query, season)).start()
            if season:
                id, name, start_date, end_date = season
                print(f"\n\t\tActive Season:\n")
                print(f"\t\tID: {id}")
                print(f"\t\tName: {name}")
                print(f"\t\tStart Date: {start_date}")
                print(f"\t\tEnd Date: {end_date}\n")
                return True
            return False
        except Exception as e:
            print(f"An error occurred while retrieving active season: {str(e)}")


    @log_decorator
    def show_active_tenders(self):

        """Retrieve and display all active tenders."""

        try:
            query = '''
                SELECT id, name, description, season_id, status FROM tenders WHERE status = TRUE
            '''
            tenders = execute_query(query, fetch='all')

            if tenders:
                for tender in tenders:
                    tender_id, name, description, season_id, status = tender
                    print(f"\n\t\t\tTender ID: {tender_id}")
                    print(f"\t\t\tName: {name}")
                    print(f"\t\t\tDescription: {description}")
                    print(f"\t\t\tSeason ID: {season_id}")
                    print(f"\t\t\tStatus: {'Active' if status else 'Inactive'}\n")
            else:
                print("No active tenders found.")
            
            return True

        except Exception as e:
            print(f"An error occurred while retrieving active tenders: {str(e)}")
            return False



class Application:
    @log_decorator
    def show_all_applications(self):
        try:
            query = '''
                SELECT id, name, description, status, season_id, user_id
                FROM applications
            '''
            applications= execute_query(query=query, fetch='all')
            threading.Thread(target=execute_query, args=(applications)).start()
            if applications:
                print("\n\t\t\tAll Applications:\n")
                for application in applications:
                    id, name, description, status ,season_id, user_id = application
                    print(f"\t\t\tID: {id}")
                    print(f"\t\t\tName: {name}") 
                    print(f"\t\t\tDescription: {description}")
                    print(f"\t\t\tStatus: {'True' if status else 'False'}")
                    print(f"\t\t\tSeason ID: {season_id}")
                    print(f"\t\t\tUser ID: {user_id}\n")
                return True
            return False
        except Exception as e:
            print(f"An error occurred while retrieving applications: {str(e)}")
            return False

    @log_decorator
    def accept_application(self):
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

    @log_decorator   
    def refuse_application(self):
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
    def user_profile(user_data):

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
                print("\n\t\t\tYour Profile:\n")
                print(f"\t\t\tid:{id}")
                print(f"\t\t\tName: {first_name}")
                print(f"\t\t\tLast Name: {last_name}")
                print(f"\t\t\tPhone Number: {phone_number}")
                print(f"\t\t\tEmail: {email}")
                print(f"\t\t\tAddress: {address}")
                print(f"\t\t\tRole: {role.capitalize()}")
                print(f"\t\t\tStatus: {'True' if status else 'False'}\n")
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
                SELECT tender_id, season_id, user_id
                FROM votes
                WHERE user_id= %s
            '''
            params = (user_id,)
            tenders= execute_query(query, params=params, fetch='all')
            if tenders:
                print("\n\t\t\tYour Tenders:\n")
                for tender in tenders:
                    tender_id, season_id , status = tender
                    print(f"\t\t\tTender_id: {tender_id}")
                    print(f"\t\t\tSeason ID: {season_id}")
                    print(f"\t\t\tStatus: {'True' if status else 'False'}\n")
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
                print("\n\t\t\tYour Applications:\n")
                for application in applications:
                    id, name, description, status,  season_id = application
                    print(f"\t\t\tID: {id}")
                    print(f"\t\t\tName: {name}")
                    print(f"\t\t\tDescription: {description}")
                    print(f"\t\t\tStatus: {'True' if status else 'False'}")
                    print(f"\t\t\tSeason ID: {season_id}\n")
                return True
            print("No Applications")
        except Exception as e:
            print(f"Error retrieving applications: {e}")
            return False
    threading.Thread(target = user_applications,).start()
            
        
    @log_decorator
    def user_votes(self):

        """Retrieve and display the number of votes a user has cast."""

        try:
            user_id = input("Enter your ID: ").strip()

            query1 = '''
                SELECT tender_id, season_id FROM votes
                WHERE user_id = %s
            '''
            
            
            query = '''
                SELECT COUNT(*) AS total_votes
                FROM votes
                WHERE user_id = %s
            '''
            

            votes = execute_query(query1, (user_id,), fetch='all')  
            total_votes_result = execute_query(query, (user_id,), fetch='one') 

            if votes:
                print("\n\t\t\tYour Votes:\n")
                for vote in votes:
                    tender_id, season_id = vote
                    print(f"\t\t\tTender ID: {tender_id}")
                    print(f"\t\t\tSeason ID: {season_id}\n")
            else:
                print("No votes found.")
            
            if total_votes_result:
                total_votes = total_votes_result[0]  
                print(f"\t\tYour total votes : {total_votes}")
            else:
                print("No votes found.")
            return True
        except Exception as e:
            print(f"Error retrieving votes: {e}")
            return False


            
