from Database.db_settings import execute_query



def create_tables():
    Create_states_table = '''
    CREATE TABLE IF NOT EXISTS states (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE NOT NULL
    );'''

    Create_regions_table = '''
    CREATE TABLE IF NOT EXISTS regions (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        state_id INT REFERENCES states(id) ON DELETE CASCADE,
        UNIQUE (name, state_id)
    );'''

    Create_districts_table = '''
    CREATE TABLE IF NOT EXISTS districts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        region_id INTEGER REFERENCES regions(id),
        UNIQUE (name, region_id)
    );'''

    Create_users_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(20),
        email VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        passport_info VARCHAR(100) UNIQUE NOT NULL,
        address TEXT,
        role VARCHAR(12) NOT NULL,
        status BOOLEAN DEFAULT FALSE
    );'''

    Create_seasons_table = '''
    CREATE TABLE IF NOT EXISTS seasons (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        start_date TIMESTAMP,
        end_date TIMESTAMP,
        status BOOLEAN DEFAULT FALSE
    );'''

    Create_tenders_table = '''
    CREATE TABLE IF NOT EXISTS tenders (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        description TEXT NOT NULL,
        district INTEGER REFERENCES districts(id),
        start_date TIMESTAMP,
        end_date TIMESTAMP,
        user_id INTEGER REFERENCES users(id),
        season_id INTEGER REFERENCES seasons(id),
        status BOOLEAN DEFAULT FALSE
    );'''

    Create_votes_table = '''
    CREATE TABLE IF NOT EXISTS votes (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        season_id INTEGER REFERENCES seasons(id),
        tender_id INTEGER REFERENCES tenders(id),
        UNIQUE (user_id, season_id, tender_id)
    );'''


    Create_applications_table = '''
   CREATE TABLE IF NOT EXISTS applications (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    status BOOLEAN DEFAULT FALSE,
    season_id INTEGER REFERENCES seasons(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);'''




    execute_query(Create_states_table)
    execute_query(Create_regions_table)
    execute_query(Create_districts_table)
    execute_query(Create_users_table)
    execute_query(Create_seasons_table)
    execute_query(Create_tenders_table)
    execute_query(Create_votes_table)
    execute_query(Create_applications_table)
