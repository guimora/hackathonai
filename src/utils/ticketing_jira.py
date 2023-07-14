from jira import JIRA

jira_connection = JIRA(
    basic_auth=('starsteygsv@gmail.com', 'ATATT3xFfGF0c92k-MmmhiKfW9Ua_--Q3tLygF5LM4e1gN2qFQ0oCNZssVWneUQtT9G8qPA0U6U6_pnHxaSoBAqSrc-o0fGIXMasfXgZ00HP1IoH2S_XN2cGQ_dX2vlnaoEFvV1XDebhv4WUGJp4pKwPb4L4V6m8xKqHAAtQxdcdObYqmGngC5M=CEB50659'),
    server="https://hackai.atlassian.net/"
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