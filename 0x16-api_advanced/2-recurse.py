#!/usr/bin/python3
# This script demonstrates a recursive function to query the Reddit API for hot articles in a given subreddit.

import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API for hot articles in a given subreddit and accumulates their titles into a list.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): List to store the titles of hot articles. Defaults to an empty list.
        
    Returns:
        list: A list containing the titles of all hot articles for the given subreddit. Returns None if the subreddit is invalid.
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
            children = data[1].get('data', {}).get('children', [])
            
            # Base case: If no children, return the accumulated list
            if not children:
                return hot_list
            
            # Recursive case: Process the first child and recurse with the rest
            first_child = children.pop(0)
            title = first_child.get('data', {}).get('title', '')
            hot_list.append(title)
            
            # Recurse with the remaining children
            return recurse(subreddit, hot_list)
        else:
            print(None)  # Print None if the subreddit is invalid
            return None
    except Exception as e:
        print(None)  # Print None in case of an error
        return None

# Example usage
subreddit_name = "Python"
titles = recurse(subreddit_name)
if titles:
    print("Titles of hot articles:")
    for title in titles:
        print(title)
else:
    print("No results found or subreddit is invalid.")

