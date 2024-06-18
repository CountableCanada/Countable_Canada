from scrapers.alberta import *
from scrapers.albertavotes import *
import os

def get_votes():
    alberta = votescrapte()
    votes = alberta
    return votes

def csvfile_vote(filename, votes):
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    print(downloads_path)
    file_path = os.path.join(downloads_path, f"{filename}Votes.csv")
    file = open(file_path, "w", encoding="utf-8-sig")
    file.write ("Bill_number, Bill_Title, Date_of_Vote, RepName, RepVote, Status, Province\n")
    for vote in votes:
        file.write(f"{vote['num']}, {vote['title']}, {vote['Date_of_Vote']},{vote['RepName']}, {vote['RepVote']}, {vote['Result']}, {vote['province']}\n")
    file.close()

def get_bills():
    alberta = extalberta()
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