import re
import csv
import requests
from bs4 import BeautifulSoup


url = "https://ja.wikipedia.org/"
response = requests.get(url)
# parse html
soup = BeautifulSoup(response.content, "html.parser")

today = soup.find("div", attrs={"id": "on_this_day"})
today_list=[]

for i, list in enumerate(today.find_all("li")):
    today_text = list.get_text().replace("（", "(").replace("）", ")")
    match = re.search("\((.*?)年\)", today_text)
    if match:
        today_list.append([i+1, list.get_text(), match.group(1)])
    else:
        today_list.append([i+1, list.get_text()])
    
print(today_list)

with open("wiki_today.csv", "w", encoding='UTF-8') as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerows(today_list)

print("completed")