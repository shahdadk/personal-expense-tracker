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
                transaction_list.append(row.strip("\n").split(","))
        
        return transaction_list

class TransactionCategorizer:
    """This class categorizes transactions."""
    def __init__(self, transactionList: list, categoryList: list):
        self.transactionList = transactionList
        self.categoryList = categoryList

    def categorize(self) -> list:
        """Description:
        This method adds your transactions into three categories.
        @returns three floats: food, necessities, and total spending. 
        """
        totalOfTransactions=0
        totalCount=len(self.transactionList)-1

        categoryStats={"misc": {"count": 0, "average" : 0, "percentage" : 0, "total" : 0}} 

        for category in self.categoryList:
            categoryStats[category[0]] = {"count": 0, "average" : 0, "percentage" : 0, "total" : 0}
        
        for transactions in self.transactionList[1:]:
            transactions[2] = transactions[2].lower()

            for category in self.categoryList:
                    
                for y in range(0,len(category[1])):
                    if category[1][y] in transactions[2]:
                        categoryStats[category[0]]["total"]+=float(transactions[3])
                        categoryStats[category[0]]["count"]+=1
                
            totalOfTransactions += float(transactions[3])

        categoryCount = 0
        categoryTotal = 0

        for key in categoryStats:
            if key != "misc":
                categoryStats[key]["average"] = categoryStats[key]["total"] / categoryStats[key]["count"]
                categoryStats[key]["percentage"] = categoryStats[key]["total"] / totalOfTransactions * 100
                categoryCount += categoryStats[key]["count"]
                categoryTotal += categoryStats[key]["total"]
        
        categoryStats["misc"]["total"] = totalOfTransactions - categoryTotal
        categoryStats["misc"]["percentage"] = categoryStats["misc"]["total"] / totalOfTransactions
        categoryStats["misc"]["count"] = totalCount - categoryCount
        categoryStats["misc"]["average"] = categoryStats["misc"]["total"] / categoryStats["misc"]["count"]
        
        return categoryStats

    def printCategories(self, categoryStats):
        """Description: 
        This method prints a table of your spending categories. 
        @param categoryStats: which is all the categories and their respective stats. 
        """
        print("Category    | Count | Total     | Average   | Percentage of Total")
        for category in categoryStats:
            percent = categoryStats[category]["percentage"]
            count = categoryStats[category]["count"]
            total = categoryStats[category]["total"]
            average= categoryStats[category]["average"]

            print(f"{category:<11} | {count:>5} | ${total:<8,.2f} | ${average:<8,.2f} | {percent:05.2f}%")
    
def getCategories(categoryFiles):
    """Description:
    This method gets the categories from the category files. 
    @param categoryFiles: list of file names in categoryFiles.csv
    @returns categoryList: a list of categories and their respective entries. 
    """
    categoryList=[]
    csvReader = CSVReader()
    for x in categoryFiles:
        categoryList.append([x[0], csvReader.read(x[1])[0]])
    return categoryList

def main():
    csvReader = CSVReader()

    transactionList = csvReader.read('ExpensesPriv.csv')

    categoryFiles=csvReader.read('categoryFiles.csv')

    categoryList= getCategories(categoryFiles)

    categorizorInstance = TransactionCategorizer(transactionList, categoryList)

    categoryStats = categorizorInstance.categorize()

    categorizorInstance.printCategories(categoryStats)

if __name__ == "__main__":
    main()