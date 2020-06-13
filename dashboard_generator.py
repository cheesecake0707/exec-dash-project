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


#validate
if user_choice not in file_name:
    print("Hey, didn't find a file at that location")
    exit()

#calculations
print("-----------------------")
print("MONTH: ","March 2018") #need to figure out how to pull date and year

csv_file_path = user_choice

import pandas as pd
df = pd.read_csv(csv_file_path)
df_dedup = df.groupby(["product"])["sales price"].sum()
print(df_dedup) #need sorting, need $ format
print(df["sales price"].sum())


#import csv


#with open(csv_file_path, "r") as csv_file:
    #reader = csv.DictReader(csv_file)
    #for row in reader:
        #price_usd_unit = "(${0:.2f})".format(float(row["unit price"]))
        #price_usd_sales = "(${0:.2f})".format(float(row["sales price"]))
        #print(row["product"], price_usd_sales)


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
