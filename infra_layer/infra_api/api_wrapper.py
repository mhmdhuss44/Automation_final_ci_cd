import json
import os

import requests
from jira import JIRA

class APIWrapper:
    # PATH_JSON = r"C:\Users\mhmdh\Desktop\savedCi\Automation_final_ci_cd\config_api.json"
    PATH_JSON = r"config_api.json"


    def __init__(self):
        self.response = None
        self.my_request = requests
        self.load_config()
        self.token = os.environ.get('JIRA_TOKEN')
        self.auth_jira = JIRA(basic_auth=('mhmdhuss44@gmail.com', self.token), options={'server': self.jira_url})

    def load_config(self):
        with open(self.PATH_JSON, 'r') as file:
            json_content = json.load(file)

        self.url = json_content.get('url')
        self.text = json_content.get('words')
        self.jira_url = json_content.get('jira_url')
        self.emailAdress = json_content.get('emailChrome')
        self.usr_id = json_content.get('userid')
        self.auth_path=json_content.get('auth_path')



    def api_get_request(self, url, reqBody=None):
        headers = {
            "Authorization": self.auth_path
        }
        self.response = self.my_request.get(url, headers=headers)

        if self.response.ok:
            return self.response
        else:
            return self.response.status_code


    def api_post_request(self, url, reqBody):
        headers = {
            "Authorization": self.auth_path
            # Add other headers if needed
        }
        self.response = requests.post(url, json=reqBody, headers=headers)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code


    def api_patch_request(self, url, reqBody):
        headers = {
            "Authorization": self.auth_path
            # Add other headers if needed
        }
        self.response = requests.patch(url, json=reqBody, headers=headers)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code


    def create_issue(self, summary, description, project_key, issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': f'failed test: {summary}',
            'description': description,
            'issuetype': {'name': issue_type},
        }
        new_issue = self.auth_jira.create_issue(fields=issue_dict)
        return new_issue.key
