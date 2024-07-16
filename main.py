empty_list=[]

with open('ExpensesPriv.csv') as Expenses:
    for row in Expenses:
        empty_list.append(row.split(","))


misc_tot=0
food_tot=0
necessity_tot=0
total=0

list_of_necessity=["amazon","esso","hopper","uw","sobeys","petro","ziggy","shopper","home",]

list_food=["domino","popeye","tim","mcdonald"]

for x in empty_list[1:]:
    x[2] = x[2].lower()

    for y in range(0,len(list_food)):
        if list_food[y] in x[2]:
            food_tot+=float(x[3])
    
    for y in range(0,len(list_of_necessity)):

        if list_of_necessity[y] in x[2]:
            necessity_tot +=float(x[3])
        
    total+= float(x[3])

    

print ("_____________________________________________________________\n")
print("Your total spending on food this month is " + str(food_tot))
print("Your total spending on necessities this month is " + str(necessity_tot))
print("You have a total of " + str(total-food_tot-necessity_tot) + " in the misc category")
print ("_____________________________________________________________")