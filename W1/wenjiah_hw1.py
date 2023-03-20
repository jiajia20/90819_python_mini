# Name: Wenjia Hu
# Andrew ID: wenjiah

# Problem 1

# format the print output to look like this (YEAR TITLE ARTIST):

#print title with formating
print ('{:<15} {:>40} {:>40}'.format('YEAR','TITLE','ARTIST'))

#print the line
length = 95
line = '-' * length
print(line)

#read csv and print csv line by line
import csv

with open('songs.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        year, title, artist = row
        print('{:<15} {:>40} {:>40}'.format(year, title, artist))
        
       
###############################################
# Problem 2
#print title with formating
print ('{:<15} {:>40} {:>40}'.format('YEAR','TITLE','ARTIST'))

#print the line
length = 95
line = '-' * length
print(line)

import csv

songTable = []
with open('songs.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        year, title, artist = row
        oneSong = [year, title, artist ]
        songTable.append(oneSong)

#print(songTable)

songTable.sort( key = lambda x: x[1])

for oneSong in songTable:
    year, title, artist = oneSong
    print('{:<15} {:>40} {:>40}'.format(year, title, artist))

###############################################

# Problem 3

yearDict = {content[0]: content for content in songTable}

print(yearDict)

while True:
    year = input('Enter a year: ')
    if year == 'DONE':
        break
    elif year in yearDict:
        print(yearDict[year])
    else:
        print('Not found')


# Problem 4

#To do this, first create artistDict as an empty dict. 
# Loop over songTabe. For each entry, ask if the artist is in artistDict – if not, add it (with [ ] to make it a list); if it is, append the item to the existing list. 
# Print just the entry for ‘Elvis Presley' as a check; 

artistDict = {}
for oneSong in songTable:   
    if oneSong[2] not in artistDict:
        artistDict[oneSong[2]] = [oneSong]
    else:
        artistDict[oneSong[2]].append(oneSong)


#write a while loop that prompts the user to enter an artist. 
# Use artistDict to look up that artist; if they’re in the dict, print the value(s), 
# otherwise, print ‘Not found’. Continue asking the user until they enter ‘DONE’.

while True:
    artist = input('Enter an artist: ')
    if artist == 'DONE':
        break
    elif artist in artistDict:
        print(artistDict[artist])
    else:
        print('Not found')