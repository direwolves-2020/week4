import sqlite3
from Model import Pokemon, PokeAPI


conn = sqlite3.connect('pokemon_database.db')
c = conn.cursor()

c.execute(
    """DELETE FROM user 
    """
)

c.execute(
    """ INSERT INTO user (username, password) 
        VALUES ('judith', 'pwd'), ('shlomo', 'pwd');
    """
)

conn.commit()
c.close()

print("Tables seeded")