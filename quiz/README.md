# Quiz Week4


In the 'real world' one would usually be required to register an API key 
in order to use most web APIs. For the sake of simplicity and to avoid 
possible complications with registration, we will be using a website that
doesn't require registration;
https://pokeapi.co/

The API is:
http://pokeapi.co/api/v2/
or more precisely
http://pokeapi.co/api/v2/ {endpoint}

So for example, to get all the 'berry' items,
we hit the API:
`requests.get("http://pokeapi.co/api/v2/berry").json()`
And so on. Documentation is available at
https://pokeapi.co/docsv2/

We will be working with 3 endpoints:
http://pokeapi.co/api/v2/pokemon/{id or name} 

http://pokeapi.co/api/v2/pokemon-species/{id or name}

http://pokeapi.co/api/v2/pokemon-habitat/{id or name}

look these up in the docs.

Your assignment is to create a database with (at least) 4 tables
'user' 'pokemon' 'species' 'habitat'

create a seed.db file seeding at least one user,

The MVC should allow one to add users, add/delete pokemon belonging to a user,
and look up how many pokemon a user/users have, how many by species, and how many by habitat.
Read the docs carefully for the 3 endpoints, in addition to a foreign key
in the pokemon table pointing to user, you should think about how to configure
the other two tables in relation to pokemon table.
Is there a many-to-many relationship between any of the tables? If so, how to implement it.
The habitat endpoint includes a list of species that inhabit this habitat.
Does the species endpoint have the corresponding habitat data. What can you
say about the relationship between these two?
When a user adds a pokemon to their account, what other information needs to be updated so that the database contains all the relevant information.
In your logic, think of how to handle requests for non existent data
(trying to add a pokemon that doesn't exist). 
