# import csv
#
# def save_to_file(jobs):
#     file = open("jobs.csv", mode='w', newline='', encoding="utf-8")
#     writer = csv.writer(file)
#     writer.writerow(["title", "company", "location", "link"])
#     for job in jobs:
#         writer.writerow(list(job.values()))
#     return

import openpyxl

def save_to_file(jobs):
    wb = openpyxl.Workbook() # 임시로 엑셀 파일 생성
    sheet = wb.active # 활성화된 시트 불러오기
    sheet.append(["title", "company", "location", "link"])
    for job in jobs:
        sheet.append(list(job.values()))
    wb.save('jobs.xlsx') # 파일 저장
    return
