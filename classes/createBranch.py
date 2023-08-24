# python3.8.4
# inputs: gitlab, branch
# dependencies: createProject.py
# created 24-aug-2023
# ref: https://docs.gitlab.com/ee/api/branches.html#create-repository-branch

class Branch:

    def __init__(self, gitlab, branch):
        self.gitlab = gitlab
        self.branch = branch

    def __str__(self):
        return self.gitlab + "/5/repository/branches?branch=" + self.branch + "&ref=main"