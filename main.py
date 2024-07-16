empty_list=[]

with open('ExpensesPriv.csv') as Expenses:
    for row in Expenses:
        empty_list.append(row.split(","))


food_tot=0
necessity_tot=0
total=0

list_of_necessity=["amazon","esso","hopper","uw","sobeys","petro","ziggy","shopper","home"]

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
print(f"Your total spending on food this month is {food_tot:.2f}")
print(f"Your total spending on necessities this month is {necessity_tot:.2f}")
print(f"You have a total of {total-food_tot-necessity_tot:.2f} in the misc category")
print ("_____________________________________________________________")