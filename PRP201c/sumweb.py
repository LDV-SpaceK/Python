import urllib.request
from bs4 import BeautifulSoup

# Function to retrieve and process the HTML content
def get_sum_from_url(url):
    # Open the URL and read the HTML content
    response = urllib.request.urlopen(url)
    html = response.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all span tags
    span_tags = soup.find_all('span', class_='comments')
    
    # Initialize a variable to hold the sum of the numbers
    total_sum = 0

    # Loop through the span tags and extract the numbers
    for tag in span_tags:
        # Get the text content of the span tag and convert it to an integer
        number = int(tag.text)
        # Add the number to the total sum
        total_sum += number

    return total_sum

# Main function
def main():
    # Ask the user for the URL
    url = input('Enter - ')
    
    # Get the sum from the URL
    total_sum = get_sum_from_url(url)
    
    # Count the number of span tags
    span_tags_count = len(BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser').find_all('span', class_='comments'))

    # Print the results
    print(f'Count {span_tags_count}')
    print(f'Sum {total_sum}')

# Execute the main function
if __name__ == '__main__':
    main()