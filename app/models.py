from django.db import models
from django.utils.translation import gettext_lazy as _

'''User model represents a user who will login to the platform'''
class User(models.Model):
    display_name = models.CharField(max_length=140)
    address = models.CharField(max_length=140, blank=True)
    email = models.CharField(max_length=200)
    password = models.TextField()

class Player(models.Model):
    profile_picture_url = models.TextField(blank=True) 
    cover_picture_url = models.TextField(blank=True)
    name = models.CharField(max_length=200) 
    position = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Team(models.Model):
    name = models.CharField(max_length=200)
    story = models.CharField(max_length=512, blank=True)
    logo_url = models.TextField(blank=True)
    cover_picture_url = models.TextField(blank=True)
    team_colors = models.CharField(max_length=64, blank=True)
    established_year = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
    stadium_ground_name = models.CharField(max_length=140, blank=True)
    formally_registered = models.BooleanField(default=False)
    owner_name = models.CharField(max_length=200, blank=True)
    head_coach = models.CharField(max_length=200, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class TeamMemberRole(models.TextChoices):
    PLAYER = "player", _("Player")
    MANAGER = "manager", _("Manager")
    OWNER = "owner", _("Owner")
    TECHNICAL_STAFF = "technical_staff", _("Technical Staff")
    SUPPORT_STAFF = "support_staff", _("Support Staff")

class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    role = models.CharField(choices=TeamMemberRole)

class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Venue(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(decimal_places=4,max_digits=8)
    lng = models.DecimalField(decimal_places=4,max_digits=8)

class ScheduledMatch(models.Model):
    home_team = models.ForeignKey(Team, related_name="home_team", on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name="away_team", on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING)
    scheduled_on = models.DateField()
    start_at = models.DateTimeField()
    duration_minutes = models.IntegerField(blank=True, null=True)
    is_played = models.BooleanField(default=False)
    is_postponed = models.BooleanField(default=False)
