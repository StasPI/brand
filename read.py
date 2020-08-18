import xlrd

excel_link = r'A:\prod.xlsx'


def reader(excel_link, table_name):
    rb = xlrd.open_workbook(excel_link)
    sheet = rb.sheet_by_name(table_name)
    return [sheet.row_values(rownum) for rownum in range(sheet.nrows)]


a = reader(excel_link, 'Бренд')
b = reader(excel_link, 'Продукт')
print(a[1])
print(b[1])