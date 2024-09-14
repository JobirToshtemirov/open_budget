import threading
from Database.db_settings import execute_query
from Decorator.decorator import log_decorator


class Vote:
    
    @log_decorator
    def send_application(self):

        """Send an application for a season in the database"""
        
        try:
            season_id = input("Enter season ID: ").strip()
            user_id = input("Enter your ID: ").strip()
            
            season_query = '''
            SELECT id FROM seasons WHERE id = %s
            '''
            season_result = execute_query(season_query, (season_id,), fetch='one')
            
            if season_result:
                user_query = '''
                SELECT id FROM users WHERE id = %s
                '''
                user_result = execute_query(user_query, (user_id,), fetch='one')
                
                if user_result:
                    name = input("Enter application name: ").strip()
                    description = input("Enter application description: ").strip()
                    
                    application_query = '''
                    INSERT INTO applications (name, description, season_id, user_id) 
                    VALUES (%s, %s, %s, %s)
                    '''
                    execute_query(application_query, (name, description, season_id, user_id))
                    print("Application submitted successfully!")
                    return True
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False
                

    @log_decorator
    def vote_for_tender(self):
        """Vote for a tender in the database"""
        try:
            select_user = '''
            SELECT id FROM users WHERE status = True
            '''
            user_result = execute_query(select_user, fetch='one')
            
            if user_result:
                user_id = user_result['id']  
            
                
                season_id = input("Enter season ID: ").strip()
                tender_id = input("Enter tender ID: ").strip()

                tender_query = '''
                SELECT * FROM tenders WHERE id = %s AND season_id = %s
                '''
                tender_result = execute_query(tender_query, (tender_id, season_id), fetch='one') 
                
                if tender_result:
                    vote_query = '''
                    INSERT INTO votes (season_id, tender_id, user_id) 
                    VALUES (%s, %s, %s)
                    '''
                    execute_query(vote_query, (season_id, tender_id, user_id)) 
                    print("Vote submitted successfully!")
                    return True
                else:
                    print("Tender not found or your vote already exists.")
                    return False
            else:
                print("No active user found.")
                return False
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False

