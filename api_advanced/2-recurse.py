#!/usr/bin/python3
"""Module that recursively collects the titles of all hot posts."""
import requests

USER_AGENT = "linux:api_advanced:v1.0 (by /u/holberton_student)"


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of the titles of all hot posts of a subreddit.

    Follows Reddit's pagination recursively using the 'after' value.
    Returns None if the subreddit is invalid or has no results.
    """
    if hot_list is None:
        hot_list = []
    if not subreddit or not isinstance(subreddit, str):
        return None
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": USER_AGENT}
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
    except requests.RequestException:
        return hot_list or None
    if response.status_code != 200:
        return hot_list or None
    try:
        data = response.json().get("data", {})
    except ValueError:
        return hot_list or None
    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list or None
