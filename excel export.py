# import openpyxl
# book=openpyxl.load_workbook(r"C:\Users\USER\Desktop\Copy of Calculate Sales Commission(1).xlsx")
# shet=book.active
# cell=shet.cell(row=12,column=3)
# print(cell.value)
# for column in shet.iter_cols():
#     for cell in column:
#         print(cell.value)


"""use excel"""
# import pandas as pd
# sajith=pd.read_excel(r"C:\\Users\\USER\Desktop\pythonexcel2.xlsx")
# print(sajith)
# #
# import pandas as pd
#
# # Set display options to show all rows and columns
# pd.set_option()
# pd.set_option()

# Read the Excel file
# sajith = pd.read_excel(r"C:\Users\USER\Desktop\pythonexcel2.xlsx")
#
# # Print the DataFrame
# print(sajith)


"""extract excel"""

# import openpyxl
# excel=openpyxl.load_workbook(r"C:\Users\USER\Desktop\Copy of Calculate Sales Commission(1).xlsx")
# shet=excel.active
#
# for row in shet.iter_rows():
#     for cell in row:
#         print(cell.value,end=" ")


#
# import pandas as pd
#
# sajith1=pd.read_excel(r"C:\Users\USER\Desktop\Copy of Calculate Sales Commission(1).xlsx",nrows=20)
# print(sajith1)




#
# from openpyxl import load_workbook
#
# work_book = load_workbook("C:\\Users\\USER\\Documents\\feb 121.xlsx")
# sheet1 = work_book["sheet1"]
# data_sheet1 = []
#
# for row in sheet1.iter_rows():
#     data_row = []
#     for cell in row:
#         data_row.append(cell.value)  # Append the value of the cell, not the cell object itself
#     data_sheet1.append(data_row)
#
# sheet2 = work_book["sheet2"]
# data_sheet2 = []
#
# for row in sheet2.iter_rows():
#     data_row = []
#     for cell in row:
#         data_row.append(cell.value)
#     data_sheet2.append(data_row)
#
# for row in data_sheet1:
#     print(row)
#
# for row in data_sheet2:
#     print(row)
