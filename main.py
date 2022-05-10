#I have taken the amount that u will deposit as n1
n1 = int(input("Enter your amount \n"))

#I have imported preetty library
from prettytable import PrettyTable

#Adding rows to the table

myTable = PrettyTable(["Coin" , "percentage" , "value"])
myTable.add_row(["Bitcoin" , "0.4" , n1*0.4])
myTable.add_row(["Etherum" , "0.15" , n1*0.15])
myTable.add_row(["Aave" , "0.375" , n1*0.0375])
myTable.add_row(["Compound" , "0.375" , n1*0.0375])
myTable.add_row(["Uniswap" , "0.375" , n1*0.0375])
myTable.add_row(["Pancake swap" , "0.375" , n1*0.0375])
myTable.add_row(["Biance" , "0.1" , n1*0.1])
myTable.add_row(["Cardano" , "0.05" , n1*0.05])
myTable.add_row(["Solana" , "0.05" , n1*0.05])
myTable.add_row(["Decentralizer" , "0.01" , n1*0.01])
myTable.add_row(["Litecoin" , "0.025" , n1*0.025])
myTable.add_row(["Dash" , "0.025" , n1*0.025])
myTable.add_row(["Dogecoin" , "0.01" , n1*0.01])
myTable.add_row(["Bitcoin cash" , "0.02" , n1*0.01])
myTable.add_row(["Tether" , "0.01" , n1*0.01])
print(myTable)
















































# for i in range(1):
#     print(1 * 0.4)
#
#
#









