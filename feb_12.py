# from openpyxl import load_workbook
#
# workbook = load_workbook("C:\\Users\\USER\Documents\\feb 121.xlsx")
#
# sheet1 = workbook['sheet1']
# data_sheet1 = []
#
# for row in sheet1.iter_row(values_only=True):
#     data_sheet1.append(data_row)
#
# sheet2 = workbook['sheet2']
# data_sheet2 = []
#
# for row in sheet2.iter_row(values_only=True):
#     data_sheet2.append(data_row)
#
# print("data from sheet1:")
# for row in data_sheet1:
#     print(row)
#
# print("data from sheet2:")
# for row in data_sheet2:
#     print(row)
#

# from openpyxl import load_workbook
# work_book = load_workbook("C:\\Users\\USER\\Documents\\feb 8th.csv")
# sheet1 = work_book["Sheet1"]
# data_sheet1 = []
#
# for row in sheet1.iter_rows():
#     data_row = []
#     for cell in row:
#         data_row.append(cell.value)
#     data_sheet1.append(data_row)
#
# sheet2 = work_book["Sheet2"]
# data_sheet2 = []
#
# for row in sheet2.iter_rows():
#     data_row = []
#     for cell in row:
#         data_row.append(cell.value)
#     data_sheet2.append(data_row)
#
# print("Data from sheet1")
# for row in data_sheet1:
#     print(row)
#
# print("Data from sheet2")
# for row in data_sheet2:
#     print(row)

#
# from openpyxl import load_workbook
#
# sheet2 = work_book["Sheet2"]
# data_sheet2 = []
#
# for row in sheet2.iter_rows():
#     data_row = []
#     for cell in row:
#         data_row.append(cell.value)
#     data_sheet2.append(data_row)
#
# # print("Data from sheet1")
# for row in data_sheet1:
#     print(row)
#
# # print("Data from sheet2")
# for row in data_sheet2:
#     print(row)
# work_book = load_workbook("C:\\Users\\USER\\Documents\\pythonexcelll.xlsx")
# sheet1 = work_book["Sheet1"]
# data_sheet1 = []
#
# for row in sheet1.iter_rows():
#     data_row = []
#     for cell in row:
#         data_row.append(cell.value)
#     data_sheet1.append(data_row)

#







####
# from openpyxl import load_workbook
#
# work_book=load_workbook("C:\\Users\\USER\Documents\\feb 12.xlsx")
# sheet1=work_book["sheet1"]
# data_sheet1=[]
#
# for row in sheet1.iter_row():
#     data_row=[]
#     for cell in row():
#         data_row.append(cell.value)
#     data_sheet1.append(data_row)
#
#
# sheet2=work_book["sheet2"]
# data_sheet2=[]
#
#
# for row in sheet2.iter_row():
#     data_row=[]
#     for cell in row():
#         data_row.append(cell.value)
#     data_sheet2.append(data_row)
#
#
# for row in data_sheet1:
#     print(row)
#
# for row in data_sheet2:
#     print(row)
#
#
################################################################
# import openpyxl
# book=openpyxl.load_workbook("C:\\Users\\USER\\Documents\\feb.xlsx")
# sheet=book.active
# # cell=sheet.cell(row=2,column=1)
# # print(cell.value)
# for column in sheet.iter_cols():
#     for cell in column:
#         print(cell.value)


#################################################################################################################3


