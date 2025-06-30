# Timenye

This is a platform for organizing, recording, scheduling Social Sports events.
It is also a community project to help people get better acquianted with open source contributions, particularly Malawian devs.

> NOTE: It is a Work In Progress and still in discovery/idea phases

## The Idea

Timenye aims to help people manage information about social sporting events better and to provide a way for people who want to participate in such events to know more about them. It is mainly targeted at people who play or organize social sporting events such as football matches between teams, however, it could always evolve to managing more "professional" events too.

Anyways, the idea is that the platform will keep things like Team information, games results, player stats, etc.. Each team can have a manager, coach, owners, contacts etc.. 

Notifications will help alert people when there is a game, and request/schedule a game will enable teams to request games with each other easily as well as figure out if there could be scheduling issues.

## Stack

We will develop timenye as a Django application. The main reason for choosing Django is that it will enable us to have different apps for different sporting disciplines using Django's app modules approach sounds right.

* Python 3
* Django 4.x
* Django Rest Framework
* Bootstrap 5 as base CSS framework
* VueJS for some parts
* SQLite for the database
* Redis for cache
* Flutter 3.10+ for building the mobile app

## Installation Guide  
> NOTE: The installation already presume that you have  installed python and django in your machine Windows,Mac,Linx
### Folk and Cron the Repository
1. Folk the Reposiroty then Cron the repository into your device:
   ```bash
   git clone https://github.com/mHubmw/finalangathe.git](https://github.com/geekquest/timenye.git)
   cd Timenye
### Create and Activate Virtual Environment on Windows
2. Create a virtual environment to install all your depedencies for this project and activate it :
   ```bash
   python -m venv .venv
   .venv\Scripts\activate.bat
### Create and Activate Virtual Environment on Mac,Linux
3. Create a virtual environment to install all your depedencies for this project and activate it :
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

### Install Project Dependencies
4. install project dependencies which are in requirements.txt :
   ```bash
   pip install -r requirements.txt
### Download and Configure Database
5. Download Postgress Database and install in your Machine  using this link  :
   https://www.postgresql.org/download/
### Update .env file 
6. install project dependencies which are in requirements.txt :
   ```bash
   'DB_ENGINE': 'django.db.backends.postgresql',
   'DB_NAME': '',          # Your database name
   'DB_USER': 'postgres',      # Your database user (e.g., 'postgres')
   'DB_PASSWORD': '',   # The password you set (e.g., 'Lunar123#')
   'DB_HOST': 'localhost',     # Local server
   'DB_PORT': '5432',  # Default Postgres port

### Migrate Database 
7. Migrate our tables into our database  :
   ```bash
   python manage.py  migrate

 ### Migrate Database 
8. Start our django  application  :
   ```bash
   python manage.py  runserver    

## Design Notes

- Autocomplete hints and suggestions as a person is typing
- Linear Bandits algo for recommendation engine

## References

- https://github.com/HackSoftware/Django-Styleguide
- https://www.b-list.org/weblog/2020/mar/16/no-service/
- https://spookylukey.github.io/django-views-the-right-way/context-data.html
