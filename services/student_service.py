from database.db_manager import connect_db

#function to get all rows from table
def get_all_students():
    conn  = connect_db()        #connect to database
    cursor = conn.cursor()      #create cursor (used to run SQL)

    cursor.execute("SELECT * FROM students")     #run SQL query
    data = cursor.fetchall()                    #get all rows

    cursor.close()
    conn.close()

    return data

#function to add student
def add_student(name, age, course):
    conn = connect_db()
    cursor = conn.cursor()

    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    print("Student added successfully!")

#function to update student
def update_student(id, name, age, course):
    conn = connect_db()
    cursor = conn.cursor()

    query = "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s"  
    values = (name, age, course, id)

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    print("student update successfully!!")  

#function to delete
def delete_student(id):
    conn = connect_db()
    cursor = conn.cursor()

    query = "DELETE FROM students WHERE id=%s"    
    values = (id,)

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    print("Student deleted successfully!!!")

#student search by id
def student_search_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM students WHERE id=%s" 
    values = (id,)

    cursor.execute(query, values)
    data = cursor.fetchone()        #get result

    cursor.close()
    conn.close()  

    return data                    #return result