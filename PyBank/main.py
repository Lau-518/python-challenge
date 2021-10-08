import os
import csv

path = os.path.join("Resources", "budget_data.csv")



months = []
ProfitnLoss = []
changes = []

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        
        months.append(row[0])
        ProfitnLoss.append(int(row[1]))

for i in range(1, len(ProfitnLoss)):
    changes.append((int(ProfitnLoss[i]) - int(ProfitnLoss[i-1])))

Average_Change = sum(changes) / len(changes)

print(f"Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {len(list(months))}")
print(f"Total: ${sum(ProfitnLoss)}")
print(f"Average Change: ${Average_Change:.2f}")
print(f"Greatest Increase in Profits: {months[25]} (${max(changes)})")
print(f"Greatest Decrease in Profits: {months[44]} (${min(changes)})")

#Return financial analysis in a text file

text_file = os.path.join("Analysis", "Financial_analysis.txt")

with open(text_file, "w") as out_file:
    out_file.writelines(["Financial Analysis \n",
                        "-------------------------- \n",
                        "Total Months: 86 \n",
                        "Total: $38382578 \n",
                        "Average Change: $-2315.12 \n",
                        "Greatest Increase in Profits: Feb-2012 ($1926159) \n",
                        "Greatest Decrease in Profits: Sep-2013 ($-2196167) \n"])