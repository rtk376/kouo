import argparse
from lib import print_top_starred_repos

if __name__ == '__main__':
    ### Initialising the command line argument parser
    parser = argparse.ArgumentParser(description='Input a GitHub username to get top 5 starred public repositories')
    parser.add_argument('-u', '--username', type=str, nargs=1, dest='username', help='Github username')
    parser.add_argument('-t', '--top', type=int, default=[5], nargs=1, dest='num_top',
                        help='Number of top starred repositories shown')

    ### Parsing the arguments
    try:
        args = parser.parse_args()
    except argparse.ArgumentError:
        print(parser.print_help())

    username = args.username[0]
    num_top = args.num_top[0] #how many repos to show
    ### Print the username
    print(f'Username: {username} \n')
    ### Print top num_top starred repos
    print_top_starred_repos(username, num_top)

