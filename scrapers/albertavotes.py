from bs4 import BeautifulSoup
import requests

def votescrapte ():
    website = "https://www.assembly.ab.ca/members/members-of-the-legislative-assembly"
    response = requests.get(website, headers={"User-Agent": "countable"})
    votes = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        members = soup.find_all("div", class_=["item"])
        for mem in members:
            url = mem.find('a')
            name = None
            if (url is not None):
                name = url.get_text()
                url = url.get('href')
                votes +=voteCollect(name, url)
            print("member collected")
    return votes

def voteCollect(name, url):
    website = f"https://www.assembly.ab.ca/{url}"
    response = requests.get(website, headers={"User-Agent": "countable"})
    votes = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        votess = soup.find_all("div", class_="division mla_table")
        RepName= soup.find("h2", class_="nott ls1").get_text().replace(",", " ").replace("Mr", '').replace("Ms", '').replace("Honourable", '').replace("Premier", '').replace("Member ", '').replace("Dr", "").replace(" ECA", "").replace(" KC", "").replace(". ", "").strip()
        Jurisdiction = 'Alberta'
        for vote in votess:
            Date = vote.find("div", class_="col1").find(class_="data").get_text().replace("-", " ")
            Title = vote.find("div", class_="col2").find(class_="data").get_text().replace(",", " ").replace("  ", " ")
            if (("Bill" not in Title) or ("Motion" in Title) or ("Committee" in Title) or ("Amendment" in Title) or ('amendment' in Title)):
                continue
            Tit = Title.replace("Bill ", '').split(' ', 1)[0]
            YorN = vote.find("div", class_="col3").find(class_="data").get_text()
            resu = vote.find("div", class_="col4").find(class_="data").get_text()
            vote_data = {
                'num': Tit,
                'title': Title,
                'Date_of_Vote': Date, 
                'RepName': RepName,
                'RepVote': YorN,
                'Result': resu,
                'province': Jurisdiction
            }
            votes.append(vote_data)
    return votes