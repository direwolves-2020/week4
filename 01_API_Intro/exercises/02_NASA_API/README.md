NASA API
========

NASA has an API! For now, we're only worried about one part of it:
[NeoWs](https://api.nasa.gov/api.html#neows-swagger) -- the Near Earth
Object Web Service -- and specifically, `/rest/v1/neo/browse`.

##### Create a small MVC app.

* A user should be able to make the following choices:
* see the name of all potentially hazardous NEO's
* view details of the largest and smallest asteroids by estimated
  diameter
* view a list of every NEO by name and select to view details
* The model might just be a wrapper that builds a class from a single
API call.
* Do *not* spend all day on this. Terminal Trader is the single most
important exercise to prepare you for the assessment.
