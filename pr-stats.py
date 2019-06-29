#!/usr/bin/env python
import requests
import datetime
import calendar
import argparse

ap = argparse.ArgumentParser(description='Easy way to get info about PR:')

ap.add_argument("user", help="insert github username")
ap.add_argument("--prnum", help="from which pr collect info")
ap.add_argument("--version", help="output version the app",
                action="store_true")
ap.add_argument('--token', help="insert token for login", type=str)
ap.add_argument('--days', help="how long (days) opened pr", action="store_true")
ap.add_argument('--day', help="Day of the week opened", action="store_true")
ap.add_argument('--hd', help="Hour of the day opened", action="store_true")
ap.add_argument('--who', help="User who opened", action="store_true")
args = ap.parse_args()

USERNAME = args.user
if args.version:
    print("Version 1.0.0")
    quit()

if args.prnum:
    prNumber = args.prnum
else:
    prNumber = '55'

user = "evg-mlechko"
token = args.token
url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls/%s' % prNumber
pulls = requests.get(url, auth=(user, token))
pullsjson = pulls.json()
jsondate = pullsjson["created_at"]
converted_created_at = datetime.datetime.strptime(jsondate,
                                                  "%Y-%m-%dT%H:%M:%SZ")
# Parameters
days_opened = datetime.datetime.now() - converted_created_at
day_of_the_week = calendar.day_name[converted_created_at.weekday()]
hour_of_the_day = converted_created_at.hour
user_who_opened = pullsjson['user']['login']

if args.days:
    print("Numbers of days opened: " + str(days_opened.days))
if args.day:
    print("Day of the week opened : " + day_of_the_week)
if args.hd:
    print("Hour of the day opened: " + str(hour_of_the_day))
if args.who:
    print("User who opened: " + user_who_opened)
