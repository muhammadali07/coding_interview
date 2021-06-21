#I still need this to take multiple datasets and assign a sheet to each.


def xls(*out, "*"sheet):
    import os, errno
    import spss
    import csv
    import xlwt

#Takes the active dataset in spss and saves off a CSV file.
    spss.Submit(r"""
    SAVE TRANSLATE OUTFILE= '%s.csv'
    /TYPE=CSV /ENCODING='Locale' 
    /MAP /REPLACE /FIELDNAMES 
    /CELLS=VALUES.
    """ % (out))
   
#formats CSV and adds excel style formatting
    DATA=list()
    with open(out+'.csv') as f:
        reader=csv.reader(f)
        headings = f.next().split(",")
        for row in reader:
            DATA.append(row)
    print headings
    wb = xlwt.Workbook()
    ws = wb.add_sheet(sheet)


# Add headings with styling and froszen first row
    heading_xf = xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center')

    rowx = 0
    ws.set_panes_frozen(True) # frozen headings instead of split panes
    ws.set_horz_split_pos(rowx+1) # in general, freeze after last heading row
    ws.set_remove_splits(True) # if user does unfreeze, don't leave a split there
    for colx, value in enumerate(headings):
        ws.write(rowx, colx, value, heading_xf)

    for i, row in enumerate(DATA):
        for j, col in enumerate(row):
            ws.write(i+1, j, col)
#ws.col(1).width = 256 * max([len(row[0]) for row in DATA])
    wb.save(out+'.csv')