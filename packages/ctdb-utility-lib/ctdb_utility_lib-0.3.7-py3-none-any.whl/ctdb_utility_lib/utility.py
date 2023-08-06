import string
from xmlrpc.client import boolean
import psycopg2
import re
from datetime import datetime


def connect_to_db():
    """
    Connects to the database and returns a connection object.
    """
    return psycopg2.connect(
        database="Contact_Tracing_DB",
        user="postgres",
        password="password",
        host="34.134.212.102",
    )

# check email format
def valid_email_format(email: str) -> bool:
    regex = "^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$"

    return re.search(regex, email) != None

def valid_aspect_ratio_format(aspect_ratio: str) -> bool:

    width_length = aspect_ratio.split(":")

    return (
        len(width_length) == 2 and width_length[0].isnumeric() and width_length[1].isnumeric()
    )

def _execute_statement(conn, statement):
    """
    Executes a PSQL statement with a given connection.

    Returns a cursor with the response of the statement.
    """
    cursor = conn.cursor()
    cursor.execute(statement)
    conn.commit()

    return cursor

def get_room_aspect_ratio(room_id: str, conn) -> list:

    # run query to get aspect ratio for specified room
    cur = _execute_statement(
        conn, f"SELECT aspect_ratio FROM rooms WHERE room_id = '{room_id}'"
    )
    result = cur.fetchone()
    return result[0].split(":")


def add_personal_scan(scanner_email: str, scanned_email: str, conn):
    """
    Adds a personal scan entry to the personal_scan table.
    """
    if not (valid_email_format(scanner_email) and valid_email_format(scanned_email)):
        return -1

    cur_date = datetime.now()

    cur = _execute_statement(
        conn,
        f"INSERT INTO personal_scans (id, scanner_email, scanned_email, scan_time) VALUES (DEFAULT, '{scanner_email}', '{scanned_email}', TIMESTAMP '{cur_date}');",
    )

    return 0

# add a scan to the scans table in db
# returns error message in case of an invalid email format
# throws exception in case of error accessing db
def add_scan(email: str, room_id: str, x_pos: float, y_pos: float, conn):

    # Invalid email format
    if not valid_email_format(email):
        return -1

    # invalid position
    if x_pos < 0 or x_pos > 1 or y_pos < 0 or y_pos > 1:
        return -1
    
    #get aspect ratio
    aspect_ratio = get_room_aspect_ratio(room_id,conn)

    # create current datetime obj
    current_date_time = datetime.now()

    # add scan info to scans table
    cur = _execute_statement(
        conn,
        f"INSERT INTO scans (scan_id, person_email,scan_time,room_id,x_pos,y_pos) \
            VALUES (DEFAULT,'{email}',TIMESTAMP '{current_date_time}','{room_id}','{x_pos * float(aspect_ratio[0]) }','{y_pos * float(aspect_ratio[1])}')"
    )

    # success
    return 0

# retrieves scan info
# returns -1 if no match found
def get_scan(scan_id: int, conn):

    cur = _execute_statement(conn, f"SELECT * FROM scans WHERE scan_id = '{scan_id}'")

    result = cur.fetchone()

    cur.close()

    return result

# Checks if a person with the specified email exists in the people table
def exists_in_people(email: str, conn) -> bool:

    cur = _execute_statement(conn, f"SELECT EXISTS(SELECT 1 FROM PEOPLE WHERE email = '{email}')")
    
    result = cur.fetchone()
    
    return result[0]
    
# add person to people table
def add_person(first: str, last: str, id: int, conn):

    # generate email
    email = first + last + str(datetime.now().timestamp()) + "@fake.com"
    email = email.lower()

    # person exists in the people table
    if exists_in_people(email, conn):
        return None

    name = first + " " + last

    # add person info to people table
    cur = _execute_statement(
        conn,
        f"INSERT INTO PEOPLE (email,name,student_id) \
        VALUES ('{email}','{name}',{id})",
    )
    return email

# retrieves info for person with email from db
# returns -1 if no match found
def get_person(email: str, conn):

    cur = _execute_statement(conn, f"SELECT * FROM PEOPLE WHERE email = '{email}'")
    # person row
    result = cur.fetchone()

    return result[0]

# Checks if room with room_id already exists
def exists_in_rooms(room_id: str, conn):

    cur = _execute_statement(conn, f"SELECT EXISTS( SELECT 1 FROM ROOMS WHERE room_id = '{room_id}')")
    
    result = cur.fetchone()

    return result[0]
# add room entry to room table
def add_room(room_id: str, capacity: int, building_name: str, aspect_ratio:string, conn):

    if not (room_id and building_name and valid_aspect_ratio_format(aspect_ratio)):
        return -1

    # person exists in the people table
    if exists_in_rooms(room_id, conn):
        return -1

    # add room to rooms table
    cur = _execute_statement(
        conn,
        f"INSERT INTO ROOMS (room_id,capacity,building_name,aspect_ratio) \
        VALUES ('{room_id}','{capacity}','{building_name}','{aspect_ratio}')",
    )
    return 0

# retrieves room info
# returns -1 if no match found
def get_room(room_id: str, conn):

    cur = _execute_statement(conn, f"SELECT * FROM ROOMS WHERE room_id = '{room_id}'")
    # room row
    result = cur.fetchone()

    return result

# retrieves all users from people table
def get_all_users(conn):

    # execute query
    cur = _execute_statement(conn, f"SELECT * FROM PEOPLE")
    # rows
    result = cur.fetchall()

    return result
