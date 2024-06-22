# # import sqlite3

# # # Function to establish a connection to the SQLite database
# # def connect_db():
# #     conn = sqlite3.connect('/Users/yaminshweyihtay/Downloads/nijisketchdata.db')
# #     return conn

# # # Function to insert a new reservation into the database
# # def insert_reservation(guest_name, guest_phone, guest_email, reservation_date, reservation_time, num_guests, special_requests):
# #     conn = connect_db()
# #     cursor = conn.cursor()
# #     cursor.execute("""
# #         INSERT INTO Reservation (guest_name, guest_phone, guest_email, reservation_date, reservation_time, num_guests, special_requests, reservation_status)
# #         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
# #     """, (guest_name, guest_phone, guest_email, reservation_date, reservation_time, num_guests, special_requests))
# #     conn.commit()
# #     conn.close()

# # # Function to retrieve all reservations from the database
# # def get_all_reservations():
# #     conn = connect_db()
# #     cursor = conn.cursor()
# #     cursor.execute("SELECT * FROM Reservation")
# #     reservations = cursor.fetchall()
# #     conn.close()
# #     return reservations







# # #test for using the database module
# # from databasenijisketch import insert_reservation, get_all_reservations

# # # Example usage: Insert a new reservation
# # insert_reservation('John Doe', '123-456-7890', 'johndoe@example.com', '2024-06-30', '19:00', 4, 'Window seat preferred')

# # # Example usage: Retrieve all reservations
# # reservations = get_all_reservations()
# # for reservation in reservations:
# #     print(reservation)




# import os

# # Print the absolute path of the database file
# print("Database file path:", os.path.abspath('/Users/yaminshweyihtay/Downloads/nijisketchdata.db'))



# import sqlite3
# import os

# # Function to establish a connection to the SQLite database
# def connect_db():
#     db_path = '/Users/yaminshweyihtay/Downloads/nijisketchdata.db'
    
#     # Check if database file exists
#     if not os.path.exists(db_path):
#         print(f"Database file '{db_path}' does not exist.")
#         return None
    
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
    
#     try:
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS Reservation (
#                 id INTEGER PRIMARY KEY,
#                 guest_name TEXT,
#                 guest_phone TEXT,
#                 guest_email TEXT,
#                 reservation_date TEXT,
#                 reservation_time TEXT,
#                 num_guests INTEGER,
#                 special_requests TEXT,
#                 reservation_status TEXT DEFAULT 'Pending'
#             )
#         ''')
#         conn.commit()
#         print("Connected to SQLite database.")
#         return conn
#     except sqlite3.Error as e:
#         print(f"Error creating table: {e}")
#         return None



# #testing the connection 
# from databasenijisketch import insert_reservation, get_all_reservations

# if __name__ == "__main__":
#     conn = connect_db()
#     if conn:
#         # Example usage: Insert a new reservation
#         insert_reservation(conn, 'John Doe', '123-456-7890', 'johndoe@example.com', '2024-06-30', '19:00', 4, 'Window seat preferred')

#         # Example usage: Retrieve all reservations
#         reservations = get_all_reservations(conn)
#         for reservation in reservations:
#             print(reservation)
        
#         conn.close()
#     else:
#         print("Database connection failed. Check database file path and permissions.")








# #restructured
# import sqlite3

# # Function to establish a connection to the SQLite database
# def connect_db():
#     conn = sqlite3.connect('/Users/yaminshweyihtay/Downloads/nijisketchdata.db')
#     return conn

# # Function to insert a new reservation into the database
# def insert_reservation(guest_name, guest_phone, guest_emailaddress, reservation_date, reservation_time, num_guests, special_requests, reservation_status='Pending'):
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("""
#         INSERT INTO Reservation (guest_name, guest_phone, guest_email, reservation_date, reservation_time, num_guests, special_requests, reservation_status)
#         VALUES ('Lyra', '123', 'sweet@example.com', '2024-06-30', '13:00', 5, 'Side' )
#     """, (guest_name, guest_phone, guest_emailaddress, reservation_date, reservation_time, num_guests, special_requests, reservation_status))
#     conn.commit()
#     conn.close()

# # Function to retrieve all reservations from the database
# def get_all_reservations():
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM Reservation")
#     reservations = cursor.fetchall()
#     conn.close()
#     return reservations


# #update main script 
# from databasenijisketch import insert_reservation, get_all_reservations

# if __name__ == "__main__":
#     # Example usage: Insert a new reservation
#     insert_reservation('John Doe', '123-456-7890', 'johndoe@example.com', '2024-06-30', '19:00', 4, 'Window seat preferred')

#     # Example usage: Retrieve all reservations
#     reservations = get_all_reservations()
#     for reservation in reservations:
#         print(reservation)
        
        







#-------



#Combined Code 
import sqlite3

# Function to establish a connection to the SQLite database
def connect_db():
    conn = sqlite3.connect('/Users/yaminshweyihtay/Downloads/nijisketchdata.db')
    return conn

# Function to insert a new reservation into the database
def insert_reservation(guest_name, guest_phone, guest_email, reservation_date, reservation_time, num_guests, special_requests):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Reservation (guest_name, guest_phone, guest_email, reservation_date, reservation_time, num_guests, special_requests)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (guest_name, guest_phone, guest_email, reservation_date, reservation_time, num_guests, special_requests))
    conn.commit()
    conn.close()

# Function to retrieve all reservations from the database
def get_all_reservations():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Reservation")
    reservations = cursor.fetchall()
    conn.close()
    return reservations

# # Main script to test the database functions
# if __name__ == "__main__":
#     # Example usage: Insert a new reservation
#     insert_reservation('sweet', '123-456-7890', 'johndoe@example.com', '2024-06-30', '19:00', 4)

#     # Example usage: Retrieve all reservations
#     reservations = get_all_reservations()
#     for reservation in reservations:
#         print(reservation)
