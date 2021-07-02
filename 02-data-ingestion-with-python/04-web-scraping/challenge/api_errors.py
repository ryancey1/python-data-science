#! /usr/local/bin/python3

class UserNotFoundError(Exception):
    pass


class BadCredentialsError(Exception):
    pass


class ArgsError(Exception):
    pass


class NoTokenError(Exception):
    pass
