#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests  # Import the requests library to make HTTP requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""

    # Construct the URL for the subreddit's about page
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    """Define the User-Agent header to provide information about
    my application"""
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/ChalaLe)"
    }

    # Send a GET request to the API with the specified URL and headers
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response status code is 404 (Not Found)
    if response.status_code == 404:
        return 0  # Return 0 if the subreddit is not found

    # Parse the JSON response and extract the "data" section
    results = response.json().get("data")

    # Return the number of subscribers from the "data" section
    return results.get("subscribers")
