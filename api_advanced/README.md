# api_advanced

Python scripts that query the Reddit API with the `requests` module.

| File | Description |
|------|-------------|
| `0-subs.py` | `number_of_subscribers(subreddit)` returns the subscriber count, or 0 if invalid |
| `1-top_ten.py` | `top_ten(subreddit)` prints the titles of the first 10 hot posts, or `None` |
| `2-recurse.py` | `recurse(subreddit, hot_list=None, after=None)` recursively returns all hot post titles, or `None` |
| `3-count.py` | `count_words(subreddit, word_list)` recursively counts keywords in hot titles and prints them sorted |

All requests set a custom `User-Agent` and use `allow_redirects=False`
so invalid subreddits are detected instead of following the search redirect.
