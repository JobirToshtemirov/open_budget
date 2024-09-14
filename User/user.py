import threading
from Database.db_settings import execute_query
from Decorator.decorator import log_decorator


class Vote:
    @log_decorator
    def get_active_tenders(self):

        """Get all active tenders in the database"""

        tender_query = '''
        SELECT id, name, description, season_id , status FROM tenders WHERE status = True
        '''
        return threading.Thread(target= execute_query(tender_query)).start()
        


    def get_active_seasons(self):

        """Get all active seasons in the database"""

        season_query = '''
        SELECT id, name, status FROM seasons WHERE status = 'True'
        '''
        return threading.Thread(target= execute_query(season_query)).start()


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
            
                
                season_id = input("Season ID: ").strip()
                tender_id = input("Tender ID: ").strip()

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

