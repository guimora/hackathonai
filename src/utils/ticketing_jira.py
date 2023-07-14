from jira import JIRA

jira_connection = JIRA(
    basic_auth=('workspace_email', 'api_token'),
    server="https://server_name.atlassian.net"
)


def create_issue(summary: str, description: str):
    issue_dict = {
        'project': {'key': 'PJH'},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Bug'},
    }
    new_issue = jira_connection.create_issue(fields=issue_dict)
