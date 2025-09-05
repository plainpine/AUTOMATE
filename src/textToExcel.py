"""
テキストファイルからExcelファイルに変換する
注意:
    * テキストファイル配置フォルダ  ./toExcelFiles/
    * 出力ファイル名          textToExcel.xlsx

"""
def main():
    import openpyxl
    import os

    FOLDER = "./toExcelFiles/"

    # Open workbook
    wb = openpyxl.Workbook()
    sheet = wb.active

    # Get list of files
    filelist = os.listdir(FOLDER)
    filelist.sort()

    # Open file
    for file in filelist:
        with open(FOLDER + file) as fileObj:
            index = 1
            for line in fileObj:
                # Transpose line into relevant workbook column
                sheet.cell(row=index, column=(filelist.index(file) + 1)).value = line.strip()
                index += 1

    # Save workbook
    wb.save("textToExcel.xlsx")

if __name__ == '__main__':
    main()
