from flask import Flask, request, jsonify, redirect, render_template
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        url="localhost",
        database="Real Estate",  
        user="postgres",            
        password="BDLV25",     
        port=5432
    )

#method requirements
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


def add_address(address_id, street, city, state, zip_code):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO address (address_id, street, city, state, zip_code) VALUES (%s, %s, %s, %s, %s)", (address_id, street, city, state, zip_code))
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def add_credit_card(card_number, expiry_date, payment_address, email_address):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO credit_card (card_number, expiry_date, payment_address, email_address) VALUES (%s, %s, %s, %s)", (card_number, expiry_date, payment_address, email_address))
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def add_neighborhood(neighborhood_id, crime_rates):
    conn = get_connection
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO neighborhood (neighborhood_id, crime_rates) VALUES (%s, %s)", (neighborhood_id, crime_rates))
        conn.commit()
    finally:
        cursor.close()
        conn.close()


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


def delete_property(property_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM modifies WHERE property_id = %s", (property_id,))
        cursor.execute("DELETE FROM property WHERE property_id = %s", (property_id,))
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

#flask routes

@app.route("/register_user", methods=["POST"])
def register_user_route():
    data = request.form
    email = data.get("email")
    name = data.get("name")
    role = data.get("role")

    is_agent = (role == "agent")
    is_renter = (role == "renter")

    try:
        register_user(
            email_address=email,
            name=name,
            address_id=None,
            preferred_location="N/A",
            is_agent=is_agent,
            agent_info=("Agent", "Generic Agency", "123-456-7890") if is_agent else None,
            is_renter=is_renter,
            renter_preference="Quiet" if is_renter else None
        )
        return redirect("/login")
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/login", methods=["POST"])
def login():
    data = request.form
    email = data.get("email")
    password = data.get("password")  # Password is not implemented yet
    role = data.get("role")

    # TODO: Implement actual login validation logic
    return redirect("/dashboard.html")

from flask import render_template

@app.route("/search_properties", methods=["GET"])
def search_properties_route():
    location = request.args.get("location")
    max_price = request.args.get("max_price", type=float)
    min_rooms = request.args.get("number_of_rooms", type=int)
    available = request.args.get("availability", "true").lower() == "true"

    try:
        results = search_properties(location, max_price, min_rooms, available)
        return render_template("search_results.html", properties=results)
    except Exception as e:
        return render_template("search_results.html", properties=[], error=str(e))

@app.route("/property/add", methods=["POST"])
def add_property_route():
    data = request.json
    try:
        add_property(
            data["property_id"], data["type"], data["location"], data["description"],
            data["price"], data["availability"], data["square_footage"],
            data["number_of_rooms"], data["building_type"], data["business_type"],
            data["neighborhood_id"], data["agent_email"]
        )
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/property/modify", methods=["PUT"])
def modify_property_route():
    data = request.json
    try:
        modify_property(data["property_id"], data["field"], data["new_value"])
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/property/delete/<property_id>", methods=["DELETE"])
def delete_property_route(property_id):
    try:
        delete_property(property_id)
        return jsonify({"status": "deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/booking", methods=["POST"])
def book_property_route():
    data = request.json
    try:
        book_property(
            data["booking_id"], data["start_date"], data["end_date"],
            data["total_cost"], data["card_number"], data["property_id"],
            data["email_address"]
        )
        return jsonify({"status": "booked"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

