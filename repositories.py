import os

path = "../Documents/work/tmh/repositories"

def list_repositories():
    return os.listdir(path)

def open_project(repo):
    return os.system(f'code {path}/{repo}')
