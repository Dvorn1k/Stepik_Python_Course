#3.6.2
import requests
output = open('output.txt', 'w')
with open('dataset_3378_2.txt') as fInput:
    link=fInput.readline().strip()
    r=requests.get(link)
    count=0
    for i in r.text.splitlines():
        count+=1
output.write(str(count))
output.close()

# 3.6.3
import requests

output = open('output.txt', 'w')

with open('dataset_3378_3.txt') as fInput:
    link = fInput.readline().strip()
    r = requests.get(link)
    while r.text[0] != 'W':
        link = r.text.strip()
        r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/"+link)
    output.write(r.text)
output.close()
