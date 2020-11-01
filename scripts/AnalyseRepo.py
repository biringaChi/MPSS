import os
import requests
from github import Github
from pprint import pprint


g = Github(token)
# g = Github(token)
# repo = g.get_repo("biringaChi/PIF-Model")
# views = repo.get_views_traffic(per="day")
# starCount = repo.stargazers_count

# print(starCount)

for i, repo in enumerate(g.search_repositories("language:python")):
    print(repo)
    print("="*100)
    if i == 1000:
        break