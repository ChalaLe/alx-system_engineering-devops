#!/usr/bin/python3
"""
Recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests


def matches_words(list_posts, dict_words):
    """Function that counts the matches with the keywords."""
    for post in list_posts:
        for word in post.get('data').get('title').split():
            for key in dict_words.keys():
                if key.lower() == word.lower():
                    dict_words[key] += 1


def recurse(subreddit, dict_words, after=None):
    """Recursive function that queries the Reddit API and
    search keywords in titles posts."""
    api_header = {'User-Agent': 'Mozilla/5.0'}
    api_params = {'after': after}
    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    api_res = requests.get(api_url, headers=api_header, params=api_params)

    if api_res.status_code != 200:
        return

    api_data = api_res.json().get('data')
    list_posts = api_data.get('children')
    after = api_data.get('after')

    matches_words(list_posts, dict_words)

    if after is None:
        return
    recurse(subreddit, dict_words, after)


def count_words(subreddit, word_list):
    """Function that queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces).
    """
    dict_words = {}

    for word in word_list:
        dict_words[word.lower()] = 0

    recurse(subreddit, dict_words)

    # Filter and sort the dictionary in descending order
    sorted_words = {
        k: v for k, v in sorted(
            dict_words.items(),
            key=lambda item: (item[1], item[0]),
            reverse=True
        )
        if v != 0
    }

    for word, count in sorted_words.items():
        print(f"{word}: {count}")
