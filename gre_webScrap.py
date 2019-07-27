from bs4 import BeautifulSoup
import requests as req
import csv

urls = {"Argument_pool":"https://www.ets.org/gre/revised_general/prepare/analytical_writing/argument/pool",
"Issue_pool":"https://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/pool"}
for url in urls:
    #print(urls[url])
    respIssue = req.get(urls[url])
    soup = BeautifulSoup(respIssue.text, 'lxml')
    divs = soup.find_all("div",class_="divider-50".split())        
    tasksCSV = [['Sr No.', 'Task', 'Instruction', 'Response', 'comments']]
    count=0
    for div in divs:
        count+=1
        taskText=""
        #print(str(count)+" Task=======")
        taskStatement = div.findNextSibling(recursive=False)
        while taskStatement.name == "p":
            taskText+= "\n" +taskStatement.text
            #print(taskStatement.text)
            taskStatement = taskStatement.findNextSibling(recursive=False)
        #print("Task Info================")

        taskInstruction = taskStatement.findChild()
        instructionText = taskInstruction.text
        #print(taskInstruction.text)
        currentEntry = [count,taskText, instructionText, "", ""]
        tasksCSV.append(currentEntry)
    #print(url)
    with open(url+'.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(tasksCSV)

