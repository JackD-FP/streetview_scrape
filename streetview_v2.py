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
from shutil import copyfileobj
from urllib.request import urlopen

# Store all the CSV rows in the "locations" array.
locations = []
reader = csv.reader(locationscsv.data2.splitlines())
is_first_row = True
for row in reader:
    # Skip the first row.
    if is_first_row:
        is_first_row = False
        continue

    lat, lon = float(row[0]), float(row[1])
    location = (lat, lon)
    locations.append(location)

# Put your Google Street View API key here.
api_key = "AIzaSyCLx1cVxGxez6FsHD0uE671_B2W7q7q8XE"

# headings changed
api_url = "https://maps.googleapis.com/maps/api/streetview?size=640x640&location={0},{1}&fov=90&heading={2}&pitch={3}&key={4}"
row = 2
headings = [0, 45, 90, 135, 180, 225, 270]
pitch = [10, 30]

# Loop over every location, and for each location, loop over all the possible headings.
for location in locations:
    for direction in headings:
        for alt in pitch:
            # Create the URL for the request to Google.
            lat, lon = location
            url = api_url.format(lat, lon, direction, alt, api_key)

            # Create the filename we want to save as, e.g. location-2-90.jpg.
            filename = "loc_{0}-dir_{1}-alt_{2}.jpg".format(row, direction, alt)

            # Use the 'curl' command to actually make the request and save the file to disk.
            #urllib.request.urlretrieve(url, filename)
            #print("Got %s{}".format(filename))
            with urlopen(url) as response, open(filename, 'wb') as out_file:
                copyfileobj(response, out_file)
            print("Got {}".format(filename))

    # Increment the row to correlate with the Excel file.
    row += 1
    
print("Done")