# API Introduction Part 2

### Learning Objectives
***Students will be able to...***

* Make more request to an external api
* Wrap your request in Python methods and classes
* Register for a api key to use later(look at google api)

---
### Context 

* Everything on the internet revolves around data. How do we grab it? Where can we get it? What can we do with it? 

---
### Lessons

##### Part 1 - What are Wrappers

***Five Min Exercise***

* Read about [Wrapper Functions](https://en.wikipedia.org/wiki/Wrapper_function)

---

* A wrapper function is a subroutine in a software library whose main purpose is to call a second subroutine with little or no additional computation. 
* Did you like that wiki description?
* In human words, a wrapper function is making your code more effienct and DRY by `wrapping` it in a method we can invoke when we need it. 
* In terms of Python and APIs we want to `wrap` our api calls in a method so we don't have to fill our code repeating endpoints

##### Part 2 - API Limitations / API Keys

* There are so many APIs, some are free and others require payment
* You may also stumble upon an `API key` requirement
* API keys are used to limit who and how many requests can be made in a given time frame
* Some companies that have free APIs but require a key are Rotten Tomatoes, Twitter, Facebook, Google Maps, and many more. 
* Usually you will request a key. If and when provided you will have to use that key in your Endpoint call
* When you get a key to an API make sure to see if there are limitations and what those limitations are.

##### Part 3 - Gitignore and Environmental Variables

* If everybody gets a unique key how can we keep it safe so nobody steals it
* NEVER PUSH YOUR KEY TO GITHUB
* You can create a `gitignore` file and choose which files to not push to github
* You can also use Environmental Variables. 

***Five Min Exercise***

* In yesterdays folder, outside the OMDB folder make a new folder 
* Create a sqlite3 database in that folder
* Create a readme file and a py file
* Create a text file
* gitignore the text and database files
* push to github and see what happens

##### Part 4 - A Brief extension of RESTful Practices

***It may not make complete sense until next phase when we start building web applications that others can access***

* We know that we can employ RESTful practices to API operations following CRUD and HTTP Verbs
* Remember APIs are not only external. Your SQLite MVC applications should follow RESTful practices
* Six Restful Rules From [This Blog](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) and also the [REST Wiki](https://en.wikipedia.org/wiki/Representational_state_transfer#Uniform_interface)
    * Client-Server
    * Stateless
    * Cacheable
    * Layered System
    * Uniform Interface
    * Code on Demand
* The same endpoint can be used multiple times. The HTTP Verb / Method is important in telling the application what the type of request is

##### Resources


 - [Github Ignoring Files](https://help.github.com/articles/ignoring-files/)
 - [Miguel Grinberg RESTful API with Python and Flask](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
 - [REST Wiki](https://en.wikipedia.org/wiki/Representational_state_transfer#Uniform_interface)

