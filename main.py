

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

        for x in self.TransactionList[1:]:
            x[2] = x[2].lower()

            for y in range(0,len(list_food)):
                if self.FoodList[y] in x[2]:
                    food_tot+=float(x[3])
            
            for y in range(0,len(self.NecessityList)):

                if self.NecessityList[y] in x[2]:
                    necessity_tot +=float(x[3])
                
            total+= float(x[3])

        return food_tot, necessity_tot, total

class Printer:
    
    def __init__(self, totals):
        self.totals=totals
    
    def PrintCategories():
        print("         Total  |  Average  |  Percentage of Total")
        x=1
        for x in totals:

            print("Category "+str(x)) 
            x=+1
        


list_of_necessity=["amazon","esso","hopper","uw","sobeys","petro","ziggy","shopper","home"]

list_food=["domino","popeye","tim","mcdonald"]


csvReader = CSVReader()



TransactionList = csvReader.read('ExpensesPriv.csv')

TransactionList2 = csvReader.read('ExpensesPriv2.csv')


CategorizorInstance = TransactionCategorizer(TransactionList, list_of_necessity, list_food)

totals = CategorizorInstance.Categorize()








# print ("_____________________________________________________________\n")
# print(f"Your total spending on food this month is {food_tot:.2f}")
# print(f"Your total spending on necessities this month is {necessity_tot:.2f}")
# print(f"You have a total of {total-food_tot-necessity_tot:.2f} in the misc category")
# print ("_____________________________________________________________")]