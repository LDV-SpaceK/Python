import urllib.request
from bs4 import BeautifulSoup

def retrieve_names(url, count, position):
    # Print the URL being processed
    print(f"Retrieving: {url}")

    # Loop to follow the links as per the count
    for _ in range(count):
        # Open the URL and read the HTML content
        response = urllib.request.urlopen(url)
        html = response.read()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Find all anchor tags
        tags = soup.find_all('a')
        
        # Get the href attribute of the link at the specified position
        if len(tags) < position:
            print("Error: Not enough links found")
            return
        href = tags[position - 1].get('href', None)
        
        # Construct the new URL
        url = urllib.parse.urljoin(url, href)
    
    # Return the final URL
    return url

def main():
    # Ask the user for the starting URL, count, and position
    url = input('Enter URL: ')
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))

    # Retrieve the last URL
    last_url = retrieve_names(url, count, position)

    # Print the last URL which will have the final name
    if last_url:
        print(f"Retrieving: {last_url}")
        last_name = last_url.split('_')[-1].replace('.html', '')
        print(f"The answer to the assignment is: {last_name}")

if __name__ == '__main__':
    main()
