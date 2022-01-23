from lib2to3.pgen2 import driver

from selenium import webdriver
import time
import pandas as pd
print('hello')
driver = webdriver.Chrome("D:\Webdriver\chromedriver.exe")
driver.get('https://www.englishfootballleaguetables.co.uk/final/f1892-93.html')
listOfDivision = []


def filterArray(list):
    flag = False;
    typeOfTable = 'First Division'
    for x in range(3, len(list)):
        print(list[x].text)
        print(typeOfTable)
        if(flag == True and list[x].text in 'Home Away' and list[x].text != ''):
            break
        if list[x].text in 'Home Away' and list[x].text != '':
            flag =True
            typeOfTable = 'Second Division'
        contains_digit = any(map(str.isdigit, list[x].text))
        if len(list[x].text) > 45 and contains_digit and "deducted" not in list[x].text and "rules" not in list[x].text and "game" not in list[x].text  and "finish" not in list[x].text and "League" not in list[x].text and "league" not in list[x].text and "Division" not in list[x].text:
            listOfRows.append(list[x])
            listOfDivision.append(typeOfTable)


listOfItems= []
for c in range (129):
    time.sleep(5)
    try:
        tables = driver.find_element_by_class_name("final4")
    except:
        a = driver.find_element_by_link_text("Next Season").click();
        time.sleep(5)
        continue
    entries = tables.find_elements_by_tag_name("tr")

    # test = entries[3].find_elements_by_tag_name("td")
    listOfRows = []
    filterArray(entries)


    currentItems = []
    data = {}
    for element in listOfRows:
        values = element.find_elements_by_tag_name("td")
        for j in range(0, 17):
            header = values[j].text
            currentItems.append(header)
        listOfItems.append(currentItems)
        currentItems = []

    time.sleep(12)
    a = driver.find_element_by_link_text("Next Season").click();



df =pd.DataFrame(listOfItems, columns=['a','b','c','a','a','a','a','a','a','a','a','a','a','a','a','a','a'])
df['div'] = listOfDivision
df.to_csv('file.csv')

time.sleep(10)
driver.close()