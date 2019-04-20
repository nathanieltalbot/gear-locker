The program is hosted on Heroku, and can be accessed by navigating to https://nuhoc-gear-locker.herokuapp.com/. To view and manipulate the data in the database, you can connect directly to the Postgresql database via the command line. 
First, install postgresql on your local machine. If on Windows, the best bet is to run on the linux subsystem, see here: https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#0  
On Ubuntu linux, install postgresql by running sudo apt-get install postgresql postgresql-contrib
On Mac, see here: https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb

The Heroku CLI must be installed -- see this page https://devcenter.heroku.com/articles/heroku-cli . This works smoothest on Linux (or Linux on Windows) but can be done on any major platform. 

To connect to the database, open a terminal window and type in heroku pg:psql postgresql-acute-37734 --app nuhoc-gear-locker. 

When prompted, log in using the following credentials: 
Email: talbot.na@husky.neu.edu
Password: CS3200Database!

This should allow you to interact with the postgresql command line. To list tables, run the command \dt. 

To list data in tables, enter any standard SQL command (e.g. SELECT * FROM club_member;) and the result should be printed in the terminal. 

This data will update with operations performed on the website. 
