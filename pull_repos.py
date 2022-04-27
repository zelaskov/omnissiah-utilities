import os

def download_repos(company):
    directory = company
    parent_dir = "../"    
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '%s' created" %directory)
    os.system(f"cd {path} && gh repo list {company} --limit 9999 --json url | jq '.[]|.url' | xargs -n1 git clone")
