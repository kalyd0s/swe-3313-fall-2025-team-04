## Environment Setup
What you need:
1. Install Python(Version 3.12 or 3.13)
   
The project should use a current version of Python
  - Python - [Official Link](https://www.python.org/downloads/)

Download the installer for
  - Windows(.exe)
  -  macOS(.pkg)
  - Linux(use package manager)
  
Important(Windows Only)
- Add Python to Path to avoid manual environment variable setup
  
    
2. Verify Installation
- Open a terminal and run: python --version and pip --version
  

3. Create a Project Directory
- Example: myproject/

4. Create a virtual environment

A virtual environment isolates all project-specific packages
- python- m venv .venv - this will create a folder called .venve in the project directory
  
5.  Activate the virtual environment
   - macOs/Linux( source .venv/bin/activate
   - Windows(.\venv/Scripts\activate

     After activation, the terminal prompt will appear as (.venv)
     
6. Install Flask
   - open terminal and run pip install flask
   - if the project includes a requirement.txt file then do pip install -r requirements.txt

7. Verify Flask Installation
- use python -c "import flask; print('Flask installed:', flask.version__)"

8. Run the application
- once dependencies are installed, the application can be launched with a standard .py file
  
 ---
 ## Database Setup

 The application uses SQLite database for data storage, inlcuding user accounts, administrator accounts, and inventory information
 
 1. Ensure Virtual Environment is active
Before running database commands, active the virtual environment:
  - macOS/Linux(.venv/bin/activate)
  - Windows(.\venv\Scripts\activate)
 
 2. Create a Database
    - The database file(app.db) is generated automatically
    - Run the database setup script: python init_db.py
  This performs the following:
    - Creates all required tables(Users Inventory,etc)
    - Loads seed data into each table
    - Inserts:
      -  1 user
      - 1 administrator (is_admin = True)
      - Inserts inventory records used by the application
        
  3. Seed data details
     
 - User Accounts:
  - Regular User:
    - username: "user1"
    - password: hashed passwprd stored in database
    - is_admin: False
  - Administrator:
    - username: "admin"
    - password: hashed password stored in database
    - is_admin: True
   
- Inventory:
  
  Examples include: 
   - Price
   - Product Name
   - Item ID
   
4. No Sales Orders Required
- Only users and inventory need to be preloaded
      
5. Verifying Database Configuration
- After running init_db.py, app.db should now exist
    
      
6. Application Database Usage
  - When the flask application run, it should automatically connect to the app.db using
    the connection settings in the configuration file(config.py) or in the flask app factory
---
## How to Start and Login
 - Step 1- Open a terminal (Use Terminal( macOS/Linux) or Command Prompt/ Powershell (Windows))
 - Step 2 - Navigate to the project directory
   - Example: Desktop/project
 - Step 3- Activate the virtual environment
   -  macOS/Linux (.venv/bin/activate)
   -  Windows (.\.venv\Scripts\activate)
   -  You must see (.venv) before continuing
 - Step 4 - Start the Flask application
   - run the main file.py
   - you should see Running on http:// 127.0.0.1:5000
 - Step 5 - Open the application in a browswer
   - Once the terminal shows that the flask is running, open the URL in any browser
   - http://localhost:5000 or if it uses a custom port, replace 5000 with that number
 - Step 6- Login Credentials
 - 
       
    
 
 






