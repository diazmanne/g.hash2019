class Photo(object):
    def __init__(self, position, orientation, numOfTags, tags):
        self.position = position
        self.orientation = orientation
        self.numOfTags = numOfTags
        self.tags = tags

    def whatPosition(self):
        return self.position

    def whatOrientation(self):
        return self.orientation

    def whatNumOfTags(self):
        return self.numOfTags

    def whatTags(self):
        return self.tags


def main():
    import sys
    filename = sys.argv[1]
    file = open(filename,"r")
    my_photos = []
    numOfPhotos = int(file.readline())
    print(numOfPhotos)
    i = 0
    for line in file:
        listOfTags = int(line.strip()[2])
        my_photos.append(Photo(i, line.strip()[0], listOfTags, line.strip().split(' ')[2:(listOfTags+2)]))
        i += 1
    for j in range(i):
        print(my_photos[j].whatPosition(), my_photos[j].whatOrientation(), my_photos[j].whatNumOfTags(), my_photos[j].whatTags())


if __name__ == "__main__": main()