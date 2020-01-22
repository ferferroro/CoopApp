# Cooperative Management Application

CoopApp is a web application. It is designed to handle basic Cooperative operations such as, house keeping of Funds, maintaining members along with contribution collection, maintaining borrowers and their loans.

While the initial design is to handle a Cooperative, this can also be used as a personal housekeeping app to monitor individuals that has a debts on you.

## Demo
Preview of CoopApp is deployed on Heroku.

Demo: [http://flaskcoopdemo.herokuapp.com/](http://flaskcoopdemo.herokuapp.com/)


Please take note that Heroku Postgres dev plan is limited to 10,000 rows. Please dont spam the demo :)

## Prerequisites

These are the stuffes you need in order for the CoopApp to run.

[Python 3.8](https://www.python.org/)

[Pipenv](https://pipenv-fork.readthedocs.io/en/latest/) -> [Tagalog video](https://www.youtube.com/watch?v=uRfUDbAj_50)

[PostgreSQL](https://www.postgresql.org/)


## Installation

####1. Clone the repository:

Open a terminal or a Gitbash

*You can Fork this repo to make a copy of your own in case you want to add functionaliy

Select a directory and clone this github repo, (*If you forked this repo clone your own version, so you can commit further changes*)

```
git clone https://github.com/ferferroro/CoopApp.git
```

####2.Install Requirements:

After cloning, make sure you are in the working directory or inside the CoopApp folder

```
cd CoopApp
```

This repo already has a Pipfile included so the simplest way to install requirements is by typing:

```
pipenv install
```

You should start to see the progress of the installation and the speed of installation is depending on your internet connection. 
*Note: that install command should activate/launch the virtual environment.*


####3. Setup the app configuration:

After installing requirements, you should create your OWN postgre database along with your OWN db credentials. * Dont worry about the table and fields, we'll run a migrations for it.*

```
up to you what you name it. e.g. your_db_name
```

Inside the CoopApp directory, open config.py and under DevConfig and change the values so the app will use your OWN database

```
SQLALCHEMY_DATABASE_URI = 'postgresql://your_db_username:your_db_pass@localhost/your_db_name'
```

Inside the CoopApp directory, open app.py and make sure you are using your DevConfig

```
app.config.from_object('config.DevConfig')
```

####4. Run Migrations:

Make sure the virual environment is still active then type:

```
flask db upgrade
```

####5. Reset the DB:

After Migrations, fields should be created. Now we should create a default 'dev/dev' account so we can login. Make sure the virual environment is stil active then type:

```
python fake.py
```

####6. All Set! Let's start running the CoopApp:

Make sure the virual environment is active then type:

```
python app.py
```

That should run the app on localhost port 5000, open a chrome browser and type. *From running fake.py - the default account should be username: dev and password: dev*

```
http://127.0.0.1:5000/
```


## Deployment

Nothing specific here, choose your own Server.

Unless you want to deploy a your own demo on Heroku, you can always contact me.

## Built With

* [Flask](https://www.palletsprojects.com/p/flask/) - The web framework used
* [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - ORM
* [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) - Migration
* [Flask Sijax](https://pythonhosted.org/Flask-Sijax/) - Manage Ajax requests
* [Flask WTF](https://flask-wtf.readthedocs.io/en/stable/) - HTML Forms handler
* [Flask Login](https://flask-login.readthedocs.io/en/latest/) - User session management
* [Sufee Admin](https://github.com/puikinsh/sufee-admin-dashboard) - UI made by [Colorlib](https://colorlib.com/)


## Author

* **Romel Fernando - [Buy me Coffee](https://www.paypal.com/paypalme2/ferferroro)**


## License

This project is licensed under the MIT License.

