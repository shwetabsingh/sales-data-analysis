import matplotlib.pyplot as plt

inputFilePath = "D://My Python Project//File 2//sales.csv"
outputFilePath= "D://My Python Project//File 2//change_sales.csv"

# Read the CSV file
with open(inputFilePath, 'r') as file:
    lines = file.readlines()
# print('type : ')
# print(type(lines))
# print('data : ')
# print(lines)
# Extract sales and expenditure data
header = lines[0].strip().split(',')
data = [line.strip().split(',') for line in lines[1:]]
sales_index = header.index('sales')
month_index = header.index('month')
month = [(row[month_index]) for row in data]
expenditure_index = header.index('expenditure')
sales = [float(row[sales_index]) for row in data]
expenditure = [float(row[expenditure_index]) for row in data]

# Display sales data vertically
print("Sales data:")
for sale in sales:
    print(sale)

# Calculate total yearly sales
total_sales = sum(sales)
print('Total yearly sales:')
print(total_sales)

# Calculate monthly average sales
average_sales = total_sales / len(sales)
print('Monthly average sales:')
print(average_sales)

# Calculate lowest sales month
min_sales = min(sales)
print('Lowest sales per month:')
print(min_sales)

# Calculate highest sales month
max_sales = max(sales)
print('Highest sales per month:')
print(max_sales)

# Calculate total yearly expenditure
total_expenditure = sum(expenditure)
print('Total yearly expenditure:')
print(total_expenditure)

# Calculate monthly average expenditure
average_expenditure = total_expenditure / len(expenditure)
print('Monthly average expenditure:')
print(average_expenditure)

# Calculate percentage change in monthly sales
percent_sale=[]
for i in range(len(sales)):
    if i > 0:
        perChange_sales = (sales[i] - sales[i - 1]) / sales[i - 1] * 100
    else:
        perChange_sales=0
    percent_sale.append(perChange_sales)
    print(perChange_sales)

print("Change in sales:")
salesChanges= []
for change in percent_sale:
    change_sales = round(change, 2)
    salesChanges.append(change_sales)
    print(change_sales)

# Calculate percentage change in monthly expenditure
change_expenditure = [(expenditure[i] - expenditure[i-1]) / expenditure[i-1] * 100 if i > 0 else 0 for i in range(len(expenditure))]
change_expenditure = [round(change, 2) for change in change_expenditure]

# Display change in expenditure
print("Change in expenditure:")
for change in change_expenditure:
    print(change)

# Write changes to a new CSV file
with open(outputFilePath, 'w') as file:
    file.write(','.join(header + ['change_sales', 'change_expenditure']) + '\n')
    for i in range(len(data)):
         file.write(','.join(data[i] + [str(salesChanges[i]), str(change_expenditure[i])]) + '\n')


plt.plot(month, change_expenditure,label = 'expenditure')
plt.plot(month, salesChanges, label='sales')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Change in Expenditure and sales ')
plt.legend()
plt.show()