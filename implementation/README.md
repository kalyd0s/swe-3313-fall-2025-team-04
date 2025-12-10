## Environment Setup
What you need:
1. Install Python(Version 3.13)
   
The project should use a current version of Python
  - Python - [Official Link](https://www.python.org/downloads/)

Download the installer:
  - Windows(.exe)
  -  macOS(.pkg)
  - Linux(use package manager)
  
Important(Windows Only)
- Click "Python to Path" during installation
  
    
2. Verify Python Installation
- Open the terminal and type:

  - Windows:
       - "python --version"
       - "pip --version"
  - MacOs:
       - python3 --version
       - pip3 --version
         
   You do not need to download Flask because it is manually listed in our requirements.txt.

3. Run the application
- Once dependencies are installed, the application can be launched with a standard .py file. Please proceed to "How to Start and Login"
  
 ---
 ## Database Setup

 The application uses a SQLite database for data storage, inlcuding user accounts, administrator accounts, and inventory information
 
 1. Ensure Virtual Environment is active
Before running database commands, activate the virtual environment:
  - macOS/Linux: " .venv/bin/activate"
  - Windows: ".venv\Scripts\activate"
 
 2. Create a Database
    - The database file(app.db) is generated automatically
    - Run the database setup script: python init_db.py
      
  This performs the following:
    - Creates all required tables(Users, Inventory, and etc)
    - Loads seed data into each table
    - Inserts:
      -  1 user
      -  1 administrator (is_admin = True)
      - Inserts inventory records used by the application
        
  3. Seed data details
     
 - User Accounts:
  - Regular User:
    - username: "user1"
    - password: ""
    - is_admin: False
  - Administrator:
    - username: "admin"
    - password: "admin"
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
 - Step 1- Open the terminal --> Command + space ( macOS/Linux) 
 - Step 2 - Navigate to the project directory. For example, if it is saved to your desktop, paste the following into your terminal. 
   - cd ~/Desktop/"Big Bang Brokers"
   - For Windows, go to the project folder and open the command prompt from there
 - Step 3- Activate the virtual environment 
   -  macOS/Linux: "source .venv/bin/activate"
   -  Windows: ".\.venv\Scripts\activate" or ".\.venv\Scripts\activate.bat" if execution of scripts is disabled
   -  You must see (.venv) before continuing
 - Step 4 - Install the requirements.txt --> "pip3 install -r requirements.txt" 
 - Step 5 - Start the Flask application
   - run the main application: "python3 main.py"
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
    
 
 






