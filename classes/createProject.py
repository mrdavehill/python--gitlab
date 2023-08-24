# python3.8.4
# inputs: gitlab, branch, name, description, path, namespace_id, template_project_id
# dependencies: 
# created 24-aug-2023
# ref: https://docs.gitlab.com/ee/api/projects.html#create-project

class Project:

    def __init__(self, gitlab, name, description, path, namespace_id, template_project_id):
        self.gitlab = gitlab
        self.name = name
        self.description = description
        self.path = path
        self.namespace_id = namespace_id
        self.template_project_id = template_project_id
        self.payload = {"name": self.name, "description": self.description, "path": self.path, "namespace_id": self.namespace_id, "initialize_with_readme": "false", "use_custom_template": "true", "template_project_id": self.template_project_id}

    def __str__(self):
        return self.gitlab