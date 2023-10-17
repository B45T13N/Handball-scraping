# database_connection_provider.py

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def create_connexion():
    try:
        connexion = mysql.connector.connect(
            host=os.getenv('DATABASE_HOST'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            database=os.getenv('DATABASE_NAME')
        )

        return connexion
    except Exception as e:
        print(f'Error: {e}')
        print('Error during the db connexion')

def close_connexion():
    if connexion:
        connexion.close()

create_connexion()