# Timenye Design

This document outlines the initial design of the timenye platform and documents the initial ideas.
It is intended to be a guiding document, not a full specification. However, it may be updated to 
align with new ideas or changes in thinking. Always check in on what's in here as it will give a
good idea of what the platform is about or features we intend to have.


## Domain Model

### Users

Users in Timenye are people (and in other cases, machines e.g. bots, APIs) that authenticate onto the platform
and can perform various actions. Users have different roles depending on what functionality of feature they have
access to.

Initially, we will have the following roles:

- **superusers/admins** - super users manage and maintain the platform and all the data on it.
- **regular_user** - a regular user is interested in following sporting events, but doesn't necessarily play or participate as a player
- **player** - a player is a user who participates in sporting events either as an Individual or part of a team
- **team_manager** - a team manager manages a registered team on the platform, there must be atleast one team manager for each team
- **team_admin** - a team administrator role may be assigned to users to assist team managers in administrative duties like adding players.

### Teams

A Team is a grouping of Individuals that participates in atleast one sporting event. A Team must be registered and have
a unique name on the platform (we may have to look into the unique name issue across disciplines). A Team has one or more
players and atleast one Team Manager. A Team may be managed by Team Administrators.

### Sports

The timenye platform supports different sporting disciplines. A sport or sporting discipline may also have it's own charateristics
or rules based on how the sport is played. As such, the platform will allow superusers to customize the sports discipline, although
some elements will be coded into the system based on the understanding of global sporting rules and conventions.

Each sport MUST have it's own module to modularize the platform and isolate sports from each other. However, sports will be registered
in the database with an ID to enable referencing with other data models.

#### Sport: Football
TODO: write about football sport module here

#### Sport: Basketball
TODO: write about basketball sport module here

#### Sport: Netball
TODO: write about netball sport module here

#### Sport: Volleyball
TODO: write about volleyball sport module here
