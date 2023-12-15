This app just a simple clone report application.
It has 3 types of report daily, weekly and monthly.

It uses celery to manipulate the type report, If that report pass some critical times.

to run it you need some setup :

- first fill up "SECRET_KEY" and "DEBUG" in settings.py
- activate you docker engine (I already setup compose-docker.yml for you)
- run Redis on port 6379
- create migrations folder
- run makemigrations and migrate 

see the result after week or month. 

Becuase of matter of time, i already check that for you.

good luck with this.