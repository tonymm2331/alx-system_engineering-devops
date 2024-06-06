#!/usr/bin/python3
# This script demonstrates a recursive function to query the Reddit API for hot articles in a given subreddit,
# count occurrences of specified keywords, and print the counts in a sorted manner.

import requests

def count_words(subreddit, word_list, hot_list=[], counts={}, depth=0):
    """
    Recursively queries the Reddit API for hot articles in a given subreddit, counts occurrences of specified keywords,
    and prints the counts in descending order followed by alphabetical order for ties.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count occurrences of.
        hot_list (list): List of article titles fetched so far. Defaults to an empty list.
        counts (dict): Dictionary to store counts of each keyword. Defaults to an empty dictionary.
        depth (int): Depth of recursion to prevent infinite recursion. Defaults to 0.
        
    Prints:
        str: Counts of specified keywords in descending order followed by alphabetical order for ties.
    """
    base_url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "Custom/0.1"}  # Set a custom User-Agent
    
    try:
        # Prevent infinite recursion
        if depth > 100:
            return
        
        # Construct the URL for the subreddit
        url = f"{base_url}{subreddit}/hot.json"
        
        # Make the GET request
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract the post titles from the JSON response
            data = response.json()
            children = data[1].get('data', {}).get('children', [])
            
            # Base case: If no children, return
            if not children:
                return
            
            # Recursive case: Process the first child and recurse with the rest
            first_child = children.pop(0)
            title = first_child.get('data', {}).get('title', '').lower().replace('.', '').replace('!', '').replace('_', '')
            words = title.split()
            
            for word in words:
                if word in word_list:
                    counts[word] = counts.get(word, 0) + 1
            
            # Recurse with the remaining children
            return count_words(subreddit, word_list, hot_list, counts, depth+1)
        else:
            print(None)  # Print None if the subreddit is invalid
            return None
    except Exception as e:
        print(None)  # Print None in case of an error
        return None

# Example usage
subreddit_name = "Python"
keywords = ["javascript", "java"]
counts = count_words(subreddit_name, keywords)
if counts:
    # Sort counts in descending order by count, then alphabetically by keyword
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    print("\nKeyword Counts:")
    for keyword, count in sorted_counts:
        print(f"{keyword}: {count}")
else:
    print("No results found or subreddit is invalid.")
