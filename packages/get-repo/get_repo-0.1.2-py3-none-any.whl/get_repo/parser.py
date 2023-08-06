import giturlparse


def parse(url: str) -> str:
    git_url = giturlparse.parse(url)
    if not (git_url.resource and git_url.owner and git_url.name):
        raise InvalidGitUrl(f'{url} is not a valid git url')

    return '/'.join([git_url.resource, git_url.owner, git_url.name])


class InvalidGitUrl(Exception):
    pass
