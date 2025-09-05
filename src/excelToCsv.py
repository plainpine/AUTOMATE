#! python3
# excelToCsv.py
import os
import csv
import openpyxl

def excelToCsv(folder):
    os.chdir(folder)

    for excelFile in os.listdir("."):
        # xlsxファイルでなければスキップする
        if not excelFile.endswith('xlsx'):
            continue
        wb = openpyxl.load_workbook(excelFile)

        for sheet_name in wb.sheetnames:
            # ワークブックのシートをループする
            sheet = wb[sheet_name]

            # Excelファイル名とシート名からCSVファイル名を作る
            csvFilename = excelFile.split('.')[0]+'_'+sheet.title+'.csv'
            csvFileObj = open(csvFilename, 'w', newline='')

            # CSVファイル用にcsv.writerオブジェクトを生成する
            csvWriter = csv.writer(csvFileObj)

            # シートの行をループする
            for rowObj in sheet.rows:
                row_data = []    # セルをこのリストに追加する
                # 行のセルをループする
                for cellObj in rowObj:
                    # セルをrow_dataに追加する
                    row_data.append(cellObj.value)
                # row_dataをcsvファイルに書き出す
                csvWriter.writerow(row_data)

            csvFileObj.close()

if __name__ == "__main__":
    excelToCsv('excelSpreadsheets')
