import threading
from Database.db_settings import execute_query
from Decorator.decorator import log_decorator


class Vote:
    @log_decorator
    def get_active_tenders():

        """Get all active tenders in the database"""

        tender_query = '''
        SELECT id, name, description, season_id , status FROM tenders WHERE status = 'True'
        '''
        return execute_query(tender_query)


    def get_active_seasons():

        """Get all active seasons in the database"""

        season_query = '''
        SELECT id, name,  status FROM seasons WHERE status = 'True'
        '''
        return execute_query(season_query)


    @log_decorator
    def vote_for_tender(self):

        """Vote for a tender in the database"""

        try:
            season_id = input("Season ID: ").strip()
            tender_id = input("Tender ID: ").strip()

            tender_query = '''
            SELECT * FROM tenders WHERE id = %s AND season_id = %s
            '''
            tender_query = execute_query(tender_query, (tender_id, season_id))
            if tender_query:
                vote_query = '''
                INSERT INTO votes (season_id, tender_id) VALUES (%s, %s)
                '''
                threading.Thread(execute_query, args=(vote_query, (tender_query,))).start()
                print("Vote submitted successfully!")
                return True
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False
        
    @log_decorator
    def send_application():

        """Send an application for a tender in the database"""
        
        try:
            season_id = input("Enter season ID: ").strip()
            user_id = input("Enter your ID: ").strip()

            season_idd ='''
            SELECT id FROM seasons WHERE id = %s
            '''
            user_idd ='''
            SELECT id FROM users WHERE id = %s
            '''

            if season_id == season_idd and user_id == user_idd:
                name = input("Enter application name: ").strip()
                description = input("Enter application description: ").strip()

                tender_query = '''
                INSERT INTO applications (name, description, season_id, user_id) VALUES (%s, %s, %s, %s)
                '''
                threading.Thread(execute_query, args=(tender_query, (name, description, season_id, user_id))).start()
                print("Application submitted successfully!")
                return True
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False
        
    
