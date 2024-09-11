from Database.db_settings import execute_query



def create_tables():
    Create_states_table = '''
CREATE TABLE IF NOT EXISTS states (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);'''


    Create_regions_table = '''
CREATE TABLE IF NOT EXISTS regions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    state_id INTEGER REFERENCES states(id)
);'''


    Create_districts_table = '''
CREATE TABLE IF NOT EXISTS districts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    region_id INTEGER REFERENCES regions(id),
    state_id INTEGER REFERENCES states(id)
);'''


    Create_users_table ='''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(255) NOT NULL UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    passport_info VARCHAR(100) NOT NULL UNIQUE,
    address TEXT,
    role VARCHAR(12) NOT NULL,
    status BOOLEAN DEFAULT FALSE
);'''


    Create_seasons_table ='''
CREATE TABLE IF NOT EXISTS season (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    status BOOLEAN DEFAULT FALSE
);'''


    Create_tenders_table ='''
CREATE TABLE IF NOT EXISTS tender (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users (id),
    district INTEGER REFERENCES districts(id),
    description TEXT,
    season_id INTEGER REFERENCES season(id),
    status BOOLEAN DEFAULT FALSE
);'''


    Create_votes_table =''' 
CREATE TABLE IF NOT EXISTS votes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    season_id INTEGER REFERENCES season(id),
    tender_id INTEGER REFERENCES tender(id)
);'''


    Create_offers_table = '''
CREATE TABLE IF NOT EXISTS offers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    status BOOLEAN DEFAULT FALSE,
    season_id INTEGER REFERENCES season(id),
    user_id INTEGER REFERENCES users(id)
);'''


    execute_query(Create_states_table)
    execute_query(Create_regions_table)
    execute_query(Create_districts_table)
    execute_query(Create_users_table)
    execute_query(Create_seasons_table)
    execute_query(Create_tenders_table)
    execute_query(Create_votes_table)
    execute_query(Create_offers_table)
