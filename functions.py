import mysql.connector as mysql
import time
from random import choice,randrange
from string import ascii_letters as alphabets

def new_user_id():
    user_id = ''
    for i in range(1):
        user_id += (choice(alphabets).upper())
    for i in range(3):
        user_id += str(randrange(0,10))
    return user_id    

#DONE
def create_connection():
    connect = mysql.connect(host = 'localhost', user = 'root', passwd = 'tiger', db = 'couriers')
    return connect

#DONE
def create_tables(connect):
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS packages (id varchar(80) PRIMARY KEY, sender char(80), recipient char(80), address varchar(80), weight float(3,1), date_of_delivery date, delivery_status char(80), delivery_boy_id varchar(80))')
    cursor.execute('CREATE TABLE IF NOT EXISTS customers (id varchar(80) PRIMARY KEY, username char(80), password varchar(80))')
    cursor.execute('CREATE TABLE IF NOT EXISTS company (id varchar(80) PRIMARY KEY, username varchar(80), password varchar(80))')
    cursor.execute('CREATE TABLE IF NOT EXISTS courier_boys (id varchar(80) PRIMARY KEY, username varchar(80))')
    connect.commit()

#DONE
def existing_user_id(connect, username):
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM customers WHERE username = '{}'".format(username))
    ids = cursor.fetchone()
    id = ids[0]
    return id

#DONE
def update_user_id(connect, new_user_id, username):
    cursor = connect.cursor()
    cursor.execute("UPDATE customers SET id = '{}' WHERE username = '{}'".format(new_user_id, username))
    connect.commit()

#DONE
def customer_add_package(connect, package):
    cursor = connect.cursor()
    cursor.execute("INSERT INTO packages (id, sender, recipient, address, weight, date_of_delivery, delivery_status, delivery_boy_id) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}','{}')".format(package[0], package[1], package[2], package[3], package[4], package[5], package[6], package[7]))
    connect.commit()

#DONE
def customer_get_package(connect, package_id):
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM packages WHERE id='{}'".format(package_id))
    return cursor.fetchone()

#DONE
def customer_get_all_package(connect, username):
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM PACKAGES WHERE sender = '{}'".format(username))
    return cursor.fetchall()

#DONE
def customer_update_package(connect, new_package):
    cursor = connect.cursor()
    cursor.execute("UPDATE packages SET id = '{}', sender='{}', recipient='{}', address='{}', weight='{}', date_of_delivery='{}', delivery_status='{}', delivery_boy_id='{}' WHERE id='{}'".format(new_package[0], new_package[1], new_package[2], new_package[3], new_package[4], new_package[5], new_package[6], new_package[7], new_package[0]))
    connect.commit()

#DONE
def customer_delete_package(connect, package_id):
    cursor = connect.cursor()
    cursor.execute("DELETE FROM packages WHERE id='{}'".format(package_id,))
    connect.commit()

#DONE
def add_customer(connect, customer):
    cursor = connect.cursor()
    cursor.execute("INSERT INTO customers VALUES ('{}', '{}', '{}')".format(customer[0], customer[1], customer[2]))
    connect.commit()

#DONE
def get_customer(connect, id):
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM customers WHERE id='{}'".format(id))
    return cursor.fetchone()

#DONE
def update_customer(connect, password, username):
    cursor = connect.cursor()
    cursor.execute("UPDATE customers SET password='{}' WHERE username='{}'".format(password, username))
    connect.commit()

#DONE
def delete_customer(connect, id):
    cursor = connect.cursor()
    cursor.execute("DELETE FROM customers WHERE id='{}'".format(id))
    connect.commit()

#DONE
def signup(connect):
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM customers WHERE username='{}'".format(username))
    customer = cursor.fetchone()
    user_id = new_user_id()
    for i in range(1):
        if customer is not None:
            print("Username is already taken.")
            break
    add_customer(connect, (user_id, username, password))
    print("Signup successful.")
    data = [user_id, username, password]
    return data

