import urllib.parse
import urllib.request
import json

def get_plus_code(location):
    # Encode the location for the URL
    params = urllib.parse.urlencode({'q': location})
    url = f'http://py4e-data.dr-chuck.net/opengeo?{params}'

    try:
        # Open the URL and read the JSON data
        response = urllib.request.urlopen(url)
        json_data = response.read().decode()

        # Print the raw JSON data for debugging
        print(f'Raw JSON data: {json_data}')

        # Parse the JSON data
        data = json.loads(json_data)

        # Print the parsed JSON for debugging
        print(f'Parsed JSON data: {data}')

        # Extract the plus_code
        plus_code = data.get('plus_code', 'No plus code found')
        return plus_code
    except Exception as e:
        print(f'Error: {e}')
        return 'Error retrieving plus code'

def main():
    # Ask the user for the location
    location = input('Enter location: ')
    
    # Retrieve the plus_code from the JSON response
    plus_code = get_plus_code(location)
    
    # Print the results
    print(f'Retrieving {location}')
    print(f'Plus code: {plus_code}')

if __name__ == '__main__':
    main()
