import pandas as pd
from faker import Faker
from sys import argv
from connection import create_db_connection, Error
import random


global fake
fake = Faker(["pt_PT"])

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")



def populate_contact(connection):

    for i in range(1,31):
        name = fake.name()
        email = fake.email()
        phnumber = random.randint(910000000,969999999)

        execute_query(connection, f"INSERT INTO contact (idContact, name, email, phone) VALUES ('{i}', '{name}', '{email}', '{phnumber}')")



def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        return result
    except Error as err:
        print(f"Error: '{err}'")

# creating a connection
connection = create_db_connection("localhost", "root", argv[1], "dorlux")


populate_contact(connection)

