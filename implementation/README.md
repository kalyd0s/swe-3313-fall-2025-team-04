## Environment Setup
What you need:
1. Install Python(Version 3.13)
   
The project should use a current version of Python
  - Python - [Official Link](https://www.python.org/downloads/)

Download the installer for
  - Windows(.exe)
  -  macOS(.pkg)
  - Linux(use package manager)
  
Important(Windows Only)
- Add Python to Path to avoid manual environment variable setup
  
    
2. Verify Python Installation
- Open the terminal and type: "python3 --version" and "pip3 --version"
  

3. Create Directory
- Example: myproject/


4. Create a virtual environment(optional)

A virtual environment will isolate all project-specific packages
- python- m venv .venv - this will create a folder called .venv in the project directory
  
5.  Activate the virtual environment
   - macOs/Linux: "source .venv/bin/activate"
   - Windows: ".\venv/Scripts\activate"

     After activation, the terminal prompt will appear as (.venv)
     
6. Install Flask
   - open terminal and run pip3 install flask
   - if the project includes a requirement.txt file then type "pip3 install -r requirements.txt"

7. Verify Flask Installation
- use python -c "import flask; print('Flask installed:', flask.version__)"

8. Run the application
- once dependencies are installed, the application can be launched with a standard .py file
  
 ---
 ## Database Setup

 The application uses SQLite database for data storage, inlcuding user accounts, administrator accounts, and inventory information
 
 1. Ensure Virtual Environment is active
Before running database commands, active the virtual environment:
  - macOS/Linux: .venv/bin/activate
  - Windows: .\.venv\Scripts\activate
 
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
  - When the flask application runs, it should automatically connect to the app.db using
    the connection settings in the configuration file(config.py) or in the flask app factory
---
## How to Start and Login
 - Step 1- Open the terminal --> Command + space ( macOS/Linux) or Command Prompt/Powershell (Windows))
 - Step 2 - Navigate to the project directory. For example, if it is saved to your desktop, paste the following into your terminal.
   - cd ~/Desktop/"Big Bang Brokers"
 - Step 3- Activate the virtual environment 
   -  macOS/Linux: "source .venv/bin/activate"
   -  Windows: ".\.venv\Scripts\activate"
   -  You must see (.venv) before continuing
 - Step 4 - Install the requirements.txt --> pip3 install -r requirements.txt
 - Step 5 - Start the Flask application
   - run the main application: python3 main.py
   - If the server runs successfully, you should see a similar message like running on http:// 127.0.0.1:5000
 - Step 6 - Open the application in a browser
   - Once the terminal shows that flask is running, open the URL in any browser
   - Go to http:// localhost:5000 or http:// 127.0.0.1:5000. If it uses a custom port, replace 5000 with that number
 - Step 7- Login Credentials
   | Username | Password | Role           |
   |----------| ---------|----------------|
   | user1    | user123  | Regular User   |
   | admin    | admin    | Administrator  |

 - Step 8 -Shut down the application
  - To stop the flask server:
    - Return to the terminal running the application and press CTRL-C
   
   This will stop the application
   
--- 
## TroubleShooting
    
 
 






