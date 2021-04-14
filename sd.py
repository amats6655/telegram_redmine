import time
from redminelib import Redmine
import auth

redmine = Redmine(auth.URL, key=auth.API)


def get_issue(place):
    if place == 'campus':
        issues = redmine.issue.filter(
            assigned_to_id=312,
            status='open',
            limit=5
        )
        return issues
    elif place == 'school':
        issues = redmine.issue.filter(
            assigned_to_id=14210,
            status='open',
            limit=5
        )
        return issues
    elif place == 'kcu':
        issues = redmine.issue.filter(
            assigned_to_id=17532,
            status='open',
            limit=5
        )
        return issues
    elif place == 'lyceum':
        issues = redmine.issue.filter(
            assigned_to_id=17853,
            status='open',
            limit=5
        )
        return issues


def search_issue(id):
    return redmine.issue.get(id)