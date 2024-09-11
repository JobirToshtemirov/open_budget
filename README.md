# open_budget

Python + PostgreSQL Terminal-Based Application
This is a terminal-based mini-project built using Python and PostgreSQL. It provides a simple interface for managing data through a command-line interface, with PostgreSQL as the underlying database. The project is a demonstration of basic CRUD (Create, Read, Update, Delete) operations, authentication, and role-based access control in a terminal environment.

Features
User Authentication (Admin and Regular users)
Admin can create and manage voting seasons.
Regular users can vote for neighborhoods (махалли) within cities and areas.
CRUD operations for managing data such as areas, cities, and neighborhoods.
PostgreSQL database integration with proper schema management.
Prerequisites
Before running this project, ensure you have the following installed:

Python 3.x
PostgreSQL
psycopg2 (Python PostgreSQL adapter)
You can install psycopg2 by running:

    pip install psycopg2
Installation
Clone the repository:
    git clone https://github.com/your-username/project-name.git
cd project-name
Set up PostgreSQL:
Create a new PostgreSQL database.
Modify the config.py file (or equivalent configuration file) with your PostgreSQL credentials.
Example:


    DB_HOST = "localhost"
    DB_NAME = "your_database"
    DB_USER = "your_username"
    DB_PASSWORD = "your_password"
Create database tables:
Run the provided SQL script to create the necessary tables.


    psql -U your_username -d your_database -f setup.sql
Install dependencies:
Use pip to install required Python libraries:


    pip install -r requirements.txt
Usage
Start the application:


    python main.py
Admin functionality:
Admin users can manage voting seasons and control data related to areas, cities, and neighborhoods.
Admins have full CRUD access to all relevant data.
User functionality:
Regular users can log in, view available voting seasons, and cast their vote for neighborhoods.
Database Structure
The PostgreSQL database includes the following tables:

Users: Stores information about users (admins and regular users).
Areas: Stores data about various areas.
Cities: Contains cities that belong to different areas.
Neighborhoods (Махалли): Represents the voting options where users can cast their vote.
Voting Seasons: Admins can manage seasons for voting events.
Votes: Tracks users' votes for neighborhoods during a voting season.
Contributing
Feel free to fork this repository and make your own contributions. If you find any bugs or have suggestions, please open an issue.

License
This project is licensed under the MIT License.