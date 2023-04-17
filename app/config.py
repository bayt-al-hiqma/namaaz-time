import os

# Google Maps API key
API_KEY = 'your_api_key_here'

# MySQL database credentials
MYSQL_USER = 'your_username_here'
MYSQL_PASSWORD = 'your_password_here'
MYSQL_HOST = 'your_host_here'
MYSQL_DATABASE = 'your_database_here'

# Define the base directory of the application
basedir = os.path.abspath(os.path.dirname(__file__))

# Define the path to the instance folder
INSTANCE_DIR = os.path.join(basedir, '..', 'instance')

# Override any settings with the values in instance/config.py
try:
    app.config.from_pyfile('config.py', silent=True)
except FileNotFoundError:
    pass
