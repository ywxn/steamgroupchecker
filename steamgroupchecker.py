"""
Simple python script designed to test the whether steam groups use unicode or not.
"""

import requests
from bs4 import BeautifulSoup

def unicodeCheck(groupName,groupTag):
    nameVariable = 0
    tagVariable = 0
    for characterName in groupName:
        if ord(characterName) > 127:
            nameVariable = nameVariable + 1
    for characterTag in groupTag:
        if ord(characterTag) > 127:
            tagVariable = tagVariable + 1
    if nameVariable > 0:
        print("The group name contains unicode.")
    else:
        print("The group name does not contain unicode.")
    if tagVariable > 0:
        print("The group tag contains unicode.")
    else:
        print("The group tag does not contain unicode.")
    

def main():
    while True:
        url = input("Enter the url of the steam group here: ")
        content = requests.get(url)
        soup = BeautifulSoup(content.content, 'html.parser')
        groupName = soup.select_one(".grouppage_header_name").text
        groupTag = soup.select_one(".grouppage_header_name > span:nth-child(1)").text
        unicodeCheck(groupName,groupTag)
        yesNo = input("Do you want to test another group (yes/no)? ")
        while yesNo.lower() not in ("yes","no"):
            yesNo = input("Do you want to test another group(yes/no)? ")
        if yesNo == "no":
            break


if __name__ == "__main__":
    main()
