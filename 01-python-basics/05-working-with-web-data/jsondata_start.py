#
# Example file for parsing and processing JSON
#
import urllib.request
import json


def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    # output the number of events, plus the magnitude and each event name
    if "count" in theJSON["metadata"]:
        print(theJSON["metadata"]["count"], "\n")

    print("** All Events **")

    # for each event, print the place where it occurred
    for feature in theJSON["features"]:
        print(feature["properties"]["place"])

    print("\n--------------\n")
    print("** Events >4.0 magnitude **")
    # print the events that only have a magnitude greater than 4
    for f in theJSON["features"]:
        mag, place = float(f["properties"]["mag"]), f["properties"]["place"]
        if mag >= 4:
            print(mag, place, sep="\t|\t")

    print("\n--------------\n")
    print("** Events with more than 1 reporting **")
    # print only the events where at least 1 person reported feeling something
    for f in theJSON["features"]:
        felt, place, mag = f["properties"]["felt"], f["properties"]["place"], f["properties"]["mag"]
        if felt != None and int(felt) > 0:
            print(f'{felt} person reported', "%2.2f" % mag, place, sep="\t|\t")


def main():

    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    if webUrl.getcode() == 200:
        printResults(webUrl.read())
    else:
        print("Received an error. Cannot parse.")


if __name__ == "__main__":
    main()
