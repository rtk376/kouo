from github import Github, GithubException


def print_top_starred_repos(username, num_top):
    '''
    This
    :param username:
    :param num_top:
    :return:
    '''
    g = Github()  # instantiating main class
    try:
        user = g.get_user(username)
    except GithubException:
        print('Specified user does not exist, please enter a different username')
        exit()

    user_repos = user.get_repos()

    rns = []  # list to store repository names and their star count

    if user_repos.totalCount == 0:
        print('Specified user does not have any public repositories')
        exit()

    for repo in user_repos:
        if repo.stargazers_count > 0:
            rns.append([repo.name, repo.stargazers_count])

    if len(rns) == 0:
        print('Specified user does not have any starred repositories')
        exit()

    sorted_rns = sorted(rns, key=lambda x: x[1], reverse=True)  # sorted list of repos with starcount (highest first)
    print(f'Top {num_top} starred repositories:')
    for repo in sorted_rns[:num_top]:
        print(repo[0], repo[1])