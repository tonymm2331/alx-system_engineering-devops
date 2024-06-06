#!/usr/bin/python3
# This script demonstrates how to query the Reddit API for the number of subscribers of a subreddit.
# It handles invalid subreddits gracefully by returning 0 and sets a custom User-Agent to avoid Too Many Requests errors.

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to return the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        
    Returns:
        int: The number of subscribers for the given subreddit. Returns 0 if the subreddit is invalid.
    """
    base_url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "Custom/0.1"}
    
    try:
        # Construct the URL for the subreddit
        url = f"{base_url}{subreddit}.json"
        
        # Make the GET request
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract the subscriber count from the JSON response
            data = response.json()
            subscriber_count = data[1]['data']['children'][0]['data']['subscriber_count']
            
            return subscriber_count
        else:
            print(f"Failed to retrieve data: {response.status_code}")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage
subreddit_name = "Python"
num_subscribers = number_of_subscribers(subreddit_name)
print(f"The subreddit '{subreddit_name}' has {num_subscribers} subscribers.")
