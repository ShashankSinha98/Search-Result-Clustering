import requests

# Define the API endpoint URL
api_url = 'http://127.0.0.1:8000/api/query/'

def GetQueryAndClusterCount():
    try:
        # Make a GET request to the API endpoint
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response, assuming it's JSON data
            data = response.json()
            
            # Now you can work with the data returned by the API
            print("Data from API:")
            print(data[-1])
            return data[-1]
        else:
            print(f"Error: Status code {response.status_code} received from the API.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
