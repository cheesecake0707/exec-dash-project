# dashboard_generator.py

#info input
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

import datetime
user_choice_formatted = (user_choice.replace('.csv',''))
user_choice_formatted_02 = (user_choice_formatted.replace('sales-',''))
month_year = datetime.datetime.strptime(user_choice_formatted_02, '%Y%m').strftime('%B %Y')


print("-----------------------")
print("MONTH: ",month_year)

print("-----------------------")
print("CRUNCHING THE DATA...")


#info output: total monthly sales

print("-----------------------")

csv_file_path = user_choice
import pandas as pd

df = pd.read_csv(csv_file_path)
df_group = df.groupby(['product'])['sales price'].sum()
df_group_dict = df_group.to_dict()
total_monthly_sales = sum(df_group_dict.values())
print("TOTAL MONTHLY SALES: ", "${:,.2f}".format(total_monthly_sales))

#info output: top selling products

print("-----------------------")
print("TOP SELLING PRODUCTS:")
df_group_dict_sort = sorted(df_group_dict.items(), key=lambda x: x[1], reverse=True)
for i in df_group_dict_sort:
	print(i[0], "${:,.2f}".format(i[1]))


#info outputs: visualizing the data

print("-----------------------")
print("VISUALIZING THE DATA...")

import plotly
import plotly.graph_objs as go

products = []
sales_price = []
for i in df_group_dict_sort:
    products.append(i[0])
    sales_price.append("${:,.2f}".format(i[1]))

fig = go.Figure(go.Bar(
            x=sales_price,
            y=products,
            text=sales_price,
            textposition='auto',
            orientation='h'))

fig.update_layout(
    title="Top-selling Products in " + month_year,
    xaxis_title="Sales(USD)",
    yaxis_title="Product Name")

fig.show()




