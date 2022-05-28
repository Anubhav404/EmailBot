# # # Program extracting first column
# # import xlrd
# # import pandas
# # import csv
# # loc = ("C:/Users/Anubhav soni/anubhav/Bot-A-Thon/ExcelFile.xlsx")
# # # loc = csv.reader(loc)
# # wb = xlrd.open_workbook(loc)
# # sheet = wb.sheet_by_index(0)
# # sheet.cell_value(0, 0)
# #
# # for i in range(sheet.nrows):
# #     print(sheet.cell_value(i, 0))
#
#
# import pandas as pd
# # import sys
# workbook = pd.read_excel('ExcelFile.xlsx')
# workbook.head()
#
# # workbook = pd.read_excel('ExcelFile.xlsx', encoding=sys.getfilesystemencoding())
# print(workbook['Name'].loc[0])


# import os
# import pandas as pd
# import openpyxl
# os.getcwd()
# os.chdir(r"C:\Users\Anubhav soni\anubhav\Bot-A-Thon")
#
# file = 'ExcelFile.xlsx'
# data = pd.ExcelFile(file)
# print(data.sheet_names)
# df = data.parse('Input File 2')
# df.info
# df.head(10)
#
# ps = openpyxl.load_workbook('ExcelFile.xlsx')
# sheet = ps['Input File 2']
# print(sheet.max_row)
#
# emails = []
# for row in range(5, sheet.max_row + 1):
#
#     email = sheet['D' + str(row)].value
#     emails.append(email)
#     # cost_per_pound = sheet['C' + str(row)].value
#     # pounds_sold = sheet['D' + str(row)].value
#     # total_sales = sheet['E' + str(row)].value
#
# print(emails)
# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('FeedbackForm1.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
