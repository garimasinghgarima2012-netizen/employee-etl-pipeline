import mysql.connector

DB_CONFIG = {
    
    'host': "127.0.0.1",
    'port': 3306,
    'database':'etl',
    'user': 'root',
    'password':'Password'
}

def get_connection():
    try:
      con=mysql.connector.connect(**DB_CONFIG)
      if con.is_connected():
          print("Database connected successfully")
          return con
      
    except Exception as e:
        print("error",e)
        
if __name__== "__main__":
    get_connection()