#DONE
def login(connect):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM customers WHERE username='{}' AND password='{}'".format(username, password))
    customer = cursor.fetchone()
    user_id = existing_user_id(connect, username)
    for i in range(1):
        if customer is None:
            print("Invalid login.")
            break
    return [user_id, username, password]

#DONE
def company_login():
    company_id = ''
    for i in range(1):
        company_id += (choice(alphabets).upper())
    for i in range(3):
        company_id += str(randrange(0,10))
    email_id = input("Enter your Email ID : ")
    password = input("Enter your Password: ")
    connect = create_connection()
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM company WHERE username='{}' AND password='{}'".format(email_id, password))
    company = cursor.fetchone()
    for i in range(1):
        if company is None:
            print("The credentials seemed wrong. Please try again.")
            select = "none"
            return select

#DONE
def display_all_data(connect):
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM packages WHERE delivery_status = 'NOT DELIVERED YET'")
    return cursor.fetchall()

#DONE
def display_id(connect):
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM packages;")
    return cursor.fetchall()

#DONE
def update_status(connect, id):
    cursor = connect.cursor()
    print("Enter (1) to change to ON THE WAY : \nEnter (2) to change to DELIVERED : ")
    ask = int(input("Enter you choice (1,2) : "))
    for i in range(1):
        if ask == 1:
            cursor.execute("UPDATE packages SET delivery_status = 'ON THE WAY' WHERE id = '{}'".format(id))
            connect.commit()
            print("Delivery status has been changed to ON THE WAY")
        elif ask == 2:
            cursor.execute("UPDATE packages SET delivery_status = 'DELIVERED' WHERE id = '{}'".format(id))
            connect.commit()
            print("Delivery status has been changed to DELIVERED")
        else:
            print("Enter a valid responsse")
            break

#DONE
def display_one_data(connect, id):
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM packages WHERE id = '{}'".format(id))
    data = cursor.fetchone()
    print("___________________________________________________________________________________")
    print(data[0],"is the ID of the package")
    print(data[1],"is the user name who send the package")
    print(data[2],"is the user who is gonna receive the package")
    print(data[3],"is the address to send the package")
    print(data[4],"is the weight of the package")
    print(data[5],"is the due date of the delivery of this package")
    print(data[6],"is the Delivery Status of the package")
    print("___________________________________________________________________________________")

#DONE
def company_delete_package(connect):
    cursor = connect.cursor()
    cursor.execute("DELETE FROM packages WHERE delivery_status='DELIVERED'")
    connect.commit()
    print("Delivered Orders are deleted")

def add_courier_boys_data(connect):
    cursor = connect.cursor()
    cursor.execute("INSERT INTO courier_boys VALUES ('AM12', 'Aman')")
    cursor.execute("INSERT INTO courier_boys VALUES ('VI12', 'Vivek')")
    cursor.execute("INSERT INTO courier_boys VALUES ('AS12', 'Ashok')")
    cursor.execute("INSERT INTO courier_boys VALUES ('HA12', 'Harsh')")
    cursor.execute("INSERT INTO courier_boys VALUES ('AA12', 'Aayush')")
    connect.commit()

def courier_boy_login(connect, user_id, user_name):
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM courier_boys WHERE id = '{}' AND username = '{}'".format(user_id, user_name))
    courier_boy = cursor.fetchone()
    for i in range(1):
        if courier_boy == None:
            print("Your Log-In details seems incorrect.\nPlease try again...")
            break

def courier_boy_packages(connect, user_id):
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM PACKAGES WHERE delivery_boy_id = '{}'".format(user_id))
    print("Here is your list of orders to complete")
    return cursor.fetchall()

def assign_boy_to_courier(connect, package_id, courier_boy_id):
    cursor = connect.cursor()
    cursor.execute("UPDATE packages, courier_boys SET packages.delivery_boy_id = courier_boys.id WHERE packages.id = '{}' and courier_boys.id = '{}'".format(package_id, courier_boy_id))
    connect.commit()
    print(courier_boy_id,'has been assigned the order',package_id)
