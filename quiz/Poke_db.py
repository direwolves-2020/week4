import sqlite3


db = 'poke.db'

conn = sqlite3.connect(db)
c = conn.cursor()
conn.execute(
    """
    CREATE TABLE user (
        id INTEGER PRIMARY KEY,
        name TEXT
    );"""
)

conn.execute(
    """
    CREATE TABLE pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT,
        species_id INTEGER
    );""")

conn.execute(
    """
    CREATE TABLE user_pokemon_link(
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        pokemon_id INTEGER
    );""")

conn.execute(
    """
    CREATE TABLE pokemon_species(
        id INTEGER PRIMARY KEY,
        habitat TEXT,
        shape TEXT,
        color TEXT);""")
conn.commit()

#Seeding
c.execute(
    """
    INSERT INTO 
    user ('name')
    VALUES ('Ken')
    ;
    """
)
conn.commit()
