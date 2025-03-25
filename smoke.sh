#! /bin/bash

# Smoke test for the infactory client



nf login
nf show-state

# These should list all projects, organizations, and teams
nf projects
nf organizations
nf teams

# This should show a selection prompt
nf project select
nf organization select
nf team select

# This should list the projects, organizations, and teams for the selected project, organization, and team
nf projects
nf organizations
nf teams

# This should show the current project, organization, and team
nf project show
nf organization show
nf team show
