import os

from lib.utils.util_console_mgmt import cls


def demo_sqlite():
    import sqlite3

    # DB connection
    con = sqlite3.connect(rf"{os.getcwd()}\db\sql_db.db")  #:memory: - db in memory/ on the wing
    cur = con.cursor()  # Create cursor to operate on db
    while True:
        print("1. Create structure")
        print("2. Manage students")
        print("3. Manage course")
        user_input = input("Choose an option: ")
        match user_input:
            case "1":
                # Create tables
                sql_script_courses = """
                create table if not exists courses(
                    id integer primary key autoincrement,
                    name nvarchar(100) not null,
                    profile nvarchar(250)
                )
                """
                cur.execute(sql_script_courses)

                sql_script_students = """
                create table if not exists students(
                    id integer primary key autoincrement,
                    first_name nvarchar(100) not null,
                    last_name nvarchar(100),
                    course_id integer not null,
                    foreign key(course_id) references courses(id)
                )
                """
                cur.execute(sql_script_students)
                con.commit()  # Commit above db operations, without it DB will not be created
                cls()
            case "2":
                #Write code to add student
                user_input = input("Would you like to add student? \nY - yes \nN - no\n")
                if user_input == "Y" or user_input == "y":
                    print("Courses list: ")
                    cur.execute("select * from courses")
                    for k in cur.fetchall():
                        print(f"ID: {k[0]}, Name:{k[1]}, Profile:{k[2]}")
                    user_input_id = input("To which course ?: ")
                    user_input_fname = input("First name: ")
                    user_input_lname = input("Last name: ")
                    add_student_sql = f"""
                    insert into students(first_name, last_name, course_id)
                    values('{user_input_fname}', '{user_input_lname}', '{user_input_id}')
                    """
                    cur.execute(add_student_sql)
                    con.commit()
                    print(f"Student {user_input_fname} has been added...")

                user_input = input("Would you like to delete student? \nY - yes \nN - no\n")
                if user_input == "Y" or user_input == "y":
                    print("Students: ")
                    cur.execute("select id, first_name, last_name from students")
                    for k in cur.fetchall():
                        print(f"{k[0]}. {k[1]} {k[2]}")
                    user_input_delete = input("Which student would you like to remove (id): ")
                    remove_student_sql = f"""
                    delete from students
                    where id == '{user_input_delete}'
                    """
                    cur.execute(remove_student_sql)
                    con.commit()
                    print(f"Student has been removed...")
            case "3":
                print("Courses list: ")
                cur.execute("select * from courses")
                for k in cur.fetchall():
                    print(f"ID: {k[0]}, Name:{k[1]}, Profile:{k[2]}")

                user_input = input("Would you like to add course? \nY - yes \nN - no\n")
                if user_input == "Y" or user_input == "y":
                    course_name = input("Course name: ")
                    course_profile = input("Course profile: ")
                    add_course_sql = f"""
                    insert into courses(name, profile)
                    values('{course_name}', '{course_profile}')
                    """
                    cur.execute(add_course_sql)
                    con.commit()
                    print(f"Course {course_name} has been added...")
                cls()
            case _: break
    cls()


def demo_postgresql():
    import psycopg2
    try:
        con = psycopg2.connect("dbname='nazwa_bazy' user='user_name' password='user_password' host='localhost'")
        cur = con.cursor()
    except:
        print("Something went wrong.")