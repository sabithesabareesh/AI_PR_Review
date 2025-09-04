import os
from github import Github

class GitHubUtils:
    def __init__(self): self.gh=Github(os.getenv("GH_TOKEN"))
    def get_pull_request_files(self,repo,pr): return [(f.filename,f.patch or "") for f in self.gh.get_repo(repo).get_pull(pr).get_files()]
    def comment_on_pr(self,repo,pr,text): self.gh.get_repo(repo).get_pull(pr).create_issue_comment(text)
    def merge_pr(self,repo,pr): return self.gh.get_repo(repo).get_pull(pr).merge()
    def add_labels(self,repo,pr,labels): self.gh.get_repo(repo).get_pull(pr).as_issue().add_to_labels(*labels)
