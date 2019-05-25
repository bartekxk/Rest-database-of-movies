# Rest api for movies database implement in Django,
The application has three subpages

## /movies
We can add a movie by entering its title, the data will be downloaded from the website http://www.omdbapi.com/ . Then they are placed in the database with their own id. It is also checked if the movie exists in the database from which we collect the data.

## /comments
In the comments we can add a comment only to existing ones in the database. They are identified by the id number. Each added comment is validated in this respect. There is also an option to filter after movie id.

## /top
This is the ranking of added videos relative to added comments. We can also filter them against the release year of the movie. For example, /top?date_from=2000&date_to=2019.

A lot of live tests have been added in the app. For example, checking the date of filtering, the existence of a movie to which a comment or existence of a movie in the database from which the data is downloaded is added.
