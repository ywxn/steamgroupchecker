"""
Simple python script designed to test the whether steam groups have an original name or tag.
"""

import requests
from bs4 import BeautifulSoup

def unicodeCheck(groupName,groupTag):
    nameVariable = 0
    tagVariable = 0
    for characterName in groupName:
        if ord(characterName) > 127:
            nameVariable = nameVariable + 1
        else:
            pass
    for characterTag in groupTag:
        if ord(characterTag) > 127:
            tagVariable = tagVariable + 1
        else:
            pass
    if nameVariable == 0:
        print("The group name does not contain unicode.")
    else:
        print("The group name contains unicode.")
    if tagVariable == 0:
        print("The group tag does not contain unicode.")
    else:
        print("The group tag contains unicode.")
    

def main():
    while True:
        url = input("Enter the url of the steam group here: ")
        content = requests.get(url)
        soup = BeautifulSoup(content.content, 'html.parser')
        soup2 = BeautifulSoup(content.content, 'html.parser')
        groupName = soup.select_one("div.group_content:nth-child(2) > div:nth-child(1)").text
        groupTag = soup2.select_one(".grouppage_header_name > span:nth-child(1)").text
        unicodeCheck(groupName,groupTag)
        yesNo = input("Do you want to test another group (yes/no)? ")
        while yesNo.lower() not in ("yes","no"):
            yesNo = input("Do you want to test another group(yes/no)? ")
        if yesNo == "no":
            break


if __name__ == "__main__":
    main()
