#!/usr/bin/env python

from github import Github
#from git import Repo
import os
from events import Commit, Comment, ReviewComment
from operator import attrgetter

user = os.environ['GITHUB_USER']
password = os.environ['GITHUB_PASSWORD']
#repo_dir = "/Users/rporres/Work/git/src-d/infrastructure"

g = Github(user, password)
#repo = Repo(repo_dir)

prs = []
repo_fullname = 'src-d/infrastructure'
repo = g.get_repo(repo_fullname)
#for state in ['open', 'closed']:
#    events = []
#    for pull in repo.get_pulls(state):
pull = repo.get_pull(7)
events = []
events.extend([Commit(c) for c in pull.get_commits()])
events.extend([Comment(c) for c in pull.get_comments()])
events.extend([ReviewComment(r) for r in pull.get_review_comments()])

ordered = sorted(events, key=attrgetter('created_at'))

for event in ordered:
    print event
