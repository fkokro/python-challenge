#import relevant libraries
import os
import csv

#To be safe set path for working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Set file path
csvpath = os.path.join("budget_data.csv")


#List of stored data
date = []
Profit_Losses = []
change_list = []
total_change = 0
Total_Profit_Losses = 0
value = 0
change = 0

#Open and read csv file
with open(csvpath, newline='') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')

    
    #Store header row   
    budget_header = next(budget_data) 
    

    for r in budget_data:
        
        #Create list for column attributes
        date.append(r[0])
        Profit_Losses.append(r[1])
       
       #Sum Profit/Losses Column
        Total_Profit_Losses += int(r[1])

        #Stores the total change over the entire period
        change = int(r[1])-value
        change_list.append(change)
        value = int(r[1])

    #remove first index from total change list
    change_list.pop(0)
    
    #The number of months in the data set
    Total_months =len(list(date))
    
    #The average total change over the entire period
    avg_change = round(sum(change_list)/len(list(change_list)), 2)
    
    #The greatest increase
    maxTri = max(change_list)
    maxTri_index = change_list.index(maxTri)
    maxTri_date = date[maxTri_index]

    
    #The greatest decreases
    minTri = min(change_list)
    minTri_index = change_list.index(minTri)
    minTri_date = date[minTri_index]
    
    
    
#Analysis
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(Total_months)}")
print(f"Total: ${str(Total_Profit_Losses)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {maxTri_date} (${str(maxTri)})")
print(f"Greatest Decrease in Profits: {minTri_date} (${str(minTri)})")

#Export analysis to text file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(Total_months)}")
line4 = str(f"Total: ${str(Total_Profit_Losses)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {maxTri_date} (${str(maxTri)})")
line7 = str(f"Greatest Decrease in Profits: {minTri_date} (${str(minTri)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

   
    