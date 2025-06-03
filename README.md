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

## Design Notes

- Autocomplete hints and suggestions as a person is typing
- Linear Bandits algo for recommendation engine

## References

- https://github.com/HackSoftware/Django-Styleguide
- https://www.b-list.org/weblog/2020/mar/16/no-service/
- https://spookylukey.github.io/django-views-the-right-way/context-data.html
