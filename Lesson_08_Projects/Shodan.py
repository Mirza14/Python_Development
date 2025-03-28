# Import Modules
import shodan

# API Key to access Shodan
API_KEY = input ("Please enter your shodan API Key: ")

# Initialze the API object
api = shodan.Shodan(API_KEY)

TV = api.search('Samsung Smart TVs')
country = api.protocols({'http'})
