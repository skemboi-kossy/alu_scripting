#!/usr/bin/python3
"""Module that prints the titles of the first 10 hot posts of a subreddit."""
import requests

USER_AGENT = "linux:api_advanced:v1.0 (by /u/holberton_student)"


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.

    Prints None if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": USER_AGENT}
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
    except requests.RequestException:
        print(None)
        return
    if response.status_code != 200:
        print(None)
        return
    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return
    for post in posts:
        print(post.get("data", {}).get("title"))
