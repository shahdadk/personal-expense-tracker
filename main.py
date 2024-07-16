empty_list=[]

with open('ExpensesPriv.csv') as Expenses:
    for row in Expenses:
        empty_list.append(row.split(","))


misc_tot=0
food_tot=0
necessity_tot=0

for x in range(1, len(empty_list)):
    empty_list[x][2] = empty_list[x][2].lower()

    if "mcdonald" in empty_list[x][2] or "domino" in empty_list[x][2] or "popeye" in empty_list[x][2] or "tim" in empty_list[x][2]:
        food_tot+=float(empty_list[x][3])

    elif "amazon" in empty_list[x][2] or "esso" in empty_list[x][2] or "hopper" in empty_list[x][2] or "uw" in empty_list[x][2] or "sobeys" in empty_list[x][2] or "petro" in empty_list[x][2] or "ziggy" in empty_list[x][2] or "shopper" in empty_list[x][2] or "home" in empty_list[x][2]:
        necessity_tot+=float(empty_list[x][3])
    
    else:
        misc_tot+=float(empty_list[x][3])


print ("_____________________________________________________________\n")
print("Your total spending on food this month is " + str(food_tot))
print("Your total spending on necessities this month is " + str(necessity_tot))
print("You have a total of " + str(misc_tot) + " in the misc category")
print ("_____________________________________________________________")