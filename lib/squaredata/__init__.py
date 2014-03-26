#datachef.squaredata

#FIXME: This will be moved to data chef, refer from there
def dict_from_xls(f, sheet_index=0, start_row=1):
    import mmap
    import xlrd
    data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    book = xlrd.open_workbook(file_contents=data)
    sheet = book.sheet_by_index(sheet_index)

    def item(i, j):
        return (sheet.cell_value(0, j), sheet.cell_value(i, j))

    return ( dict(item(i, j) for j in range(sheet.ncols)) \
                 for i in xrange(start_row, sheet.nrows) )


