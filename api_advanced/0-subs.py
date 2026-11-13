#!/usr/bin/python3
"""Module that queries the Reddit API for a subreddit's subscriber count."""
import requests

USER_AGENT = "linux:api_advanced:v1.0 (by /u/holberton_student)"


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a subreddit.

    Returns 0 if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": USER_AGENT}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False, timeout=10)
    except requests.RequestException:
        return 0
    if response.status_code != 200:
        return 0
    try:
        return response.json().get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
