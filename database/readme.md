### if __name__ == "__main__":
Run the code below ONLY if I run this file directly
If you run:
### python db_manager.py
👉This condition becomes TRUE
👉So code inside runs ✅

If you import this file in another file:
### from database.db_manager import connect_db
👉 Then it becomes FALSE
👉 Code inside will NOT run ❌

### conn = connect_db()
👉 Call your function
👉 Try to connect to MySQL
👉 Store result in conn

### if conn:
👉 Means:
If connection is successful → conn is NOT empty → TRUE ✅
If failed → conn = None → FALSE ❌