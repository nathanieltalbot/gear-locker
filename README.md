# NUHOC Gear Locker
###### A database management system for the NUHOC Gear Locker

## Technologies
The database is primarily constructed using Python, Flask, and Postgresql
To communicate with Postgresql, Python will use the SQLAlchemy library which allows for an object-oriented 'Pythonic' way of interacting with the database, as opposed to raw SQL statements in the Python code.

The project is hosted on Heroku and version controlled through GitHub

# Setup

### Environment Setup
(For more reference, see this post:
https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc)

Setup is assuming running the program on the Ubuntu command line. It has been tested on Ubuntu 14.04 running on the Windows subsystem but should work elsewhere

First, ensure that Python 3.5+ is installed, using `sudo apt-get python3`

Ensure that all requirements in requirements.txt are installed by the pip package manager (`pip install ...`)
Additionally, install python virtualenv using `pip install virtualenv`

Set up a directory for this (I called this gear-locker) (`mkdir gear-locker`) and move into it (`cd gear-locker`)

Set up a virtual environment here using `virtualenv env`

Activate this virtual environment using `source env/bin/activate`

### Git setup

Clone this repository into the directory you just created

### Database Setup with Postgresql
Install postgresql (`sudo apt-get install postgresql`)

Create the database with `sudo createdb gearLockerDB`

Check this had properly created with `psql -d gear-locker`

### Set up environment variables

Run `export APP_SETTINGS="config.DevelopmentConfig"`

Set up the database url using `export DATABASE_URL="postgresql:///localhost/gearLockerDB"`

Also add these to a file called .env. The file should look like this:

`export APP_SETTINGS="config.DevelopmentConfig"`
`export DATABASE_URL="postgresql:///localhost/gearLockerDB"`

### Migrate the database

run `python manage.py db init`
This will create a folder named `migrations` in the environment
Now run `python manage.py db migrate`
Which should add the table `club_member` to the database
Apply these migrations using `python manage.py db upgrade`

Check to see if these migrations were successful by logging into the database with `psql gearLockerDB` and running `\dt`

### Running the server
Run `python manage.py runserver`

Log onto `http://127.0.0.1:5000/add_member`. You should see an interface to add a member 

(more interfaces to come) 
