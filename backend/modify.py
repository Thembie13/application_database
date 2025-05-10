from flask import Flask
import psycopg2

app = Flask(__name__)
# --- Database Connection ---
def get_connection():
    return psycopg2.connect(
        url="localhost",
        database="Real Estate",  
        user="postgres",            
        password="BDLV25",     
        port=5432
    )
# --- Register Users --- 
def register_user(email_address, name, address_id, preferred_location, is_agent=False, agent_info=None, is_renter=False, renter_preference=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (email_address, name, address_id, preferred_location) VALUES (%s, %s, %s, %s)", (email_address, name, address_id, preferred_location))

        if is_agent and agent_info:
            cursor.execute("INSERT INTO agent (email_address, job_title, agency, contact_info) VALUES (%s, %s, %s, %s)", (email_address, agent_info))

        if is_renter and renter_preference:
            cursor.execute("INSERT INTO renter (email_address, renter_preference) VALUES (%s, %s)", (email_address, renter_preference))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

# --- Add Addresses ---
def add_address(address_id, street, city, state, zip_code):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO address (address_id, street, city, state, zip_code) VALUES (%s, %s, %s, %s, %s)", (address_id, street, city, state, zip_code))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

# --- Add Credit Card ---
def add_credit_card(card_number, expiry_date, payment_address, email_address):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO credit_card (card_number, expiry_date, payment_address, email_address) VALUES (%s, %s, %s, %s)", (card_number, expiry_date, payment_address, email_address))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

# --- Add neighborhood ---
def add_neighborhood(neighborhood_id, crime_rates):
    conn = get_connection
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO neighborhood (neighborhood_id, crime_rates) VALUES (%s, %s)", (neighborhood_id, crime_rates))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

# --- Add nearby schools --- 
def add_nearby_school(neighborhood_id, school_name, crime_rates):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO nearby_schools (neighborhood_id, school_name, crime_rates) VALUES (%s, %s, %s)", (neighborhood_id, school_name, crime_rates))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
