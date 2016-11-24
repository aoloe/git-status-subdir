#!/usr/bin/python

import os

from dulwich.repo import Repo
from dulwich import porcelain as git



current_path = '/home/ale/src'
# current_path = os.getcwd()
if not current_path.endswith(os.sep):
        current_path = current_path + os.sep

print(current_path)

# print os.walk(current_path).next()[1]

def get_repositories(current_path) :
    repositories = {}
    for directory in os.walk(current_path).next()[1] :
        repository_path = current_path+directory+'/'
        if os.path.isdir(repository_path+'.git') :
            repositories[directory] = repository_path
    return repositories

# repositories = get_repositories(current_path)

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


directories = get_immediate_subdirectories(current_path)

for item in directories :
    print(item)
    path = os.path.join(current_path, item)
    print(path)
    if os.path.isdir(os.path.join(path, '.git')):
        r = Repo(path)
        print(git.status(r))
