from scrapers.alberta import *
import os

def get_bills(keyword):
    alberta = extalberta(keyword)
    bills = alberta
    return bills

def csvfile(filename, bills):
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    print(downloads_path)
    file_path = os.path.join(downloads_path, f"{filename}.csv")
    file = open(file_path, "w", encoding="utf-8-sig")
    file.write ("Title, PDF_url, Status_Reading, Date_of_Vote, Status_Passed, Bill_Summary_Original, Bill_Summary, Gov_Level, Jurisdiction \n")
    for bill in bills:
        file.write(f"{bill['title']}, {bill['url']}, {bill['RA']}, {bill['Date_of_Vote']}, {bill['Status_Reading']}, {bill['Original']},{bill['Summary']}, {bill['Gov_Level']}, {bill['Jurisdiction']}\n")
    file.close()