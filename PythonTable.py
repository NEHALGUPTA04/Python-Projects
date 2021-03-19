from prettytable import PrettyTable
Table = PrettyTable(["Student","Class","Subject","Branch"])
Table.add_row(["Nehal","A","Python","CSE"])
Table.add_row(["Granth","B","Java","IT"])
Table.add_row(["Ajay","C","DBMS","AI"])
Table.add_row(["Nilesh","D","OS","DS"])
Table.add_row(["Namami","E","C++","IOT"])

print(Table)