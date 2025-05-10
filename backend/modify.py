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

def add_property(property_id, type, location, description, price, availability, square_footage, number_of_rooms, building_type, business_type, neighborhood_id, agent_email):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO property (property_id, type, location, description, price, availability, square_footage, number_of_rooms, building_type, business_type, neighborhood_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (property_id, type, location, description, price, availability, square_footage, number_of_rooms, building_type, business_type, neighborhood_id))
        
        cursor.execute("INSERT INTO modifies (email_address, property_id) VALUES (%s, %s)", (agent_email, property_id))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def modify_property(property_id, field, new_value):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = f"UPDATE property SET {field} = %s WHERE property_id = %s"
        cursor.execute(query, (new_value, property_id))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def search_properties(location=None, max_price=None, min_rooms=None, available_only=True):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM property WHERE 1=1"
        params = []

        if location:
            query += " AND location = %s"
            params.append(location)
        if max_price:
            query += " AND price <= %s"
            params.append(max_price)
        if min_rooms:
            query += " AND number_of_rooms >= %s"
            params.append(min_rooms)
        if available_only:
            query += " AND availability = TRUE"

        cursor.execute(query, tuple(params))
        results = cursor.fetchall()
        return results
    finally:
        cursor.close()
        conn.close()

def book_property(booking_id, start_date, end_date, total_cost, card_number, property_id, email_address):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO booking (booking_id, start_date, end_date, total_cost, card_number, property_id, email_address) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
            (booking_id, start_date, end_date, total_cost, card_number, property_id, email_address))

        cursor.execute("UPDATE property SET availability = FALSE WHERE property_id = %s", (property_id,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()