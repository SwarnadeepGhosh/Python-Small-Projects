# https://github.com/SwarnadeepGhosh
import os


# Make a directory for each place name
def makePlaceDirectories(places):
    for place in places:
        os.mkdir(place)


# Extract the place names from the file names
def extractPlace(fileName):
    first_ = fileName.find('_')
    fileName = fileName[first_+1:]
    second_ = fileName.find('_')
    fileName = fileName[:second_]
    return fileName


def organize_photos(directory):
    # Getting a list of the file names
    os.chdir(directory)
    originals = os.listdir()
    places = []

    for fileName in originals:
        place = extractPlace(fileName)
        if place not in places:
            places.append(place)

    makePlaceDirectories(places)

    # Move files into the right directories
    for fileName in originals:
        place = extractPlace(fileName)
        os.rename(fileName, os.path.join(place, fileName))


organize_photos('Photos')
