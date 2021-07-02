#! /usr/local/bin/python3

"""Return the date a GitHub user was created"""

# load modules
import os
import sys
import requests
from datetime import datetime
from api_errors import *


def getUsername(args=sys.argv):
    """Return the GitHub username passed in from CLI, otherwise raise an error"""
    if args.__len__() != 2:
        raise ArgsError
    return args[1]


def getRequest(params):
    """Returns the requested information from the API"""
    return requests.get(params["request_url"], headers=params["header"])


def getToken():
    """Return GitHub API token"""
    t = os.getenv("GITHUB_TOKEN")
    # test BadCredentialsError
    # TOKEN = TOKEN[:-1]
    if t is None:
        raise NoTokenError
    return t


def populateParams(user, token):
    """Populate a parameter dictionary for API request"""
    return


def getUserCreateDate():
    """Use API to get a specified user's profile creation date"""
    global user
    user, token = getUsername(), getToken()

    params = {"request_url": f'https://api.github.com/users/{user}',
              "header": {
                  "Authorization": f"token {token}"
              }}
    answer = getRequest(params)
    if answer.status_code != 200:
        if answer.json()['message'] == 'Not Found':
            raise UserNotFoundError
        if answer.json()['message'] == 'Bad credentials':
            raise BadCredentialsError
    user_json = answer.json()
    created_at = user_json['created_at']

    # created_at[:-1] strips off trailing 'Z':
    # '2020-03-29T19:02:29Z' -> '2020-03-29T19:02:29'
    # '%Y-%m-%dT%H:%M:%S' recognizes the T seperator
    asdate = datetime.strptime(
        created_at[:-1], '%Y-%m-%dT%H:%M:%S')
    date = datetime.strftime(asdate, "%b %d, %Y")
    time = datetime.strftime(asdate, "%I:%M:%S %p")
    print(f'{user} was created on {date} at {time}')


def main():
    try:
        getUserCreateDate()
    except (NoTokenError):
        sys.exit(f"No API token found. Make sure '$GITHUB_TOKEN' exists.")

    except (UserNotFoundError):
        sys.exit(f"404 - GitHub user '{user}' could not be found.")

    except (BadCredentialsError):
        sys.exit(f"404 - Credentials not accepted by GitHub.")

    except (ArgsError):
        sys.exit("USAGE: python3 github.py USERNAME")


if __name__ == '__main__':
    main()
