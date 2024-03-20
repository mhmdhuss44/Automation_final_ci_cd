import json
import requests
from jira import JIRA

class APIWrapper:
    PATH_JSON = r"C:\Users\mhmdh\Desktop\ci_cd_end\automation_project_ci_cd\config_api.json"


    def __init__(self):
        self.token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzNDY5NTAzLCJqdGkiOiJmOTU5NTQwMjAzOGE0YzAxOWQzMjBmYWE1NGNkNDQyNSIsInVzZXJfaWQiOjh9.FZSD986Uk5xvLy7qN5USWy1gHh5EcYhW93fQBMh4XAo"
        self.response = None
        self.my_request = requests
        self.load_config()
        self.auth_jira = JIRA(basic_auth=('mhmdhuss44@gmail.com', self.token), options={'server': self.jira_url})

    def load_config(self):
        with open(self.PATH_JSON, 'r') as file:
            json_content = json.load(file)

        self.url = json_content.get('url')
        self.text = json_content.get('words')
        self.jira_url = json_content.get('jira_url')

    # def api_get_request(self, url, reqBody=None):
    #     headers = {'Authorization': f'Bearer {self.token}'}  # Add token to the headers
    #     self.response = self.my_request.get(url, headers=headers)
    #
    #     if self.response.ok:
    #         return self.response
    #     else:
    #         return self.response.status_code
    #
    # def api_post_request(self, url, reqBody):
    #     headers = {'Authorization': f'Bearer {self.token}'}  # Add token to the headers
    #     self.response = requests.post(url, json=reqBody, headers=headers)
    #     if self.response.ok:
    #         return self.response
    #     else:
    #         return self.response.status_code


    def api_patch_request(self, url, reqBody):
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1Zjk2YjIyZmI1YjlkMDU4YTFlYmNhMSIsInJvbGUiOiJVU0VSIiwicHJvdmlkZXIiOiJsb2NhbCIsImVtYWlsIjoibWhtZGh1c3M0NEBnbWFpbC5jb20iLCJleHRyYVVzZXJEYXRhIjp7ImFwcHMiOlsiZ2Z3Il19LCJjcmVhdGVkQXQiOjE3MTA4NDQ3NjYyMTksImlhdCI6MTcxMDg0NDc2Nn0.sF1arO_w-etp81SYVsGuS84V3nl-t761BX3ddKoSoos"
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
