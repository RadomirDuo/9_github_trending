import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    delta_days = 7
    url = 'https://api.github.com/search/repositories'
    range_days = 'created:>{}'.format((datetime.now() - timedelta(days=delta_days)).strftime('%Y-%m-%d'))
    query_parameter = {'q': range_days,
                       'sort': 'stars',
                       'order': 'desc',
                       'per_page': top_size,
                       }
    query_trending_repo = requests.get(url, params=query_parameter)
    return query_trending_repo.json().get('items')


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(repo_owner, repo_name)

    query_of_issues = requests.get(url)
    return len(query_of_issues.json())


if __name__ == '__main__':
    top_size = input('Введите количество репозиториев для показа: ')
    print('\n')
    top_github_repositories = get_trending_repositories(top_size)
    for repo in top_github_repositories:
        print('Название: {}'.format(repo['name']))
        print('Описание: {}'.format(repo['description']))
        print('Кол-во звёзд: {}'.format(repo['stargazers_count']))
        print('Кол-во задач: {}'.format(get_open_issues_amount(repo['owner']['login'],repo['name'])))
        print('Ссылка: {}\n'.format(repo['svn_url']))
