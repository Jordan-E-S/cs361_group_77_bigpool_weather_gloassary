Oregon State CS361 Microservice: Weather Key Terms

Given a starting letter, the microservice will return a list of weather key terms that begin with that letter.
Given a weather key term, the microservice will return the definition of that term.

API Specification

Retrieve Key Terms by Letter

Request Example
GET http://replace-with-your-url/terms/?letter=A

Response Example in JSON
{
"letter": "A",
"terms": [
"ACID RAIN",
"ADIABATIC",
"ADVECTION",
"ADVISORY",
"AGL",
"AIR MASS",
"ALBEDO"
]
}

Retrieve Definition of a Key Term

Request Example
GET http://replace-with-your-url/definition/?term=BLIZZARD

Response Example in JSON
{
"term": "BLIZZARD",
"definition": "A storm lasting about 3 hours or longer with sustained winds of 35 mph or greater and blowing snow reducing visibility."
}
