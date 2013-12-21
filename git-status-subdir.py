#!/usr/bin/python

import commands
import subprocess
import os
import sys


pr = subprocess.Popen( "/usr/bin/git status" , cwd = os.path.dirname( '/home/ale/docs/src/htdocs-get-github/' ), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr.communicate()

print "Error : " + str(error) 
print "out : " + str(out)

current_path = '/home/ale/docs/src'
# current_path = os.getcwd()
if not current_path.endswith(os.sep):
        current_path = current_path + os.sep

print current_path

# print os.walk(current_path).next()[1]

def get_repositories(current_path) :
    repositories = {}
    for directory in os.walk(current_path).next()[1] :
        repository_path = current_path+directory+'/'
        if os.path.isdir(repository_path+'.git') :
            repositories[directory] = repository_path
    return repositories

repositories = get_repositories(current_path)

#print repositories

def get_git_actions(repository_path) :
    pr = subprocess.Popen( "/usr/bin/git status --porcelain" , cwd = os.path.dirname( repository_path ), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
    (out, error) = pr.communicate()

    # print "Error : " + str(error) 
    # print "out : " + str(out)
    return str(out)


for key, value in repositories.iteritems() :
    actions = get_git_actions(value)
    if actions != "" :
        print ">>> "+key
        print actions
    # break
