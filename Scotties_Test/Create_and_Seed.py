import sqlite3

db = 'Pokemon'

conn = sqlite3.connect(db)
c = conn.cursor()

#Dropping tables if they exist for easy wiping/reseeding
#After tables are confirmed to not exist they are added

#Creating Users table
conn.execute(
    """
    DROP TABLE if exists USERS;
    """
)
conn.execute(
    """
    CREATE TABLE USERS(
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    );""")

#Creating Pokemon table
conn.execute(
    """
    DROP TABLE if exists POKEMON; 
    """
)
conn.execute(
    """
    CREATE TABLE POKEMON (
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        habitat TEXT 
    );""")

#Creating Users_Pokemon Table
conn.execute(
    """
    DROP TABLE if exists USERS_POKEMON; 
    """
)
conn.execute(
    """
    CREATE TABLE USERS_POKEMON (
        user_id INTEGER, 
        pokemon_id INTEGER, 
        CONSTRAINT USERS
                FOREIGN KEY (user_id)
                REFERENCES USERS (id)
        CONSTRAINT POKEMON
                FOREIGN KEY (pokemon_id)
                REFERENCES POKEMON (id)
    );""")


#Creating Types table
conn.execute(
    """
    DROP TABLE if exists TYPES; 
    """
)
conn.execute(
    """
    CREATE TABLE TYPES (
        id INTEGER PRIMARY KEY, 
        type TEXT 
    );""")


#Creating Pokemon_Types Table, initially there was only type_id (I would prefer this way)
#However when viewing pokemon I could not figure out a query that returned both types
#for pokemon with two types without creating a duplicate, ex below: 
"""
OUTPUT FOR ODDISH
(oddish, grassland, grass)
(oddish, grassland, poison)
DESIRED
(oddish, grassland, grass, poison)
"""
#I tried everything I could think of, if you have an idea on a SQL query that would accomplish
# the desired let me know, for now I am fine with how I made it because pokemon have a max of 2 types 
conn.execute(
    """
    DROP TABLE if exists POKEMON_TYPES; 
    """
)

conn.execute(
    """
    CREATE TABLE POKEMON_TYPES (
        pokemon_id INT, 
        type_id INT,
        type_id_2 INT, 
        CONSTRAINT TYPES
                FOREIGN KEY (type_id)
                REFERENCES TYPES (id)
        CONSTRAINT TYPES
                FOREIGN KEY (type_id_2)
                REFERENCES TYPES (id)
        CONSTRAINT POKEMON
                FOREIGN KEY (pokemon_id)
                REFERENCES POKEMON (id)
    );""")



conn.commit()
print("Tables created Successfully")

#Seeding 
users = ["scottie", "scottie1"]


conn.execute('DELETE FROM USERS')

for credentials in users: 
    conn.execute("""
            INSERT INTO USERS ('username', 'password') 
            VALUES (?,?)""", (users[0], users[1]))




conn.commit()
c.close()
conn.close()

print("Seeding Success")