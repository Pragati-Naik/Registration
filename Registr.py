import mysql.connector

# Connect to MySQL
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pragati07@",
        database="reg"
    )

# Create (Insert) operation
def create_record(name, email, phone_number, dob):
    try:
        conn = connect()
        cursor = conn.cursor()
        insertQuery = "INSERT INTO Registration (Name, Email, PhoneNumber, DateOfBirth) VALUES (%s, %s, %s, %s)"
        values = (name, email, phone_number, dob)
        cursor.execute(insertQuery, values)
        conn.commit()
        print("Record created successfully.")
    except mysql.connector.Error as e:
        print(f"Error creating record: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Read operation for a specific record
def read_record(record_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        selectQuery = "SELECT * FROM Registration WHERE ID = %s"
        cursor.execute(sql, (record_id,))
        row = cursor.fetchone()

        if row:
            print(row)
        else:
            print(f"No record found with ID: {record_id}")

    except mysql.connector.Error as e:
        print(f"Error reading record: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


# Read operation
def read_records():
    try:
        conn = connect()
        cursor = conn.cursor()
        selectAllQuery = "SELECT * FROM Registration"
        cursor.execute(selectAllQuery)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except mysql.connector.Error as e:
        print(f"Error reading records: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Update operation
def update_record(record_id, new_name, new_phone_number):
    try:
        conn = connect()
        cursor = conn.cursor()
        updateQuery = "UPDATE Registration SET Name = %s, PhoneNumber = %s WHERE ID = %s"
        values = (new_name, new_phone_number, record_id)
        cursor.execute(updateQuery, values)
        conn.commit()
        print("Record updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error updating record: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Delete operation
def delete_record(record_id):
    try:
        conn = connect()
        cursor = conn.cursor()
        deleteQuery = "DELETE FROM Registration WHERE ID = %s"
        cursor.execute(deleteQuery, (record_id,))
        conn.commit()
        print("Record deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error deleting record: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Example with phone number
create_record("Pragati Naik", "pragati@gmail.com", "9874563210", "2000-04-09")
# update_record(1, "naik Pragati", "9876543210")
# delete_record(1)
