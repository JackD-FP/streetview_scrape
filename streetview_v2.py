# This version of the SimpleGoogleStreetView script addresses a bug in which
# Processing Python Mode on Windows cannot load files with the Python open()
# function. Thus, you can place your CSV locations into the 'data' variable
# in locationscsv.py instead.
#
# https://github.com/jdf/processing.py/issues/274
#
# Once the issue is resolved or a workaround found, this file will go away.

import csv
import urllib.request
import locationscsv
import location
import os
from shutil import copyfileobj
from shutil import move
from urllib.request import urlopen

# Store all the CSV rows in the "locations" array.
# locations = []
# reader = csv.reader(locationscsv.data2.splitlines())
# is_first_row = True
# for row in reader:
#     # Skip the first row.
#     if is_first_row:
#         is_first_row = False
#         continue

#     lat, lon = float(row[0]), float(row[1])
#     location = (lat, lon)
#     locations.append(location)

# new generator for locations
# locations = location.sampled_coor(20, -33.879566188116925, 151.20523132580067, -33.8763648946121, 151.20617251473382)
locations = location.coor

# Put your Google Street View API key here.
api_key = "AIzaSyCLx1cVxGxez6FsHD0uE671_B2W7q7q8XE"

# headings changed
api_url = "https://maps.googleapis.com/maps/api/streetview?size=512x512&location={0},{1}&fov={2}&heading={3}&pitch={4}&source=outdoor&key={5}"
row = 2
headings = [0, 45, 90, 135, 180, 225, 270]
fov = 50
pitch = [10, 45]

# Loop over every location, and for each location, loop over all the possible headings.
for location_ in locations:
    os.makedirs("loc_{}".format(row), exist_ok=True)
    for direction in headings:
        for alt in pitch:
            # Create the URL for the request to Google.
            lat, lon = location_
            url = api_url.format(lat, lon, fov, direction, alt, api_key)

            # Create the filename we want to save as, e.g. location-2-90.jpg.
            filename = "loc_{0}-dir_{1}-alt_{2}.jpg".format(row, direction, alt)

            # Use the 'curl' command to actually make the request and save the file to disk.
            with urlopen(url) as response, open(filename, 'wb') as out_file:
                copyfileobj(response, out_file)
            print("Got {}".format(filename))
            move(filename, "loc_{}".format(row))

    # Increment the row to correlate with the Excel file.
    row += 1
    
print("Done") 