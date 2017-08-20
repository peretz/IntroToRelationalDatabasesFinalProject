# Introduction To Relational Databases: Final Project - Swiss system tournament planner.

This project is based on Udacity's Introduction to Relational Databases final project. The objective
of this project is learning the key concepts around using a relational database (e.g. postgreSQL),
which include:

* *Principles* behind a relational database.
* *Common SQL commands* (e.g. CREATE, SELECT, INSERT INTO, UPDATE, DROP, DELETE, VIEW, ...)
* *Database schema design* and *normalization.*
* The *python DB-API* standard.

In order to learn these concepts, the project implements a [Swiss system tournament
planner](https://en.wikipedia.org/wiki/Swiss-system_tournament).

## File Structure.

There are three files in the tournament planner:

*tournament.sql:* Defines the database schema and some useful views. In addition, this
file is in charge of creating (or if needed re-creating) the database.

*tournament.py:* This file defines a set of functions to access the database. For example, you can find
functions to create, query and sort records in the database.

*tournament_test.py:* This file contains all the tests required to corroborate that the functions
and schema previously defined are properly implemented.

## Environtment setup.

We use a postgreSQL database to implement this project. An easy way to install the database and have
a different environment to work with without affecting our development environment is by using a
Vagrant Virtual Machine (VVM). In [this link,](https://www.udacity.com/wiki/ud197/install-vagrant) there
is a tutorial provided by Udacity on how to install the VVM.

## Run the tests.

Before actually running the tests, we need to set up the database. To set up the database, we need
to access the VVM and execute the command `psql`. This command opens a psql command line interface.
Inside the psql command line we need to execute the following command:

`\i tournament.sql`

This will create the database, the tables and the views needed to run the tournament.py script.

Once the command completes executing, we exit the psql command line by calling `\q`. This brings us
back to the linux command line. In this command line, we call the python *tournament_test.py* script.
This script will execute a series of tests in the database and the function defined in tournament.py module.
This corroborates that the database and module have been successfully implemented.

## Final thoughts.

Now you are ready to use the tournament.py module to plan your Swiss system tournament. For any
further questions, check Udacity's documentation for the project. The documentation can be found in
[here.](https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true)
