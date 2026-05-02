import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "8653",
            database = "student_db"
        )
        return conn

    except Exception as e:
        print("Error: ", e)
        return None


if __name__ == "__main__":
    conn = connect_db()

    if conn:
        print("✅ Connected successfully!")
        conn.close()
    else:
        print("❌ Connection failed")  