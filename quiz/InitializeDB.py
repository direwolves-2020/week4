import sqlite3

conn = sqlite3.connect('pokemon_database.db')

#creates user, pokemon, user_pokemon, species, and habitat tables

conn.execute (
    """
    CREATE TABLE IF NOT EXISTS user (
        username TEXT PRIMARY KEY,
        password TEXT
    );
    """   
)

conn.execute (
    """
    CREATE TABLE IF NOT EXISTS pokemon (
        pokemon_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pokemon_name TEXT,
        species_name TEXT,
        habitat_name TEXT,
        FOREIGN KEY(species_name) REFERENCES species(species_name),
        FOREIGN KEY(habitat_name) REFERENCES habitat(habitat_name)
    );
    """   
)

conn.execute (
    """
    CREATE TABLE IF NOT EXISTS user_pokemon (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pokemon_id INTEGER,
        username TEXT,
        FOREIGN KEY(pokemon_id) REFERENCES pokemon(pokemon_id),
        FOREIGN KEY(username) REFERENCES user(username)
    );
    """
)

conn.execute (
    """
    CREATE TABLE IF NOT EXISTS species (
        species_name TEXT PRIMARY KEY
    );
    """   
)

conn.execute (
    """
    CREATE TABLE IF NOT EXISTS habitat (
        habitat_name TEXT PRIMARY KEY 
    );
    """
)

conn.close()

