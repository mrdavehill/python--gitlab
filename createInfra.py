#!/usr/bin/python3
# python3.8.4
# inputs: everything
# dependencies: all
# created 23-aug-2023

import pytest
import requests
requests.packages.urllib3.disable_warnings()
from classes. import *
from classes.var import *
import json

@pytest.fixture(scope='session', autouse=True)
def projectToken():
    url = gitlab + "/1/pipeline?ref=main"
    authenticate = requests.post(url, headers={"PRIVATE-TOKEN": token}, verify=False)
    return authenticate.headers

def testCreateProject(projectToken):
    data = project.Project(gitlab, name, description, path, namespace_id)
    push = requests.post(data, data=json.dumps(data.payload), verify=False, headers=headers)
    assert push.status_code == 200

def testCreateBranch(projectToken):
    data = branch.Branch(gitlab, branch)
    push = requests.post(data, data=json.dumps(data.payload), verify=False, headers=headers)
    assert push.status_code == 200

def testCreatePipeline(projectToken):
    data = pipeline.Pipeline(gitlab, branch, createDev, createTest, createLive, projectName)
    push = requests.post(data, data=json.dumps(data.payload), verify=False, headers=headers)
    assert push.status_code == 200