# from bs4 import BeautifulSoup
# import requests

# def votescrapte ():
#     website = "https://www.assembly.ab.ca/members/members-of-the-legislative-assembly"
#     response = requests.get(website, headers={"User-Agent": "countable"})
#     votes = []
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, "html.parser")
#         members = soup.find_all("div", class_=["item"])
#         for mem in members:
#             url = mem.find('a')
#             name = None
#             if (url is not None):
#                 name = url.get_text()
#                 url = url.get('href')
#                 votes.append(voteCollect(name, url))


# def voteCollect(name, url):
#     website = f"https://www.assembly.ab.ca/{url}"
#     response = requests.get(website, headers={"User-Agent": "countable"})
#     votes = []
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, "html.parser")
#         votess = soup.find_all("div", class_="division mla_table")
#         for vote in votess:
#             Date = vote.find("div", class_="col1").find(class_="data").get_text()
#             print(Date)
#             Title = vote.find("div", class_="col2").find(class_="data").get_text()
#             print(Title)
#             YorN = vote.find("div", class_="col3").find(class_="data").get_text()
#             print(YorN)
#             resu = vote.find("div", class_="col4").find(class_="data").get_text()
#             print(resu)
#         exit()
#         # for vote in votess:
#         #     url = vote.find('a')
#         #     name = None
#         #     if (url is not None):
#         #         name = url.get_text()
#         #         url = url.get('href')
#         #     votes.append(voteCollect(name, url))

# votescrapte()