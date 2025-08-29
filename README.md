# Timenye

This is a platform for organizing, recording, scheduling Social Sports events.
It is also a community project to help people get better acquianted with open source contributions, particularly Malawian developers.

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


## Getting Started

The following instructions should help you get the project on your local development environment to 
run or contribute to.

First clone the repository. If you just want to get it workin on your machine, use the following command :-

```sh
$ git clone https://github.com/geekquest/timenye.git 
```

Alternatively, Fork the repository to your account and use the following - this way you can
push changes to your fork and send in Pull Requests (PRs) to contribute to the project.

```sh
$ git clone git@github.com:<YourUsername>/timenye.git
```

If you are a member of the geekquest organization, you can use the following command instead of creating a Fork.

```sh
$ git clone git@github.com:geekquest/timenye.git
```

You should now have a repository/directory named `timenye` in which ever directory you ran the command in.

Next, you need to setup the Python development environment - we recommend using [`uv`](https://docs.astral.sh/uv) as it provides a single tool for a lot of Python dependency and project management.


The following commands should get the dependencies of the project installed locally:

```sh 
$ cd timenye

$ uv install
```
Next, you have to setup a Postgresql database - this project uses/recommends postgresql as the database. You will need the database to store information the Django app needs.

After creating your database, copy the `.env.example` file to a new file `.env` and update
the configuration to match your created database

With that done, we can now run the migrations and run the server

```
$ uv run manage.py migrate

$ uv run manage.py runserver
```

### Updating the Look and Feel with Tailwind

This project uses tailwindcss via django-tailwind. In general, you will have to open a new terminal
and run the following to enable the tailwindcss pre-processor to pick-up changes you make to the 
templates

The first time you are setting up, you will need to start with this command - this command
will install dependencies (requires Node and npm to be installed) for tailwindcss to work.

```sh
$ uv run manage.py tailwind init
```

Every other time after the first/initial run you will only need to run

```sh

$ uv run manage.py tailwind dev
```


Please refer to the django-tailwind docs for 
more information.


## Design Notes

- Autocomplete hints and suggestions as a person is typing
- Linear Bandits algo for recommendation engine

## References

- https://github.com/HackSoftware/Django-Styleguide
- https://www.b-list.org/weblog/2020/mar/16/no-service/
- https://spookylukey.github.io/django-views-the-right-way/context-data.html
