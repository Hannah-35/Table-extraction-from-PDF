import camelot

tables = camelot.read_pdf('CCAA.2016.7813856.pdf', pages='5')
print(tables)
tables.export('CCAA.2016.7813856.pdf', f='csv', compress=True)
tables[0].to_csv('CCAA.2016.7813856.pdf')
print('done')

