# Your Movie Database

##### Description

* Today you learned about apis. Now we're going to utilize a free non-key movie database. 
* Since IMDB does not have a free or open API, there is a service called "OMDB" which takes the data from IMDB and opens it to the public, well most of it anyway. 
* [OMDB API Documentation](http://omdbapi.com/)



##### Objective

* Build a terminal application utilizing the MVC pattern
* MVP:
	* A user should be able to search for a movie by title
	* If multiple movies appear then a list should populate with the title and year
	* A user should be able to choose which one from the list to view
	* When a single movie is populated it should show the title, year, director, cast, and plot
    * You should use the following strategy before you get started writing any code:
        * First, you should first write out your [User stories](https://www.mountaingoatsoftware.com/agile/user-stories).
        * Next, you should write out your [Pseudocode](http://programmers.stackexchange.com/questions/136292/what-is-pseudocode).
        * Last, you should sit down and write your code.
	
***NOTES***

* For this exercise the models file will hold the endpoints to talk to the OMDB API
* Since we do not have our own database this will NOT be a full CRUD application. 
* Instead you will only be using the `GET` HTTP Method 
* The OMDB documentation does not tell you the endpoint to get multiple results. Here it is

```
http://www.omdbapi.com/?s=
```
* Follow the `s=` with the title of the movie you want


##### Luxury Goals

* Have everything set up already? 
* Why don't you take it one step further and allow users to create an account
* After they log into the account they should have the ability to search movies as above, but also store their favorite movies to a sql database.
