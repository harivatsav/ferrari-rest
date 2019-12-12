# docker-REST




A docker container running python flask environment shows a good RESTful web service example



Database is created in JSON which consists of ID, Name of different Ferrari cars, its  fastest time taken to reach from 0 to 100 , Engine specification, Top speed and the year when the cars where launched.

3 get routes:

First route displays all the records,

Second route displays the list of cars according to their year.

Third route shows the list of cars when selected according to their ID

GET request 1: Go to http://localhost:5000/getcars/  to list all records.                               

GET request 2: Go to http://localhost:5000/getcars/2015 to select a specific year 2015 for example         

GET request 3: Go to http://localhost:5000/getcars/2015/14 to select a specific car according to the ID.


To run in docker:

Build the image using command:
docker build -t flaskapp .

Run the Docker container using the command:
docker run -d -p 5000:5000 flaskapp


