import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    url = 'https://api.github.com/search/repositories'
    range_days = 'created:>{}'.format((datetime.now() - \
                                      timedelta(days=7)).strftime('%Y-%m-%d'))
    query_parameter = {'q': range_days,
                       'sort': 'stars',
                       'order': 'desc',
                       'per_page': top_size,
                       }
    query_trending_repo = requests.get(url, params=query_parameter)
    return query_trending_repo.json().get()


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(repo_owner, repo_name)
    query_of_issues = requests.get(url)
    return len(query_of_issues)

if __name__ == '__main__':
    pass