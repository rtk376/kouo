from github import Github, GithubException
from requests import ConnectionError

def get_user(username):
    '''
    This function retrieves the user object corresponding to the required username, if such user exists
    :param username: string object with the username
    :return: Github.NamedUser object corresponding to the username
    '''
    g = Github()  # instantiating main class
    ### Attempting to retrieve Github user by username
    try:
        user = g.get_user(username)
    except GithubException:
        print('Specified user does not exist, please enter a different username')
        exit()
    except ConnectionError:
        print('Please ensure a stable internet connection')
        exit()

    return user

def print_top_starred_repos(username, N):
    '''
    This function prints top N starred repositories of a given user on GitHub, if the user exists and has starred repos.
    :param username: string object with the username
    :param N: number of top starred repos to print
    :return:
    '''

    ### Retrieving info about the given user and all their repositories
    user = get_user(username)
    user_repos = user.get_repos()

    rns = []  # list to store repository names and their star count as [repo_name, star_count]

    # Check if user has any public repos
    if user_repos.totalCount == 0:
        print('Specified user does not have any public repositories')
        exit()

    # Fill the rns list with starred repos and their star count
    for repo in user_repos:
        # only append starred repos, otherwise "top N" makes no sense
        if repo.stargazers_count > 0:
            rns.append([repo.name, repo.stargazers_count])

    # Abort if user has no starred repos
    if len(rns) == 0:
        print('Specified user does not have any starred repositories')
        exit()

    # Sort the starred repos list by star count
    sorted_rns = sorted(rns, key=lambda x: x[1], reverse=True)  # sorted list of repos with starcount (highest first)
    print(f'Top {min(N, len(sorted_rns))} starred repositories:')
    # printing top N starred repos, or as many as the user has if < N
    for repo in sorted_rns[:N]:
        print(repo[0], repo[1])