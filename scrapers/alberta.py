from bs4 import BeautifulSoup
import requests
from openai import OpenAI
import os
import PyPDF2
import re
import fitz  # PyMuPDF

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(organization=os.environ.get('ORG'), api_key=os.environ.get('AI'))


def download_pdf(url):
    response = requests.get(url)
    text = ""
    if response.status_code == 200:
        pdf_data = response.content
        pdf_document = fitz.open(stream=pdf_data, filetype="pdf")
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
            # print(f"Page {page_num + 1}:")
            # print(text)
            # print("\n")
    else:
        print("pdf download failed")
    print("doc downloaded")
    return text

# def read_pdf(file_path):
#     with open(file_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ""
#         for page in range(1, len(reader.pages) - 1):
#             text += reader.pages[page].extract_text()
#     return text

def get_summary(keywords):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a PDF analyzer " +
            "Your job is to come up with a short summary under 100 words "+ 
            "of the given pdf by going on the link given"},
            {"role": "user", "content": 
             "Give me a summary of the PDF in the following link:" + keywords}
        ]
    )
    return response.choices[0].message.content

def extalberta():
    website = f"https://www.assembly.ab.ca/assembly-business/assembly-dashboard?legl=50000&session=1&sectiona=a&btn=e&anchor=a20240529#"
    response = requests.get(website, headers={"User-Agent": "countable"})
    bills = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        billz = soup.find_all("div", class_=["bill billgt", "bill billpb", "bill billpr"])
        for bill in billz:
            pdf = bill.find("div", class_="doc_item")
            title = pdf.get_text().replace('\xa0', ' ')
            url = pdf.find('a').get('href')
            date = bill.find("div", class_="collapse")
            date = date.find_all("div")
            Status_reading = None
            Date_of_vote = None
            RA = None
            local_file_path = "pdf.pdf"
            pdf_text = download_pdf(url)
            # pdf_text = read_pdf(local_file_path)
            summary = pdf_text.replace(",", " ").replace("\n", " ").replace("\t", " ").replace("\s", " ")
            summary = re.sub(r'[\s\n\t]', ' ', summary)
            original = summary
            if (len(summary) > 30000):
                ind = len(summary) // 5
                summary = f"{get_summary(summary[:ind])}{get_summary(summary[ind:ind*2])}{get_summary(summary[ind*2:ind*3])}{get_summary(summary[ind*3:ind*4])}{get_summary(summary[ind*4:])}".replace(",", " ").replace("\n", " ").replace("\t", " ").replace("\s", " ")
                summary = re.sub(r'[\s\n\t]', ' ', summary)
            else:
                summary = get_summary(summary).replace(",", " ").replace("\n", " ").replace("\t", " ").replace("\s", " ")
                summary = re.sub(r'[\s\n\t]', ' ', summary)
            
            # if os.path.exists(local_file_path):
            #     os.remove(local_file_path)
            # else:        
            #     print("File error")
            
            for dat in date:
                if (dat.get('class') is not None and len(dat.get('class')) > 1 and 'b_entry'.__eq__(dat.get('class')[0])):
                    if (dat.get('class')[1].replace('b_','') != "CF"):
                        Date_of_vote = dat.find("div", class_="b_date").get_text().replace(',', ' ').replace('on ', '')
                        Status_reading = dat.find("div", class_="b_status").get_text().replace(',', ' ')
                        # if (Status_reading.__eq__("outside of House sitting")):
                        #     Status_reading = "Yes"
                        # else:
                        #     Status_reading = "No"
                        RA = dat.get('class')[1].replace('b_','')

            Gov_lv= 'Provincial'
            Jurisdiction = 'Alberta'
            bill_data = {
                'title': title,
                'url': url,
                'RA': RA,
                'Date_of_Vote': Date_of_vote, 
                'Status_Reading': Status_reading,
                'Original': original[:5000],
                'Summary': summary,
                'Gov_Level': Gov_lv,
                'Jurisdiction': Jurisdiction
            }

            bills.append(bill_data)
    return bills

        