import os
import csv

# path
filepath = os.path.join("Resources", "budget_data.csv")

# open filepath of csv file
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

# skip header row
print(f"Header: {csv_header}")

# net amount of profit and loss
profit = []
months = []

# loop through each row of data after header
for rows in csvreader:
    profit. append(int(rows[1]))
    months. append(rows[0])

# find revenue change
    revenue_change = []

    for y in range(1, len(profit)):
        revenue_change.append((int(profit[y]) - int(profit[y-1])))

    # calculate revenue_average

    revenue_average = sum(revenue_change) / len(revenue_change)

    # total len of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(revenue_change)

    # greatest_decrease in revenue
    greatest_decrease = min(revenue_change)

    # print analysis results

    print("financial analysis")

    print(".................................................................." + "\n")

    print("total m onths: " + str(total_months))

    print("total: " + str(sum(profit)))

    print("Average change:" + str(revenue_average))

    print("Greatest Increase in profits: " +
          str(months[revenue_change.index(max(revenue_change))+1]) + " " + str(greatest_increase))

    print("Greatest Decease in profit: " +
          str(months[revenue_change.index(min(revenue_change))+1]) + " " + str(greatest_decrease))

    csvfile.close()

    # write to a text file

    writepath = "C:\\Users\\hp\\OneDrive\\Desktop\\bootcamp Git\\UBHM-VIRT-DATA-PT-08-2022-U-LOLC\\02-Homework\\03-Python\\python_challenge\\analysis"
    t = open("output. text", "w")

    t.write(".................................................................." + "\n")

    t.write("total months: " + str(total_months))

    t.write("total: " + str(sum(profit)))

    t.write("Average change:" + str(revenue_average))

    t.write("Greatest Increase in profits: " +
            str(months[revenue_change.index(max(revenue_change))+1]) + " " + str(greatest_increase))

    t.write("Greatest Decease in profit: " +
            str(months[revenue_change.index(min(revenue_change))+1]) + " " + str(greatest_decrease))

    t.close()
