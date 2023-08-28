# Import the csv library
import csv

# Open the sample csv file and print it to screen
with open("csv_example.csv") as f:
    print(f.read())

# Open the sample csv file, and create a csv.reader object
with open("csv_example.csv") as f:
    csv_python = csv.reader(f)
    # Loop over each row in csv and leverage the data in code
    for row in csv_python:
        print("{device} is in {location} " \
              "and has IP {ip}.".format(
                  device = row[0],
                  location = row[2],
                  ip = row[1]
                  )
                )