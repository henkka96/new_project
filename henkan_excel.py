import xlsxwriter
"Moro moro"
"Heippa heippa"
workbook = xlsxwriter.Workbook('Hello.xlsx')

worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()