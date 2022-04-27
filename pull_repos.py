import os


def download_repos(company):
    """
    downloads all git repositories in github org
    """
    directory = company
    parent_dir = "../"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print(f"Directory {directory} created")
    os.system(f"cd {path} && gh repo list {company} \
             --limit 9999 --json url | jq '.[]|.url' | xargs -n1 git clone")
