# we call here module resquests
from pymongo  import MongoClient
import requests
import json
from App import App

# here we get value from user 
question=str(input('Votre Name API : '))

while(question==''):
  print('Plase write your input ')
  question=str(input('Votre Name API : '))


question = question.lower()+''+ 'api'



#this url a API google 
url = "https://google.serper.dev/search"
payload = json.dumps({
  "q": f"{question}",
  "gl": "us",
  "hl": "en",
  "autocorrect": True
})
headers = {
  'X-API-KEY': '6d67c92ad45ec7a962737bb18b5fb1036f015aae',
  'Content-Type': 'application/json'
}
try:
  response = requests.request("POST", url, headers=headers, data=payload)
  data = response.json()

except requests.exceptions.RequestException as e:
  print(e)
# here we fetching data to JSON 

#we call items for searching 
filter = data['organic']


# here Backup file
backup=[]
faile = open('main.txt','w')

# and here we are fetching data and save in backup 
print('**** That the best Link for your ',question,'****')
for i in filter :
    print(i['link'])
    backup.append(i['link'])



file = open(f'{question}.txt','x')

file = open(f'{question}.txt','w')
file.write(f' **** That the best Link for your {question.upper()} **** ')
file.write(str(backup))
file.close()






