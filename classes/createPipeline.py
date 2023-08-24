# python3.8.4
# inputs: gitlab, branch, createDev, createTest, createLive, projectName
# dependencies: createProject.py, createBranch.py
# created 24-aug-2023
# ref: https://docs.gitlab.com/ee/api/pipelines.html#create-a-new-pipeline

class Pipeline:

    def __init__(self, gitlab, branch, createDev, createTest, createLive, projectName):
        self.gitlab = gitlab
        self.branch = branch
        self.createDev = createDev
        self.createTest = createTest
        self.createLive = createLive
        self.projectName = projectName
        self.payload = { "ref": self.branch, "variables": [ {"key": "CREATE_DEV", "value": self.createDev}, {"key": "CREATE_TEST", "value": self.createTest}, {"key": "CREATE_LIVE", "value": self.createLive} ] }

    def __str__(self):
        return self.gitlab + self.projectName + "/169/pipeline"