import os
import urllib.request
import re

#Starting off variables at empty state
Count = 0
all_requests = 0
past_year_requests = 0
unsuccessful_requests = 0
redirected_requests = 0
past_year = '/1995'
d = {}
weeks = {}
months = {}
file_names = {}

FilePath = './http_access_log.txt'
FileExists = os.path.exists(FilePath)

if FileExists == False:
    print("file not found. Downloading file.")
    url = "https://s3.amazonaws.com/tcmg476/http_access_log"
    urllib.request.urlretrieve(url,"./http_access_log.txt")


with open("http_access_log.txt") as file_in:
    array = []
    for line in file_in:
        array.append(line)



with open("http_access_log.txt") as fh:
    Lines = fh.readlines()
    for line in Lines:
        all_requests += 1
        if past_year in line:
            past_year_requests += 1  
            if '403 -' in line or '404 -' in line:
                unsuccessful_requests += 1
            if '302 -' in line:
                redirected_requests += 1
        result = re.split('.+ \[(.+) .+\] "[A-Z]{3,5} (.+) HTTP/1.0" ([0-9]{3})', line)
        if len(result) == 5:
            date = result[1]
            file = result[2]
            
            date = date.split(':')
            if date[0] in d:
                d[date[0]] += 1
            else:
                d[date[0]] = 1
               
            date[0] = date[0].split('/')
            if date[0][1] + " " + date[0][2] in months:
                months[date[0][1] + " " + date[0][2]] += 1
            else:
                months[date[0][1] + " " + date[0][2]] = 1
            
            if file in file_names:
                file_names[file] += 1
            else:
                file_names[file] = 1

#Section for 1994
input = open(FilePath, "r")
outputOct94 = open("October-1994.txt", "w")
outputNov94 = open("November-1994.txt", "w")
outputDec94 = open("December-1994.txt", "w")

for line in input:
	if "/Oct/1994" in line:
		outputOct94.write(line)
	elif "/Nov/1994" in line:
		outputNov94.write(line)
	elif "/Dec/1994" in line:
		outputDec94.write(line)

input.close()
outputOct94.close()
outputNov94.close()
outputDec94.close()

#Section for 1995
input = open(FilePath, "r")
outputJan95 = open("January-1995.txt", "w")
outputFeb95 = open("Febuary-1995.txt", "w")
outputMar95 = open("March-1995.txt", "w")
outputApr95 = open("April-1995.txt", "w")
outputMay95 = open("May-1995.txt", "w")
outputJun95 = open("June-1995.txt", "w")
outputJul95 = open("July-1995.txt", "w")
outputAug95 = open("August-1995.txt", "w")
outputSep95 = open("September-1995.txt", "w")
outputOct95 = open("October-1995.txt", "w")

for line in input:
	if "/Jan/1995" in line:
		outputJan95.write(line)
	elif "/Feb/1995" in line:
		outputFeb95.write(line)
	elif "/Mar/1995" in line:
		outputMar95.write(line)
	elif "/Apr/1995" in line:
		outputApr95.write(line)
	elif "/May/1995" in line:
		outputMay95.write(line)
	elif "/Jun/1995" in line:
		outputJun95.write(line)
	elif "/Jul/1995" in line:
		outputJul95.write(line)
	elif "/Aug/1995" in line:
		outputAug95.write(line)
	elif "/Sep/1995" in line:
		outputSep95.write(line)
	elif "/Oct/1995" in line:
		outputOct95.write(line)

input.close()
outputJan95.close()
outputFeb95.close()
outputMar95.close()
outputApr95.close()
outputMay95.close()
outputJun95.close()
outputJul95.close()
outputAug95.close()
outputSep95.close()
outputOct95.close()
            
        
print("\n")
print("Requests per day: ")
for key, value in d.items():
    print(str(key) + " - Occurrences: " + str(value))
print("\n")

print("\n")
print("Requests per month: ")
for key, value in months.items():
    print(str(key) + " - Occurrences: " + str(value))

print("\n")       
print("Total requests within a year: " + str(past_year_requests))
print("Total requests: " + str(all_requests))

print("\n")
print("Unsuccessful: " + str(unsuccessful_requests))
print("Redirected: " + str(redirected_requests))

print("\n")
print("Most requested: " + str(list(file_names.keys())[0]))
print("Least requested: " + str(list(file_names.keys())[-1]))
print("\n")

