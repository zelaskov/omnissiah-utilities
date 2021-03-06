import os

PATH = "../Documents/work/repositories"


def list_repositories():
    """
    lists all repositories in provided path
    """
    return sorted(os.listdir(PATH))


def open_project(repo):
    """
    opens the specific repository in VSC
    """
    return os.system(f'code {PATH}/{repo}')
