[![YK logo](organiser/static/img/yodaKode-sml.png)](https://github.com/roeszler) 

## MINI PROJECT - Organiser Application:
* GitHub: https://github.com/roeszler/organiser-flask-sqlalchemy
* Live App via Render: https://discos-diary.onrender.com/

## Summary:
This project applies Structured Query Language (SQL) to and from a test database following the Create, Read, Update, Delete (C.R.U.D) paradigm using primarily Python and a variety of plugins. 

It demonstrates the application of the highest layer of abstraction uses SQLAlchemy's full Object Relational Mapping (ORM) capabilities inc conjunction with the Flask framework with the Materialize CSS and Jinja template engines. This demonstrates the use of Python classes and objects, instead of using database tables and connections. 

Requirements include:
* click==8.1.3
* Flask==2.1.3
* Flask-SQLAlchemy==2.5.1
* psycopg2==2.9.3
* SQLAlchemy==1.4.39
* Werkzeug==2.1.2

and including:

* Jinja2==3.0.1
* MaterializeCss==1.0.0

### What is it?
The app is a simple contact organiser that extends into a task management app.
### What does it do?
* Sample CRUD functionality to a simple ElephantSQL database using SQLAlchemy
### How do you use it?
Create, Read, Update, Delete User details that include:
* ID
* Name
* Date of birth
* Gender (female, male, other)
* Profession

Using:
* Flask
* SLQAlchemy ORM,  (PostgreSQL Databases)
* Materialize frontend CSS framework


Outcomes:
* How to perform full CRUD functionality, which allows us to create, read, update, and delete items on our database. This will be done in the context of a Flask application with SLQAlchemy’s ORM.
* Create HTML-based user interfaces to demonstrate these CRUD calls in action.
* In the spirit of good user experience, we will style these interfaces using the Materialize frontend framework.

Install addons:
`$ pip3 install Flask-SQLAlchemy psycopg2`

Secrets:
`touch env.py`
`pip install -r requirements.txt`
``

etc...

### One to Many Relationship
Since each of our tasks need a category selected (a one-to-many relationship), one category can be applied to many different tasks, but one task cannot have many categories. 

The foreign key pointing to the specific category (category_id) uses `db.ForeignKey` so our database recognizes the relationship between the tables
and point to the ID from our Category class, and therefore we need to use lowercase `'category.id'` .

#### Note:
The `ondelete="CASCADE"` to function that once a category is deleted, it will perform a **cascading effect** and also delete any task linked to it.

`category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)`

### Current Bug:
2/3/23 Forgotten how to update the content of my modified table structure in models.py to be reflected on the ElephantSQL database that I have used. 
* `python manage.py makemigration && migrate` seems to be in my head, but that is a Django command… 
* I am about to try `flask --app flaskr init-db`, 
As it is kind-of working at the moment, I thought I would send it on through to the repo.
