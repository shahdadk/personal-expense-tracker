

class CSVReader:
    """This class handles reading CSV files."""
    def __init__(self):
        pass
    
    def read(self, csv_file: str) -> list:
        """Description:
        This method reads your CSV file and returns the content as a list.
        @param csv_file - name of the csv file. 
        @returns a transaction list.
        """
        transaction_list=[]
        with open(csv_file) as expenses:
            for row in expenses:
                transaction_list.append(row.split(","))
        
        return transaction_list
    
""" Hints:

1. Import categories identifiers through CSV (Dont hardcode anything) DONE

2. Each transaction will belong in a category, each category is a list of transactions DONE

3. For each category return three sets TOtal, Average, and Percentage of TOt DOne

4. Refer to SCreenshot in dsicord for method input and output DONE

5. Create a instance level variable for total transactions (when calculating percetnage) in the init constructor Ddid differently

6. read w3 schools 


"""

class TransactionCategorizer:
    """This class categorizes transactions."""
    def __init__(self, TransactionList: list, NecessityList: list, FoodList: list):
        self.TransactionList = TransactionList
        self.NecessityList = NecessityList
        self.FoodList = FoodList

    def Categorize(self) -> tuple[float, float, float]:
        """Description:
        This method adds your transactions into three categories.
        @returns three floats: food, necessities, and total spending. 
        """
        food_tot=0
        necessity_tot=0
        total=0
        foodCounter=0
        necessityCounter=0
        

        for x in self.TransactionList[1:]:
            x[2] = x[2].lower()

            for y in range(0,len(self.FoodList[0])):
                if self.FoodList[0][y] in x[2]:
                    food_tot+=float(x[3])
                    foodCounter+=1
            
            for y in range(0,len(self.NecessityList[0])):

                if self.NecessityList[0][y] in x[2]:
                    necessity_tot +=float(x[3])
                    necessityCounter+=1
                
            total+= float(x[3])

        averageFood=food_tot/foodCounter

        averageNecessity=necessity_tot/necessityCounter

        miscTot=total-food_tot-necessity_tot

        averageMisc=miscTot/(len(transactionList)-foodCounter-necessityCounter)

        foodPercent=food_tot/total*100  

        necessityPercent=necessity_tot/total*100

        miscPercent=miscTot/total*100


        return food_tot, averageFood, foodPercent, necessity_tot, averageNecessity, necessityPercent, miscTot, averageMisc, miscPercent, total

class Printer:
    
    def __init__(self, totals):
        self.totals=totals
    
    def PrintCategories(self):
        print("                 Total   |  Average  |   Percentage of Total")
        print(f"Food Category:   {totals[0]:.2f}      {totals[1]:.2f}        {totals[2]:.0f}") 
        print(f"Necessity Category: {totals[3]:.2f}    {totals[4]:.2f}    {totals[5]:.0f}")
        print(f"Misc Category:    {totals[6]:.2f}    {totals[7]:.2f}         {totals[8]:.0f}")

csvReader = CSVReader()

transactionList = csvReader.read('ExpensesPriv.csv')

necessityList = csvReader.read('necessityList.csv')

foodList = csvReader.read('foodList.csv')

CategorizorInstance = TransactionCategorizer(transactionList, necessityList, foodList)

totals = CategorizorInstance.Categorize()

printerInstance= Printer(totals)

Run=printerInstance.PrintCategories()

