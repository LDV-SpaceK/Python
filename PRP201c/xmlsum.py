import urllib.request
import xml.etree.ElementTree as ET

def extract_and_sum_counts(url):
    # Open the URL and read the XML data
    response = urllib.request.urlopen(url)
    xml_data = response.read()

    # Parse the XML data
    tree = ET.fromstring(xml_data)

    # Find all 'count' tags
    counts = tree.findall('.//count')
    
    # Initialize the sum of counts
    total_sum = 0

    # Loop through each count tag and sum up the values
    for count in counts:
        total_sum += int(count.text)
    
    # Return the sum of counts
    return total_sum

def main():
    # Ask the user for the URL
    url = input('Enter location: ')
    
    # Open the URL and read the XML data
    response = urllib.request.urlopen(url)
    xml_data = response.read()
    
    # Retrieve and sum counts from the XML
    total_sum = extract_and_sum_counts(url)
    
    # Print the results
    print(f'Retrieving {url}')
    print(f'Retrieved {len(xml_data)} characters')
    print(f'Sum: {total_sum}')


if __name__ == '__main__':
    main()
