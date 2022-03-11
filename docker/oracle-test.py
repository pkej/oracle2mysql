# myscript.py
# Import os module
import os
# Import sys module
import sys
# Import Oracle library
import cx_Oracle

key_value = "OCI_HOME"
print("The value of", key_value, " is ", os.environ[key_value])




# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
connection = cx_Oracle.connect(user="hr", password="welcome",
                               dsn="localhost/orclpdb1")

cursor = connection.cursor()
cursor.execute("""
        SELECT first_name, last_name
        FROM employees
        WHERE department_id = :did AND employee_id > :eid""",
        did = 50,
        eid = 190)
for fname, lname in cursor:
    print("Values:", fname, lname)