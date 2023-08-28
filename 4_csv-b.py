import csv

# Collect information from the user and save to variables
print("Let's add a new router.")
hostname = input("What is the hostname? ")
ip = input("What is the ip address? ")
location = input("What is the location? ")

# Create new list representing device
device = [hostname, ip, location]

# Open the csv file in "append" mode to add new device
with open("csv_example.csv", "a") as f:
    # Create a csv.writer object from the file
    csv_writer = csv.writer(f)
    # Add new row based on new device
    csv_writer.writerow(device)