import psycopg2

def establish_connection():
    url="localhost",
    database="Real Estate", 
    username="postgres",            
    password="BDLV25",
    port=5432

    try:
        conn = psycopg2.connect(
            host=url, database=database, user=username, password=password, port=port
        )
        print("Connected to PostgreSQL database.")
        conn.close()
    except Exception as e:
        print("An error occurred: ", e)

