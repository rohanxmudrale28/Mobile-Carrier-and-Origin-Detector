#print ("Rohan Mudrale")
#Copyright © 2024 Rohan Mudrale. All rights reserved.
import phonenumbers
from phonenumbers import geocoder
from test import number
import folium

check_number = phonenumbers.parse(number)

# I will be using Geocoder to determine the location of phone number in English language. Isnt it crazy? 
#These libiraries will give location in the form of country
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

#Now to get mobile carrier or service provider

from phonenumbers import carrier 
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
 

