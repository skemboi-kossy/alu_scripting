#!/usr/bin/python3
"""Module that recursively counts keywords in the hot post titles."""
import requests

USER_AGENT = "linux:api_advanced:v1.0 (by /u/holberton_student)"


def print_results(counts, word_list):
    """Print keyword totals sorted by count (desc), then name (asc)."""
    lowered = [w.lower() for w in word_list]
    totals = {}
    for word, count in counts.items():
        total = count * lowered.count(word)
        if total > 0:
            totals[word] = total
    for word, total in sorted(totals.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, total))


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count keywords in the titles of a subreddit's hot posts.

    Matching is case-insensitive and whole-word only. Duplicates in
    word_list are summed. Prints nothing if the subreddit is invalid
    or no keyword matches.
    """
    if counts is None:
        counts = {}
    if not subreddit or not isinstance(subreddit, str):
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": USER_AGENT}
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            print_results(counts, word_list)
            return
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        print_results(counts, word_list)
        return
    wanted = set(w.lower() for w in word_list)
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for word in title.lower().split():
            if word in wanted:
                counts[word] = counts.get(word, 0) + 1
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    print_results(counts, word_list)
