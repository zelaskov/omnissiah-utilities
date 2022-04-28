import os

PATH = "../Documents/work/repositories"


def list_repositories():
    """
    lists all repositories in provided path
    """
    return os.listdir(PATH)


def open_project(repo):
    """
    opens the concrete repository in VSC
    """
    return os.system(f'code {PATH}/{repo}')
