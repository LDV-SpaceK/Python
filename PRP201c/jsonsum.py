import urllib.request
import json

def extract_and_sum_counts(url):
    # Open the URL and read the JSON data
    response = urllib.request.urlopen(url)
    json_data = response.read().decode()

    # Parse the JSON data
    data = json.loads(json_data)

    # Extract the list of comments
    comments = data['comments']
    
    # Initialize the sum of counts
    total_sum = 0

    # Loop through each comment and sum up the counts
    for comment in comments:
        total_sum += comment['count']
    
    # Return the sum of counts
    return total_sum

def main():
    # Ask the user for the URL
    url = input('Enter location: ')
    response = urllib.request.urlopen(url)
    json_data = response.read().decode()
    # Retrieve and sum counts from the JSON
    total_sum = extract_and_sum_counts(url)
    
    # Print the results
    print(f'Retrieving {url}')
    print(f'Retrieved {len(json_data)} characters')
    print(f'Sum: {total_sum}')

if __name__ == '__main__':
    main()
