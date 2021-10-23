import os
import dotenv

dotenv.load_dotenv('venv/.env')

server = os.environ['server']
port = os.environ['port']
database = os.environ['database']
user = os.environ['user']
password = os.environ['password']
