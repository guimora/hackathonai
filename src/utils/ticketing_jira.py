import os

from jira import JIRA

jira_connection = JIRA(
    basic_auth=(os.getenv("JIRA_EMAIL"), os.getenv("API_KEY")),
    server=os.getenv("JIRA_SERVER")
)


def create_issue(summary: str, description: str) -> str:
    issue_dict = {
        'project': {'key': 'HAC'},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Task'},
    }
    new_issue = jira_connection.create_issue(fields=issue_dict)
    return new_issue