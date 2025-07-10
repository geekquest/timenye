from django.db import models

# Create your models here.

class User(models.User):
    pass 

class Player(models.User):
    name = None 
    position = None 
    user = None

class Team(models.Model):
    name = char()
    story = char()
    logo_url = char()
    cover_picture_url = char()
    city = None 
    district = None 
    stadium_ground_name = None 
    formally_registered = None 
    owner_name = None 
    head_coach = None
    created_by = User 
    pass 

class TeamMemberRole(enum):
    PLAYER = 'player'
    MANAGER = 'manager'
    OWNER = 'owner'
    TECHNICAL_STAFF = 'technical_staff'
    SUPPORT_STAFF = 'support_staff'

class TeamMember(models.Model):
    user = user()
    team = Team()
    role = TeamMemberRole

class Sport(models.Model):
    name = models.Character(unique=True)

class Venue(models.Model):
    name = char()
    lat = decimal()
    lng = decimal()

class ScheduledMatch(models.Model):
    home_team = Team()
    away_team = Team() 
    venue = Venue()
    scheduled_on = date() 
    start_at = time()
    duration_minutes = integer()
    is_played = bool()
    is_postponed = bool()