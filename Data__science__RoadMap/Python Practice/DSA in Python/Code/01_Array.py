# Array is a method of clubbing multiple entities of similar type into a larger group.

# In python, list is implemented as dynamic array. In other languages like java, c++ we have static and dynamic arrays both.

'''
# Exercise: Array DataStructure

1. Let us say your expense for every month are listed below,
	1. January -  2200
 	2. February - 2350
    3. March - 2600
    4. April - 2130
    5. May - 2190

Create a list to store these monthly expenses and using that find out,

    1. In Feb, how many dollars you spent extra compare to January?
    2. Find out your total expense in first quarter (first three months) of the year.
    3. Find out if you spent exactly 2000 dollars in any month
    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    5. You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this

'''
# Solution 

# creating a list of monthly expences
from platform import mac_ver


monthly_expenses = [2200,2350,2600,2130,2190]

# Question 1 -> Answer : 
print("\nIn Feb, " +str(monthly_expenses[1]-monthly_expenses[0]) + " dollars you spent extra compare to January")

# Question 2 -> Answer : 
print("\nMy total expense in first quarter (first three months) of the year " + str(monthly_expenses[0]+monthly_expenses[1]+monthly_expenses[2]))

# Question 3 -> Answer :
flag = False 
for index in monthly_expenses:
    if index == 2000:
        flag = True

if flag:
    print("\nYou Spent exactly 2000 dollars in a month")
else:
    print("\nYou never Spent exactly 2000 dollars in any month.")

# Question 4 -> Answer : 
monthly_expenses.append(1980)
print("\nJune expense is 1980. So new monthly expense list is : " + str(monthly_expenses))

# Question 5 -> Answer : 
new_april_expense = monthly_expenses[3]-200
monthly_expenses.insert(3,new_april_expense)
print("\nI returned an item that you bought in a month of April and got a refund of 200$. So new monthly expense list is : " + str(monthly_expenses))

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in monthly_expenses)