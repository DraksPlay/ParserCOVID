import requests
from bs4 import BeautifulSoup as bs
import json
import openpyxl


def save(data):
    wb = openpyxl.load_workbook("data.xlsx")
    sheet = wb["sheet"]
    i = 1
    while True:
        if sheet[f"A{i}"].value == None:
            sheet[f"A{i}"] = data
            break
        i += 1
    wb.save("data.xlsx")
    wb.close()


def parser():
    r = requests.get("https://стопкоронавирус.рф/information/")
    soup = bs(r.text, "html.parser")
    new = soup.findAll("section")[0].find("div").find("div").find("cv-stats-virus").attrs[":stats-data"]
    data = json.loads(new)["sickChange"]
    result = ""
    for i in data:
        try:
            x = int(i)
            result += i
        except ValueError:
            pass
    save(int(result))


if __name__ == '__main__':
    parser()