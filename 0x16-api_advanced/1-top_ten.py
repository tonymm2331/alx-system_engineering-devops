#!/usr/bin/python3
# This script demonstrates how to query the Reddit API for the titles of the first 10 hot posts in a subreddit.

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API to fetch and print the titles of the first 10 hot posts listed for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        
    Prints:
        str: Titles of the first 10 hot posts. Prints None if the subreddit is invalid.
    """
    base_url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "Custom/0.1"}  # Set a custom User-Agent
    
    try:
        # Construct the URL for the subreddit
        url = f"{base_url}{subreddit}/hot.json"
        
        # Make the GET request
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract the post titles from the JSON response
            data = response.json()
            posts = data[1]['data']['children'][:10]  # Get the first 10 posts
            
            for post in posts:
                title = post['data']['title']
                print(title)
        else:
            print(None)  # Print None if the subreddit is invalid
    except Exception as e:
        print(None)  # Print None in case of an error

# Example usage
subreddit_name = "Python"
top_ten(subreddit_name)
# Peace
