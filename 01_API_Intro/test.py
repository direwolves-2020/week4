# import requests

# spell = requests.get("http://spell-buddy.herokuapp.com/api/spells?name=magic%20missile").json()

# print(spell)

# EXAMPLE CODE BELOW, NOT MEANT TO ACTUALLY WORK!!!

import requests

class Models:

	def __init__(self):
		pass

	def get_single_movie(self, movie_title):
		result = requests.get("http://omdb.com/api/?t={x}".format(x=movie_title)).json()

		if result != null:
			return result

	def get_db(self, movie):
		c.conn(db)
		x = c.execute("""
			SELECT * FROM movies WHERE title = ?;
			""",(movie,))

		result = c.fetchone
		return result





