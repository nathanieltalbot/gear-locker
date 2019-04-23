# NUHOC Gear Locker

## Purpose
The main purpose of this project was to create a working database of gear and members for [NUHOC](nuhoc.com), the outdoors club at Northeastern University. The club runs a gear locker, renting gear to students with an active membership, and needs to track the membership status of all of the members, as well as the rental and return status of all of its gear. This project, currently in the alpha stage (with a working proof of concept) aims to solve this issue. 

## Software used:
* Python3, mainly with the following libraries:
  * [Flask](http://flask.pocoo.org/), a micro web framework for small applications.
  * [SQLAlchemy](https://www.sqlalchemy.org/), an object-oriented framework for Python to natively interact with a SQL database.
* [Postgresql](https://www.postgresql.org/), an open-source, SQL-based, ACID compliant database well-suited for web applications.
* [Bootstrap](https://getbootstrap.com/) a flexible open-source HTML, CSS, and JS toolkit for web development.

**The project is currently hosted on Heroku and can be accessed at [nuhoc-gear-locker.herokuapp.com](nuhoc-gear-locker.herokuapp.com)**

## Attribution
A number of online resources were used to aid in the initial development of this project. The main resource was [this tutorial](https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc) which was invaluable in initial setup of Flask and Postgresql and deployment to Heroku. StackOverflow and the extensive SQLAlchemy documentation (see [this link](https://docs.sqlalchemy.org/en/13/orm/tutorial.html) for a good resource on the ORM capabilities of SQLAlchemy). 
