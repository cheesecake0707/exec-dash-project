# dashboard_generator.py

#input
import os
import glob
path = "/Users/Renee/Documents/GitHub/exec-dash-project/monthly-sales"
extension = "csv"
os.chdir(path)
file_name = glob.glob("*.{}".format(extension))
print(file_name)

user_choice = input("Please choose from the above file list (without ''): ")

import csv

csv_file_path = user_choice

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row["date"], row["product"], row["unit price"], row["units sold"], row["sales price"])

#validate

if user_choice not in file_name:
    print("Hey, didn't find a file at that location")
    exit()


#print("-----------------------")
#print("MONTH: March 2018")

#print("-----------------------")
#print("CRUNCHING THE DATA...")

#print("-----------------------")
#print("TOTAL MONTHLY SALES: $12,000.71")

#print("-----------------------")
#print("TOP SELLING PRODUCTS:")
#print("  1) Button-Down Shirt: $6,960.35")
#print("  2) Super Soft Hoodie: $1,875.00")
#print("  3) etc.")

#print("-----------------------")
#print("VISUALIZING THE DATA...")
