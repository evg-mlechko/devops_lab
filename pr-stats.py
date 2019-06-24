#!/usr/bin/env python
import requests
import datetime
import calendar
import argparse

ap = argparse.ArgumentParser(description='Easy way to get info about PR:')

ap.add_argument("user", help="insert github username")
ap.add_argument("--repo", help="insert number of github pull-request")
ap.add_argument("--version", help="output version the app",
                action="store_true")
# , action="store_true"

args = ap.parse_args()

USERNAME = args.user
if args.version:
    print("Version 1.0.0")
    quit()

if args.repo:
    prNumber = args.repo
else:
    prNumber = '55'

user = "evg-mlechko"
token = 'b8945f269fcc212e085f149af3efe95290b16335'
url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls/%s' % prNumber
pulls = requests.get(url, auth=(user, token))
pullsjson = pulls.json()

jsondate = pullsjson["created_at"]
converted_created_at = datetime.datetime.strptime(jsondate,
                                                  "%Y-%m-%dT%H:%M:%SZ")

days_opened = datetime.datetime.now() - converted_created_at
print("Numbers of days opened: "+str(days_opened.days))

day_of_the_week = calendar.day_name[converted_created_at.weekday()]
print("Day of the week opened : " + day_of_the_week)

hour_of_the_day = converted_created_at.hour
print("Hour of the day opened: " + str(hour_of_the_day))

user_who_opened = pullsjson['user']['login']
print("User who opened: " + user_who_opened)
