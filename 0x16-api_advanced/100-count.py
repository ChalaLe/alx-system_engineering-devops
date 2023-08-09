#!/usr/bin/python3
"""
This module contains functions to query the Reddit API and count
keywords in hot articles.
"""

import requests


def matches_words(list_posts, dict_words):
    """
    Counts the matches with the keywords.

    Args:
        list_posts (list): List of posts.
        dict_words (dict): Dictionary of keywords and their counts.
    """
    for post in list_posts:
        for word in post.get('data').get('title').split():
            for key in dict_words.keys():
                if key.lower() == word.lower():
                    dict_words[key] += 1


def recurse(subreddit, dict_words, after=None):
    """
    Recursive function that queries the Reddit API and searches i
    keywords in titles of posts.

    Args:
        subreddit (str): Reddit subreddit.
        dict_words (dict): Dictionary of keywords and their counts.
        after (str, optional): After page identifier.
    """
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
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces).

    Args:
        subreddit (str): Reddit subreddit.
        word_list (list): List of keywords.
    """
    dict_words = {}

    for word in word_list:
        dict_words[word.lower()] = 0

    recurse(subreddit, dict_words)

    # Filter and sort the dictionary alphabetically
    sorted_words = {
        k: v for k, v in sorted(
            dict_words.items(),
            key=lambda item: item[0]
        )
        if v != 0
    }

    for word, count in sorted_words.items():
        print(f"{word}: {count}")
