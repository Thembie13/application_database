<<<<<<< HEAD
print("Start code")
from flask import Flask
import psycopg2

app = Flask(__name__)
# --- Database Connection ---
def get_connection():
    return psycopg2.connect(
        url="localhost",
        database="Real Estate",  # Replace with your database name
        user="postgres",            # Replace with your PostgreSQL username
        password="BDLV25",     # Replace with your password
        port=5432
    )
# --- Register Users --- 
def register_user(email_address, name, address_id, preferred_location, is_agent=False, agent_info=None, is_renter=False, renter_preference=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (email_address, name, address_id, preferred_location)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (email_address) DO NOTHING;
        """, (email_address, name, address_id, preferred_location))

        if is_agent and agent_info:
            cursor.execute("""
                INSERT INTO agent (email_address, job_title, agency, contact_info)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (email_address) DO NOTHING;
            """, (email_address, agent_info))

        if is_renter and renter_preference:
            cursor.execute("""
                INSERT INTO renter (email_address, renter_preference)
                VALUES (%s, %s)
                ON CONFLICT (email_address) DO NOTHING;
            """, (email_address, renter_preference))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

# --- Add Addresses ---
def add_address(address_id, street, city, state, zip_code):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO address (address_id, street, city, state, zip_code)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (address_id) DO NOTHING;
        """, (address_id, street, city, state, zip_code))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

# --- Add Credit Card ---
def add_credit_card(card_number, expiry_date, payment_address, email_address):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO credit_card (card_number, expiry_date, payment_address, email_address)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (card_number) DO NOTHING;
        """, (card_number, expiry_date, payment_address, email_address))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
=======
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
>>>>>>> acec715239678a94a398eea0a428db06fd8dfbe4

